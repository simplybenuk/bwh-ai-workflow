---
name: bwh-grill
description: Run an exhaustive, decision-tree interview about a plan, design, or idea. Trigger only when the user explicitly asks to be grilled, interrogated, exhaustively questioned, or stress-tested through questions. Do not trigger for ordinary clarification, ideation, specification, review, or requests to implement work.
---

# Grill a decision

Question the user until the decision tree has no unresolved branch. This explicit interview mode does not replace the normal BWH rule to minimize questions.

## Build the decision tree

1. State the subject and intended outcome of the interview.
2. Inspect the repository and available evidence for discoverable facts. Do not ask the user for facts the environment can establish.
3. Map each unsettled decision and the decisions that depend on it.
4. Define the current frontier as decisions whose prerequisites are settled.
5. Ask only the frontier in the current round.

If independent workers are available, they may research separate factual prerequisites. Otherwise research them sequentially. An unresolved fact blocks only its dependent branch, not unrelated frontier questions.

## Ask each round

Number every question and include a recommendation:

```text
Q1 - <short title>: <decision, options, and material trade-offs>
Recommendation: <recommended answer and concise reason>
```

Use a structured question interface when one is available. Otherwise use the plain-text format above. Ask the full current frontier together, then wait. Do not answer for the user or continue down a dependent branch before its prerequisite is settled.

This explicit mode may return reversible technical decisions to the user. Product scope, success criteria, permissions, security posture, external contracts, and expensive-to-reverse choices always remain human decisions.

## Recompute until settled

After each answer:

1. update the decision tree;
2. identify conflicts, new branches, and closed branches;
3. research newly discoverable facts;
4. ask the next frontier.

When no branch remains, summarize the shared understanding and ask the user to confirm it. Do not act on the result, edit implementation files, commit, push, publish, or make external changes.

## Optional decision record

Only when the user asks to capture the result, persist a concise record containing:

- the subject and desired outcome;
- settled decisions and reasons;
- evidence-backed facts;
- explicit non-goals;
- unresolved uncertainty, if any;
- the recommended next workflow.

Route an early idea to `bwh-ideate`, a settled design needing a specification to `bwh-spec`, and feedback on an existing draft to `bwh-refine-spec`. Persisting the record does not authorize the next workflow or implementation.
