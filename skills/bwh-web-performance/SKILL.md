---
name: bwh-web-performance
description: Run human-steered improvement rounds for web performance journeys; not a general site audit or a single-issue fix.
---

# Web performance improvement rounds

Use this skill for bounded, repeatable web journeys where the goal is to improve
loading, responsiveness, or resource use across human-steered rounds.

## Required workflow

- Read and follow [human-steered improvement rounds](../../contracts/improvement-rounds.md).
- Apply [model routing](../../contracts/model-routing.md) for standard toolkit
  consistency. Keep deliverables independent of model choice.
- The improvement-rounds contract owns cadence, team selection, measurement
  integrity, human checkpoints, run records, and publication boundaries. This
  skill supplies web-performance methods and domain judgment.
- Read the consuming repository's instructions, verification guidance, and
  existing evidence before proposing or changing implementation.

## Bound the assessment

- Identify the user journeys, routes, devices, and interaction points in scope;
  name exclusions and correctness properties that must remain true.
- Inspect existing performance budgets and telemetry. Use project-defined
  targets where they exist; label any proposed target as a proposal.
- Prefer representative routes, realistic content, and repeatable local or
  isolated environments. Record relevant hardware, browser configuration,
  network shaping, cache state, concurrency, and build revision.
- Keep lab measurements distinct from field measurements. Describe simulated
  network or device conditions as lab proxies, never as real-user outcomes.

## Evidence and method

- Select a small set of native objective measures tied to the journey: elapsed
  loading or interaction time, bytes transferred, request count, CPU or memory
  use, and project-defined user-experience measures where available.
- For each measure, record its unit, direction, scenario, collection method,
  revision, fixture, environment, and sampling plan before collecting baseline.
- Repeat noisy runs under comparable conditions. Preserve individual samples,
  sample count, median or justified summary, and spread; retain failed runs.
- Report distributions only when the sample supports them. Do not claim tail
  percentiles from a small sample or treat a best run as representative.
- Capture a trace or equivalent bottleneck evidence for the chosen journeys;
  connect suspected costs to rendering, scripting, network, layout, or resource
  contention rather than guessing from a single aggregate number.
- Verify that the journey still renders correct content and completes its key
  interactions. Include errors, failed requests, and resource regressions beside
  speed improvements.
- Keep field evidence, synthetic lab evidence, and reviewer judgment in
  separate sections. Missing field data is unknown, not a pass.

## Domain judgment

Assess applicable categories with cited evidence and contract anchors:

- Journey coverage: do selected paths represent important user work?
- Perceived speed: are waits and feedback appropriate at key steps?
- Responsiveness: do interactions remain usable under representative load?
- Resource efficiency: are transfers, CPU, memory, and requests justified?
- Stability of performance: are results repeatable across the recorded runs?
- Correctness: do content, state, and interactions remain accurate?

Use N/A with a reason when evidence cannot support a category. Do not convert
measurements into judgment scores or combine unlike metrics into a new score.

## Safeguards and checkpoint evidence

- Do not use shared or production systems for load generation or experiments
  without explicit authority. Prefer disposable environments and representative
  fixtures that exclude secrets and personal data.
- Avoid changes that hide work, defer essential content without justification,
  or trade correctness and accessibility for a faster measurement.
- Follow the consuming repository's required checks and verify affected
  consumers. Do not invent universal web performance thresholds.
- At the contract's human checkpoint, provide comparable before/after results,
  sample distributions and uncertainty, targets and status, trace evidence,
  correctness checks, environment details, changes, trade-offs, and unresolved
  suggestions. Link inspectable artifacts and identify any limited coverage.
