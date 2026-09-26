# `burn` skill discovery

## Idea and desired outcome

Create a skill called `burn` for a user who has expiring usage on a usage plan and wants to spend some of it productively in the current project before reset. The skill should inspect the current usage and reset window, find worthwhile work that fits project conventions, make progress in bounded steps, and stop with a reviewable result before the allowance resets or execution is interrupted.

## Actors

- A project contributor with usage that will expire at a known reset.
- The agent working in the contributor's current project.
- A reviewer who needs a coherent stopping point and clear account of what changed.

## Problem and opportunity

Unused allowance may expire, while open-ended work can consume it without leaving a useful result. A dedicated skill can turn the remaining window into project-aligned improvements while protecting the work from an abrupt reset, runaway execution, or unreviewable partial changes.

## Known facts

- The user wants usage checked and monitored during work.
- Work should follow the project's conventions and improve the project.
- The skill should stop before reaching the usage limit, at a coherent point that can be reviewed.
- The skill must not continue running across a usage reset and consume the next allowance.
- The skill is intended for use inside a project, rather than as a general-purpose usage optimizer.

## Assumptions

- **A1, authorized usage evidence.** The skill may read usage and reset information exposed by the active host or supplied by the user, but must not infer exact values from private transcript history or access unrelated accounts. This is observable when it states the source and uncertainty of its starting usage and reset estimate.
- **A2, bounded project work.** It should prefer small, independently reviewable improvements, inspect local instructions and project state first, and avoid broad rewrites or external side effects. This is observable in the diff and its handoff.
- **A3, preserve a safety margin.** It should stop new work early enough to summarize and leave a reviewable state, rather than targeting the final unit of available usage. This is observable when it stops with allowance or time remaining.
- **A4, no reset crossover.** It should treat the reset as a hard deadline, stop active work before it, and verify it has no continuing task or process that can consume the next allowance. This is observable at the deadline boundary.

## Scope

- Read available usage and reset information, communicate uncertainty, and re-check it as work proceeds.
- Inspect project instructions, worktree state, and likely improvement areas before choosing bounded work.
- Make useful in-scope project improvements in small steps, following project validation and change conventions.
- Maintain a stop margin, finish or safely halt active work before reset, and leave a clear summary of changes, validation, remaining usage uncertainty, and follow-up candidates.

## Non-goals

- Maximizing usage consumption as an end in itself.
- Spending money, changing plans, accessing another account, or expanding permissions.
- Starting long-running or unattended work that could cross the reset boundary.
- Automatically committing, publishing, deploying, or contacting others.
- Replacing normal project approval, test, review, or publication rules.

## Success signals

- It produces a useful, project-conventional, reviewable change rather than activity for its own sake.
- It reports where usage and reset estimates came from and marks unavailable or uncertain values clearly.
- It stops early enough to leave a coherent handoff and does not run into the next usage period.
- Its work respects repository instructions and existing validation and publication boundaries.

## Risks

- The host may not expose a reliable usage counter or reset timestamp; estimates could be wrong.
- Usage can be consumed quickly or nonlinearly, so periodic checks alone may not ensure a safe stop.
- An overly broad task can leave a partial or risky change at the reset boundary.
- A skill that is vague about "improvement" may trigger on ordinary coding requests or overreach into unrelated cleanup.
- Background commands or delegated work can continue consuming usage after the main interaction appears to stop.

## Dependencies

- A defined way to identify the active plan's remaining allowance and reset time, or a user-provided estimate when the host lacks that information.
- Clear project instructions and conventions for selecting and validating changes.
- Host behavior that allows active work and any launched processes to be stopped or awaited before the deadline.

## Material options

### Option A: rely on host telemetry only

The skill reads live usage and reset metadata when available and declines to proceed when it cannot establish a safe window. This gives tighter monitoring but depends on host capabilities.

### Option B: accept user-provided values as fallback (recommended)

Use host telemetry when available; otherwise ask the user for remaining allowance and reset time, label them estimates, re-check when possible, and choose a more conservative task and margin. This is more portable while keeping uncertainty visible.

### Option C: infer usage from conversation activity

Estimate remaining allowance from tokens or activity in the current conversation. This is portable in appearance but too unreliable to support a hard stop boundary; do not use as an authoritative signal.

## Decisions still needed

- What usage plan and host signals should the first version support, and should it proceed when values are only user estimates?
- What default stop margin should apply when the reset time or consumption rate is uncertain? The specification should define a conservative policy and a fallback when time cannot be estimated.
- Should `burn` autonomously choose and implement small improvements, or present candidates for the user to choose before editing? Recommendation: permit bounded autonomous changes when the user's prompt explicitly asks to burn usage, while keeping normal project guardrails and avoiding expensive or hard-to-reverse work.

## Recommended next step

Use `bwh-spec` to define the supported usage signals, stop policy, work-selection behavior, and completion criteria before implementing the skill.
