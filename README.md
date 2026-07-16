# bwh-ai-workflow

Reusable agent scaffolding, workflow contracts, custom skills, and regression evals for spec-driven software delivery.

## Design

- `skills/` contains reusable workflow skills.
- `contracts/` contains shared autonomy, handoff, and completion rules.
- `adapters/` contains project-specific policies and validation commands.
- `templates/` contains project-context and adapter templates.
- `evals/` contains representative cases and scoring guidance.

The core stays model-agnostic. Projects supply their own source-of-truth files, task schema, validation commands, security rules, and release policy through an adapter.

Shared contracts also define collaboration style, model-routing measurement, and persisted workflow states. Skills reference these contracts rather than duplicating them.

## Add to a project

The recommended path is to install the repository as a Codex plugin, then run the adopter skill from the target project.

### Recommended: install the Codex plugin

The repository must be public or available through your Git credentials. Run these commands once:

```bash
codex plugin marketplace add simplybenuk/bwh-ai-workflow
codex plugin add bwh-ai-workflow@bwh-ai-workflow
```

Then navigate to the project that should receive the workflow:

```bash
cd /path/to/target-project
```

Start Codex in that project and invoke:

```text
$bwh-adopt
```

The skill detects whether the workflow is absent or already installed. It adds or updates `.agents/skills` and `.agents/contracts`, preserves `AGENTS.md` and project-specific adapters, creates or updates `.agents/bwh-ai-workflow.lock`, and runs the project’s relevant validation and workflow smoke test.

The target project remains authoritative for domain rules, schemas, permissions, validation, and release policy. Review any adapter placeholders or update conflicts reported by the skill before continuing.

### Manual pinned installation

For environments where the plugin cannot be installed, the workflow can still be copied as a pinned source package. From the target project root:

```bash
mkdir -p .agents/skills .agents/contracts
git clone https://github.com/simplybenuk/bwh-ai-workflow.git /tmp/bwh-ai-workflow
git -C /tmp/bwh-ai-workflow checkout <commit-or-tag>
cp -R /tmp/bwh-ai-workflow/skills/bwh-* .agents/skills/
cp -R /tmp/bwh-ai-workflow/contracts/. .agents/contracts/
```

Record the installed source and revision in a project-local lock note, for example `.agents/bwh-ai-workflow.lock`:

```text
source: https://github.com/simplybenuk/bwh-ai-workflow.git
revision: <commit-sha-or-tag>
installed_at: <yyyy-mm-dd>
```

Then create the project adapter. It should document the project's source-of-truth paths, task/PRD schema, validation commands, security and tenancy rules, branch/commit policy, available tools, and human output-testing checklist. Do not replace the project's `AGENTS.md` with the generic workflow repository.

For a project using the conventional Codex layout, the result should look like:

```text
project/
  .agents/
    skills/
      bwh-agent-review/
      bwh-development/
      bwh-ideate/
      bwh-refine-spec/
      bwh-spec/
    contracts/
      autonomy.md
      collaboration.md
      completion.md
      handoff.md
      model-routing.md
      states.md
    bwh-ai-workflow.lock
  adapters/ or docs/agents/
    bwh-ai-workflow.md
```

The target project remains the authority for domain rules, schemas, permissions, validation, and release policy. This repository supplies reusable workflow behavior only.

Each project should maintain an adapter and context map that point to its existing vision, architecture, ADRs, feature specs, schema, domain rules, planning artifacts, and runbooks. The workflow repository provides the loading contract and templates; it does not duplicate project documentation.

## Update an existing project

Update in a temporary checkout first and compare the installed revision with the lock note:

```bash
rm -rf /tmp/bwh-ai-workflow-update
git clone https://github.com/simplybenuk/bwh-ai-workflow.git /tmp/bwh-ai-workflow-update
git -C /tmp/bwh-ai-workflow-update checkout <new-commit-or-tag>
diff -ru .agents/skills /tmp/bwh-ai-workflow-update/skills
diff -ru .agents/contracts /tmp/bwh-ai-workflow-update/contracts
```

Before applying an update:

1. Read the workflow changelog or commit diff.
2. Run the project's representative workflow evals against the current installation.
3. Review changes to skill triggers, output headings, states, stop rules, and contracts.
4. Preserve or update the project adapter where local tools, paths, or validation changed.
5. Copy the new pinned skills and contracts, then update `.agents/bwh-ai-workflow.lock`.
6. Run the project's relevant checks and one end-to-end workflow smoke test.

Do not overwrite project-specific adapters, `AGENTS.md`, source-of-truth documents, PRD files, or local customisations without reviewing the diff. If the update regresses an eval, restore the previous pinned revision and record the failure before trying another prompt change.

The recommended migration loop is: change one skill, contract, model, reasoning setting, or tool-routing rule at a time; run the same eval cases; compare correctness, completeness, tokens, latency, tool calls, retries, and cost; then keep the change only if quality remains acceptable.

## Workflow

```text
bwh-ideate -> bwh-spec -> bwh-refine-spec (repeat) -> bwh-development -> bwh-agent-review -> human output testing
```

The human has two deliberate gates: read and approve the spec, then test the resulting product behavior. Readiness for development is a state recorded in the spec, not a separate user-facing stage. The agent review sits between implementation and human testing and checks the implementation against the approved spec, project guardrails, and validation evidence.

Available skills:

- `bwh-adopt` — install this workflow into a project or update an existing pinned installation.
- `bwh-ideate` — turn an early idea into a bounded direction and discovery brief.
- `bwh-spec` — create the decision-ready specification and its development-readiness artifacts.
- `bwh-refine-spec` — repeatedly revise the spec and readiness artifacts until the human approves it.
- `bwh-development` — implement the next bounded task with project validation.
- `bwh-agent-review` — independently review the completed work before human output testing.

The agent review is conditional in depth, but should be used for every substantive implementation task. The review must not silently become a second implementation pass; it reports findings and requests targeted fixes when needed.
