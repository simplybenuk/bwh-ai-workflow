# Review and checkpoint format

## Common reviewer brief

Give all reviewers the same task-specific brief. Fill the fields from the run index and captured evidence, then add the rubric below.

> Review the specified journeys and states at the recorded revision. Inspect the supplied screenshots directly, relevant code, and interaction evidence. Work read-only and complete the review yourself. Do not contact other reviewers or edit files. Identify missing evidence and separate observed defects from preferences. Score each category out of 10 with one or two lines of evidence and a screen/state/file reference. Use N/A with a reason when a category cannot be assessed. Rank recommendations by user impact, giving the affected screen/state, problem, proposed change, expected benefit, and any product decision or shared-component risk. For a later scoring pass, assess the resulting UI afresh, explain score changes, and include remaining problems and regressions.

Supply scope and exclusions, device priority, artifact paths, relevant source paths, interaction results, revision, and the phase being reviewed. For a subsequent pass, also supply baseline screenshots and that model's prior scores. Withhold peer outputs until the pass is complete. A replacement model has no personal score history; disclose that comparison limit.

## Rubric

1. Visual hierarchy and clarity
2. Mobile layout and touch ergonomics
3. Consistency with the design system
4. Status communication, including warnings and domain states
5. Error, empty, and loading states
6. Copy and microcopy, following the project's house style
7. Accessibility, including contrast, focus, labels, target sizes, and announcements
8. Flow efficiency, including steps and taps for the main tasks
9. Overall judgment

Use these anchors consistently across reviewers and rounds:

- 1-2: serious obstacles to understanding or completing the task.
- 3-4: substantial recurring problems.
- 5-6: usable, with noticeable friction or inconsistency.
- 7-8: clear and cohesive, with specific remaining weaknesses.
- 9-10: strong evidence of polish across the reviewed states, with little remaining friction.

Overall is a reasoned judgment, not a required arithmetic average. Do not score absent evidence as a success. Distinguish screenshot observations, code inspection, and exercised interactions, especially for accessibility and efficiency.

## Merged scorecard and recommendations

Use a table with one row per category and separate before, after, and delta columns for each reviewer. Keep N/A values and comparability notes explicit. Preserve individual scores rather than replacing them with an average. If a chart helps compare rounds, accompany it with the score table.

Assign stable suggestion IDs within the run. Merge duplicate recommendations under one ID while retaining reviewer attribution. Each suggestion records:

- priority, affected journey/screen/state, and evidence;
- problem, proposed change, and expected user benefit;
- reviewers agreeing, disagreeing, or raising a different solution;
- product decisions, shared-component effects, and implementation scope;
- disposition and reason, plus the human's steering when given.

Keep full reviewer responses beside the evidence. Record team changes and missing reviews. A partial team is an incomplete review pass until the human agrees to change the team.

## Round checkpoint

Present enough for a design decision without requiring the human to read the raw reviews:

1. Round number, scope, assessed revision, and reviewer team.
2. Before/after pairs for changed screens, mobile first, with stable filenames and local links or authorised hosted images. Flag missing pairs.
3. Scorecard and concise evidence for the main gains, regressions, and disagreements.
4. Changes made, reasons, deferred baseline suggestions, and effects elsewhere in the app.
5. Actual validation results and evidence limits.
6. New ranked suggestions with IDs and specific questions for decisions that need human judgment.
7. A clear request to stop, select or adjust suggestions for another round, or supply new direction.

Save this report locally and update the run index to `awaiting human`. Do not launch implementation work while waiting. When the human stops, update it to `stopped` and link the deferred suggestions. When they commission another round, record that steering before work begins.
