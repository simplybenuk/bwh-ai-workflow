# BWH Agent Toolkit

BWH Agent Toolkit is a portable collection of agent skills for product discovery, specification, software delivery, engineering analysis, verification, and technical writing.

The public name is `BWH Agent Toolkit`. The repository, marketplace, and package identifier remains `bwh-ai-workflow` so existing installations can update without changing identity.

## What is included

The toolkit has 17 active skills split into profiles.

### Workflow

- `bwh-adopt` installs or updates the toolkit in a project.
- `bwh-ask` answers repository and workflow questions without advancing work.
- `bwh-ideate` turns an early idea into a bounded discovery brief.
- `bwh-spec` creates a development-ready specification for approval.
- `bwh-refine-spec` revises a draft specification from feedback and evidence.
- `bwh-development` implements approved work with validation and traceability.
- `bwh-agent-review` independently reviews completed implementation.
- `bwh-archive-change` archives an accepted change and its evidence.

### Engineering

- `bwh-diagnose-bugs` investigates failures without silently implementing a fix.
- `bwh-blast-radius` maps the likely impact of a proposed change.
- `bwh-create-verification` creates a reusable verification skill and fixture.
- `bwh-review-architecture` reports observed architectural costs and options.
- `bwh-prototype` builds disposable evidence for an uncertain idea.

### Authoring

- `bwh-technical-writing` writes or edits evidence-backed technical prose.
- `bwh-grill` runs an exhaustive, evidence-first questioning session when requested.
- `bwh-write-agent-instructions` creates clear instructions for agent readers.
- `bwh-skills-audit` reviews a skill collection and recommends what to keep, change, add, or retire.

The `full` profile contains every skill. Project installs default to `workflow`. Machine-level plugin installs expose the full collection.

## Hosts

The skill behavior is agent agnostic. Only package metadata, project paths, and invocation syntax vary by host.

| Host | Project agent home | Instruction file | Invocation |
| --- | --- | --- | --- |
| Codex | `.agents/` | `AGENTS.md` | `$bwh-<skill>` |
| Claude Code | `.claude/` | `CLAUDE.md` | `/bwh-<skill>` |
| Cursor | `.cursor/` | `AGENTS.md` or a user-selected project rule | `/bwh-<skill>` |

Codex, Claude Code, and Cursor manifests ship from the same repository. Their validation status remains `pending` until the representative live-host checks in `docs/testing/bwh-agent-toolkit-expansion.md` pass.

## Install on a machine

### Codex

Add this repository as a marketplace, then install the plugin.

```bash
codex plugin marketplace add simplybenuk/bwh-ai-workflow
codex plugin add bwh-ai-workflow@bwh-ai-workflow
```

For development from a local checkout, use its path instead.

```bash
codex plugin marketplace add /path/to/bwh-ai-workflow
codex plugin add bwh-ai-workflow@bwh-ai-workflow
```

### Claude Code

```bash
claude plugin marketplace add simplybenuk/bwh-ai-workflow
claude plugin install bwh-ai-workflow@bwh-ai-workflow
```

### Cursor

Install the repository through Cursor's plugin interface using the package identifier `bwh-ai-workflow`. The Cursor manifest is `.cursor-plugin/plugin.json`.

Restart or begin a new agent session after installation so the host reloads its skill catalog.

## Install in a project

Use `scripts/install.py` from a clean checkout pinned to a commit. Choose the target host and profile explicitly.

```bash
python3 scripts/install.py \
  --source /path/to/bwh-ai-workflow \
  --target /path/to/project \
  --host codex \
  --profile full \
  --dry-run

python3 scripts/install.py \
  --source /path/to/bwh-ai-workflow \
  --target /path/to/project \
  --host codex \
  --profile full
```

Accepted installer host values are `codex`, `claude-code`, and `cursor`. Their live validation status remains pending. Supported profiles are `workflow`, `engineering`, `authoring`, and `full`.

The installer copies exact blobs from the selected Git revision. It rejects dirty source checkouts, tracked symlinks, unsafe lock paths, unresolved skill references, and local changes to managed files. Writes use exclusive temporary files and atomic replacement. Tracked `0644` and `0755` modes are preserved.

## Locks, updates, and recovery

Each project install writes `<agent-home>/bwh-ai-workflow.lock` in version 2 JSON format. The lock records the source, commit, host, profile, installed skills and contracts, and a digest for every managed file.

Run the installer with `--dry-run` before an update. It preserves project instructions, adapters, context maps, unrelated files, and locally edited managed files. Profile changes remove only files whose current digest still matches the previous lock.

Version 1 workflow locks migrate to version 2. Commit SHAs and tags are accepted for the recorded old revision. If validation fails inside the install transaction, the installer restores touched files and keeps the previous lock. External project checks happen after installation. If they fail, reinstall the previous revision and profile recorded before the update.

## Repository layout

```text
skills/                  portable skill instructions and references
contracts/               shared autonomy, completion, review, and host rules
catalog.json             profiles, dependencies, status, and provenance
scripts/                 installer and validators
tests/                   installer and metadata regression tests
evals/cases/toolkit/     behavior and routing cases
evals/results/           scored policy evaluation records
templates/               project adapter and context templates
docs/                    discovery, specification, delivery, and test records
```

Projects remain authoritative for their own rules, schemas, source-of-truth files, validation commands, security policy, and release process.

## Validate a checkout

```bash
python3 -m unittest discover -s tests -q
python3 scripts/validate_catalog.py
python3 scripts/validate_skills.py
python3 scripts/validate_package.py
git diff --check
```

The repository includes case matrices and scored policy evaluations. Those records do not replace live checks in Codex, Claude Code, and Cursor.

## Provenance and privacy

`catalog.json` records the exact upstream repository, revision, licence, source paths, and BWH adaptations for every derived skill. `THIRD_PARTY_NOTICES.md` contains the upstream notices.

The toolkit does not require transcript collection. `bwh-skills-audit` defaults to repository and catalog evidence. Any usage analysis must be explicitly authorized, read-only, aggregate-only, and stripped of secrets and private content.

## Licence

BWH Agent Toolkit is released under the MIT Licence. See `LICENSE` and `THIRD_PARTY_NOTICES.md`.
