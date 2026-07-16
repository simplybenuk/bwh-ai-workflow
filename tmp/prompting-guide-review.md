# GPT-5.6 Sol Prompting Guide Review

## Overall assessment

The setup is directionally strong and already follows the most important guidance: outcome-first prompts, explicit stop conditions, human approval boundaries, model-agnostic skills, and independent validation.

The main remaining gaps are shared-contract activation, precise output schemas, executable evals, adapter-specific tool routing, model-routing measurement, collaboration style, and formal workflow state transitions.

## Findings

### 1. Shared contracts are not connected to the skills

The repository contains `contracts/autonomy.md`, `contracts/handoff.md`, and `contracts/completion.md`, but the skills do not explicitly reference or load them. They currently function as documentation rather than reliably active instructions.

Each skill should identify the contracts it uses, or the project adapter should assemble them into the system prompt.

### 2. Outputs are underspecified

The skills describe what to do, but not exact output shapes. Add an `Output` section to each skill.

For example, `bwh-agent-review` should consistently return:

```text
verdict
blocking_findings
should_fix_findings
validation_evidence
residual_risks
human_test_focus
```

`bwh-spec` should consistently return:

```text
artifact_path
status
decisions
assumptions
open_questions
requirements
task_outline
validation_plan
```

This is the most important prompt-quality improvement still missing.

### 3. The evals are examples, not yet executable evals

The eval documentation promises scoring, but the cases currently contain prompts and invariants only. Add expected output fields, pass/fail criteria, severity weighting, representative fixtures, baseline traces, and measurements for tokens, latency, and tool calls.

Without this, model and prompt migration cannot be evaluated reliably.

### 4. Tool routing is absent

This is acceptable for the generic repository, but the Wolds Record adapter should define available tools, prerequisite reads, validation commands, fallback behavior for empty or suspicious results, and actions requiring approval.

The generic skills should remain tool-agnostic.

### 5. Model-routing guidance is missing

Keeping skills model-agnostic is correct. Add a separate routing contract that says:

- preserve the current reasoning effort as the baseline;
- test one lower effort before increasing it;
- escalate based on risk, not task size; and
- record model, reasoning effort, latency, cost, and outcome in eval traces.

### 6. Collaboration style is implicit

Add a short shared style contract:

> State the current phase and intended outcome before substantial work. Ask only material questions. Report conclusions, evidence, blockers, and next actions. Do not narrate routine tool calls.

### 7. State transitions should be formalized

Define the workflow states explicitly:

```text
DRAFT
NEEDS REFINEMENT
READY FOR HUMAN APPROVAL
APPROVED FOR DEVELOPMENT
IN DEVELOPMENT
READY FOR HUMAN TESTING
NOT READY FOR HUMAN TESTING
```

This will improve handoffs, retries, compaction, and persisted workflow state.

## Guidance that does not need implementation yet

Programmatic Tool Calling is not justified yet because this repository does not currently contain a bounded data-reduction stage.

Citations and retrieval budgets are primarily adapter concerns. They matter when a project uses external research or grounded retrieval, but they do not need to be embedded in the generic skills.

Frontend rendering and image-detail guidance are also project-specific and should remain outside the generic workflow core.

## Priority order

1. Add exact output contracts.
2. Make skills reference the shared contracts.
3. Turn prose evals into scored regression cases.
4. Add model-routing and phase-state contracts.
5. Add adapter-specific tool routing.

## Conclusion

Do not create another workflow stage. The current workflow is sound. Strengthen its contracts and measurement so GPT-5.6 changes can be tested incrementally without rewriting the process.
