---
name: bwh-model-selector
description: Select models and reasoning effort for delegated work whenever an agent plans or executes a task, including specification, development, investigation, and review. Prefer capable lower-tier subagents, require permission for higher-tier models, and warn when model guidance is stale.
---

# Model selector

Use this execution policy alongside the task's owning skill. It does not create a new workflow stage or change the requested deliverable. Apply [autonomy](../../contracts/autonomy.md) and the consuming project's instructions and adapter.

## Before delegation

1. Read [model guidance and host mechanics](agents/model-guide.md). Compare its review date with today's UTC date from the environment or a clock. Warn once per task when it is at least 60 days old, missing, invalid, or in the future. Include the review date, age when known, and the need to refresh it. A stale guide is advisory, not a reason to stop useful work. Do not reset the date merely because the skill ran. If the current date is unavailable, report that freshness could not be checked.
2. Identify the current agent's actual model and supported effort from session metadata. Discover the delegation tool's available models and settings. A model mentioned in a prompt, source document, or guide is not evidence of runtime availability. If identity or ranking is unknown, work locally and explain that safe lower-tier delegation could not be established.
3. Break non-trivial work into bounded jobs and delegate useful independent parts to the least costly capable lower-tier models available. Keep the main context for decisions, integration, and verification. Skip delegation for a trivial answer, tightly coupled work where handoff costs exceed the benefit, unavailable tools, or no suitable lower tier. Explain material delegation limitations briefly. Do not create a suite just to use many models.

Proceed when each delegated job has an available model, an established lower rank, a supported effort, and a checkable result. Choose by capability needed and total expected cost including context, retries, review, and latency. Lower price alone does not establish a lower capability tier.

## Model ceiling and escalation

Autonomous children must be strictly below their immediate parent in the maintained same-family ranking. The current model at lower effort is still the same tier and is not an eligible child. Equal-tier children need an explicit user exception. Models from different families, unknown models, and models without an established ordering are incomparable. Ask before using them unless the user has already approved the exact choice or an explicit cross-family ordering.

If a higher-tier model would materially help, ask before launching it or switching the main session to it. Name the proposed model and effort, the bounded job, why the current agent and eligible children are insufficient, and the expected quality benefit and usage or latency trade-off. Use observed failures or concrete task demands. Do not invent a price estimate. Continue unaffected work while awaiting an answer; silence is not approval. Existing approval applies only to its stated scope.

A failed lower-tier run does not grant escalation authority. First improve its evidence and verification, then consider one supported effort increase or another eligible lower tier. Prefer doing the difficult part on the main agent over repeated weak attempts. Stop retries when they no longer add evidence. Any change that crosses the ceiling still needs approval, even if it may be cheaper per finished task.

## Delegation and quality

- Give each child its job, relevant instructions, permitted actions, minimal source material, acceptance criteria, and a concise evidence format. Request file or source citations, uncertainty, and validation results. Use fresh context rather than the full conversation when supported.
- Select different model types only when they suit distinct jobs and are eligible. Parallelize independent reads, tests, or edits with separate ownership. Keep dependent decisions and overlapping edits sequential.
- Tell children to complete their bounded job themselves without further delegation unless specifically authorised. If further delegation is authorised, pass this policy, their actual model identity, and the applicable approval scope. Each parent must enforce its own ceiling.
- Verify decisive source claims and inspect edits before integration. Run the task's required checks. Summaries and a passing child verdict do not replace evidence. Retain required independent review; if no eligible reviewer can do it adequately, report the review incomplete or request a specific model exception.
- Keep task completion and acceptance standards unchanged. Split off easy evidence gathering from consequential architecture, security, migration, or product judgments rather than assigning those judgments to a model unable to support them.

For specs, delegate source extraction, existing-behaviour checks, and contradictions; retain scope decisions and synthesis. For development, delegate isolated changes, test execution, or focused review where competence and verification permit. For review, delegate bounded evidence checks while the reviewer owns the verdict.

## Handoff and maintenance

Briefly report material model choices and effort, why they fit, evidence checked, and any fallback, permission request, or freshness warning. Record latency, tokens, retries, and outcome when available for an eval, without inventing telemetry. Routine runs need no separate selection artifact.

When asked to refresh the guide, consult current official sources and runtime availability. Update the relevant family recommendations, source links, review date, and rank evidence together. Preserve uncertain or unverified claims as such. Do not install models, change global defaults, or rewrite project instructions merely to apply this skill.
