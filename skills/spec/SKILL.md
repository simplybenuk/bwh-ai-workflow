---
name: bwh-spec
description: Turn a rough product or engineering idea into a bounded, decision-ready specification for downstream planning and execution.
---

# Spec

## Goal

Produce a decision-ready spec that another agent can translate into independently verifiable implementation tasks.

## Workflow

1. Establish the problem, affected actors, desired outcome, constraints, and work type.
2. Inspect only the smallest useful set of project planning and source-of-truth artifacts.
3. Ask only questions whose answers could materially change scope or design. Otherwise record explicit assumptions.
4. Define goals, non-goals, requirements, proposed design, risks, security, rollout, tests, acceptance criteria, decisions, and material open questions.
5. Review task readiness before handing off.

Use the consuming project's spec conventions. Keep the spec model-agnostic and proportional to the work.

## Stop conditions

Stop for user input when a missing decision would materially change product direction, architecture, permissions, tenancy, security, migration, rollout, or recovery. Otherwise continue with a labelled assumption.

## Handoff

Return the spec path or artifact, confirmed decisions, assumptions, open questions, and recommended next step. Do not edit execution plans unless explicitly requested.
