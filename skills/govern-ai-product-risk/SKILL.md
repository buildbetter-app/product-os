---
name: govern-ai-product-risk
description: Govern AI product risks through use-case boundaries, harm analysis, controls, accountability, testing, monitoring, incident response, and review triggers. Use when an AI capability affects customers, sensitive data, consequential decisions, external actions, or regulated and high-impact workflows.
---

# Govern AI Product Risk

## Contract

Risk governance must be proportionate to real use and consequence. It does not replace legal, security, privacy, safety, or domain-expert review and must not claim compliance merely because a checklist is complete.

## Workflow

1. Define intended users, affected non-users, purpose, prohibited uses, deployment context, data, model and tool capabilities, autonomy, and decision consequences.
2. Map harms across incorrect output, omission, bias, privacy, security, manipulation, overreliance, loss of control, unsafe action, economic impact, and downstream reuse.
3. Rate severity, likelihood, exposure, detectability, reversibility, and distribution across relevant populations. Preserve uncertainty and credible worst cases.
4. Select controls by layer: product scope, data, model, prompt, retrieval, tools, permissions, interface, human review, rate limits, logging, monitoring, and operations.
5. Assign accountable owners, evidence requirements, approval rights, exceptions, expiry, and independent reviewers for high-impact decisions.
6. Define misuse, abuse, red-team, accessibility, privacy, security, and domain tests with release-blocking thresholds.
7. Establish monitoring, user reporting, containment, rollback, notification, remediation, and incident-review paths.
8. Reassess when models, prompts, data, tools, autonomy, audience, geography, policy, or observed harm changes.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use customer evidence, surveys, projects, documents, knowledge gaps, release context, and prior incidents where accessible. Respect access boundaries and do not expose sensitive evidence in the risk artifact.

## Output

Return use-case boundaries, stakeholder and harm map, risk register, layered controls, owners, required reviews, test plan, release gates, monitoring, incident process, and reassessment triggers.

## Quality Gate

Reject generic risk lists detached from the use case, controls with no owner or evidence, high-impact automation with nominal review, and unsupported claims that the product is safe, unbiased, secure, or compliant.

## Provenance

Independently authored. Informed by the empirical and user-control disciplines in [ai-evals](https://github.com/RefoundAI/lenny-skills/tree/main/skills/ai-evals) and [ai-native-ux](https://github.com/RefoundAI/lenny-skills/tree/main/skills/ai-native-ux).
