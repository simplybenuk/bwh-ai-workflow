---
name: bwh-adopt
description: Install or update the BWH Agent Toolkit in a project, select a catalog profile, preserve local project instructions and customisations, and record the exact pinned installation. Use when asked to adopt, install, sync, upgrade, update, or change a BWH toolkit profile.
---

# Adopt the BWH Agent Toolkit

Apply `../../contracts/autonomy.md`, `../../contracts/completion.md`, and `../../contracts/host-conventions.md`.

The toolkit source consists of `catalog.json`, catalogued `skills/`, shared `contracts/`, and project templates. The consuming project remains authoritative for its agent instruction file, adapter, context map, source-of-truth documents, validation commands, permissions, and release policy.

## Resolve scope and source

1. Confirm that the target is a project root.
2. Resolve each requested host through the host convention contract. Treat each host as a separate install target with its own lock.
3. Use the profile the user named. Default a project installation or existing version 1 installation to `workflow`. Treat installation through a host's machine-level plugin mechanism as `full`.
4. Resolve the source from an explicit path first, the current toolkit checkout second, or a temporary checkout of `https://github.com/simplybenuk/bwh-ai-workflow.git` last.
5. Resolve and record an exact commit or tag. Do not install from an unrecorded floating checkout.
6. Read and validate `catalog.json`. Stop on an unknown profile, inactive profile member, missing dependency, invalid path, or incomplete provenance.

Prefer `scripts/install.py` from the resolved source for project copies. Run it with the explicit target and host, add `--profile <name>` when the user selected a non-default profile, and use `--dry-run` before an update. If the helper cannot run, follow the same rules below manually.

## Install or update

1. Inspect the project instruction file, agent home, existing lock, adapter, and context map before writing.
2. Resolve the selected profile and every declared dependency. Copy only those skill directories. Copy shared contracts when any selected skill declares them.
3. Preserve unrelated skills, project-owned files, and all files outside the managed set.
4. Before replacing a managed file, compare it with the digest recorded in a version 2 lock. For a version 1 lock, compare it with the file at the recorded source revision. If neither comparison is possible, treat the file as locally modified.
5. When a managed file has local edits, stop and show the conflict. Ask the user to choose replace, merge, or skip. Do not make that choice for them.
6. Remove a file excluded by a new profile only when the old lock proves it was managed and its current digest still matches the recorded digest. Preserve every changed or unproven file.
7. Stage copies and keep recoverable backups until installed frontmatter, references, and contracts pass and the new lock is written. The helper keeps backups only through this internal transaction and restores them on an internal failure.
8. Do not rewrite a version 1 lock until the update has copied and validated successfully. Existing version 1 installations receive `workflow` unless their recorded files or the user's request establish another profile.

Write `<agent-home>/bwh-ai-workflow.lock` as JSON with:

- `format_version` set to `2`;
- package identifier, source, pinned revision, and installation date;
- host, install scope, and selected profile;
- exact installed skill names and contract paths;
- catalog schema version;
- a digest for every managed file.

## Project adapter and context

If the project has no adapter or context map, use `templates/project-adapter.md` and `templates/project-context.md` at the project's documented locations. Fill values only from repository evidence. Leave explicit placeholders for unknown values and report them. Never replace either file during an update.

Record the host, agent home, profile, lock path, active temporary artifacts, completed archive bundles, artifact classification, shared-reference updates, and archive manifests. Keep host paths and invocation syntax out of other project artifacts.

## Validate and report

Validate the installed skill names and frontmatter, relative references, required contracts, lock contents, and adapter fields inside the helper transaction. Before an update, retain the old lock details and revision until external project checks finish. Run project checks and one representative workflow smoke test after the helper completes. If either fails, reinstall the prior pinned revision and profile using the retained lock details. The helper does not retain its temporary backup after a successful internal transaction.

Report whether the operation was an install or update, host and agent home, profile, source and revision, managed directories, preserved conflicts, adapter and context status, validation, smoke-test result, and remaining action.

Do not commit, push, publish, remove a plugin, move an installation between agent homes, rename an instruction file, or delete project documentation without separate authority.
