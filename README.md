# Product OS

Product OS is an open, evidence-first operating system for product work. It packages 32 focused agent skills across discovery, strategy, delivery, and product operations.

The skills are vendor-neutral and usable from any agent harness that supports the common SKILL.md format. When BuildBetter MCP is available, evidence-heavy skills use organization Skillsets and customer context as an acceleration layer; every workflow still has an artifact-only fallback.

## Packs

| Pack | Purpose | Skills |
| --- | --- | ---: |
| Discovery | Research, interviews, synthesis, jobs, journeys, competition, opportunities | 8 |
| Strategy | Validation, vision, strategy, positioning, ICP, market size, prioritization, bets | 8 |
| Delivery | Experiments, metrics, requirements, scope, roadmap, premortem, alignment, verification | 8 |
| Operate | Launch, pricing, growth, PMF, reviews, decisions, sunset | 8 |
| Complete | All Product OS skills | 32 |

Each skill has a canonical, verb-led name. See [docs/naming.md](docs/naming.md) for the normalization rules and [docs/source-audit.md](docs/source-audit.md) for the source review and license treatment.

## Use

Install or copy an individual directory under skills into your agent's skill surface. SkillRank can index every directory independently because each contains its own SKILL.md and agents/openai.yaml.

BuildBetter-ready pack templates live in skillsets. Generate fully embedded import payloads with:

    python3 scripts/export_buildbetter_templates.py

Generated payloads land in dist/buildbetter and match BuildBetter's managed Skillset model: one skillset create payload plus ordered skill create payloads with full Markdown content.

Validate the repository with:

    python3 scripts/validate_product_os.py

## Design principles

- Evidence before confidence.
- Outcomes before features.
- Decisions before documents.
- Exact states instead of implied completion.
- Progressive disclosure and small, focused skills.
- Vendor-neutral core with optional BuildBetter acceleration.
- Explicit approval for publishing, sending, customer access, billing, deletion, and other consequential mutations.

## License

Product OS is MIT licensed. The skills are independently authored, cite their influences, and do not incorporate text from the CC BY-NC-SA source reviewed during research. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
