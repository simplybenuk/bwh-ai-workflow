---
name: burn
description: Use only when the user explicitly asks to spend soon-expiring usage in the current project productively. Find and complete useful project improvements quickly, monitor weekly and rolling five-hour limits, use subagents when parallel work saves time, and stop at the weekly 2–3% remainder target before the weekly reset.
---

# Burn expiring usage

Apply the shared contracts in `../../contracts/autonomy.md`, `../../contracts/collaboration.md`, `../../contracts/completion.md`, `../../contracts/context-loading.md`, and `../../contracts/handoff.md`, plus the current project's instructions and adapter when present.

## Goal

Use soon-expiring allowance at a high rate to make one or more useful improvements in the current project. Aim to stop with 2–3% of the weekly allowance remaining. A rolling five-hour refill is a chance to continue within the same weekly period. Never continue into the next weekly allowance.

## Workflow

1. **Establish both limits.** Read remaining weekly usage, remaining rolling five-hour usage, and both reset times from authorized host information when available. Otherwise ask the user for estimates or use estimates they already supplied. Record which values are live and which are estimates. Do not infer precise usage from transcript length, token counts, or conversation activity.
2. **Confirm a safe run window.** Work out when the weekly allowance resets and reserve at least 10 minutes before then for integration, required validation, cleanup, and handoff. Increase the reserve if active work, validation, or delegated tasks need longer to stop safely. If weekly reset timing is unknown or too uncertain to protect, do bounded work that can finish now and hand off rather than starting a long run.
3. **Inspect and rank work.** Read the applicable project instructions, adapter, working tree state, and the smallest relevant source-of-truth files. Find concrete opportunities such as recorded TODOs, a reproducible defect, incomplete behavior, focused validation gaps, or documentation that is wrong or missing. Rank candidates by project benefit, confidence, time to finish, and integration risk. Do not invent work just to consume usage.
4. **Choose bounded work.** Prefer short tasks with clear acceptance conditions and quick feedback. Choose more than one improvement only when each can be finished, integrated, and checked before the weekly stop boundary. If the next work unit might take weekly usage below 2%, choose a smaller unit or stop early and report why.
5. **Delegate useful independent tasks.** Split work when the expected time saved exceeds setup, coordination, conflict-resolution, and integration time. Assign non-overlapping areas where possible. Give each subagent the relevant project instructions, bounded outcome, acceptance conditions, validation expectations, five-hour checkpoint, and hard weekly stop time including the reserve. Keep usage monitoring, scope, task selection, integration, and stop decisions with the primary agent. If delegation is unavailable or slower, work sequentially.
6. **Monitor and work in checkpoints.** Re-check both balances before starting another unit and before integration or validation. When usage is estimated and cannot be refreshed, use smaller tasks and stop more conservatively. Complete or pause delegated work at a reviewable checkpoint before waiting for a five-hour refill. Have all subagents stop and report before the refill; after it, resume with fresh bounded tasks only if the weekly allowance remains above target.
7. **Wait for a five-hour refill only when safe.** If the rolling five-hour allowance is exhausted but weekly usage remains above target, wait for its reset only if the host can reliably observe the reset and resume. An overnight run may cross one or more rolling five-hour refills within the same weekly period. Do not leave commands, subagents, or other work running during the wait. If the host cannot safely wait and resume, finish a coherent unit and hand off resume instructions instead of running unattended.
8. **Stop at the weekly target or boundary.** Aim to stop when 2–3% of weekly usage remains. Do not intentionally consume the final 2%. Stop starting work as soon as the best supported live reading or estimate enters the target band. Stop earlier if the next unit might cross below 2%, the 10-minute weekly reserve begins, reset timing becomes uncertain, or active work cannot be stopped safely before weekly reset. The earliest condition wins. Never carry work into the next weekly allowance.
9. **Integrate and hand off.** Inspect the final diff. Complete relevant, non-destructive project validation if it fits before the weekly boundary and within the reserved time. Otherwise leave the change in a coherent state and name the unverified checks with exact follow-up steps. Confirm every delegated task and process has stopped. Report useful outcomes, changed files, validation, usage sources and confidence, why work stopped, follow-up candidates, and whether all agents and processes have stopped.

## Work and authority boundaries

- The explicit request authorizes inspection and small, reversible project improvements that follow project rules. It does not authorize purchases, plan changes, account access, destructive actions, commits, pushes, publication, deployments, or external communication.
- Preserve local changes. Do not overwrite the user's work or select a candidate that conflicts with another active task.
- Follow project approval gates. Leave work that requires broader scope or separate authority as a follow-up candidate.
- Delegation does not grant more authority. Every subagent inherits the same project rules, usage constraints, and stop boundary.
- Never claim a precise usage balance unless the active host provides it. Do not claim a run can be stopped at exactly 2–3% when usage is uncertain or consumed in coarse steps.
- Do not start detached, non-interruptible, or unbounded work near a limit. If the host cannot stop active work or delegated tasks safely before the weekly reset, do not start a long or overnight run.

## Stop conditions

Stop starting new work when any of these apply:

- Weekly usage is in the 2–3% target band, or the next work unit could intentionally consume the final 2%.
- The weekly stop reserve has begun.
- The weekly reset time is unknown or too uncertain to protect.
- A task, validation step, or delegated assignment may continue beyond the weekly reset.
- Waiting for a five-hour refill cannot be monitored and resumed safely.
- A project rule, permission, or data-integrity concern makes the next improvement unsafe.

At a stop condition, leave the best coherent state available, stop or collect all delegated work, and hand off. Do not spend usage merely to hit an exact number.

## Reduced capability

- If usage counters are unavailable, use user estimates and label their confidence. If no reasonable estimate of weekly reset is available, do not start work that could outlast the safe window.
- If subagents are unavailable or overhead would outweigh the speedup, work sequentially.
- If reliable timers or resumable execution are unavailable, do not leave the agent waiting unattended through a five-hour reset. Complete a bounded unit and tell the user what to resume after the refill.
- If project-specific validation cannot finish before the weekly stop, report it as unverified instead of starting it too late.
