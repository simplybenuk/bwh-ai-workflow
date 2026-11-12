---
name: bwh-reliability
description: Run human-steered reliability improvement rounds on bounded systems; not a broad risk audit or a one-off incident fix.
---

# Reliability improvement rounds

Use this skill to improve reliability for bounded services or workflows through
iterative, human-steered work with repeatable, isolated evidence.

## Required workflow

- Read and follow [human-steered improvement rounds](../../contracts/improvement-rounds.md).
- Apply [model routing](../../contracts/model-routing.md) for standard toolkit
  consistency. Keep deliverables independent of model choice.
- The improvement-rounds contract owns cadence, team selection, measurement
  integrity, human checkpoints, run records, and publication boundaries. This
  skill supplies reliability methods and domain judgment.
- Read consuming-repository instructions, operational procedures, recovery
  expectations, and required checks before proposing changes.

## Scope and fault evidence

- Bound the service or workflow, critical outcomes, dependencies, failure
  conditions, recovery boundary, exclusions, and correctness properties.
- Inspect existing incidents, telemetry, service objectives, retry policies,
  and recovery evidence. Treat established targets as authoritative; label
  proposed targets clearly.
- Define a small deterministic fault matrix before baseline: each injected
  condition, expected outcome, observation, recovery action, and stop condition.
  Keep the matrix proportionate to the risk and scope.
- Run fault injection only in a disposable isolated environment with synthetic
  or sanitized data. Production and shared-service faults require explicit
  authority. Confirm isolation and a safe reset before each scenario.
- Record revision, environment, configuration, workload, fixture size, fault
  point, duration, concurrency, and reset method. Repeat the same scenarios.

## Evidence and method

- Count attempted scenarios and successful outcomes with explicit denominators.
  Classify correctness, timeout, duplicate, loss, recovery, and resource-budget
  outcomes separately; retain failures and explain exclusions.
- Include successful completion latency or throughput where it helps, but pair
  it with correctness, timeout, resource use, retry count, and recovery time.
- Check that retries, queues, backoff, and deadlines stay within declared
  budgets and do not create uncontrolled amplification or duplicate effects.
- Verify recovery behavior: service returns to expected state, data integrity
  holds, pending work is handled correctly, and restore procedures are tested.
  A restore is successful only after verification of restored contents and
  required application behavior.
- Distinguish measured deterministic scenario outcomes from observed field
  reliability. A simulated success fraction is not an availability estimate or
  a claim about production failure rates.
- Record run-to-run variation for noisy outcomes. Do not infer rare-event rates
  or population reliability from a small fault matrix.

## Domain judgment

Assess applicable categories with cited evidence and contract anchors:

- Fault containment: do failures remain within the intended boundary?
- Correct outcomes: are data and externally visible effects correct?
- Recovery: does the system return to a verified usable state?
- Retry behavior: are attempts bounded, safe, and free of harmful duplication?
- Resource control: do failure paths respect time, memory, and work budgets?
- Observability: can operators identify the condition and recovery status?

Use N/A with a reason where evidence cannot support a category. Keep judgment
separate from scenario counts and avoid composite reliability scores.

## Safeguards and checkpoint evidence

- Never inject faults into production or shared services without explicit,
  scenario-specific authority. Do not use real customer data or uncontrolled
  traffic; document isolation and reset before execution.
- Avoid destructive or irreversible recovery experiments. Preserve backups and
  verify the disposable system can be restored before beginning.
- Follow repository-required checks and validate application correctness on
  affected consumers. Do not equate a green check with reliability readiness.
- At the contract's human checkpoint, provide the fault matrix, attempts and
  outcome counts, timeout/duplicate/loss/recovery/resource evidence, restore
  verification, targets and status, environment, changes, trade-offs, and
  inspectable artifacts. State explicitly what the simulation cannot establish.
