# Visual Regression and Rendered Evidence

Use this reference for existing-product redesigns, broad visual changes, theme work, RTL/LTR changes, responsive changes, typography changes, and runtime design configuration.

Visual QA should produce evidence, not just a statement that the UI was reviewed.

## Baseline first

Before broad visual changes, capture a representative baseline when browser or screenshot tooling is available.

Choose surfaces by risk and frequency, not by convenience.

Useful dimensions:

- high-frequency routes
- critical workflows
- complex tables/forms
- Light/Dark
- RTL/LTR
- desktop/tablet/mobile
- empty/error/loading/stale/permission states
- owner-configurable variants when present

Do not attempt to capture every possible screen in a large product. Record the chosen coverage.

## Screenshot matrix

Use stable names so before/after evidence can be paired.

Example:

```text
customer-list__desktop__light__rtl__default__before.png
customer-list__desktop__light__rtl__default__after.png
customer-list__mobile__dark__rtl__filters-open__before.png
customer-list__mobile__dark__rtl__filters-open__after.png
```

A matrix row should identify:

- route or surface
- viewport
- theme
- direction
- state
- role if relevant
- baseline/current

## Stable capture

Reduce false diffs when practical:

- use deterministic fixture data
- freeze or mask timestamps/animated counters
- avoid random avatars/IDs when they do not matter
- wait for fonts and stable layout
- disable non-essential animation for capture
- use the same viewport and device scale
- keep the same data/filter state

Do not hide dynamic behavior that is itself part of the UX being evaluated.

## Compare by category

Inspect differences in:

### Layout
- overflow
- clipping
- unexpected wrapping
- misalignment
- incorrect sticky behavior
- changed information priority
- layout shift

### Typography
- missing fonts
- changed line breaks
- truncation
- poor mixed-script rendering
- inconsistent weights
- broken vertical rhythm

### Theme and color
- contrast
- incorrect semantic colors
- Light/Dark drift
- invisible borders/focus
- logo variant
- chart readability

### RTL/LTR
- mirrored content that should not mirror
- broken technical LTR values
- wrong action order
- pagination/breadcrumb errors
- sticky-column mistakes

### Responsive
- inaccessible actions
- hidden critical content
- table overflow
- unusable dialogs/drawers
- touch-target crowding

### States
- loading skeleton mismatch
- empty/error regression
- stale/partial state ambiguity
- permission state leakage

## Pixel diff vs semantic review

Pixel comparison is useful for detecting unexpected changes, but a pixel match is not proof of good UX.

Use two layers:

1. mechanical screenshot difference detection when tooling exists
2. semantic visual review against the intended design/UX outcome

A deliberate redesign can have a large pixel diff and still be correct.

## Thresholds

Do not invent a universal pixel-diff threshold.

Use:
- existing project threshold if available
- a documented project-specific threshold
- targeted masks for accepted dynamic regions
- manual review for significant intentional changes

Any threshold should be treated as a regression detector, not a design-quality score.

## Before/after evidence

For a meaningful redesign, record:

- what changed
- why it changed
- representative before/after captures
- regressions checked
- unresolved visual risks
- surfaces not captured

## Runtime configuration

If an Owner Control Center exists, include representative screenshot coverage for:

- default config
- draft preview
- published config
- rollback result
- Light/Dark
- RTL/LTR
- compact/comfortable density where supported
- invalid config fallback

Preview and published output should be visually consistent for the same resolved configuration.

## CI integration

When the project already has visual-regression tooling, extend it rather than introducing a second system.

Possible existing mechanisms include:

- Playwright screenshots
- Storybook visual tests
- framework/browser snapshot tools
- hosted visual-diff services

Do not add external paid services unless the user/project has chosen them.

## Final report

State:

- baseline captured: yes/no
- number of surfaces/states captured
- comparison method
- regressions found/fixed
- accepted intentional changes
- untested surfaces
