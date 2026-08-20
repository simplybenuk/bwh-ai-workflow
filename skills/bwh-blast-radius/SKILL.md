---
name: bwh-blast-radius
description: Review what a proposed or implemented code change could break beyond its diff, then prove the smallest important safety claims with repository evidence or real execution. Use when the user asks for a blast-radius review, asks what a change could break, or wants a focused pre-merge risk check. Do not use for broad architecture review or completed-implementation acceptance review.
---

# Review blast radius

Remain read-only unless the user separately authorizes a test or helper artifact. Read-only inspection and existing validation commands are allowed. Do not commit, push, publish, or modify external systems.

## Trace the change

1. Read the complete change and identify added, changed, and removed behavior.
2. Trace direct and indirect callers far enough to reach stable boundaries.
3. Inspect relevant data contracts, stored data, serialized formats, configuration, feature flags, and external consumers.
4. Check ordering and timing, including initialization, concurrency, retries, teardown, and asynchronous work where relevant.
5. Inspect the actual pinned dependency version and local patches before relying on library behavior.

Search results establish presence, not safety. A search that finds no caller can clear a specific caller risk, but it cannot prove that a wire format or external consumer is unaffected.

## Reduce the review to safety claims

State the smallest set of facts that must hold for the change to be safe. For each claim, record the strongest available proof:

1. reasoned assertion;
2. repository or dependency source evidence;
3. demonstrated unreachable failure path;
4. existing test or authorized focused execution of real code;
5. reproduction in the running user-facing system.

Run real code for material claims when an existing command can do so safely. If proof needs a new test or helper file, ask before writing it. Mark every claim that stops short of proof as unproven and explain the missing check.

For wide changes, divide inspection by boundary if independent workers are available. Give each worker separate read-only scope and merge only evidence-backed findings. Otherwise inspect the same boundaries sequentially. If structured questions are unavailable, request authority for a helper artifact as a numbered plain-chat question and wait before writing it.

## Classify findings

- **Confirmed risks** have a plausible failure path supported by repository evidence. Cite the relevant path and line or symbol. State likelihood, impact, and the check that would expose the failure.
- **Cleared risks** name a specific concern and the evidence that rules it out.
- **Unproven claims** identify a safety dependency that available evidence could not settle.

Do not invent callers, consumers, APIs, or failure paths. Omit generic possibilities that do not connect to the inspected repository.

## Report

Return these sections:

1. `Change` explains the behavior that differs, including effects not obvious from the diff.
2. `Safety claims` lists each claim, its proof level, and the evidence.
3. `Confirmed risks` lists only retained, cited risks.
4. `Cleared risks` records material concerns that evidence removed.
5. `Unproven` names missing evidence without rounding it up to certainty.
6. `Before merge` recommends the cheapest check that catches the most important credible failure.

Redact private values from evidence. Separate direct observations from inference.
