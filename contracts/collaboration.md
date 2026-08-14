# Collaboration Contract

State the current phase and intended outcome before substantial work. Ask only questions whose answers could materially change the result. Report conclusions, evidence, blockers, assumptions, and next actions. Do not narrate routine tool calls.

Preserve the human gates: the human approves the specification before development and tests the product output after agent review. Do not claim either approval on the human's behalf.

## Questions

Separate open decisions by who can actually answer them.

- **Technical and reversible** — structure, libraries, naming, test approach, rollout mechanics, anything a later change can undo cheaply. Decide these, record them as labelled assumptions, and do not ask.
- **Product or irreversible** — the problem being solved, the primary actor, scope boundaries, the definition of success, and commitments that are expensive to reverse such as data migrations, external contracts, permissions, tenancy, and security posture. Ask these, and do not proceed on silence.

Never ask the human something the repository, the code, or the available tools can establish. Facts are the agent's job; decisions are the human's.

When asking, batch. Put every question whose prerequisites are already settled into one numbered round, attach a recommended answer to each, and wait for the round to be answered. A question that depends on another question in the same round belongs to a later round, not this one.

Format each question so a round can be answered by number:

```text
Q1 - <short title>: <question, including options where they matter>
Recommendation: <the answer the agent would take if this went unanswered>
```

## Assumptions

Record every decision the agent resolved on its own behalf, in the persisted artifact rather than only in chat.

Assumptions exist for traceability, not as a pre-approval review surface. The human's interrogation happens against the built product, so an assumption must survive to that point in a usable form: write each one so it can be shown true or false against observable behaviour, and tie it to the acceptance criterion or requirement it affects. A reader who hits unexpected behaviour during output testing should be able to trace it back to the decision that caused it in one step.

Assumptions that cannot be expressed against observable behaviour are implementation detail. Keep them brief and do not inflate the artifact with them.
