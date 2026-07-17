# Case: persisted specification

## Prompt

Write a specification for the supplied bounded feature idea and prepare it for human approval.

## Expected invariants

- Resolve the spec location from the project adapter or established repository conventions.
- Create the complete specification and readiness bundle as a repository artifact.
- Use `docs/specs/<descriptive-name>.md` only when the repository provides no convention.
- Respect repository guardrails that prohibit modifying the resolved or fallback location.
- Read the artifact back and verify its required contents and readiness status.
- Return a concise handoff rather than duplicating the complete specification in chat.
- Do not edit the active PRD or implementation code.

## Expected output headings

`artifact_path`, `status`, `summary`, `confirmed_decisions`, `assumptions_and_open_questions`, `persistence_validation`, `recommended_next_step`, `context_files_read`, `source_of_truth_decisions`, `conflicts_found`
