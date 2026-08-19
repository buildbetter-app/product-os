---
name: design-ai-product-evaluation
description: Design an empirical evaluation system for an AI product using representative tasks, quality dimensions, human and automated judgments, slices, thresholds, regressions, and online outcomes. Use when defining AI quality, replacing vibe checks, comparing models or prompts, or setting release gates.
---

# Design AI Product Evaluation

## Contract

Evaluate the product behavior users experience, not a model in isolation. No single score captures usefulness, safety, reliability, latency, and cost. Automated graders require validation against qualified human judgment.

## Workflow

1. Define the user decision or job, workflow context, AI responsibility, failure consequences, and release decision the evaluation must support.
2. Decompose quality into task-specific dimensions such as correctness, completeness, grounding, instruction adherence, calibration, consistency, safety, style, latency, and cost.
3. Build a representative evaluation set from real or carefully governed synthetic tasks, including common, difficult, adversarial, multilingual, accessibility, and high-impact slices.
4. Define reference answers or rubrics only where they are valid. Preserve tasks with multiple acceptable outputs and specify pairwise, scalar, categorical, or task-success judgments.
5. Choose human reviewers, deterministic checks, model graders, simulations, and online measures for each dimension. Measure grader agreement, bias, and drift.
6. Establish baselines, uncertainty, minimum acceptable thresholds, regression budgets, hard safety gates, and tradeoff rules across quality, latency, and cost.
7. Run blinded comparisons when possible. Investigate failures by slice and mechanism rather than averaging them away.
8. Connect offline results to staged online behavior, monitoring, incident review, dataset refresh, and versioned release decisions.

## BuildBetter Acceleration

If BuildBetter MCP is available, search organization skills first. Use calls, signals, surveys, projects, documents, synthetic persona studies, and customer outcomes to build tasks and rubrics. Remove or govern sensitive data and keep synthetic judgments distinct from real-user evidence.

## Output

Return evaluation purpose, quality dimensions, dataset and slices, rubric, evaluators, grader validation, baselines, thresholds, results plan, release gates, monitoring, and unresolved coverage.

## Quality Gate

Reject cherry-picked demos, one-number quality claims, graders never calibrated to humans, datasets contaminated by the system under test, and release gates that ignore high-impact slices or regression risk.

## Provenance

Independently authored. Informed by [ai-evals](https://github.com/RefoundAI/lenny-skills/tree/main/skills/ai-evals) and [product-experiments](https://github.com/RefoundAI/lenny-skills/tree/main/skills/product-experiments).
