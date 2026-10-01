# Feedback and Status

Use when success, warning, error, progress, notice, status, toast, banner, or system feedback is materially in scope.

## Match feedback to scope

Choose the feedback surface according to where the condition matters.

### Inline

Use for:

- one field;
- one row;
- one control;
- one local section;
- a local validation/result.

### Page/surface-level

Use for:

- a condition affecting the current page/workspace;
- unresolved prerequisite;
- partial page failure;
- important local warning.

### Global/persistent

Use only when the condition matters beyond the current surface.

### Transient

Use for low-risk acknowledgement where the user does not need to act or revisit the message.

Do not use transient toast-only feedback for critical failure or recovery instructions.

## Status semantics

Status should communicate meaning in text, not color alone.

Useful distinctions may include:

- ready;
- pending;
- running;
- success;
- warning;
- degraded;
- failed;
- paused;
- cancelled;
- stale;
- disconnected;
- unknown.

Do not label an uncertain state as success.

## Progress truthfulness

Use exact percentage only when progress is actually measurable.

Otherwise use:

- phase;
- step;
- indeterminate progress;
- queued/running status;
- last update.

Do not simulate progress to make a task feel faster.

## Optimistic vs confirmed state

When the UI updates optimistically, distinguish local acknowledgement from authoritative confirmation if failure would matter.

Rollback or recovery should be understandable.

Do not show "Saved" or "Completed" before the system can support that claim.

## Failure feedback

A useful failure message answers:

- what failed;
- what was affected;
- whether user work/data was preserved;
- whether retry is safe;
- what the user can do next.

Avoid generic "Something went wrong" when better information is available.

Do not expose raw internal exceptions as primary user messaging.

## Partial success

When some items succeed and others fail:

- report both;
- show affected count/items when useful;
- preserve failed context;
- provide recovery/retry where supported.

Do not show a generic success confirmation for a partially failed operation.

## Status persistence

Feedback should persist long enough for its consequence.

A status that requires action must not disappear before the user can act.

A dismiss action does not mean the underlying problem is resolved.

## Announcements

Dynamic status changes should be available to assistive technologies when the update matters and is not otherwise discoverable.

Avoid announcing every minor live update.

Use announcement priority proportional to urgency.

## Repeated notifications

Avoid flooding users with repeated identical notices.

Where the underlying issue persists:

- consolidate;
- update existing status;
- provide a durable location;
- suppress redundant transient messages.

## Validation

Verify:

- success;
- warning;
- local error;
- global error;
- partial success;
- long-running progress;
- optimistic failure/rollback when relevant;
- screen-reader discoverability for important dynamic status;
- non-color meaning;
- persistence/dismiss behavior.
