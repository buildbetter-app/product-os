#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SKILLSETS = ROOT / "skillsets"
OUTPUT = ROOT / "dist" / "buildbetter"


def parse_frontmatter(content: str) -> dict[str, str]:
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing frontmatter")
    end = lines.index("---", 1)
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def display_name(skill: str) -> str:
    path = SKILLS / skill / "agents" / "openai.yaml"
    content = path.read_text(encoding="utf-8")
    match = re.search(r'^\s*display_name:\s*"([^"]+)"\s*$', content, re.MULTILINE)
    if not match:
        raise ValueError(f"{skill}: missing display_name")
    return match.group(1)


def expand_manifest(stem: str, stack: tuple[str, ...] = ()) -> tuple[dict, list[str]]:
    if stem in stack:
        raise ValueError(f"cyclic include: {' -> '.join((*stack, stem))}")
    path = SKILLSETS / f"{stem}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    names = list(data.get("skills", []))
    for child in data.get("includes", []):
        _, child_names = expand_manifest(child, (*stack, stem))
        names.extend(child_names)
    return data, names


def render(stem: str) -> str:
    manifest, names = expand_manifest(stem)
    skills = []
    for position, name in enumerate(names):
        source_path = Path("skills") / name / "SKILL.md"
        content = (ROOT / source_path).read_text(encoding="utf-8")
        metadata = parse_frontmatter(content)
        skills.append(
            {
                "position": position,
                "sourcePath": source_path.as_posix(),
                "create": {
                    "name": display_name(name),
                    "description": metadata["description"],
                    "content": content,
                },
            }
        )
    payload = {
        "schemaVersion": 1,
        "source": {
            "type": "github",
            "repository": "https://github.com/buildbetter-app/product-os",
            "license": "MIT",
        },
        "skillset": {
            "name": manifest["name"],
            "slug": manifest["slug"],
            "description": manifest["description"],
        },
        "skills": skills,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate deterministic BuildBetter managed Skillset payloads."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when generated payloads differ from committed files.",
    )
    args = parser.parse_args()

    OUTPUT.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    for path in sorted(SKILLSETS.glob("*.json")):
        expected = render(path.stem)
        target = OUTPUT / f"{path.stem}.json"
        if args.check:
            actual = target.read_text(encoding="utf-8") if target.exists() else ""
            if actual != expected:
                failures.append(target.relative_to(ROOT).as_posix())
        else:
            target.write_text(expected, encoding="utf-8")

    if failures:
        print("Out-of-date BuildBetter templates:")
        for failure in failures:
            print(f"  {failure}")
        return 1
    verb = "Checked" if args.check else "Generated"
    print(f"{verb} {len(list(SKILLSETS.glob('*.json')))} BuildBetter templates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
