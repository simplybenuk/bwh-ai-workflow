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
ideate -> spec -> ready for development -> development -> agent review -> human output testing
```

The human has two deliberate gates: read and approve the spec, then test the resulting product behavior. The agent review sits between implementation and human testing and checks the implementation against the approved spec, project guardrails, and validation evidence.

Available skills:

- `bwh-ideate` — turn an early idea into a bounded direction and discovery brief.
- `bwh-spec` — create the decision-ready specification for human approval.
- `bwh-ready-for-development` — convert an approved spec into executable PRD work and check readiness.
- `bwh-development` — implement the next bounded task with project validation.
- `bwh-agent-review` — independently review the completed work before human output testing.

The agent review is conditional in depth, but should be used for every substantive implementation task. The review must not silently become a second implementation pass; it reports findings and requests targeted fixes when needed.
