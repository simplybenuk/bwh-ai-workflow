# bwh-ai-workflow

Reusable agent scaffolding, workflow contracts, custom skills, and regression evals for spec-driven software delivery.

## Design

- `skills/` contains reusable workflow skills.
- `contracts/` contains shared autonomy, handoff, and completion rules.
- `adapters/` contains project-specific policies and validation commands.
- `evals/` contains representative cases and scoring guidance.

The core stays model-agnostic. Projects supply their own source-of-truth files, task schema, validation commands, security rules, and release policy through an adapter.

## Workflow

```text
bwh-ideate -> bwh-spec -> bwh-refine-spec (repeat) -> bwh-development -> bwh-agent-review -> human output testing
```

The human has two deliberate gates: read and approve the spec, then test the resulting product behavior. Readiness for development is a state recorded in the spec, not a separate user-facing stage. The agent review sits between implementation and human testing and checks the implementation against the approved spec, project guardrails, and validation evidence.

Available skills:

- `bwh-ideate` — turn an early idea into a bounded direction and discovery brief.
- `bwh-spec` — create the decision-ready specification and its development-readiness artifacts.
- `bwh-refine-spec` — repeatedly revise the spec and readiness artifacts until the human approves it.
- `bwh-development` — implement the next bounded task with project validation.
- `bwh-agent-review` — independently review the completed work before human output testing.

The agent review is conditional in depth, but should be used for every substantive implementation task. The review must not silently become a second implementation pass; it reports findings and requests targeted fixes when needed.
