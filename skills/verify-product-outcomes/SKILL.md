---
name: verify-product-outcomes
description: Compare implemented and observed product behavior against intended customer outcomes, requirements, quality constraints, and release evidence. Use when implementation or deployment is complete, during UAT, while reviewing intended versus implemented behavior, or before declaring a feature complete.
---

# Verify Product Outcomes

## Contract

Verification is evidence, not a claim. Distinguish code complete, tests passed, deployed, observed, customer validated, and outcome achieved. Verify the user journey and failure paths, not only the happy-path implementation.

## Workflow

1. Resolve the authoritative requirements, decision records, designs, acceptance scenarios, release artifact, environment, and exact version or SHA.
2. Convert intended outcomes and constraints into a traceability matrix with observable evidence.
3. Inspect the implemented surface and supporting behavior. Test primary journeys, permissions, empty and error states, accessibility, recovery, analytics, and operational controls.
4. Compare artifact intent, implementation, automated checks, environment state, and observed behavior. Record evidence links, screenshots, logs, or IDs.
5. Classify gaps as missing requirement, implementation divergence, regression, ambiguous spec, instrumentation gap, or accepted tradeoff.
6. Assess severity from customer outcome and risk, not code size.
7. Produce a verdict per requirement and an overall verified, conditional, or failed state. Name what remains unverified.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use projects, linked tickets, evidence, documents, signals, surveys, and agent-session or release context when deployed. Keep BuildBetter evidence distinct from browser, test, CI, staging, and production proof.

## Output

Return exact artifact and environment identifiers, traceability matrix, evidence, gaps, severity, verdict, remaining unknowns, and required follow-ups.

## Quality Gate

Never infer production behavior from a branch, staging from CI, customer validation from UAT, or outcome achievement from shipment. Missing evidence stays missing.

## Provenance

Independently authored. Informed by [uat-ux-debug](https://github.com/mekenthompson/ProductOS/tree/main/skills/uat-ux-debug), [intended-vs-implemented](https://github.com/phuryn/pm-skills/tree/main/pm-ai-shipping/skills/intended-vs-implemented), and [product-reviews](https://github.com/RefoundAI/lenny-skills/tree/main/skills/product-reviews).
