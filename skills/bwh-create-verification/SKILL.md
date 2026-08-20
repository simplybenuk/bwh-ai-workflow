---
name: bwh-create-verification
description: Create a project-local verify-<app> skill that launches, checks, drives, observes, and safely cleans up the project's primary user-facing system. Use when a repository lacks a repeatable user-level verification workflow or the user asks to create a verification or control skill for an app. Do not use merely to run an existing verification skill.
---

# Create project verification

Create instructions that another agent can follow without prior knowledge of the project. Read the project's agent instructions and [`../../contracts/host-conventions.md`](../../contracts/host-conventions.md), then resolve the project-local skill directory for the target host. Do not hard-code a host directory in this portable skill.

Writing the generated skill and any helper files requires the user's authorization to change the project. Do not change production systems, external data, or shared user sessions. Ask for a documented disposable environment or dry-run mode when verification would otherwise mutate them.

## Inspect the project

Establish these facts from repository evidence before asking the user:

- the primary user-facing system and any secondary interfaces;
- the documented local launch command, readiness signal, environment needs, and seed data;
- existing browser, command-line, API, test, or application drivers;
- observable evidence such as rendered state, terminal output, response bodies, logs, files, or stored records;
- port, profile, data-directory, account, and process isolation;
- the exact shutdown procedure.

Inspect these facts sequentially when independent workers are unavailable. If unresolved isolation or write authority requires a user decision and structured questions are unavailable, ask one numbered plain-chat question with a recommendation, then wait.

Prefer an existing driver. Add a helper only when the project has no suitable path and the user has authorized the file. If the project cannot start, report the blocker. Do not silently repair unrelated application code while creating verification instructions.

## Generate `verify-<app>`

Use a short lowercase application name. Put only `name` and `description` in the generated `SKILL.md` frontmatter. Ground every command, path, selector, prompt, route, and readiness check in the repository. Remove every placeholder.

Include these sections:

1. `Launch` gives the exact start command, isolation settings, readiness signal, recorded process identity, and normal shutdown command.
2. `Doctor` gives a read-only check for the expected instance, version or build, address, profile, and authentication state where relevant.
3. `Drive` names the existing harness and stable user-level handles. Prefer accessible names, documented prompts, route paths, and commands over coordinates or incidental layout.
4. `Evidence` defines what proves both the user action and resulting state. Verify side effects through a second observable view. State what disposable or dry-run mode prevents.
5. `Cleanup` stops only processes recorded by this run and removes only its isolated scratch state. Preserve evidence.
6. `Helpers` documents every bundled helper and its invocation. Omit the section when no helper exists.

## Seed the feature map

Create `features/README.md` and a small set of feature files based on actual routes, commands, menus, or project documentation. Aim for three to five important features when that many are discoverable. Use [`references/feature-map-format.md`](references/feature-map-format.md).

## Prove the generated skill

1. Follow its launch instructions in a disposable local environment.
2. Run its doctor check.
3. Drive one mapped feature through the real user path.
4. Capture the named action and result evidence.
5. Run cleanup after success and after each failed attempt.
6. Confirm that the process and scratch state are gone while the evidence remains.

Do not call the generated skill complete until this check passes. If the available host lacks a preferred driver, use the next existing user-level interface and document the reduced coverage. If no credible driver exists, stop with the missing capability rather than inventing proof.

Do not commit, push, publish, install machine-wide files, or mutate production without separate authorization.

## Report

Return the generated skill path, mapped features, exercised feature, evidence location, cleanup result, and any unverified interface or isolation limit.
