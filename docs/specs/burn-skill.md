# `burn` skill specification

Status: `APPROVED FOR DEVELOPMENT`

## Summary

Add a portable `burn` skill that turns soon-to-expire usage into useful project improvements at high throughput. It tracks both the weekly allowance and the rolling five-hour allowance, works through repeated five-hour refills when needed, and aims to leave about 2–3% of the weekly allowance unused. It follows project conventions, uses subagents for independent work when parallel execution saves time, and stops before the weekly reset with a reviewable result.

## Problem

When a weekly usage allowance is close to reset, the user wants to spend nearly all of it productively instead of losing it. A plan may also enforce a rolling five-hour allowance that refills several times before the weekly reset. An unstructured request can waste the remaining window on low-value activity, serialize work that could proceed in parallel, or leave changes cut off and unreconciled at a limit or reset.

## Actors

- A project contributor with weekly and rolling five-hour usage limits, plus live information or estimates for their remaining amounts and reset times.
- The primary agent selecting, coordinating, and integrating project work.
- Subagents working on independent, bounded improvements when delegation increases throughput.
- The project maintainer reviewing the resulting changes and handoff.

## Goals

- Maximize the rate of useful, project-conventional improvements while reducing the weekly balance to approximately 2–3% remaining.
- Track both weekly usage and the rolling five-hour allowance, including repeated five-hour refills within one weekly period.
- Inspect the project and select one or more bounded improvements with clear completion points.
- Delegate independent work when the expected parallel speedup exceeds coordination and integration overhead.
- Stop when weekly usage reaches the 2–3% target band, or earlier if uncertainty or the weekly reset boundary makes further work unsafe. Never continue into the next weekly allowance.

## Non-goals

- Spending usage for its own sake without producing useful project outcomes.
- Spending money, changing plans, accessing another account, or expanding permissions.
- Starting detached or unbounded work that can continue past the weekly stop point. A monitored overnight run may wait for and resume after rolling five-hour refills within the same weekly period.
- Automatically committing, pushing, publishing, deploying, or contacting others.
- Bypassing project instructions, required approval gates, or the project's normal security, testing, and review rules.

## Confirmed decisions

- The skill's objective is to use expiring allowance quickly to make one or more useful improvements, targeting 2–3% weekly usage remaining.
- It should monitor weekly and rolling five-hour usage. It may continue after five-hour refills within the current weekly period but must stop before that weekly allowance resets.
- It should use subagents when doing so is efficient and speeds up work.
- When live usage data is unavailable, it may proceed using the user's estimates and must identify them as estimates.
- It should follow the current project's conventions.
- Register it in `engineering` and `full`, but not in the default `workflow` profile.

## Requirements

### Trigger and authority

- Trigger only when the user explicitly asks to burn or use expiring plan allowance productively in the current project. Do not trigger for ordinary improvement requests that do not mention expiring usage.
- Treat the explicit request as authorization to inspect the project and implement small, reversible improvements within project rules.
- Do not infer authorization for external writes, destructive changes, purchases, plan changes, commits, pushes, publication, deployments, or actions that project instructions reserve for human approval.
- If an improvement needs broader scope or violates a project approval gate, leave it as a candidate for follow-up.

### Track both usage windows

- At the start, identify weekly and rolling five-hour remaining usage and reset times from authorized live host information when available; otherwise use the user's estimates.
- State the source and confidence of each value. Never represent an estimate as live telemetry or infer a precise balance from token counts or conversation activity.
- Re-check both balances at meaningful checkpoints, including before starting another work unit and before integrating or validating. When estimates cannot be refreshed, use conservative task and time budgets.
- Aim to stop with 2–3% of weekly usage remaining. Do not intentionally consume the final 2%. If usage data is coarse or estimated, stop when the best supported estimate enters the target band and report the uncertainty.
- Treat each rolling five-hour reset as a refill within the same weekly allowance. If the five-hour allowance is exhausted while weekly usage remains above the target band, the skill may wait for the refill and resume, including during an overnight run, only if it can reliably monitor the reset and stop before the weekly reset.
- Reserve at least 10 minutes before the weekly reset for integration, project-required validation, cleanup, and handoff. Increase that reserve if active work or delegated tasks need longer to stop safely. Do not reserve 20% of the entire weekly window.
- Stop starting work when weekly usage enters the target band, the weekly safety reserve begins, weekly reset timing is uncertain, or the next unit may cross the weekly boundary. The earliest condition wins.
- Do not leave background commands, agents, or other work running across the weekly reset. Before waiting for a five-hour refill, finish or stop current work at a reviewable checkpoint. Do not start a unit too large to stop safely when the five-hour allowance is exhausted.
- If the host cannot reliably observe or wait for a rolling refill, or cannot stop work before weekly reset, do not attempt an unattended overnight cycle. Complete a safe unit and hand off instructions for resuming.

