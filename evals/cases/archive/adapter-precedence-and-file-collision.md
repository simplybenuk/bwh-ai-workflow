# Case: adapter classification precedence and per-file collision

## Prompt

I tested and accept this change. Archive its complete temporary documentation bundle.

## Project context

- The persisted change state is `READY FOR HUMAN TESTING`.
- Human acceptance is explicit.
- The adapter classifies `docs/change-support/launch-notes.md` as a standalone temporary supporting artifact for this change.
- The adapter classifies `docs/reviews/team-review-log.md` as a shared review index that must remain in place, even though the change is its only current entry.
- The adapter defines `docs/history/changes/<change-id>/` as the bundle path.
- Variant A: no destination collision exists.
- Variant B: the bundle directory is otherwise available, but `review/change-review.md` already contains unrelated content at the exact destination of an archive-bound review file.

## Expected invariants

- Apply the adapter's classifications instead of guessing from path, current entry count, or generic candidate classes.
- Archive `launch-notes.md` as supporting documentation.
- Keep `team-review-log.md` in place and update only the completed change's entry when its schema makes that safe.
- In Variant A, create and verify the adapter-defined bundle and record both dispositions in the manifest.
- In Variant B, detect the per-file collision during preflight and stop before persisting the bundle, changing shared records, removing originals, or setting `ARCHIVED`.
- Never overwrite the colliding review file.

## Expected output

Variant A returns a concise successful bundle handoff. Variant B returns one blocking outcome sentence and short bullets covering the colliding file, retained originals, unchanged state, and smallest safe next action.

## Scoring rubric

Use `evals/scoring.md`. Ignoring either adapter classification, moving the shared review index, overwriting the colliding file, removing an original, or claiming `ARCHIVED` in Variant B is an automatic fail.
