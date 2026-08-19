---
name: design-product-experiment
description: Design a product experiment that tests a decision-critical hypothesis with a valid comparison, primary metric, guardrails, stopping rule, analysis plan, and follow-up decision. Use when validating a solution, planning an A/B test, testing an assumption, or reviewing whether an experiment can produce decisive evidence.
---

# Design Product Experiment

## Contract

Design backward from the decision. Test the riskiest claim with the cheapest method that can answer it. Do not use an A/B test when observation, interview, prototype, smoke test, or technical probe is more appropriate.

## Workflow

1. State the decision and falsifiable hypothesis: population, change, expected behavior, mechanism, and time window.
2. Identify the assumption type: value, demand, comprehension, usability, feasibility, viability, or causal impact.
3. Choose the method and comparison. Define assignment unit, eligibility, control, exposure, contamination risks, and novelty effects.
4. Select one primary decision metric with exact calculation and window. Add diagnostic and guardrail metrics.
5. Estimate sample and duration from baseline, minimum meaningful effect, variance, power, seasonality, and traffic; use ranges when inputs are unknown.
6. Predefine exclusions, stopping rules, data-quality checks, segment analysis, and interpretation for positive, negative, null, or inconclusive results.
7. Define the operational plan, owner, ethics or privacy checks, and the decision each result triggers.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use signals, survey responses, people or account context, documents, and synthetic persona tests to refine hypotheses. Synthetic results can reveal questions or usability risks but cannot establish real-world causal impact.

## Output

Return decision, hypothesis, method, population, assignment, variants, metrics, sample assumptions, duration, risks, analysis plan, stopping rule, result-to-decision table, and instrumentation checklist.

## Quality Gate

Reject unfalsifiable hypotheses, multiple primary metrics, peeking-based stopping, post-hoc segments presented as confirmed, and tests too underpowered to change the decision.

## Provenance

Independently authored. Informed by [experiment-design](https://github.com/assimovt/productskills/tree/main/skills/experiment-design), [product-experiments](https://github.com/RefoundAI/lenny-skills/tree/main/skills/product-experiments), and [ab-test-analysis](https://github.com/phuryn/pm-skills/tree/main/pm-data-analytics/skills/ab-test-analysis).
