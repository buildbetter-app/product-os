---
name: plan-product-instrumentation
description: Create a product analytics tracking plan with decision questions, event semantics, identity, properties, privacy, ownership, quality checks, and release validation. Use when instrumenting a feature, operationalizing product metrics, repairing unreliable analytics, or preparing experiment measurement.
---

# Plan Product Instrumentation

## Contract

Instrumentation is a measurement contract, not an event inventory. Collect only data tied to a decision, define semantics before implementation, and minimize personal or sensitive data.

## Workflow

1. List the decisions, metric definitions, hypotheses, and journeys the instrumentation must support.
2. Map the observable states and value events from eligibility through exposure, action, outcome, failure, and recovery.
3. Reuse the existing taxonomy where semantics match. Define each new event with trigger, actor, object, timestamp, source, environment, and exclusions.
4. Define required properties, types, allowed values, null behavior, cardinality, and versioning. Keep mutable context distinct from event facts.
5. Specify anonymous, user, account, device, and session identity rules, including merges, cross-device behavior, bots, internal users, and consent boundaries.
6. Map events to metrics and analyses. Identify joins, attribution windows, late data, duplication, ordering, and warehouse or client differences.
7. Create implementation ownership and a validation plan using fixtures, expected payloads, schema checks, volume checks, and end-to-end environment evidence.
8. Define monitoring, documentation, deprecation, and change control so semantic drift becomes visible.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use customer journeys, projects, documents, signals, surveys, and prior decisions to clarify what must be observed. Do not imply BuildBetter contains product event data unless an authoritative analytics source is connected.

## Output

Return decision map, journey states, event and property dictionary, identity model, metric mapping, privacy constraints, implementation owners, validation cases, monitoring, and deprecation plan.

## Quality Gate

Reject tracking plans with ambiguous triggers, unused events, unbounded properties, undocumented identity, sensitive fields without need, or no way to prove events work in the released environment.

## Provenance

Independently authored. Informed by the measurement disciplines in [north-star-metrics](https://github.com/RefoundAI/lenny-skills/tree/main/skills/north-star-metrics) and [metrics-dashboard](https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery/skills/metrics-dashboard).
