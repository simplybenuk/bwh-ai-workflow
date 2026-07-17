# Case: persisted discovery brief

## Prompt

Explore a bounded product idea far enough that it can move into specification.

## Expected invariants

- Resolve the discovery location from the project adapter or established repository conventions.
- Create the complete discovery brief as a repository artifact.
- Use `docs/discovery/<descriptive-name>.md` only when the repository provides no convention.
- Respect repository guardrails that prohibit modifying the resolved or fallback location.
- Read the artifact back and verify its required contents.
- Return a concise handoff rather than duplicating the complete discovery brief in chat.
- Do not create a specification, implementation tasks, or code.

## Expected output

One outcome sentence and no more than four short bullets covering the discovery artifact path, material assumptions or decisions, persistence validation, and the `bwh-spec` handoff.
