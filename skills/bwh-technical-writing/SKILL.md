---
name: bwh-technical-writing
description: Write or revise human-facing technical documentation, including READMEs, tutorials, how-to guides, runbooks, reference pages, explanations, ADRs, pull request descriptions, commit messages, and edits to an existing specification. Use when accuracy, structure, terminology, and testable instructions matter. Do not use to create or refine a product or engineering specification; bwh-spec or bwh-refine-spec owns that work. Do not use for instructions whose primary reader is an agent; bwh-write-agent-instructions owns that work.
---

# Write technical documents

Write for the reader's task. Inspect the repository before drafting so paths, symbols, flags, commands, and product terms match the source.

## Choose the document's purpose

Use one primary mode for each document or clearly separated document:

- **Tutorial** helps a learner succeed by doing. Produce visible results early and state what the learner should see.
- **How-to** gives a competent reader the steps to reach one goal. Keep background elsewhere.
- **Reference** records facts for lookup. Mirror the structure of the code or interface and keep opinion out.
- **Explanation** helps the reader understand one bounded question, including context, constraints, alternatives, and justified conclusions.

Split and link when procedures and reference facts would compete. For ADRs and specifications, identify the reader's decision need and use explanation, reference, or clearly labelled sections as appropriate. Pull request descriptions and commit messages are compact records of change, reason, and validation rather than full document modes.

## Draft from evidence

1. Identify the reader, purpose, expected action, and authoritative source.
2. Read the relevant code, commands, configuration, and existing vocabulary.
3. Organize the document in the order the reader needs it.
4. Write procedures as direct commands. Put conditions and warnings before the guarded step.
5. State the expected result wherever the reader must verify a step.
6. Use the same term for the same thing throughout.
7. Check every path, symbol, flag, command, count, and claimed result against the current repository.

Do not fabricate output. If a command cannot be run, label the expected result as unverified.

## Keep the prose clear

- Prefer plain, precise words over inflated synonyms.
- Use active voice when the actor matters.
- Keep one instruction per sentence. Split dense sentences that make the reader backtrack.
- Vary sentence length when clarity allows it. Do not turn the document into clipped fragments.
- Keep technical terms that carry real meaning and define unfamiliar local terms once.
- Use numbered lists for sequences and bullets for unordered sets.
- Use sentence-case headings and descriptive link text.
- Keep reference writing factual. Reserve judgments and trade-offs for explanation, ADRs, and specifications.
- Apply the anti-slop rules available in the toolkit, but preserve the project's established voice.

## Respect the boundary with agent instructions

Route new or refined product and engineering specifications to `bwh-spec` or `bwh-refine-spec`. This skill may improve the wording or organization of an existing specification when the requested decisions and requirements are already settled.

Route documents whose primary reader is an agent to `bwh-write-agent-instructions`. This skill may edit human-facing documentation about agents, but it does not design skill triggers, instruction hierarchy, context loading, or agent completion rules.

Work through repository evidence sequentially when independent workers are unavailable. If a missing source or publication decision needs user input and structured questions are unavailable, ask a numbered plain-chat question with a recommendation and wait when the answer changes accuracy, scope, or authority.

Do not commit, push, publish, or update remote documents without separate authorization.

## Review

Confirm that:

- the selected purpose matches the document;
- procedures are ordered and testable;
- verification points include expected results;
- reference facts are separate from procedural guidance where useful;
- repository names and commands are exact;
- every claim is supported or marked unverified;
- filler, repetition, and ambiguous pronouns are gone.
