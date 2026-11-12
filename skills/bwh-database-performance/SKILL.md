---
name: bwh-database-performance
description: Run human-steered database performance improvement rounds; not a general database review or a one-query repair.
---

# Database performance improvement rounds

Use this skill to improve bounded application workloads over iterative,
human-steered rounds while preserving data correctness and access boundaries.

## Required workflow

- Read and follow [human-steered improvement rounds](../../contracts/improvement-rounds.md).
- Apply [model routing](../../contracts/model-routing.md) for standard toolkit
  consistency. Keep deliverables independent of model choice.
- The improvement-rounds contract owns cadence, team selection, measurement
  integrity, human checkpoints, run records, and publication boundaries. This
  skill supplies database methods and domain judgment.
- Read repository instructions, schema and migration conventions, verification
  guidance, and existing workload evidence before proposing changes.

## Workload boundary and dataset

- Bound the application journeys, read and write paths, affected tables,
  correctness properties, tenant boundaries, and exclusions.
- Inspect existing query plans, telemetry, budgets, and indexes where available.
  Use established project targets; clearly label proposed targets.
- Use a disposable isolated database with a representative fixture. Record row
  cardinalities, relationships, value distributions, skew, tenant mix, and data
  generation method. Ensure tested scale matches the question being answered.
- Preserve a stable dataset and workload across baseline and after runs. Record
  software and database versions, configuration, cache state, concurrency,
  transaction shape, hardware, revision, and fixture size.

## Evidence and method

- Select a proportionate set of native measures for the workload: latency
  distributions, throughput, rows or bytes read and written, CPU or memory,
  lock or wait time, storage footprint, and write amplification where relevant.
- Include both reads and writes when the change can affect both. State unit,
  direction, scenario, collection method, and sampling plan before baseline.
- Capture plans for representative parameter values, including skewed values.
  Prefer safe plan inspection; execute analyzed plans only against disposable,
  bounded data after confirming the execution is safe for that environment.
- Record plan shape, rows estimated and observed when available, buffers or
  equivalent work counters, and relevant waits. Explain plan changes with the
  workload rather than treating a plan label as a result.
- Measure repeated noisy workloads comparably; retain samples and failures and
  report a justified summary with spread. Avoid unsupported tail claims.
- Check result correctness, transaction behavior, tenant/access enforcement,
  and representative edge cases alongside speed and resource measures.
- Assess index and schema changes for read benefit, write cost, storage,
  maintenance, lock or deployment risk, and rollback or migration path.

## Domain judgment

Assess applicable categories with cited evidence and contract anchors:

- Workload representativeness: do fixtures and parameters reflect real shape?
- Query efficiency: is database work appropriate to the required result?
- Read/write balance: are gains offset by write or contention costs?
- Storage and index cost: is footprint justified and maintainable?
- Access and tenant safety: are boundaries enforced for tested paths?
- Correctness and operability: are transactions and schema changes dependable?

Use N/A with a reason where evidence is unavailable. Keep reviewer judgments
separate from native measurements and avoid combining metrics into a new score.

## Safeguards and checkpoint evidence

- Never run unbounded plans, load tests, destructive migrations, or fault work
  against production or shared data without explicit authority. Use disposable
  data and remove secrets and personal information from artifacts.
- Do not weaken constraints, isolation, authorization, or result semantics to
  improve a benchmark. Validate migration compatibility and rollback needs.
- Run consuming-repository checks and affected application correctness checks;
  do not infer success from a faster isolated query alone.
- At the contract's human checkpoint, show comparable read/write measurements,
  fixture cardinality and skew, plan evidence, correctness/access checks,
  storage and migration trade-offs, targets and status, environment, and
  inspectable artifacts. Call out limited coverage and unresolved risks.
