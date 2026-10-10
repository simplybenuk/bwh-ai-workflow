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
- Persist detailed execution evidence in the project's planning or progress artifact.
- Return a compact handoff without repeating the approved spec or exhaustive traceability.

## Expected output

A compact outcome with the authoritative plan, material changes, validation, relevant blockers or commit status, and the `bwh-agent-review` handoff. Preserve project-required formats; no fixed chat headings are required.