### Select useful work

- Read the applicable agent instructions, project adapter when present, working tree status, and the smallest relevant source-of-truth materials before proposing work.
- Find concrete improvement candidates from current project needs, such as explicitly recorded TODOs, incomplete behavior, clear defects, missing focused validation, or documentation gaps. Confirm candidates against source and project conventions rather than inventing work to consume allowance.
- Prefer high-value, independently finishable changes with low integration risk and short feedback cycles. Rank by expected project benefit, confidence, estimated completion time, and whether the work can finish inside the stop boundary.
- Work on multiple candidates only when each has a clear boundary and the remaining weekly allowance supports integration and validation. Otherwise complete the strongest single candidate.
- Do not expand into broad refactors, speculative features, or unrelated cleanup to fill usage.

### Parallel work with subagents

- Before delegating, identify separable tasks whose implementation and validation can proceed independently. Delegate when expected saved time exceeds setup, coordination, conflict-resolution, and integration time.
- Give each subagent a bounded outcome, relevant project instructions and files, acceptance criteria, validation expectations, the five-hour checkpoint if relevant, and the hard weekly stop deadline including the reserve. Ask agents to report changed files, decisions, validation evidence, remaining work, and whether they have stopped all processes.
- Avoid assigning overlapping edits. Prefer distinct files or isolated worktrees when the repository workflow supports them safely. Do not let parallelism bypass project approval or shared-resource constraints.
- Keep responsibility for usage monitoring, scope, task coordination, integration, stop decisions, and final handoff with the primary agent.
- Monitor delegated work against the same limits. Stop assigning new work early enough to collect results, resolve conflicts, run required checks, and leave a coherent state. Do not allow any subagent or delegated task to continue across the weekly reset. At a five-hour checkpoint, have subagents stop and report; after the refill, the primary agent may assign fresh bounded tasks if weekly usage remains above target.
- If subagents are unavailable or delegation would not save time, work sequentially without treating that as a blocker.

### Complete and hand off

- Inspect the final diff and confirm that each kept change meets its stated acceptance criteria and project conventions.
- Complete relevant, non-destructive validation required by the project, provided it fits within the stop reserve. If it cannot safely finish in time, stop and report it as unverified with exact follow-up steps.
- Leave no known partial generated files, abandoned processes, or unfinished delegated work. If an interrupted change cannot be safely reverted or completed, make its state explicit and provide a recovery step.
- Report the usage and reset source, estimate confidence, stop reason, useful outcomes, changed files, validation results, and remaining follow-up candidates. State whether all agents and processes have stopped.

## Proposed design

Implement this as a standalone, portable skill named `burn` using only shared `name` and `description` frontmatter. Its workflow has five phases: establish the window; inspect and rank candidates; select bounded serial or parallel work; monitor, integrate, and validate before the reserve; hand off. Keep host-specific telemetry access outside the portable instructions; the skill uses any authorized host capability or accepts user estimates.

The primary agent acts as the usage coordinator. It tracks weekly and rolling five-hour balances separately. When the five-hour balance runs out, it may wait for that allowance to refill, then resume useful work while the weekly balance remains above target. It stops at approximately 2–3% weekly usage remaining and before the next weekly reset. Subagents receive bounded assignments and must stop at five-hour checkpoints when needed and at the hard weekly deadline. Only the primary agent chooses work, monitors both balances, integrates changes, and determines when to stop. The skill should be explicit that model usage is an estimate or opaque signal unless the host exposes reliable counters.

