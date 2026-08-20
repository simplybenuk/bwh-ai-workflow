---
name: bwh-diagnose-bugs
description: Diagnose hard bugs and performance regressions through a repeatable feedback loop, minimized reproduction, falsifiable hypotheses, and targeted evidence. Use when the user asks to diagnose or debug broken, failing, throwing, flaky, or slow behavior. If the user asks only for diagnosis, report the cause and evidence without implementing a fix.
---

# Diagnose bugs

Find the cause through a signal that can distinguish the reported failure from success. Match the loop to the cheapest credible reproduction. A browser or integration path is valid when no smaller path represents the failure.

## Protect evidence

- Keep credentials in the environment. Do not place them in commands, fixtures, or reports.
- Replace secrets in logs, traces, requests, screenshots, and quoted output with `<REDACTED>`.
- Share only the lines or fields needed to support the diagnosis.
- Request a safer artifact when redaction would remove the signal.

## Build the feedback loop

1. Read the report, relevant project instructions, architecture decisions, and recent changes.
2. Define the exact observable symptom. Avoid substitutes such as "the command exits" when the report concerns incorrect output.
3. Choose the tightest credible loop. Prefer an existing focused test, command, request, or user-facing driver. Use a trace replay, small harness, differential run, repeated stress run, or guided human reproduction only when needed.
4. Run the loop and record its command, verdict, cost, limitations, and redacted signal.
5. Improve determinism by isolating state, pinning time or randomness where valid, and removing unrelated setup.

For intermittent failures, measure a reproduction rate and raise it enough to compare hypotheses. Do not call a slow but representative integration loop invalid only because it takes minutes.

Stop if no credible loop can reach the symptom. Report what was tried and identify the smallest missing access or artifact, such as a redacted trace, environment access, or permission for temporary instrumentation. Do not present an untested theory as the cause.

## Reproduce and minimize

Run the loop until it shows the reported failure. Remove inputs, callers, configuration, data, and steps one at a time. Re-run after each change and retain only elements needed for the failure. If minimization would erase a timing or integration condition, keep that condition and state why.

## Test hypotheses

1. Write three to five ranked hypotheses when the evidence supports that many. Each hypothesis must predict an observable result.
2. Test one variable at a time, starting with the cheapest high-information probe.
3. Prefer direct inspection at the boundary that separates hypotheses. Add narrowly targeted instrumentation only when inspection is insufficient.
4. Tag temporary instrumentation with a unique marker. Remove every tagged change before completion.
5. For performance regressions, establish a measured baseline and compare profiles, query plans, timings, or versions rather than relying on general logs.

Use sequential probes when independent workers are unavailable. Optional parallel investigation must not duplicate mutations, leak private evidence, or replace the shared feedback loop. If a permission or evidence question cannot use a structured question interface, ask it as a numbered plain-chat question and wait when the answer controls a write, production access, or disclosure.

## Lock down and verify

When the user authorized a fix:

1. Add a regression test before the fix when a test seam represents the real failure.
2. Run the regression test and confirm that it fails for the expected reason.
3. Apply the smallest fix that addresses the supported cause.
4. Run the regression test, then re-run the original full reproduction.
5. Remove temporary instrumentation and scratch artifacts that do not belong in the repository.

If no suitable test seam exists, record that limitation rather than adding a shallow test that cannot catch the bug.

When the user requested diagnosis only, do not edit source or test files. Read-only commands are allowed. Ask separately before adding instrumentation, a test, or a helper artifact.

Do not commit, push, publish, change external systems, or use production instrumentation without separate authorization.

## Report

Return:

- the reproduced symptom and feedback-loop command;
- the supported cause, with evidence and discarded hypotheses;
- the loop's cost and limitations;
- the fix and regression evidence, if a fix was authorized;
- removed instrumentation and any remaining uncertainty.

Distinguish observed facts from inference. Never include unredacted secrets.
