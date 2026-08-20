# Verification Notes fixture

`notes.sh` is a user-facing CLI used to evaluate `bwh-create-verification`.

- Start: no persistent process is required. Invoke `./notes.sh` for each action.
- Input: `create <title> <body>` accepts note content.
- State: `NOTES_DATA_DIR` selects an existing isolated directory. The command refuses to run without it.
- Observe: `list` prints the stored notes. Exit codes report failures.
- Doctor: `doctor` reads directory metadata to confirm that the existing data directory is writable. It does not create or change files.
- Shutdown: no process remains. Cleanup removes only the unique `NOTES_DATA_DIR` created by the run and keeps evidence elsewhere.

Create a unique empty data directory before running `doctor`. Creating the directory is launch setup, not part of the read-only doctor check.

Supported commands:

```text
./notes.sh doctor
./notes.sh create "Release checklist" "Tag and publish"
./notes.sh list
```
