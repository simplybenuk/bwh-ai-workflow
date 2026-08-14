# bwh-ai-workflow

Reusable agent scaffolding, workflow contracts, custom skills, and regression evals for spec-driven software delivery.

## Design

- `skills/` contains reusable workflow skills.
- `contracts/` contains shared autonomy, handoff, and completion rules.
- `adapters/` contains project-specific policies and validation commands.
- `templates/` contains project-context and adapter templates.
- `evals/` contains representative cases and scoring guidance.

The core stays model- and agent-agnostic. Projects supply their own source-of-truth files, task schema, validation commands, security rules, and release policy through an adapter.

Shared contracts also define collaboration style, model-routing measurement, persisted workflow states, and the per-host packaging conventions. Skills reference these contracts rather than duplicating them.

## Agent hosts

The skills and contracts contain no agent-specific behaviour. Only packaging and install layout differ, as defined in `contracts/host-conventions.md`:

| Host | Agent home | Instruction file | Plugin manifest | Skill invocation |
| --- | --- | --- | --- | --- |
| Claude Code | `.claude/` | `CLAUDE.md` | `.claude-plugin/plugin.json` | `/bwh-<skill>` |
| Codex | `.agents/` | `AGENTS.md` | `.codex-plugin/plugin.json` | `$bwh-<skill>` |

Both manifests ship in this repository, so the same checkout installs as either plugin. A project may host both agents at once; `bwh-adopt` treats each as a separate install target with its own lock file.

## Add to a project

The recommended path is to install the repository as a plugin for your agent, then run the adopter skill from the target project. The repository must be public or available through your Git credentials.

### Claude Code

```bash
claude plugin marketplace add simplybenuk/bwh-ai-workflow
claude plugin install bwh-ai-workflow@bwh-ai-workflow
```

Then start Claude Code in the target project and invoke `/bwh-adopt`.

### Codex

```bash
codex plugin marketplace add simplybenuk/bwh-ai-workflow
codex plugin add bwh-ai-workflow@bwh-ai-workflow
```

Then start Codex in the target project and invoke `$bwh-adopt`.

### What the adopter does

The skill resolves the agent host, then detects whether the workflow is absent or already installed. It adds or updates `<agent-home>/skills` and `<agent-home>/contracts`, preserves the project's agent instruction file and project-specific adapters, creates or updates `<agent-home>/bwh-ai-workflow.lock`, and runs the project’s relevant validation and workflow smoke test.

The target project remains authoritative for domain rules, schemas, permissions, validation, and release policy. Review any adapter placeholders or update conflicts reported by the skill before continuing.

### Manual pinned installation

For environments where the plugin cannot be installed, the workflow can still be copied as a pinned source package. From the target project root, with `AGENT_HOME` set to your host's agent home (`.claude` or `.agents`):

```bash
AGENT_HOME=.claude   # or .agents for Codex
mkdir -p "$AGENT_HOME/skills" "$AGENT_HOME/contracts"
git clone https://github.com/simplybenuk/bwh-ai-workflow.git /tmp/bwh-ai-workflow
git -C /tmp/bwh-ai-workflow checkout <commit-or-tag>
cp -R /tmp/bwh-ai-workflow/skills/bwh-* "$AGENT_HOME/skills/"
cp -R /tmp/bwh-ai-workflow/contracts/. "$AGENT_HOME/contracts/"
```

Contracts must stay a sibling of `skills/`, because each skill references them as `../../contracts/<name>.md`.

Record the installed source and revision in a project-local lock note at `<agent-home>/bwh-ai-workflow.lock`:

```text
source: https://github.com/simplybenuk/bwh-ai-workflow.git
revision: <commit-sha-or-tag>
installed_at: <yyyy-mm-dd>
host: <claude-code|codex>
```

Then create the project adapter. It should document the agent host and install layout, the project's source-of-truth paths, task/PRD schema, validation commands, security and tenancy rules, branch/commit policy, available tools, human output-testing checklist, temporary change-artifact classes, and completed-change archive conventions. Do not replace the project's agent instruction file with the generic workflow repository.

The installed result should look like this, with `.claude/` or `.agents/` as the agent home:

```text
project/
  .claude/            # or .agents/ for Codex
    skills/
      bwh-adopt/
      bwh-agent-review/
      bwh-archive-change/
      bwh-ask/
      bwh-development/
      bwh-ideate/
      bwh-refine-spec/
      bwh-spec/
    contracts/
      autonomy.md
      collaboration.md
      completion.md
      context-loading.md
      handoff.md
      host-conventions.md
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
diff -ru "$AGENT_HOME/skills" /tmp/bwh-ai-workflow-update/skills
diff -ru "$AGENT_HOME/contracts" /tmp/bwh-ai-workflow-update/contracts
```

Before applying an update:

1. Read the workflow changelog or commit diff.
2. Run the project's representative workflow evals against the current installation.
3. Review changes to skill triggers, output headings, states, stop rules, and contracts.
4. Preserve or update the project adapter where local tools, paths, or validation changed.
5. Copy the new pinned skills and contracts, then update `<agent-home>/bwh-ai-workflow.lock`.
6. Run the project's relevant checks and one end-to-end workflow smoke test.

If the project hosts more than one agent, repeat the update for each agent home so the installed revisions stay in step.

Do not overwrite project-specific adapters, the agent instruction file, source-of-truth documents, PRD files, or local customisations without reviewing the diff. If the update regresses an eval, restore the previous pinned revision and record the failure before trying another prompt change.

The recommended migration loop is: change one skill, contract, model, reasoning setting, or tool-routing rule at a time; run the same eval cases; compare correctness, completeness, tokens, latency, tool calls, retries, and cost; then keep the change only if quality remains acceptable.

## Workflow

```text
bwh-ideate -> bwh-spec -> bwh-refine-spec (repeat) -> bwh-development -> bwh-agent-review -> human output testing -> bwh-archive-change
```

The human has two deliberate gates: read and approve the spec, then test and accept the resulting product behavior. Readiness for development is a state recorded in the spec, not a separate user-facing stage. The agent review sits between implementation and human testing and checks the implementation against the approved spec, project guardrails, and validation evidence. After explicit human acceptance, the archive stage gathers the change's temporary workflow documentation into a verified bundle and leaves shared or permanent source-of-truth documents in place.

Available skills:

- `bwh-adopt` — install this workflow into a project or update an existing pinned installation.
- `bwh-archive-change` — archive an accepted change and its temporary workflow documentation into a verified bundle.
- `bwh-ask` — answer a question about the repository, an idea, or the workflow state without creating or advancing any artifact.
- `bwh-ideate` — turn an early idea into a bounded direction and discovery brief.
- `bwh-spec` — create the decision-ready specification and its development-readiness artifacts.
- `bwh-refine-spec` — repeatedly revise the spec and readiness artifacts until the human approves it.
- `bwh-development` — implement the next bounded task with project validation.
- `bwh-agent-review` — independently review the completed work before human output testing.

The agent review is conditional in depth, but should be used for every substantive implementation task. The review must not silently become a second implementation pass; it reports findings and requests targeted fixes when needed. Archival must not infer human acceptance from that review or from automated validation.

`bwh-ask` sits outside the pipeline. It answers a question about the repository, an idea, or the workflow state without creating or advancing any artifact, and can be invoked at any point — before ideation, mid-spec, mid-development, or standalone.
