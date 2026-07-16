# bwh-ai-workflow

Reusable agent scaffolding, workflow contracts, custom skills, and regression evals for spec-driven software delivery.

## Design

- `skills/` contains reusable workflow skills.
- `contracts/` contains shared autonomy, handoff, and completion rules.
- `adapters/` contains project-specific policies and validation commands.
- `evals/` contains representative cases and scoring guidance.

The core stays model-agnostic. Projects supply their own source-of-truth files, task schema, validation commands, security rules, and release policy through an adapter.

## Initial workflow

```text
idea -> spec -> optional risk review -> PRD -> task execution -> validation
```

The risk review is conditional for architecture, tenancy, permissions, security, migration, rollout, or recovery-sensitive work.
