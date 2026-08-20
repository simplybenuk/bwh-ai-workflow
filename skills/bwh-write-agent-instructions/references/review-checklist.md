# Agent instruction review checklist

Use this checklist after understanding the intended behavior.

## Routing

- Does the trigger name the task and its distinct branches?
- Do two instructions claim the same request?
- Can a likely user phrase miss every pointer?
- Does a negative case activate the instruction unexpectedly?

## Hierarchy

- Are ordered steps visible before branch-specific reference?
- Does each pointer say when to follow it?
- Is any required rule hidden behind more than one pointer?
- Does the project-specific instruction override shared guidance only where it needs to?

## Completion

- Can the agent test whether each step is complete?
- Would a plausible partial result pass the stated condition?
- Are evidence, validation, and stop conditions explicit?
- Are external writes and destructive actions separated from analysis?

## Pruning

- Is the same rule stated in more than one place?
- Can the environment supply a fact cheaply and more accurately?
- Is any instruction stale, unrelated to the behavior, or already the model's reliable default?
- Can a branch-only detail move behind a direct pointer?

## Evaluation

- Run at least two positive trigger cases.
- Run at least two near-miss negative cases.
- Add a missed-trigger probe using different wording.
- Test one successful outcome, one stop or safety case, and one reduced-capability case.
- Record evidence and failures without rewriting the test to match the output.
