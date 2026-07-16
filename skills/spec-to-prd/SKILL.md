---
name: bwh-spec-to-prd
description: Convert a settled product or engineering specification into small, sequenced, independently verifiable execution tasks using the consuming project's PRD schema.
---

# Spec to PRD

## Goal

Translate the referenced spec into executable tasks without inventing scope or weakening project guardrails.

## Workflow

1. Read the referenced spec first, then the smallest planning context needed to place work correctly.
2. Extract outcome, requirements, non-goals, affected surfaces, dependencies, risks, rollout constraints, and verification needs.
3. Check active, backlog, and completed work for duplicates.
4. Create small, outcome-oriented tasks sequenced from foundations and contracts through integrations, UX, and polish.
5. Validate the local PRD schema and report assumptions or excluded questions.

Use the consuming project's task schema. Prefer 2–6 tasks for a normal feature; split cross-cutting or risky work further.

## Stop conditions

Stop before editing the PRD when a material open question changes implementation scope, or when the referenced spec cannot be found. Do not invent scope.

## Handoff

Return the task count, categories/chunks, duplicate checks, assumptions, and validation evidence.
