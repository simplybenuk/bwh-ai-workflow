---
name: bwh-retro
description: Review how a delivered change was executed and propose durable improvements to the project's agent instructions or to this toolkit. Use when the human asks for a retro, a post-mortem, or what could be done better next time, and alongside archiving an accepted change. Do not use to review a work product for defects, which bwh-agent-review owns, or to audit a toolkit installation, which bwh-skills-audit owns.
---

# Retro

Apply the shared contracts in `../../contracts/autonomy.md`, `../../contracts/collaboration.md`, `../../contracts/completion.md`, `../../contracts/context-loading.md`, `../../contracts/handoff.md`, `../../contracts/model-routing.md`, and `../../contracts/states.md`, plus the consuming project's adapter.

## Goal

Turn how a change was executed into proposed edits to instructions that will be read again. A lesson nobody encodes is a lesson lost.

## Review boundary

Review the **process**: how the work was sequenced, where effort was repeated, which checks caught defects and which missed them, and which instructions were absent or wrong when they were needed.

Do not review the work product for defects. That is `bwh-agent-review`. Do not audit toolkit installation, drift, or lock state. That is `bwh-skills-audit`.

## Eligibility

Run when either holds:

- the human asks for a retro, a post-mortem, or what to do differently; or
- a change has been accepted and is being archived.

A retro needs a finished change with a durable record. If the work left no review history, no commit history and no progress log, say so and stop.

## Propose only

**Never edit, commit, or push.** Every result is a proposal awaiting human approval, including changes to this toolkit.

This holds even where `autonomy.md` would permit a local edit. The targets here are permanent instructions that shape future runs and change no application behaviour, so a wrong one is expensive and invisible. The human approves each proposal before anything is written.

## Evidence before opinion

Gather countable facts first. Do not form a conclusion, and do not read the conversation for impressions, until the counts exist.

Read durable sources only:

- review comments on the change, grouped by file and by round;
- commit history on the branch, including commits that revise an earlier commit on the same branch;
- files revised in more than two rounds;
- the progress or execution log;
- issues opened, deferred, or cut during the change;
- validation and CI failures.

Recollection of the session is not evidence. The agent that did the work shares the blind spots that produced it, which is why the counts do the arguing.

Where the host supports it, delegate evidence gathering to a subagent with no prior context, and compare its counts with your own. Report any disagreement rather than resolving it silently.

## Signals worth counting

Each of these has predicted trouble in real changes, and each is visible in the record long before anyone names it.

- **Findings concentrated in one file or component.** A majority landing in one place usually means the approach is wrong, not that the instances are unlucky.
- **A component introduced mid-change that no acceptance criterion names.** Scope that arrives as a consequence of a fix rarely gets specified, and carries its own defects.
- **The same guard or test revised more than twice.** Repeated revision usually means the guard is weaker than the thing it claims to verify.
- **Documentation corrected in more than one round.** When a document is a deliverable, its accuracy is an acceptance criterion, not tidying.
- **A denylist widened repeatedly.** Enumerating what to exclude fails on the first case nobody listed.
- **Self-review passing where independent review then found defects.** This is the signal that the work needed delegation earlier, and it is worth naming precisely, because "use a subagent" as generic advice is useless.

Absence of a signal is a finding too. Record what you checked and found clean.

## Proposal targets

Classify each lesson by where it would be read again.

- **Project agent instructions**, when the rule is specific to this repository, its stack, or its domain.
- **This toolkit**, when the rule would hold in any project using it. Name the skill or contract, and whether the change is a new rule, a sharpened trigger, or a removal.
- **An issue or backlog item**, when the lesson needs work rather than a rule.

Prefer amending an existing instruction to adding one. Context spent on every run is the scarcest thing you are proposing to consume, so a rule that applies to most work belongs in an always-loaded document, and a rule that applies to one kind of task belongs behind a pointer that names its condition.

## Stop conditions

- Stop and report nothing when the evidence shows no transferable lesson. Most changes produce none. A retro that always finds improvements is a noise generator, and the improvements it invents will cost context forever.
- Stop when a proposed rule cannot be tied to a count or a named artifact. Restating a general engineering principle is not a finding.
- Stop before editing anything, always.
- Stop and ask when the evidence supports two incompatible readings.

## Workflow

1. Confirm eligibility and identify the change, its branch, its review history, and its acceptance criteria.
2. Gather the counts from durable sources. Delegate to a fresh-context subagent where available.
3. Test each signal above against the counts. Record the ones that are clean.
4. For each surviving signal, state the fact, the count behind it, and what it cost.
5. Write each lesson as a proposed edit to a named file, with the text to add, amend, or remove. A lesson without a target is not finished.
6. Classify each proposal by target and by whether it needs always-loaded context or a conditional pointer.
7. Present proposals for approval. Do not write anything.

## Handoff

Return to the human for approval. Approved project-instruction edits go to the skill that owns that document, or to `bwh-write-agent-instructions` when the reader is an agent. Approved toolkit edits go to `bwh-write-agent-instructions`. Approved backlog items go to the project's planning workflow.

## Output

- the change reviewed, and the durable sources read
- the counts, including signals checked and found clean
- each lesson, with the count behind it and what it cost
- each proposal: target file, exact edit, always-loaded or conditional, and why that placement
- disagreements between your counts and a subagent's
- an explicit statement when no transferable lesson was found
- confirmation that nothing was written
