---
name: bwh-prototype
description: Build an isolated throwaway prototype to answer one product or engineering decision about logic, state, data shape, layout, hierarchy, or interaction. Use when evidence from a runnable experiment is needed before specification or development. Do not use to implement approved production work or treat prototype code as production-ready.
---

# Prototype

Build the smallest runnable artifact that answers one named decision question. Treat its code as evidence, not approved implementation.

Apply `../../contracts/autonomy.md`, `../../contracts/context-loading.md`, and the consuming project's adapter when present.

## Workflow

1. State one decision question, the intended reviewer, the evidence that would answer it, and what remains out of scope. Stop for clarification only when choosing the wrong question would materially change the artifact.
2. Choose a branch. Use [references/logic-prototype.md](references/logic-prototype.md) for state, transition, data-shape, or rule questions. Use [references/ui-prototype.md](references/ui-prototype.md) for layout, hierarchy, or interaction questions.
3. Resolve isolation before writing. Use a prototype location defined by the project adapter. Otherwise use an isolated temporary directory or worktree that cannot be mistaken for production code. Record the location and cleanup boundary.
4. Use in-memory data by default. When persistence is the question, use a clearly disposable local dependency and document how to reset it. Avoid production data, credentials, live mutations, and external side effects.
5. Make the artifact trivial for the reviewer to run. Expose the relevant state and include representative scenarios, including an awkward or invalid case when it bears on the question.
6. Run the launch path and demonstrate the named scenarios. Capture the command, result, observations, unresolved uncertainty, and the discovery or specification decision affected.
7. Preserve the evidence needed for review, then clean up only processes and disposable resources started by this run. Do not remove user-owned files or pre-existing processes.
8. Stop after reporting the answer. Copying code into production, editing a specification, committing, pushing, or publishing requires separate authorization.

## Constraints

- Keep the prototype narrow. Do not add production-grade tests, generalized abstractions, migration paths, or unrelated polish.
- Use repeatable launch evidence. A prototype need not have a production test suite, but it must run and demonstrate its question.
- Mark every artifact as a prototype and record its disposable dependencies.
- Treat reusable-looking code with suspicion. Reimplement or harden it through the approved development workflow before production use.

## Capability fallbacks

If a browser or interactive driver is available, use it to exercise the artifact. Otherwise run the narrowest launch or syntax check available and give the reviewer exact manual steps, marking visual or interaction claims unverified. If subagents are unavailable, compare variants or scenarios sequentially. If structured questions are unavailable, ask numbered questions in plain chat.

## Output

Return the decision question, prototype type and location, launch instructions, scenarios demonstrated, observations, conclusion, unresolved uncertainty, cleanup status, and the affected discovery or specification decision. State that production promotion remains unapproved.
