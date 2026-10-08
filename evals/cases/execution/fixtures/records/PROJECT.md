# Records fixture project

This project is a local evaluation fixture. `schema.sql` is the authoritative
database schema. `records.py` implements queries against SQLite. Callers pass
an organisation ID already authorised by their calling system; this fixture
does not implement authentication or production database policies.

Keep all query inputs parameterised and all returned data within the supplied
organisation. Required validation is `python3 -m unittest discover -v` from
this directory. Access changes also require real execution against a disposable
SQLite database containing two organisations with overlapping records.

Clear authorised changes with defined scope need no spec, PRD, progress log, or
state artifact, including features with several implementation chunks. An
internal sequence or task list is sufficient. Use a fresh independent reviewer
after implementation. Formal specs requested by the human belong in
`docs/specs/` and need human approval before implementation.

The task prompt defines allowed changes. It grants no commit, publication,
production-resource, or destructive-action authority. Archival and retrospectives
run only on an explicit request.
