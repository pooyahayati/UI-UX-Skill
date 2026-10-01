# Operational Interaction Patterns

Use this reference for high-frequency dashboards, real-time operations, search-heavy products, bulk actions, concurrent editing, and long-running jobs.

## Error prevention

Operational UX should prevent avoidable mistakes before relying on recovery.

Review:

- duplicate submit/action
- accidental destructive action
- stale edit
- concurrent edit
- unsaved changes
- partial bulk failure
- retry safety
- long-running operations
- repeated command execution
- irreversible state changes

## Duplicate actions

For submit/save/pay/create-like actions:

- disable or guard repeated submission when duplicate execution is unsafe
- show clear in-progress state
- preserve context if the request is slow
- distinguish "still working" from "failed"
- make retry semantics clear

Do not disable controls forever if the request fails.

## Stale and concurrent edits

When records can be edited by multiple users or processes:

- detect stale version where supported
- show what changed
- avoid silently overwriting newer data
- offer refresh, merge, or retry behavior appropriate to the domain
- preserve the user's unsaved input when practical

Do not make the UI appear to save successfully when the backend rejected a stale write.

## Unsaved changes

Use warnings only when meaningful work would be lost.

Prefer:

- dirty-state tracking
- safe navigation guard
- explicit save/discard
- autosave only when product semantics support it

Avoid confirmation fatigue for trivial changes.

## Bulk operations

For bulk actions:

- show selected count
- clarify scope
- distinguish all-visible vs all-filtered
- preview high-impact operations when useful
- handle partial success/failure
- show failed items and recovery path
- avoid losing the selection/context after recoverable failure

## Long-running jobs

For imports, exports, reports, syncs, large updates, or background processing:

- acknowledge start
- show progress or meaningful phase
- allow navigation when safe
- provide job history/status
- expose completion/failure
- support retry/cancel only when semantics allow it
- do not block the whole application unnecessarily

## Search UX

Distinguish search types:

### Global search

Use for finding entities/destinations across the product.

Clarify:
- searchable entity types
- scope
- recent items
- permission filtering
- result grouping

### Table/list search

Use for filtering a known dataset.

Clarify:
- which fields are searched
- debounce/server search behavior
- empty/no-result recovery
- active query state

### Command palette

Use for fast navigation/actions for frequent users.

Commands must:
- respect permissions
- be searchable by user language/terminology
- be discoverable beyond shortcut-only access
- show destructive/high-impact commands clearly

## No-result recovery

When search returns nothing:

- preserve the query
- explain scope
- suggest clearing conflicting filters
- offer nearby valid actions
- avoid pretending the dataset is empty

## Real-time dashboards

When data updates live:

- do not cause disruptive layout shifts
- keep the user's reading/selection context stable
- distinguish new data from changed data when useful
- avoid continuously resorting rows while the user is interacting unless required
- consider pause/freeze/live-toggle for dense monitoring views
- show connection status
- show stale/disconnected state
- define update frequency appropriate to the task

## Incoming updates

Possible strategies:

- subtle highlight
- "new items available" banner
- append without stealing focus
- controlled re-sort
- manual refresh for disruptive lists

Choose based on urgency and task.

## Connection state

Distinguish:

- live
- reconnecting
- delayed
- stale
- disconnected
- failed

Do not show a green/live indicator when data is no longer current.

## Notifications and alerts

Alerts should support action, not just attract attention.

Define:

- severity
- source
- age
- acknowledgement
- owner
- escalation
- next action
- resolved state

Avoid alert fatigue from low-value repeated notifications.

## QA scenarios

Test:

- double click/submit
- network timeout
- retry
- partial bulk failure
- stale edit
- second user update
- unsaved navigation
- background job completion/failure
- search plus active filters
- empty/no-result distinction
- live connection loss/recovery
- incoming data while user is reading/selecting rows
