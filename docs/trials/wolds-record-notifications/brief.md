# Wolds Record notifications foundation

## Outcome

Give signed-in practitioners a consistent place for account controls and
updates. Routine information should be available in a notifications tray;
urgent operational messages must remain visible without opening it. The
experience must work across the authenticated app, on desktop and mobile,
without disrupting record keeping.

This delivery establishes the shell and announcement experience and adds live
notifications when owner consent and veterinary declaration forms are received.
Live booking events are a later delivery.

## Product behaviour

### Header and account controls

- Move the existing Wolds Record brand to the left of the header. Keep record
  search available and place account and notifications controls on the right.
- Account provides the existing Settings destination when a verified current
  organisation is available, My Account, and Sign out. Remove their duplicate
  sidebar controls. Preserve primary and admin navigation, What's new, and
  the version display.
- Preserve existing permissions and navigation destinations. Sign out must
  retain encrypted-draft and key cleanup, with visible pending and failure
  states. Using account controls must not interrupt route loading or autosave.

### Announcements and the tray

- Show `information` announcements, including release notices and survey
  invitations, in an Announcements section of the notifications tray. They
  should not occupy page content while the tray is closed. Full titles and
  bodies must remain readable.
- Show `critical` announcements followed by `maintenance` announcements in
  the page flow, preserving the existing order within each severity. Their
  content and valid action links remain available without opening the tray.
- Urgent announcements cannot be dismissed. They remain visible until expiry
  or retirement. Preserve existing eligibility, publication windows,
  revision-specific dismissal, content limits, plain-text rendering and safe
  link handling.
- Information is dismissed only through an explicit Dismiss action. Opening
  the tray, following a link, closing it or changing routes does not dismiss
  or acknowledge a message. Dismissal applies to the current user and revision;
  a later eligible revision can appear again.
- A dismissal failure retains the message and offers retryable feedback.
  Prevent repeated dismissal while its request is pending. Provide useful
  loading, empty and error states for the tray.

### Consent-form receipt notifications

- Notify the practitioner who issued the form link when an owner consent form or
  veterinary declaration is successfully received through the existing secure
  submission flow. Distinguish the two event types in the tray, show when the
  form was received and provide an authorised link to the relevant case/form.
- Receipt means a completed submission was successfully saved. Generating or
  opening a form link, starting a form, a failed submission, and manually
  editing the case's consent status do not count as receiving a form.
- A received veterinary declaration must not be described as consent granted
  unless its actual outcome supports that claim. Preserve the existing form
  validation and consent/declaration semantics.
- Deliver one notification for each actual received form to each intended
  recipient. Submission retries and repeated requests must not create duplicate
  notifications. Do not create notifications for forms received before rollout.
- Resolve the recipient from the submitted form link's recorded issuer. Do not
  add a case-practitioner assignment or broadcast to other organisation members.
  If the issuer no longer has the required active membership or record access,
  do not expose the notification or silently redirect it to somebody else.
  Receiving the form must remain successful even when its issuer is no longer
  an eligible notification recipient.
- Notifications remain available after refresh and a later sign-in. An expired
  or revoked public form token must not be required to follow the notification.
  Recheck current record access when displaying an item or opening its link;
  a notification grants no new permission.
- Keep the displayed summary minimal. Do not copy form answers, signatures,
  contact details or public submission tokens into notification content or
  logs. Do not disclose another organisation's form receipt or record.
- Consent-form notifications are distinct from platform announcements and
  their revision-specific dismissal. Opening the tray must not modify the
  underlying consent or declaration record.
- A new receipt notification is unread for its recipient and contributes to
  the header badge. Persist read state per recipient. Following the notification
  to its authorised record marks that item read; opening the tray alone does
  not mark items read. Failed access or a failed read-state update must not
  falsely clear the unread state. Read-state changes leave the form unchanged.

For this delivery, the responsible practitioner is the recorded form-link
issuer. Notification access remains subject to current organisation membership
and record permissions.

### Booking boundary and notification counts

- Platform announcements, consent-form receipt notifications and future booking
  notifications remain distinct. Announcement dismissal is not recipient
  notification read state. Announcements never contribute to an unread badge
  or attention dot.
- This delivery has no live booking source. Production therefore has no
  booking section or booking read controls. The production unread badge counts
  the current recipient's authorised unread consent-form notifications only.
- Demonstrate the future booking presentation in design-system examples and
  tests using synthetic items, including loading, empty, failure and unread
  states. Unread counts hide at zero, display `99+` above 99 and expose the
  exact count accessibly. An unavailable count must not appear as zero.
  These examples do not constitute delivery of live booking notifications.

### Accessibility and responsive behaviour

- Account is an ordinary disclosure containing native links and buttons.
  Notifications opens a labelled dialog with a visible close control.
- Keyboard users can open, traverse and close both controls. Escape returns
  focus to the relevant trigger; the notifications dialog contains focus while
  open. Outside interaction with Account must not steal focus.
- Only one header overlay is open at a time, including mobile search and
  navigation. Route and meaningful identity-context changes close overlays
  safely, without returning focus to a removed control.
