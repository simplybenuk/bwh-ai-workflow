---
name: bwh-write-agent-instructions
description: Design, revise, or audit instructions whose primary reader is an agent, including skills, shared contracts, adapters, project agent instruction files, and documents reached through pointers. Use for trigger design, instruction hierarchy, context cost, completion criteria, pruning, and behavioral evals. Do not use for general technical documentation owned by bwh-technical-writing.
---

# Write agent instructions

Design agent-facing documents around observable behavior. Keep host discovery, installation paths, invocation syntax, and model selection in routed host references rather than portable instructions.

Apply `../../contracts/context-loading.md`, `../../contracts/autonomy.md`, and the consuming project's adapter when present.

## Workflow

1. Identify the document type, intended behavior, authority boundary, and where the document sits in the instruction hierarchy. Resolve the project agent instruction file and agent home through the host convention contract when those locations matter.
2. Define the trigger boundary before drafting. List positive triggers, near-miss negative triggers, and likely missed phrasings. Treat every pointer's wording as routing logic.
3. Map the source of truth for each rule. Keep one authoritative copy. Point to shared rules instead of restating them.
4. Separate ordered actions from reference material. Keep steps prominent. Move material needed by only one branch into a directly linked reference.
5. End each procedural step with a checkable completion condition. Make the condition demanding enough to prevent a plausible partial result from passing.
6. Prune cached facts the agent can cheaply read from the environment. Remove stale, duplicated, irrelevant, and behaviorally inert instructions.
7. Evaluate routing and behavior with positive triggers, negative triggers, missed triggers, and representative outcomes. Include authority and reduced-capability cases.
8. Report what changed, what remains authoritative, and which behavior still lacks evidence.

Read [references/review-checklist.md](references/review-checklist.md) when auditing an existing instruction set or preparing eval cases.

## Design rules

- Spend always-loaded context only on routing and rules needed on nearly every run. An explicit skill costs the human memory instead, so reserve it for work that needs deliberate invocation.
- Write a pointer that names both the material and the distinct conditions that require it. Collapse synonyms that describe the same branch.
- Co-locate a concept's definition, constraints, and exceptions. Avoid chains of references more than one hop deep.
- Phrase the desired action directly. Use prohibitions only for hard safety boundaries, paired with the safe action.
- Preserve project vocabulary and existing instruction precedence. Report conflicts rather than silently choosing a winner.
- Do not place secrets, private history, transient machine facts, or raw conversation content in agent instructions.

## Capability fallbacks

If independent readers are available, give each a raw trigger or outcome case and compare results. Otherwise, run the cases sequentially and label that limitation. If structured questions are unavailable, ask the same numbered questions in plain chat. Do not weaken completion criteria because an optional capability is missing.

## Authority

Editing the requested local instruction artifact is in scope. Installing skills, changing profiles, deleting instructions, committing, pushing, publishing, or writing to an external system requires separate authority. Show conflicting local changes before replacement.

## Output

Return the artifact or proposed diff, the trigger boundary, the source-of-truth map, eval results, unresolved conflicts, and any separately authorized next action.
