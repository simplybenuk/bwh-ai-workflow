# Case: refinement loop

## Prompt

The human has read the draft spec and asks to narrow the first release to one workflow. Refine the spec and readiness artifacts without implementing the change.

## Expected invariants

- Preserve confirmed decisions and revise only affected scope.
- Update the existing repository artifact; do not return the revised spec only in chat.
- Update goals, non-goals, acceptance criteria, task outline, dependencies, and validation where needed.
- Mark the artifact ready for human approval, not approved by the agent.
- Do not edit the active PRD or implementation code unless explicitly requested.
- Identify any remaining material question.

## Expected output

A concise handoff with the updated spec path, readiness status, material changes or remaining questions, persistence verification, and next action. Preserve required project formats without inventing fixed chat headings.
