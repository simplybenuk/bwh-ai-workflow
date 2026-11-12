---
name: bwh-maintainability
description: Improve maintainability through a bounded implementation round grounded in representative change tasks and observed repository costs. Use for iterative maintainability work; exclude standalone architecture audits, bug-only fixes, documentation-only edits, and speculative rewrites.
---

# Improve maintainability

Use this skill when the user commissions iterative changes to make a bounded area easier to understand, verify, or safely change. Route read-only structural surveys to architecture review, defects to bug diagnosis, and docs-only work to technical writing.

## Required workflow

1. Read and follow [improvement rounds](../../contracts/improvement-rounds.md) for cadence, evidence, independent review, checkpoints, and authority.
2. Read and follow [model routing](../../contracts/model-routing.md) for toolkit model selection and delegation.
3. Read project instructions, architecture decisions, ownership boundaries, verification guidance, and existing behavior tests.

The shared contract controls iteration and human checkpoints. This skill owns the maintainability scope and relevant evidence.

## Establish a bounded change surface

1. Identify the subsystem, recurring change pressure, and user-visible or operational behavior that must remain correct.
2. Inspect recent representative changes, callers, interfaces, tests, dependency direction, and local conventions. Record the revision and worktree state.
3. Define a few representative bounded change tasks. Use actual recent tasks when available; otherwise mark plausible tasks as hypothetical and keep conclusions limited.
4. Trace how each task currently crosses files, modules, interfaces, dependencies, and tests. Cite observed evidence for each claimed cost.
5. State exclusions and avoid broadening into architecture redesign, unrelated cleanup, or behavior changes without authority.

## Gather proportionate evidence

Before editing, select indicators that help explain the chosen tasks. They may include:

- locations that must be understood or edited to complete a task;
- repeated knowledge or duplicated behavior encountered on the path;
- dependency or interface crossings and tests coupled to implementation details;
- time or steps to make and verify the change in a controlled exercise;
- regressions or incorrect outcomes in relevant behavior checks.

Describe method, task, revision, files or symbols inspected, environment, and coverage. Treat locality, duplication, coupling, and change time as indicators with context, not as proof of quality. Do not set a target based on lines of code, a complexity score, or a combined maintainability metric. A small proxy exercise is not evidence of team-wide productivity.

## Review and improve

Assess judgment categories separately, citing code, interfaces, tests, or representative changes:

- locality of related behavior and change knowledge;
- clarity of module responsibilities and dependencies;
- ease of verifying behavior at stable boundaries;
- amount of incidental coordination or duplicated reasoning;
- fit with documented architecture decisions and near-term change pressure.

Use N/A with a reason when a category does not apply. Keep reviewer judgments separate from counts, task outcomes, and elapsed time. Do not treat reviewer consensus or a score as proof that a structure is correct.

Rank candidate changes by observed cost reduction, confidence, risk, and verification cost. Make one bounded pass on commissioned recommendations. Preserve public interfaces and existing behavior unless explicitly authorized to change them. Prefer concrete simplification supported by current evidence; avoid speculative abstractions, general rewrites, or cleanup unrelated to selected tasks.

## Validate and checkpoint

1. Run project-required checks and targeted behavior tests before and after the change.
2. Repeat the representative tasks or trace the same paths under comparable conditions. Record the change locality, dependencies, test boundaries, or other selected indicators before and after.
3. Check callers, interfaces, data flow, and relevant consumers for behavior changes or regressions. Note gaps in test coverage rather than assuming correctness.
4. Fix in-scope regressions and refresh affected evidence if the fix changes assessed paths.
5. Complete the after assessment and fresh suggestions required by the improvement-rounds contract.
6. Present the bounded change, behavior evidence, maintainability indicators, uncertainty, and ranked next suggestions at the required human checkpoint. Stop until the human selects or steers further work.

Keep source diffs and relevant verification output linked from the run record. If a representative task or check cannot be performed, state that limit plainly and mark its result unknown.
