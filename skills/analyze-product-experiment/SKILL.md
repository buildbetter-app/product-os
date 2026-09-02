---
name: analyze-product-experiment
description: Analyze product experiment results for validity, effect size, uncertainty, guardrails, heterogeneous effects, and the decision they support. Use when reading an A/B test, prototype study, smoke test, or other completed experiment and deciding whether to ship, extend, revise, or stop.
---

# Analyze Product Experiment

## Contract

Analyze against the decision and plan that existed before results were known. Statistical significance is neither product importance nor proof of mechanism. Preserve null, negative, and inconclusive results.

## Workflow

1. Recover the original decision, hypothesis, population, assignment, variants, primary metric, guardrails, duration, sample plan, exclusions, and stopping rule.
2. Verify exposure and data integrity: eligibility, assignment balance, sample-ratio mismatch, missingness, duplication, contamination, novelty, seasonality, and instrumentation changes.
3. Report actual sample, duration, baseline, effect size, uncertainty interval, and practical significance for the primary metric.
4. Evaluate guardrails, operational failures, quality costs, and business or customer tradeoffs even when the primary metric improves.
5. Correctly handle repeated looks, multiple metrics, clustering, low power, noncompliance, and post-hoc exclusions. State when causal interpretation is not supported.
6. Analyze predefined segments. Label unplanned slices and discovered explanations as exploratory rather than confirmed.
7. Compare results with the predeclared decision table and mechanism. Recommend ship, stop, extend, revise, or run a different test with conditions.
8. Record learning, residual uncertainty, follow-up instrumentation, and how the evidence updates the product decision.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use calls, signals, surveys, project evidence, and synthetic studies as qualitative context around results. Do not replace authoritative assignment and product analytics data with anecdotal evidence.

## Output

Return design readback, integrity checks, sample and effect estimates, uncertainty, guardrails, segment findings, interpretation limits, decision, follow-up, and evidence record.

## Quality Gate

Reject decisions based only on p-values, underpowered nulls described as no effect, post-hoc segments presented as confirmed, or analyses that ignore broken assignment, missing data, and guardrail harm.

## Provenance

Independently authored. Informed by [product-experiments](https://github.com/RefoundAI/lenny-skills/tree/main/skills/product-experiments) and [ab-test-analysis](https://github.com/phuryn/pm-skills/tree/main/pm-data-analytics/skills/ab-test-analysis).
