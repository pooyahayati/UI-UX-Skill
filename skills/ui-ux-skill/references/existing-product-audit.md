# Existing Product Audit and Improvement

Use for completed, legacy, live, or partially redesigned products.

Goal: improve UI/UX without breaking working product behavior.

Use `ux-evidence-and-metrics.md` to ground significant findings when research, analytics, support, or measurable workflow evidence is available.

Use `visual-regression.md` for broad visual changes when rendered capture tooling is available.

## Modes

### Audit only

Inspect and report. Do not modify code or assets.

### Audit and improve

Use:

`Baseline -> Audit -> Prioritize -> Fix -> Validate -> Compare -> Refine`

Proceed with low-risk fixes inside the requested scope.

### Controlled redesign

Use when structure or visual language materially blocks good UX.

Use representative screens before broad rollout.

## Establish the baseline

Inspect enough to understand:

- shell and navigation
- user roles and primary workflows
- representative high-frequency pages
- components and tokens
- typography
- palette
- brand/logo treatment
- themes
- responsive patterns
- RTL/LTR/localization
- forms, tables, filters, and charts
- loading, empty, error, partial, stale, and success states
- auth and permission-sensitive UI
- saved views and personalization when present
- owner/system appearance settings when present
- whether visual values are centralized or hard-coded
- available tests, browser, and preview tooling
- available UX evidence, telemetry, support feedback, or research
- existing screenshot/visual-regression baselines

For large products, sample representative surfaces.

## Audit coverage

Always record what was actually inspected.

Useful coverage dimensions:

- routes/screens
- workflows
- roles
- desktop/tablet/mobile
- Light/Dark
- RTL/LTR
- default/loading/empty/error/disabled/permission/stale states
- personalization/runtime-config paths
- source-code only vs rendered inspection

Do not imply full-product coverage from a representative sample.

## Preserve product contracts

Do not silently change:

- permissions
- business rules
- validation
- API contracts
- data meaning
- authentication
- routing
- destructive-action semantics
- saved user preferences
- localization behavior

Read `execution-safety.md` before implementation.

## Audit matrix

### Workflow and information architecture

Check:

- primary task clarity
- action discoverability
- unnecessary steps
- confusing navigation
- duplicated destinations
- poor grouping
- missing context
- weak feedback or recovery
- destructive-action safety
- mismatch with user mental model
- role-specific needs and repeated work
- search, bulk-action, concurrency, long-running-job, and real-time behavior where relevant

### Visual hierarchy

Check:

- primary vs secondary emphasis
- typography scale
- spacing rhythm
- alignment
- density
- unnecessary containers/cards
- radius/shadow/gradient excess
- action hierarchy
- oversized headers/sidebars

### Brand and visual identity

Check:

- logo quality and real-size legibility
- placement, clear space, responsive/theme variants
- favicon/app icon consistency
- palette contrast and semantic clarity
- typography/product fit
- icon-family consistency
- visual personality
- Light/Dark behavior

Classify:

- treatment fix
- brand refresh
- identity redesign

Actual logo or identity replacement requires explicit user intent.

### Components, tokens, and changeability

Read `design-system-architecture.md`.

Check:

- duplicated components
- uncontrolled variants
- raw color/spacing values
- hard-coded presentation in pages
- inconsistent states
- missing semantic tokens
- theme drift
- obsolete components
- inconsistent icons
- whether common design changes require editing many unrelated files
- whether runtime/user configuration is typed and bounded
- whether config precedence is deterministic

A visually good interface can still be a poor implementation if normal design changes are unnecessarily expensive or risky.

### Runtime UI governance

When an owner control center exists or would be valuable, read `runtime-ui-governance.md`.

Check:

- correct authorization
- safe allowlist
- no arbitrary CSS/JS/HTML
- draft vs published state
- preview
- validation
- version history
- rollback
- audit log
- reset
- import/export where needed
- failure fallback
- tenant scope
- user-preference precedence

Do not recommend building this feature when runtime customization has little product value.

### Personalization and Data Trust

Read `personalization-and-data-ux.md` when relevant.

Check:

- saved views
- repeated preferences
- preference persistence/reset
- role-aware defaults
- shared-view permissions
- data freshness
- last-updated time
- timezone
- filter scope
- stale/partial states
- metric definitions
- drill-down/traceability where needed

### Tables

Check:

- useful columns
- scanability
- sorting, filtering, and search
- active filters
- pagination
- selection and bulk actions
- row actions
- sticky behavior
- density
- overflow
- mobile strategy
- loading, empty, and error states
- saved views/personal columns for repeated-use workflows

### Forms

Check:

- field grouping and order
- visible labels
- validation clarity
- save and unsaved behavior
- disabled/loading state
- keyboard flow
- mobile layout
- technical LTR fields inside RTL UI

### Responsive

Check:

- navigation adaptation
- content priority
- tables, filters, and forms
- dialogs and drawers
- action placement
- charts
- overflow
- sticky elements
- touch targets
- RTL/LTR independently when relevant

### Accessibility

Read `accessibility.md`.

### Performance

Read `performance.md` when UI cost or perceived latency is relevant.

### RTL/LTR and localization

Read `rtl-ltr-typography.md`.

## Classify findings

For meaningful findings record:

- Severity: Critical / High / Medium / Low
- Impact: task failure / error risk / slowdown / confusion / accessibility / inconsistency / performance / visual quality / maintainability / governance
- Scope: local / component / page / workflow / system
- Confidence: high / medium / low
- Fix Type: safe local fix / refactor / design-system change / workflow change / governance change / product decision

Do not assign severity from personal visual taste alone.

## Safe corrective fixes

When improvement was requested, normally proceed with well-supported low-risk changes such as:

- spacing and alignment
- hierarchy cleanup
- responsive defects
- obvious RTL/LTR defects
- focus, contrast, and semantic accessibility improvements
- component-state inconsistency
- table overflow and action placement
- loading, empty, stale, and error presentation
- semantic token corrections
- consolidation of duplicated visual values
- logo usage, placement, and contrast
- typography consistency within the current direction

## Strategic changes

Follow the user's autonomy mode before broad propagation of:

- navigation model
- information architecture
- primary workflow
- new design-system foundation
- global palette or typography direction
- major density or personality change
- component-library or framework migration
- introducing a runtime Owner Control Center
- changing configuration precedence or tenant scope
- business-visible terminology
- actual logo or brand identity

## Existing product without design-profile.md

Infer an Observed Baseline.

Use it as a temporary constraint for corrective work.

Run Partial Discovery only for strategic decisions that need reconsideration.

Create `design-profile.md` once a coherent strategic direction is approved or delegated.

## Compare before/after

Evaluate:

- task clarity
- discoverability
- steps
- hierarchy
- scanability
- form and table efficiency
- repeated-work reduction
- error prevention
- feedback
- responsive behavior
- RTL/LTR
- accessibility
- performance where relevant
- data trust
- brand coherence
- maintainability and changeability

Do not use "looks newer" as evidence.

## Deliverable

Finish with:

1. audit coverage
2. major problems found
3. high-impact changes made
4. behavior intentionally preserved
5. validation performed
6. checks not performed
7. maintainability/configurability findings
8. remaining strategic decisions or risks
