---
name: bwh-ideate
description: Turn an early product or engineering idea into a bounded discovery brief with the problem, desired outcome, actors, constraints, options, and questions needed before writing a specification.
---

# Ideate

Apply the shared contracts in `../../contracts/autonomy.md`, `../../contracts/collaboration.md`, `../../contracts/completion.md`, `../../contracts/handoff.md`, and `../../contracts/model-routing.md`.

## Goal

Create enough shared understanding to begin a useful specification without prematurely designing or implementing the solution.

## Workflow

1. State the idea, affected actors, problem, opportunity, and desired outcome.
2. Separate known facts, assumptions, and decisions still needed.
3. Identify likely scope, non-goals, dependencies, risks, and success signals.
4. Compare only the options that could materially change direction.
5. Resolve the discovery location and format from the project adapter or established repository conventions. If neither defines one, use `docs/discovery/<descriptive-kebab-case-name>.md`. Stop and report a blocker instead if repository guardrails prohibit writing there.
6. Write a concise discovery brief suitable for `bwh-spec` into the consuming repository. Include the problem and outcome, actors, known facts, assumptions, decisions needed, scope and non-goals, success signals, risks, dependencies, and materially different options.
7. Read the persisted brief back and verify that its path and required contents are present. Do not report completion if the artifact was not created successfully.

Apply the question and assumption rules in `../../contracts/collaboration.md`. Ask only about product direction, the primary actor, scope boundaries, the definition of success, or a commitment that would be expensive to reverse. Decide technical and reversible matters and record them as labelled assumptions tied to the outcome they affect.

The repository file is the authoritative output. Do not substitute a discovery brief published only in chat or duplicate the complete brief in the final response.

## Stop conditions

Stop before proposing a direction when the problem, primary actor, or desired outcome is unknowable from available context and a reasonable assumption would be risky. Do not stop for a technical choice the agent can make and record.

## Handoff

Return a compact handoff with the repository-relative discovery path, a one-sentence outcome, material decisions still needed, and the recommended next step: `bwh-spec`.

## Output

Use one outcome sentence followed by at most four short bullets covering:

- discovery artifact path
- material assumptions or decisions still needed
- persistence validation
- recommended next step: `bwh-spec`
