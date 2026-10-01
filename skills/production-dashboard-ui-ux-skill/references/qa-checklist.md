# Final QA Checklist

Use before declaring major UI work complete.

## Coverage report

Record what was actually checked:

| Dimension | Coverage |
| --- | --- |
| Routes/screens | list |
| Workflows | list |
| Viewports | desktop/tablet/mobile/etc |
| Themes | Light/Dark |
| Direction | RTL/LTR |
| Roles | list or not tested |
| States | default/loading/empty/error/stale/etc |
| Personalization | tested / not applicable / not tested |
| Runtime owner config | tested / not applicable / not tested |
| Rendered inspection | yes/no |
| Automated checks | list |
| Visual baseline/diff | captured / existing / unavailable / not applicable |
| UX evidence | measured / observed / user-provided / inferred / unavailable |
| Required specialists | used / unavailable / not applicable |
| Recommended specialists | used / fallback / unavailable / not applicable |
| Not checked | list |

Do not imply coverage that was not performed.

## Visual regression

For broad visual changes, read `visual-regression.md`.

Verify where applicable:

- representative baseline exists or its absence is reported
- before/after captures use stable states/viewports
- dynamic noise is controlled without hiding relevant behavior
- pixel diffs are reviewed semantically
- intentional changes are distinguished from regressions
- uncaptured surfaces are listed

## Existing-product regression

- baseline inspected
- working tree and user changes protected
- business logic preserved
- permissions preserved
- validation and data meaning preserved
- routing and deep links preserved
- saved preferences preserved/migrated
- before/after comparison performed where meaningful

## UX evidence and validation

For significant UX findings, read `ux-evidence-and-metrics.md`.

Verify:

- evidence source is stated when available
- confidence matches evidence strength
- measured claims have a baseline/source
- no fabricated uplift, time saving, or compliance percentage
- validation method matches the hypothesis

## Product and UX

- screen purpose is clear
- primary action is discoverable
- hierarchy matches importance
- unnecessary steps and controls reduced
- repeated user choices are persisted when beneficial
- empty, error, stale, and permission states are useful
- destructive actions communicate consequence
- role-specific emphasis does not bypass authorization

## Data Trust UX

Where relevant:

- data freshness is understandable
- last-updated time is accurate
- timezone/date-range context is clear
- active filter scope is visible
- stale/partial/sync-failure states are distinguished
- important metric definitions are accessible
- summary-to-record drill-down exists where traceability is required

## Design system and changeability

Read `design-system-architecture.md`.

Verify where applicable:

- semantic tokens used
- component states consistent
- uncontrolled variants reduced
- repeated visual values are centralized
- common design changes do not require unrelated page edits
- config schema is typed/versioned
- precedence is deterministic
- invalid/missing config has a safe fallback
- icon family coherent
- spacing, radius, and elevation intentional
- no unjustified AI-dashboard clichés

## Runtime Owner Control Center

When implemented, read `runtime-ui-governance.md`.

Verify:

- unauthorized users cannot access or mutate configuration
- authorization is not UI-only
- draft changes do not affect published users
- preview matches intended output
- invalid values are blocked
- accessibility validation runs before publish where applicable
- publish is atomic
- active version is identifiable
- version history is retained
- rollback works
- reset works
- audit log records actor/time/change
- import/export validates schema where supported
- cache/config invalidation works
- failed config loading falls back safely
- tenant scope is isolated
- user preferences override only allowed fields

## User personalization

When implemented, read `personalization-and-data-ux.md`.

Verify:

- preference persistence
- reset to defaults
- migration when fields/options change
- removed columns/filters degrade safely
- `preference-reconciliation.md` rules are followed when owner/schema constraints change
- shared-view permissions
- user setting cannot grant permission/capability
- mobile/RTL/LTR behavior

## Brand and typography

- logo treatment audited
- correct variants used
- palette semantics and contrast improved
- typography works at real sizes
- local fonts load correctly
- strategic identity changes were authorized
- third-party asset licensing checked when relevant

## Theme

For each supported theme:

- surface hierarchy
- text and border contrast
- status colors
- focus, hover, selected, and disabled
- forms, tables, and charts
- overlays, tooltips, and dialogs
- logo variant

## Responsive

At representative widths:

- navigation
- primary actions
- tables
- filters
- forms
- dialogs
- charts
- sticky regions
- overflow
- touch targets

## Specialist routing

Read `specialist-routing.md`.

Verify:

- required specialist triggers were evaluated
- required specialists were actually used when available
- unavailable required specialists are explicitly reported
- specialist-dependent claims are not marked complete without specialist evidence
- lower-level specialists did not override higher-level scope, risk, architecture, security, or product constraints
- Head-delegated work returns a UI/UX handoff instead of claiming whole-project completion

For Persian-facing UI:

- `persian-writing` was used for Persian language QA when available
- Persian labels, buttons, validation, errors, notices, empty states, and mixed Persian/English content were reviewed through that specialist
- if unavailable, the report states: `Persian language QA: Unverified — required specialist unavailable.`

## RTL/LTR and localization

Where applicable:

- document lang and dir
- logical CSS
- mixed-direction isolation
- table, pagination, and breadcrumb behavior
- directional icons
- chart semantics
- dates, numbers, currency, and timezone
- text expansion and truncation
- mobile direction

## Accessibility

Read `accessibility.md`.

Record automated and manual checks separately.

## Performance

Read `performance.md` when relevant.

For runtime configuration also consider:
- configuration-fetch latency
- theme flash
- hydration mismatch
- unnecessary full-app rerenders after local preference changes

Record measurements or inspection evidence rather than unsupported claims.

## Engineering

Run available:

- unit and integration tests
- lint
- type check
- build
- visual or regression tests
- configuration schema/migration tests
- authorization tests for owner settings
- accessibility tooling
- performance tooling where relevant
- existing visual-regression tooling where relevant
- behavioral eval/fixture checks when changing this Skill itself

Do not hide failures.

## Visual review

When browser, preview, or screenshot tools are available:

1. render representative pages
2. inspect real content
3. inspect themes, directions, viewports, and states
4. inspect owner-configurable variants when implemented
5. inspect user preferences when implemented
6. fix issues
7. inspect again

If rendered QA is unavailable, say so.

## Final comparison

For redesigns compare baseline vs result on:

- task clarity
- discoverability
- steps
- hierarchy
- scanability
- form and table efficiency
- repeated-work reduction
- error prevention
- feedback
- data trust
- responsiveness
- RTL/LTR
- accessibility
- performance where relevant
- brand coherence
- maintainability and changeability

"Looks newer" is not a success criterion.
