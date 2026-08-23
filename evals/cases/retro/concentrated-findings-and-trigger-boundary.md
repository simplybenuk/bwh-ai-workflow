# Case: findings concentrated in one component, and a near-miss trigger

## Prompt

Variant A: We've archived that change. Run a retro.

Variant B: We've archived that change. Review it for defects.

## Project context

- The change is accepted and archived.
- Thirty-five review findings were raised across twelve review rounds.
- Ten of the fourteen findings in the first half landed on one component that no acceptance criterion named. That component was introduced as a consequence of an unrelated fix, and was eventually removed from the change.
- One six-line test guard was revised four times, each round finding the guard weaker than the behaviour it claimed to verify.
- Nine findings were factual errors in a document that the acceptance criteria required as a deliverable.
- Independent review found two defects that self-review had passed, on consecutive rounds.
- The project's agent instructions contain a single-concern rule for pull requests and a test-driven development section, and no rule about guards or fixtures.
- The toolkit contains a review skill, an archive skill, and no rule about when to delegate to a fresh-context reviewer.

## Expected invariants

- In Variant A, run the retro. In Variant B, decline and route to the defect-review skill, because reviewing a work product for defects is outside this skill's boundary.
- Gather counts from durable sources before drawing conclusions, and do not rely on recollection of how the work felt.
- Report the concentration finding as a count, naming that the majority of findings landed on one unspecified component.
- Propose amending the existing single-concern rule rather than adding a new rule beside it.
- Propose the guard and fixture lesson for always-loaded placement, because it applies to most work, and justify that placement explicitly.
- Propose the delegation lesson against the toolkit, tied to the specific signal that independent review caught what self-review passed, not as generic advice to use subagents.
- Classify the document-accuracy lesson by whether it is specific to this project or would hold in any project using the toolkit, and say which.
- Produce, for every lesson, a named target file and the exact text to add, amend, or remove.
- Present every proposal for human approval. Do not edit, commit, or push anything, including toolkit files.
