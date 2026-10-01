# State and Recovery

Use when loading, empty, no-result, partial, error, offline/disconnected, stale, retry, resume, draft, or long-running work is materially in scope.

## State model

Do not treat "not ideal" states as one generic error.

Distinguish when relevant:

- initial;
- loading;
- empty;
- no search result;
- no filtered result;
- partial;
- stale;
- delayed;
- syncing;
- disconnected/offline;
- permission denied;
- not configured;
- unavailable;
- error;
- retrying;
- success;
- background processing;
- cancelled.

## Loading

Preserve useful context during refresh when safe.

Prefer local loading indicators when only part of the surface is refreshing.

Avoid replacing an entire stable interface with skeletons for every small update.

Loading UI should not imply progress precision that does not exist.

## Empty state

An empty state should explain the reason when the reason is knowable.

Differentiate:

- there is genuinely no data/content;
- filters exclude all results;
- search returned none;
- setup is incomplete;
- user lacks permission;
- source failed.

Do not make all absence look like zero or "nothing here."

## No-result recovery

Preserve the user's search/filter input.

Suggest recovery such as:

- clear conflicting filter;
- broaden scope;
- change query;
- create/add item when appropriate.

Do not erase the query on failure.

## Partial state

If only part of the data/work succeeded:

- identify the reliable portion;
- identify what is missing/failed;
- avoid presenting the whole surface as complete;
- provide recovery when supported.

## Stale and delayed state

When current data may be outdated:

- show freshness/last update when material;
- distinguish stale from failed;
- preserve useful old data if safer than a blank screen;
- communicate what actions remain safe.

Do not show stale data as live/current.

## Retry

Retry behavior should be safe and understandable.

Clarify:

- what will be retried;
- whether duplicate execution is possible;
- whether prior work is preserved;
- whether user input must change first.

Do not encourage blind retry for deterministic validation/configuration failures.

## Resume

For interruptible work, define:

- what state is preserved;
- where the user returns;
- whether background work continued;
- how conflicts/staleness are handled.

Do not force a full restart after a recoverable interruption.

## Long-running work

For jobs that outlive the immediate interaction:

- acknowledge start;
- show queued/running/final state;
- allow navigation away when safe;
- preserve access to status/history;
- show completion/failure on return;
- support cancel/retry only when real semantics exist.

Do not confuse request acceptance with job completion.

## Draft and unsaved state

For meaningful user-authored work:

- define explicit save, autosave, or draft behavior;
- communicate save failure;
- protect against accidental loss where appropriate;
- preserve valid work through recoverable errors.

Avoid warning for trivial changes that creates confirmation fatigue.

## Recovery priority

Prefer:

1. prevent avoidable loss;
2. preserve user work/context;
3. explain the actual state;
4. provide the safest next action;
5. escalate to destructive reset/restart only when necessary.

## Validation

Verify representative:

- loading;
- empty;
- no-result;
- partial;
- stale;
- disconnected/offline where relevant;
- failed request;
- safe retry;
- interrupted/resumed work;
- long-running completion/failure;
- preserved draft/input;
- accessibility of state/status changes.
