# BWH Agent Toolkit development plan

Status: `READY FOR HUMAN TESTING`

Approved specification: `docs/specs/bwh-agent-toolkit-expansion.md`

## Objective

Deliver the BWH Agent Toolkit as a backwards-compatible expansion of `bwh-ai-workflow`, including catalogued profiles, safe installation and migration, Codex, Claude Code, and Cursor packaging, all nine approved skills, provenance, validation, and documentation.

## Tasks

| Task | Outcome | Dependencies | Status |
| --- | --- | --- | --- |
| P0 | Catalog, provenance, and validation base | None | COMPLETED |
| P1 | Profile-aware adoption and version 2 locks | P0 | COMPLETED |
| P2 | Toolkit display name and Cursor packaging | P0 | COMPLETED |
| P3 | `bwh-diagnose-bugs` | P0 | COMPLETED |
| P4 | `bwh-blast-radius` | P0 | COMPLETED |
| P5 | `bwh-create-verification` | P0, P1 | COMPLETED |
| P6 | `bwh-technical-writing` | P0 | COMPLETED |
| P7 | `bwh-grill` | P0 | COMPLETED |
| P8 | `bwh-write-agent-instructions` | P0 | COMPLETED |
| P9 | `bwh-review-architecture` | P0, P8 | COMPLETED |
| P10 | `bwh-prototype` | P0, P1 | COMPLETED |
| P11 | `bwh-skills-audit` | P0, P1 | COMPLETED |
| P12 | Integration, regression validation, and documentation | P2 through P11 | COMPLETED |

## Execution notes

- Work is split across bounded file groups. Shared integration files remain owned by the root development thread.
- No task may weaken the approved human gates, publication authority, privacy rules, or project ownership boundaries.
- Imported behavior must be adapted to the portable rules in the approved specification and attributed at its pinned upstream revision.
- Commits and publication remain separately authorized.

## Validation record

- 34 unit tests pass, covering catalog schema, host metadata, profile resolution, version 1 migration, version 2 lock validation, local-edit preservation, profile pruning, failed-validation recovery, path containment, Git-tree-only copies, symlink rejection, safe staging, retired-skill migration, stable source identity, frontmatter names, and relative references.
- `scripts/validate_catalog.py`, `scripts/validate_skills.py`, and `scripts/validate_package.py` pass.
- The isolated verification-notes fixture passes read-only doctor, create, second-view list, scoped cleanup, and retained-evidence checks.
- Toolkit policy eval A passes 41/41 cases with 574/574. Toolkit policy eval B plus workflow regression passes 47/47 cases with 658/658. The 12 overlapping workflow baseline cases remain 168/168.
- JSON parsing, Python compilation, shell syntax, privacy and host-leakage scans, relative-link resolution, executable-helper checks, and `git diff --check` pass.
- Clean release-candidate commit `feab4a7e1312cb5be247d4473b632fb79dc70a1c` passes the disposable fresh `full` installation and version 1 workflow migration tests. The first installs 17 skills without changing project-owned files. The second preserves a conflicting local change and migrates to the eight-skill `workflow` profile only after explicit conflict resolution.
- Automated fresh installation and version 1 update checks pass. Human AC15 confirmation remains pending. Live representative runs and required metadata for Codex, Claude Code, and Cursor remain before any host status changes from `pending`.

## Next handoff

Start a new Codex session so it reloads the machine-level full profile, then run the representative live-host and human installation checks in `docs/testing/bwh-agent-toolkit-expansion.md`. Keep all host statuses `pending` until their checks pass. No commit or publication is authorized.
