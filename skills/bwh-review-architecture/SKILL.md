---
name: bwh-review-architecture
description: Review a bounded subsystem for evidence-backed architecture improvements when maintenance, comprehension, testing, or change locality is costly. Use for a pre-spec structural survey and ranked refactor candidates. Do not use for post-implementation acceptance review owned by bwh-agent-review, and stop before interface design or implementation.
---

# Review architecture

Survey structure to find costly seams worth exploring. This is a read-only review apart from a requested report. It does not approve a refactor or design its interface.

Apply `../../contracts/context-loading.md`, `../../contracts/autonomy.md`, and the consuming project's adapter when present.

## Workflow

1. Bound the survey to the subsystem or pain point named by the user. If none is named, inspect recent change history and choose the smallest area with repeated change pressure. State the inferred boundary.
2. Read architecture decisions, project agent instructions, domain vocabulary, and relevant tests before judging the structure. Project terminology remains authoritative.
3. Trace representative changes through callers, interfaces, dependencies, tests, and data flow. Record observed costs such as scattered edits, repeated knowledge, awkward setup, leaky seams, or tests coupled to internals.
4. Apply the lens in [references/architecture-lens.md](references/architecture-lens.md). Declare it as one review lens, not a project mandate.
5. Reject candidates without repository evidence of current cost or plausible near-term change pressure. Note conflicts with architecture decisions rather than relitigating them silently.
6. Rank the remaining candidates by expected reduction in observed cost, confidence, risk, and verification cost.
7. Produce a Markdown report using [references/report-format.md](references/report-format.md). Add a diagram only when it makes a relationship materially easier to understand.
8. Stop. Do not propose a concrete interface, edit production code, or begin the refactor. Offer the top candidate to `bwh-ideate` or `bwh-spec` only after the user selects it.

## Evidence rules

- Cite files, symbols, tests, decisions, or history for every retained candidate.
- Separate observed facts, inferences, and unresolved questions.
- Use the deletion test as a diagnostic, not proof by itself.
- Treat one adapter as a possible abstraction and two justified adapters as evidence of a real seam.
- Prefer tests near the public behavior. Do not assume every small module should be merged.

## Capability fallbacks

If parallel readers are available, give them separate bounded areas and raw repository context. Otherwise, inspect the same areas sequentially. If browser or diagram rendering is unavailable, return plain Markdown and a text diagram only when needed. If structured questions are unavailable, ask numbered questions in plain chat. Missing optional capabilities must not broaden the survey or lower its evidence bar.

## Authority

Do not modify source, tests, architecture decisions, dependencies, or configuration during the review. Save a report only when the user or project workflow authorizes an artifact. Commits, pushes, publication, and any selected follow-on work require separate authority.

## Output

Return the bounded survey area, ranked candidates, top recommendation and reason, evidence quality, architecture-decision conflicts, validation limits, and the suggested `bwh-ideate` or `bwh-spec` handoff. If no candidate clears the evidence bar, say so.
