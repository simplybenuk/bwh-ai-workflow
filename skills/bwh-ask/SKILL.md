---
name: bwh-ask
description: Answer a question about the repository, an idea, or the workflow state without creating or advancing any artifact. Use before ideation, mid-spec, mid-development, or whenever a quick answer is needed without triggering a workflow stage.
---

# Ask

Apply the shared contracts in `../../contracts/collaboration.md` and `../../contracts/context-loading.md`, plus the consuming project's adapter.

## Goal

Answer the question accurately using the smallest relevant context. Produce no artifact and advance no workflow state.

## Non-goal

Do not create, edit, or persist any file. Do not advance, infer, or report a transition in `states.md`. If the question's answer would naturally become a discovery brief, specification, task, or review, answer the question directly here and name the skill that produces that artifact rather than producing it.

## Workflow

1. Identify what is actually being asked and the smallest set of sources that can answer it: code, an existing artifact, a contract, or prior conversation context.
2. Read only what is needed to answer. Do not read the entire repository by default.
3. If sources conflict or the answer is genuinely unknown from available context, say so rather than guessing.
4. Answer directly. If the answer surfaces a decision, risk, or gap that matters for later work, name it but do not resolve it here.

## Stop conditions

Stop and say the question cannot be answered from available context, rather than speculating, when the repository has no evidence either way.

## Handoff

None required. If the conversation is heading toward creating or changing an artifact, name the appropriate next skill (for example `bwh-ideate`, `bwh-spec`, `bwh-refine-spec`, `bwh-development`) instead of proceeding here.

## Output

Answer the question directly. Add at most two short bullets only when relevant:

- open decision or gap surfaced by the answer
- suggested next skill, if the conversation implies producing or changing an artifact
