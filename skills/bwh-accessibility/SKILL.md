---
name: bwh-accessibility
description: Run human-steered accessibility improvement rounds for bounded journeys; not a compliance certification or a one-defect fix.
---

# Accessibility improvement rounds

Use this skill to improve the accessibility and usability of bounded user
journeys through iterative, human-steered work.

## Required workflow

- Read and follow [human-steered improvement rounds](../../contracts/improvement-rounds.md).
- Apply [model routing](../../contracts/model-routing.md) for standard toolkit
  consistency. Keep deliverables independent of model choice.
- The improvement-rounds contract owns cadence, team selection, measurement
  integrity, human checkpoints, run records, and publication boundaries. This
  skill supplies accessibility evidence methods and domain judgment.
- Read consuming-repository instructions, accessibility guidance, design
  conventions, and required verification before proposing changes.

## Bound journeys and evidence

- Identify the users' tasks, routes, states, input modes, and content in scope;
  record exclusions and functionality that must remain usable.
- Inspect existing automated coverage and prior manual findings. Determine
  which checks can be repeated with the available environment and people.
- Use automated checks to find detectable issues, not to claim complete
  coverage. Record tool/version/configuration, routes and states exercised,
  finding count by severity or type where available, and the checked-item
  denominator. Keep unevaluated items explicitly unknown.
- Include keyboard-only completion of representative tasks: focus order,
  visibility, operation, escape or recovery, and absence of traps where relevant.
- Include assistive-technology checks for relevant semantics, names, roles,
  state changes, announcements, and task completion. Record the actual setup
  and steps so later rounds can repeat them.
- Preserve task transcripts or equivalent notes, failures, and coverage limits.
  Do not treat missing results or a clean automated scan as a pass.
- Keep issue counts with their denominator and scope. Track qualitative task
  usability separately from objective counts; do not average them together.

## Domain judgment

Assess applicable categories with cited evidence and contract anchors:

- Perceivability: can users obtain the needed information in supported modes?
- Operability: can users complete tasks with keyboard and other inputs?
- Understandability: are instructions, labels, feedback, and errors clear?
- Robustness: do semantics and state changes work across tested technology?
- Task usability: can people complete the intended task without avoidable
  confusion, loss of context, or excessive effort?
- Coverage: are important routes, states, content, and interaction types tested?

Use N/A with a reason where evidence does not apply. State who or what was
tested and avoid generalizing a small set of tasks to all users.

## Safeguards and checkpoint evidence

- Do not claim legal or standards compliance from a scan, sample, or reviewer
  agreement. Do not invent a current threshold; consult project policy and
  authoritative guidance available in the consuming repository.
- Preserve user intent and content meaning when changing labels, structure,
  focus, motion, contrast, or interaction. Check responsive states and errors
  where they affect the journey.
- Use respectful, task-focused evaluation. Do not treat disability or assistive
  technology as a defect; avoid collecting identifying participant data.
- Run required repository checks and repeat the same automated and manual
  scenarios after changes. Verify affected journeys and regressions.
- At the contract's human checkpoint, provide before/after counts with
  denominators, exact route/state coverage, automated and keyboard/assistive
  evidence, task outcomes and notes, unknowns, changes, and remaining issues.
  Keep qualitative usability separate from counts and link inspectable records.
