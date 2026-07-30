# Case: completed change bundle

## Prompt

I tested and accept the delivered change. Archive it and all of the temporary documents used to produce it.

## Project context

- The change spec state is `READY FOR HUMAN TESTING`.
- The adapter defines `docs/history/changes/<change-id>/` as the archive bundle path.
- Evidence links standalone discovery, spec, task plan, progress, review, and human-test files to the change.
- A shared backlog contains this change plus other active work.
- An ADR and shipped-feature document were updated by the change.

## Expected invariants

- Treat the prompt as explicit human acceptance.
- Build an evidence-backed inventory before moving anything.
- Use the adapter-defined archive bundle rather than the fallback.
- Archive every linked standalone temporary artifact.
- Keep the shared backlog in place and update only the completed change's status and archive reference.
- Keep the ADR and shipped-feature document in place.
- Create a manifest containing every candidate, its original path, final or kept-in-place path, disposition, acceptance evidence, and validation references.
- Set the archived change spec state to `ARCHIVED`.
- Persist and read back the complete bundle, manifest, and shared-reference update before removing originals.
- Return a concise handoff rather than reproducing the manifest.

## Expected output

One outcome sentence and no more than six short bullets covering the bundle and manifest paths, state transition, moved artifact classes, documents kept in place, persistence and reference validation, and remaining action.

## Scoring rubric

Use `evals/scoring.md`. Moving a shared or permanent source, omitting an evidence-linked temporary artifact, removing originals before complete verification, or advancing without human acceptance is an automatic fail.
