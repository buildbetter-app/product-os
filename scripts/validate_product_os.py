#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SKILLSETS = ROOT / "skillsets"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("missing closing frontmatter delimiter") from error
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values, text


def expand_manifest(stem: str, seen: set[str] | None = None) -> list[str]:
    seen = set() if seen is None else seen
    if stem in seen:
        raise ValueError(f"cyclic skillset include: {stem}")
    seen.add(stem)
    path = SKILLSETS / f"{stem}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    result = list(data.get("skills", []))
    for child in data.get("includes", []):
        result.extend(expand_manifest(child, seen.copy()))
    return result


def main() -> int:
    errors: list[str] = []
    skill_names: set[str] = set()

    for directory in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill_path = directory / "SKILL.md"
        agent_path = directory / "agents" / "openai.yaml"
        if not skill_path.exists():
            errors.append(f"{directory.name}: missing SKILL.md")
            continue
        try:
            metadata, content = frontmatter(skill_path)
        except ValueError as error:
            errors.append(f"{directory.name}: {error}")
            continue
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if set(metadata) != {"name", "description"}:
            errors.append(f"{directory.name}: frontmatter must contain only name and description")
        if name != directory.name:
            errors.append(f"{directory.name}: name does not match directory")
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{directory.name}: invalid skill name")
        if len(description) < 80 or "Use when" not in description:
            errors.append(f"{directory.name}: description needs behavior and explicit triggers")
        if "TODO" in content:
            errors.append(f"{directory.name}: unresolved TODO")
        if len(content.splitlines()) > 500:
            errors.append(f"{directory.name}: SKILL.md exceeds 500 lines")
        if "## BuildBetter Acceleration" not in content:
            errors.append(f"{directory.name}: missing BuildBetter fallback contract")
        if "## Quality Gate" not in content:
            errors.append(f"{directory.name}: missing quality gate")
        if "## Provenance" not in content:
            errors.append(f"{directory.name}: missing provenance")
        if not agent_path.exists():
            errors.append(f"{directory.name}: missing agents/openai.yaml")
        else:
            agent = agent_path.read_text(encoding="utf-8")
            if "$" + name not in agent:
                errors.append(f"{directory.name}: default prompt must mention the skill name")
            if "TODO" in agent:
                errors.append(f"{directory.name}: unresolved agent metadata TODO")
        skill_names.add(name)

    manifests = sorted(SKILLSETS.glob("*.json"))
    slugs: set[str] = set()
    for path in manifests:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("schemaVersion") != 1:
                errors.append(f"{path.name}: schemaVersion must be 1")
            slug = data.get("slug", "")
            if not NAME_RE.fullmatch(slug):
                errors.append(f"{path.name}: invalid slug")
            if slug in slugs:
                errors.append(f"{path.name}: duplicate slug {slug}")
            slugs.add(slug)
            expanded = expand_manifest(path.stem)
            if len(expanded) != len(set(expanded)):
                errors.append(f"{path.name}: duplicate skills after include expansion")
            unknown = set(expanded) - skill_names
            if unknown:
                errors.append(f"{path.name}: unknown skills {sorted(unknown)}")
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{path.name}: {error}")

    try:
        complete = set(expand_manifest("complete"))
        if complete != skill_names:
            errors.append(
                "complete.json does not cover the exact skill set: "
                f"missing={sorted(skill_names - complete)} extra={sorted(complete - skill_names)}"
            )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"complete.json: {error}")

    if len(skill_names) != 32:
        errors.append(f"expected 32 skills, found {len(skill_names)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(skill_names)} skills and {len(manifests)} skillset templates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
