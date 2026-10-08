# Workflow states

Bounded work does not require a workflow-state artifact. Report its outcome,
validation, review result, and any remaining acceptance requirement directly.
Use the consuming project's states and acceptance policy when defined.

The following states apply to the formal spec and human-testing workflow when
the project uses it:

```text
DRAFT
NEEDS REFINEMENT
READY FOR HUMAN APPROVAL
APPROVED FOR DEVELOPMENT
IN DEVELOPMENT
READY FOR HUMAN TESTING
NOT READY FOR HUMAN TESTING
ARCHIVED
```

Allowed transitions:

```text
DRAFT -> NEEDS REFINEMENT
DRAFT -> READY FOR HUMAN APPROVAL
NEEDS REFINEMENT -> READY FOR HUMAN APPROVAL
READY FOR HUMAN APPROVAL -> APPROVED FOR DEVELOPMENT  (human only)
APPROVED FOR DEVELOPMENT -> IN DEVELOPMENT
IN DEVELOPMENT -> READY FOR HUMAN TESTING
IN DEVELOPMENT -> NOT READY FOR HUMAN TESTING
NOT READY FOR HUMAN TESTING -> IN DEVELOPMENT
READY FOR HUMAN TESTING -> IN DEVELOPMENT  (human testing found more work)
READY FOR HUMAN TESTING -> ARCHIVED  (human acceptance and archive validation required)
```

`ARCHIVED` is terminal for a human-accepted change whose temporary change
documentation has been archived and verified. Supporting documents do not need
independent workflow states.

For a project using automated acceptance, passing its required checks can
establish automated acceptance. Report it as such; it is not human acceptance.
Do not add a manual testing gate or translate it to `READY FOR HUMAN TESTING`
unless human testing is actually required. Archive requests still require
explicit human acceptance and verified archival under `bwh-archive-change`,
even when the change has no formal spec or state artifact.

An agent must not advance an artifact through a human-only transition. An agent
must not infer human acceptance from review, automated tests, merged code,
inactivity, or implementation completion.

`bwh-ask` is exempt from this contract: it produces no artifact and must not
report or infer any state transition.
