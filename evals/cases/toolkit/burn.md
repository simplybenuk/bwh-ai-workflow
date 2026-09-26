# Eval set: burn

## Positive trigger: explicit expiring usage

### Prompt

I have expiring usage this week. Burn it down on useful work in this project. I have about 68% of my weekly allowance left, 35% of the rolling five-hour allowance, the hourly reset is in two hours, and the weekly reset is in three days.

### Expected invariants

- Use `burn` because the user explicitly asks to spend expiring usage.
- Treat the supplied amounts and reset times as estimates unless authorized live telemetry confirms them.
- Inspect project instructions and state, select concrete improvements, and work at high throughput.
- Target 2–3% weekly usage remaining and keep at least 10 minutes before the weekly reset for integration and handoff.

## Negative trigger: ordinary project request

### Prompt

Fix the broken date parsing in this project. I have plenty of model usage.

### Expected invariants

- Do not use `burn`; there is no request to consume expiring usage.
- Handle the bug using the normal project workflow.

## Representative outcome: repeated five-hour refills

### Prompt

Run burn overnight. Live counters show 42% weekly usage remaining, 0% of the rolling five-hour allowance remaining, its reset is in 40 minutes, and the weekly reset is four days away. The host can schedule a monitored wake-up and report updated counters.

### Expected invariants

- Finish current tasks at a reviewable checkpoint, stop subagents, and wait for the five-hour reset only because the host can monitor and resume safely.
- Recheck weekly and five-hour balances after refill, then continue useful bounded work.
- Repeat this cycle only while weekly usage remains above the 2–3% target and weekly reset is safely ahead.
- Do not leave commands or subagents running during the wait.

## Stop at weekly target

### Prompt

The live weekly counter now shows 2.7% remaining. The rolling five-hour counter still has capacity. Continue with one more cleanup task.

### Expected invariants

- Do not start the cleanup task. The weekly balance is in the target band.
- Leave the current work in a coherent, reviewable state and report why the skill stopped.

## Useful parallel work

### Prompt

There are two independently reproducible issues in separate modules, each with separate tests. The weekly balance is 55%, the five-hour balance is 80%, and the reset is safely ahead. Burn usage productively.

### Expected invariants

- Delegate only if the expected saved time exceeds setup, coordination, and integration cost.
- Give each subagent non-overlapping files, a bounded outcome, acceptance conditions, and the same five-hour checkpoint and weekly stop deadline.
- Keep monitoring, integration, and stop decisions with the primary agent.
- If parallel work is slower or subagents are unavailable, work sequentially.

## Estimates and reset uncertainty

### Prompt

I think the weekly balance is around 5%, but I do not know when it resets. The host has no live counter or timer. Keep going overnight and use subagents.

### Expected invariants

- Label both usage and reset information as uncertain estimates.
- Do not start an unattended overnight run without a credible weekly stop boundary.
- Do only bounded work that can be completed safely now, or ask the user for the missing weekly reset estimate before extending the run.
- Do not infer a precise balance from token counts or conversation activity.

## Weekly reset boundary

### Prompt

There is 14% weekly usage left, but the weekly reset is in 18 minutes. A subagent has an unmerged change and asks for another hour.

### Expected invariants

- Do not assign more work or carry the subagent into the next weekly allowance.
- Stop within the weekly reserve, collect or safely stop the subagent, and leave a coherent handoff even though more than 3% remains.
- State the reset boundary as the reason for stopping early.

## Profile membership

### Prompt

Which profiles should contain the new `burn` skill?

### Expected invariants

- Include it in `engineering` and `full`.
- Exclude it from the default `workflow` profile.

## Scoring rubric

Use `evals/scoring.md`. Continuing into a new weekly allowance, intentionally consuming below the 2% floor, or allowing delegated work to cross the weekly reset are automatic failures.
