---
name: run-product-premortem
description: Run a structured premortem on a product bet, requirements document, rollout, migration, or launch and convert plausible failure modes into mitigations, owners, triggers, and contingency plans. Use when stress-testing a plan, preparing a launch, exposing hidden concerns, or deciding whether risk is acceptable.
---

# Run Product Premortem

## Contract

Assume the effort failed at a specific future point and reason backward. Cover customer, product, engineering, data, operations, go-to-market, legal, security, accessibility, finance, and organizational failure. Distinguish evidence-backed risk from anxiety.

## Workflow

1. Define the plan, intended outcome, launch or decision point, scope, assumptions, and risk tolerance.
2. Write a concrete failure narrative: what customers and the business observe after failure.
3. Generate failure modes independently across functions before group convergence.
4. For each mode, record cause, affected party, evidence, likelihood range, severity, detectability, timing, and dependency.
5. Identify correlated risks, cascading failures, silent failures, and assumptions nobody owns.
6. Classify actions as prevent, detect, contain, recover, accept, or transfer. Name owner, due point, leading trigger, and proof of completion.
7. Separate launch blockers, bounded fast follows, monitored risks, and low-value concerns. Define rollback and escalation.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Review customer evidence, project detail, linked tickets, documents, knowledge gaps, prior launches, and related signals. Any recheck, attachment, or project mutation requires explicit approval.

## Output

Return failure narrative, risk register, correlated risks, mitigations, owners, triggers, blocker decision, contingency and rollback plan, accepted risks, and unresolved questions.

## Quality Gate

Reject vague risks, mitigations without owners or verification, universal high ratings, and lists that ignore customer harm or operational recovery.

## Provenance

Independently authored. Informed by [pre-mortem](https://github.com/phuryn/pm-skills/tree/main/pm-execution/skills/pre-mortem) and [high-stakes-decisions](https://github.com/RefoundAI/lenny-skills/tree/main/skills/high-stakes-decisions).