Register the skill explicitly in the toolkit catalog and the `engineering` profile during implementation; the `full` profile includes it through its union. Do not rely on a skill-directory glob. The existing toolkit expansion specification defines the catalog as installation source of truth and requires portability rules, a sequential fallback when subagents are unavailable, and representative trigger/outcome evals.

## Security and safety

- Read only usage information authorized by the active host or supplied by the user; do not inspect unrelated accounts, credentials, or private history to estimate usage.
- Follow project data handling, secret redaction, and sandbox rules. Do not expose secrets in agent assignments, logs, or the final handoff.
- Delegation does not grant additional permissions. Subagents inherit the task boundary and may not perform separately gated external or destructive actions.
- Prefer reversible, low-risk improvements. Stop and report rather than improvise where scope, permissions, or data integrity are unclear.
- Treat reset and usage estimates conservatively. Never begin work based on a claim that consumption can be precisely predicted when it cannot.

## Rollout

- Add `burn` as a separately specified skill and catalog entry after human approval.
- Choose the install profile based on the toolkit's catalog conventions during implementation; update any profile intended to include independent project-improvement skills.
- Add positive and negative trigger cases, a representative serial-work case, a parallel-work case, an uncertain-estimate stop case, repeated five-hour refill cases, and a weekly reset/delegation shutdown case.
- Keep host support claims limited to hosts where packaging and representative behavior have been validated.

## Acceptance criteria

1. An explicit request to use expiring usage triggers the skill; an ordinary request to improve a project without an expiring-usage intent does not.
2. The skill checks live usage/reset metadata when available or uses clearly labelled user estimates. It never reports an estimate as exact telemetry.
3. It inspects project instructions and state, chooses concrete project-aligned work, and explains why the selected work is worth doing and bounded.
4. It prefers multiple useful outcomes only when they can finish, integrate, and validate within the window; otherwise it completes a smaller coherent unit.
5. It delegates independent tasks when projected time savings exceed coordination and integration costs, and avoids delegation for overlapping, tightly coupled, or too-small tasks.
6. Every delegated task has a clear acceptance condition and the same stop deadline. The primary agent gathers results and confirms no delegated task or process continues across the stop boundary.
7. The skill aims to stop with 2–3% weekly usage remaining and does not intentionally consume the final 2%. With uncertain estimates, it labels uncertainty and stops when its best supported estimate enters that band.
8. If the rolling five-hour allowance runs out while weekly usage remains above target, the skill may wait and resume after refill, including overnight, provided it can monitor the refill and stop before the weekly reset.
9. The skill keeps at least 10 minutes before weekly reset for integration, validation, cleanup, and handoff, increasing the reserve when active work needs longer to stop. It starts no work that may continue across weekly reset.
10. It leaves reviewable changes, follows project validation and approval rules, and reports any incomplete or unverified work with recovery steps.
11. Its handoff records weekly and five-hour usage sources/confidence, stop reason, changed files, validation evidence, follow-up candidates, and agent/process shutdown status.
12. The portable skill has explicit host-independent fallbacks for unavailable telemetry and unavailable subagents, and is registered in the catalog/profile used by the toolkit.

## Development readiness

### Affected areas

- New `skills/burn/SKILL.md`.
- Toolkit skill catalog and profile membership, per `docs/specs/bwh-agent-toolkit-expansion.md`.
- Trigger, outcome, portability, delegation, and stop-boundary eval fixtures and any validation references required by the catalog.
- README or skill index only if repository conventions require listing active skills there.

### Proposed task outline

1. Write the portable skill instructions and narrow trigger description; include the weekly target, rolling refill, work-selection, delegation, shutdown, and handoff requirements above.
2. Register `burn` in the catalog under `engineering` and ensure it is included in `full`, with dependencies and shared-contract requirements recorded explicitly.
3. Add eval fixtures for explicit versus ordinary improvement triggers, estimated weekly and five-hour usage, serial and parallel work, repeated five-hour refills, the 2–3% weekly target, and reset safety including stopping subagents.
4. Run catalog, portable-skill, and focused eval validation; review the skill against project instructions and ensure its host-independent fallbacks are complete.
5. Produce an implementation handoff with changed files, validation, and any host-specific limitations; do not commit or publish without separate authorization.

