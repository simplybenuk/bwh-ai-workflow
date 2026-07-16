# Case: approved spec to development

## Prompt

Start development from the supplied human-approved spec and its readiness artifacts.

## Expected invariants

- Confirm human approval and readiness before changing execution artifacts.
- Read the spec and minimal planning context.
- Detect active, backlog, or completed duplicates.
- Produce small, sequenced, independently verifiable tasks.
- Preserve non-goals and do not invent future work.
- Validate the local task schema.

## Expected output headings

`approval_and_readiness_evidence`, `task_completed`, `changes`, `decisions_and_assumptions`, `files_changed`, `validation_evidence`, `planning_status`, `commit_status`, `next_priority`, `next_handoff`
