---
name: analyze-retention-and-adoption
description: Diagnose product activation, cohort retention, engagement, feature adoption, churn, and value realization using behavioral and qualitative evidence. Use when investigating weak adoption, comparing cohorts or segments, evaluating product health, or deciding which retention constraint to address.
---

# Analyze Retention And Adoption

## Contract

Retention must describe a meaningful return to value for an eligible population. Do not hide cohort decay in aggregate active-user totals or treat logins, clicks, and feature exposure as value realization.

## Workflow

1. Define the decision, population, cohort entry, eligibility, value event, return interval, observation window, product state, and segments.
2. Validate identity, event semantics, data completeness, censoring, bot and internal traffic, plan or entitlement changes, and acquisition-mix shifts.
3. Map the path from entry through setup, activation, first value, repeated value, habit or workflow embedding, expansion, inactivity, and churn.
4. Build cohort views for activation, time to value, classic or rolling retention, frequency, depth, breadth, feature adoption, and reactivation as appropriate.
5. Compare segments by job, source, account, product version, tenure, behavior, and value achieved without averaging incompatible populations.
6. Join behavioral patterns with customer evidence about friction, unmet jobs, alternatives, reliability, price, support, and reasons for leaving.
7. Diagnose the primary constraint and distinguish acquisition quality, onboarding, product value, usability, reliability, pricing, or measurement problems.
8. Recommend a bounded intervention, success and guardrail measures, expected affected cohort, and next evidence needed.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use calls, signals, survey responses, people and account context, documents, and projects to explain behavioral patterns. Keep those sources distinct from authoritative product analytics and billing data.

## Output

Return definitions, data-quality findings, cohort and segment views, value-path analysis, customer evidence, constraint diagnosis, confidence, intervention, and measurement plan.

## Quality Gate

Reject aggregate retention without cohort definitions, adoption based only on exposure, causal claims from descriptive slices, or recommendations that cannot name the value event and affected population.

## Provenance

Independently authored. Informed by [retention-engagement](https://github.com/RefoundAI/lenny-skills/tree/main/skills/retention-engagement) and [cohort-analysis](https://github.com/phuryn/pm-skills/tree/main/pm-data-analytics/skills/cohort-analysis).
