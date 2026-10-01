# Personalization, Role-Aware UX, and Data Trust

Use this reference for operational products where repeated use, user preferences, saved views, or trust in dashboard data materially affects UX.

## Personalization principle

Personalization should reduce repeated work without making the product unpredictable.

Prefer durable preferences for repeated choices, not one-off cosmetic controls.

## Configuration hierarchy

Use:

`Locked Constraints -> Design System Defaults -> Published Owner Config -> User Preferences`

Users may override only fields explicitly marked as user-configurable.

## Useful user preferences

Depending on product context:

- Light/Dark/System preference
- density preference
- sidebar collapsed/expanded state
- preferred landing page when safe
- table page size
- visible columns
- column order/width where supported
- saved filters
- saved sorts
- saved views
- selected dashboard layout or optional widgets
- date-range preference
- locale/display preferences where permitted
- reduced motion preference

Do not expose every system setting as a user preference.

## Saved views

For filter/table-heavy products, consider Saved Views containing:

- filter criteria
- search scope
- sort
- visible columns
- column order
- grouping
- date range
- density when appropriate

Views may be:
- private
- shared with a team
- owner/admin published

Clarify permission to create, share, edit, and delete shared views.

## Preference resilience

When owner constraints or schemas can change, read `preference-reconciliation.md`.

Preferences should:
- survive normal navigation/reloads
- degrade safely when fields/columns are removed
- migrate when schema changes
- provide reset to default
- not store sensitive data unnecessarily

## Role-aware UX

Different roles may need different:

- landing pages
- primary actions
- visible summaries
- shortcuts
- table defaults
- alerts
- terminology/context

Do not create entirely separate products when a shared shell plus role-aware emphasis is sufficient.

Role-aware presentation must follow authorization, not replace it.

Never show a privileged action merely because the UI role configuration says so if permission is absent.

## Power-user UX

For frequent operational use, consider:

- keyboard shortcuts
- command/search palette
- bulk actions
- saved views
- recent items
- quick filters
- dense mode
- inline editing where safe
- predictable focus behavior

Do not add shortcuts without discoverability or conflict handling.

## Onboarding and contextual help

For complex products, consider:

- concise first-use orientation
- contextual empty states
- inline explanations for unfamiliar metrics/actions
- progressive disclosure
- dismissible guidance
- help links near high-risk/complex operations

Avoid permanent tutorial clutter.

## Data Trust UX

A dashboard should help users understand the reliability and scope of what they see.

Where relevant expose:

- last updated time
- data freshness
- sync status
- source
- timezone
- active filter scope
- date range
- metric definition
- comparison baseline
- partial/incomplete data state
- stale data warning
- failed source/connection state

Do not present stale or partial data as if it were current and complete.

## Metric definition

Important metrics should be interpretable.

When ambiguity is likely, provide:
- concise definition
- included/excluded scope
- aggregation rule
- unit/currency
- time window
- comparison basis

Use tooltips/help panels sparingly; critical context should not require hovering.

## Global filters

When filters affect multiple widgets:

- make scope visible
- show active filters
- clarify which widgets are excluded
- avoid hidden inherited filters
- provide reset/clear behavior
- preserve/share filter state intentionally

## Data freshness states

Distinguish:

- live
- recently updated
- stale
- syncing
- delayed
- partial
- failed

Do not use color alone.

## Drill-down and traceability

For important metrics/alerts, consider a path from summary to underlying records.

Users should be able to answer:

`Why is this number here?`

when the product domain requires traceability.

## User research signals

When improving an existing product, useful evidence includes:

- high-frequency workflows
- support tickets
- repeated user mistakes
- abandoned steps
- search/filter patterns
- unused controls
- task completion time
- role-specific pain points

Do not infer user needs solely from visual inspection when stronger evidence is available.

## QA

When personalization/data-trust features exist, verify:

- preference persistence
- reset behavior
- migration/fallback
- role and permission boundaries
- shared-view permissions
- filter scope clarity
- timezone/date correctness
- stale/partial/failure states
- mobile behavior
- RTL/LTR
- accessibility