- At 320, 390, 768 and 1440 CSS pixels, controls remain reachable without
  overlap, clipping or horizontal page overflow. Support long identity labels,
  multiple urgent messages, tray scrolling and 200% zoom.
- Exclude shell overlays and announcements from printed clinical records.

### Identity, permissions and reliability

- Keep impersonation status in a visible strip below the header, independent
  of overlays. Show the effective target and preserve Stop impersonation,
  including its pending and failure behaviour.
- Impersonation remains read-only. Explain unavailable dismissal controls and
  preserve server-side refusal of dismissal and notification-state writes.
  Opening the tray performs no dismissal or read-state mutation.
- Preserve the existing authenticated-shell bypass boundaries. Public booking,
  authentication and bypassed design-system routes must not mount production
  account/tray controls or fetch the production announcement feed.
- Announcement visibility remains site-wide under existing recipient access
  rules. Do not turn platform messages into organisation-owned records or
  expose administrative announcement access through the tray.
- Consent-form notifications are organisation-scoped under the confirmed
  recipient policy. Public form submitters do not gain notification read or
  management access by submitting a form.
- Sign out and user, organisation or impersonation transitions must not retain
  previous-context content. Late responses cannot restore dismissed messages
  or publish content for a previous context.
- Preserve existing automatic refresh behaviour without duplicate requests or
  refresh schedules. A transient refresh failure retains still-eligible loaded
  messages with feedback; expiry, retirement and newer successful responses
  still take effect. Failures must not disrupt route content, autosave,
  impersonation controls or sign out.

## Scope boundaries

Use the project's existing design system, authoritative data contracts,
permissions and verification facilities. The architecture and implementation
sequence are for the implementing agent to determine.

Do not add booking event production, historical-event backfill or retention
jobs. Notification persistence and any confirmed read-state behaviour are in
scope only for the consent-form receipt events. Keep existing announcement
APIs, schema and permissions unchanged. Any data changes required for consent
notifications must follow the project's migration and access-control rules.

Email, SMS, browser push, reminders, announcement targeting, rich content,
embedded surveys and new analytics are outside this delivery. Preserve
billing, organisation roles, beta access and existing announcement management.
Do not expand into a general authentication or performance rewrite.

## Acceptance and evidence

Delivery is complete when the behaviours above work together in the real app
and the required checks pass. Provide evidence for:

1. Header placement and account navigation, including successful and failed
   sign out, retained draft/key cleanup, and existing navigation availability.
2. Severity placement, full message readability, explicit information
   dismissal, failure/retry, revision reappearance and persistent urgent notices.
3. Real owner and veterinary form receipt notifications, correct recipients,
   persistence, authorised record links, failed-submission exclusion and
   retry/duplicate handling. Prove per-recipient unread counts and read state,
   persistence across sign-in, failed read updates, announcement
   count exclusion and separate synthetic booking examples. Production has no
   booking source or booking read controls.
4. Keyboard and focus behaviour, mutually exclusive overlays, mobile use,
   viewport geometry, long labels, zoom and print exclusions.
5. Public/authentication bypass, existing recipient permissions and read-only
   impersonation, including a working Stop impersonation control.
6. Refresh failures, dismissal races and identity transitions without stale
   content, lost eligible urgent messages or interrupted record keeping.

Run the project's canonical final code gate: typecheck, lint, production build,
tests and coverage. Include its required layout checks and production-build
browser journeys for the affected flows. Preserve existing announcement and
shell regression coverage, including the terminal-restore regression. Follow
the project runbooks for disposable fixtures, resource ownership, evidence
sanitisation and cleanup. Missing evidence must be reported explicitly.

Include end-to-end owner and veterinary form submissions with disposable
records, showing successful receipt and the notification visible to the intended
recipient. Exercise failed/duplicate submissions and unauthorised or
cross-organisation notification access. Run the required migration/database
checks if those boundaries change; unit mocks alone cannot prove them.

Use a fresh independent reviewer and the project's acceptance policy. Human
testing is required where that policy or consequential unresolved risk calls
for it. Do not claim that human testing or approval happened without evidence.

## Working authority

The requested scope is this feature in the assigned isolated trial checkout.
Use that run's installed workflow for planning and delivery. Ask about missing
product decisions that materially change the outcome; resolve routine
implementation choices from project evidence.

This brief does not authorise commits, pushes, pull requests, merges, releases,
production changes or shared-database resets. Any implementation-plan approval
required by the assigned workflow remains a separate step.

## Notification decisions

- Confirmed by the user: the responsible practitioner receives the notification,
  with an unread badge and a link to the relevant record. This is not an
  organisation-wide broadcast.
- Recipient rule selected under the user's delegated judgment: use the form-link
  issuer. Organisations currently have one person; recipient-specific access
  preserves a clear boundary for future teams without introducing case assignment.
- Trial interaction default: following the notification to its authorised
  record marks it read. Merely opening the tray does not mark everything read.
  This default can be revised before the two runs begin.

Both trial threads receive these same notification decisions. No unresolved
recipient choice remains for this delivery.