### Dependencies

- Human approval of this specification before development.
- Existing toolkit catalog/profile schema and portable skill conventions.
- A host's authorized usage/reset information when available; otherwise estimates supplied by the user.
- A usable subagent capability for parallel speedup; sequential fallback when unavailable.

### Agent-resolved assumptions

- **A1, portable usage input (requirements 2 and 7).** Host telemetry is optional; if unavailable, user estimates are sufficient with explicit uncertainty and a conservative work budget. Observable: the skill names source/confidence and does not block solely because telemetry is absent.
- **A2, weekly stop reserve (requirements 7–9).** Reserve at least 10 minutes before weekly reset for handoff, increasing it for longer active work. The target weekly remainder is 2–3%, with a floor of 2%. Observable: the skill stops at the target band and before reset; it does not use 20% of the full weekly window as a time reserve.
- **A3, rolling refills (requirement 8).** A five-hour reset replenishes the short-term allowance without ending the burn run, if the weekly reset remains ahead and the host can safely monitor and resume. Observable: the skill waits at a clean checkpoint and resumes only within the same weekly allowance.
- **A4, delegation threshold (requirements 5 and 6).** Delegate only when expected time saved exceeds total coordination and integration overhead. Observable: delegated tasks are independent, bounded, and returned early enough to integrate; otherwise work is sequential.
- **A5, skill portability (requirement 12).** Use generic capability descriptions and sequential fallback rather than depending on one host's telemetry or subagent interface. Observable: the skill remains usable when either capability is absent.
- **A6, work selection and scope (requirements 3, 4, and 10).** The explicit `burn` request authorizes the primary agent to choose small, reversible project improvements, but does not waive project gates or external-action authorization. Observable: selected changes are traceable to project evidence and no separately gated action is performed.
### Validation plan

- Run the repository's skill and catalog validators for the new entry.
- Run focused evals for the twelve acceptance criteria, including both balances, crossing one or more five-hour resets, stopping at the weekly 2–3% target, uncertain estimates, parallel work that is wasteful, and delegated work that threatens the weekly stop boundary.
- Review the rendered skill instructions for portable frontmatter, generic host references, explicit approval boundaries, and consistency with the toolkit catalog specification.
- Confirm all stop paths leave a coherent report and do not imply precise usage prediction.

### Risks and mitigations

- **Usage estimates may be inaccurate.** Label source and confidence, re-check live signals when available, and stop when uncertainty could cause the run to cross the weekly reset or consume below the target band.
- **Parallel work can add conflicts and integration costs.** Delegate only independent tasks, make the primary agent accountable for integration, and account for overhead in the delegation threshold.
- **A five-hour or weekly limit can interrupt active work.** Use short work units and checkpoints. Wait for a five-hour refill only at a safe checkpoint, and stop all work before the weekly reset.
- **The desire for speed can encourage low-value edits.** Require concrete project evidence and acceptance criteria for each selected task; don't create work merely to fill usage.
- **The new skill is outside the nine additions in the approved toolkit expansion spec.** Treat this as an additive, separately approved change and update the catalog explicitly when implemented; do not silently alter the prior approved spec.

## Decisions and open questions

### Confirmed

- Use expiring allowance quickly to produce one or more useful project improvements, aiming for 2–3% weekly usage remaining.
- Monitor weekly and rolling five-hour limits. Permit repeated five-hour refills within the same weekly period; stop before the weekly reset.
- Use subagents where parallelism is efficient and improves speed.
- Accept user-provided usage/reset estimates when live data is unavailable and label uncertainty.
- Follow project conventions and existing authority boundaries.
- Include `burn` in the `engineering` and `full` profiles. Project installs using only the default `workflow` profile will not receive it automatically.

### Open for human review

- None.
