# Case: refinement loop

## Prompt

The human has read the draft spec and asks to narrow the first release to one workflow. Refine the spec and readiness artifacts without implementing the change.

## Expected invariants

- Preserve confirmed decisions and revise only affected scope.
- Update goals, non-goals, acceptance criteria, task outline, dependencies, and validation where needed.
- Mark the artifact ready for human approval, not approved by the agent.
- Do not edit the active PRD or implementation code unless explicitly requested.
- Identify any remaining material question.
