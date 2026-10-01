# Frontend Performance

Performance is part of UX. Do not optimize blindly; measure or inspect likely bottlenecks first.

## Audit areas

Review when applicable:

- initial JavaScript and CSS cost
- route-level code splitting
- expensive client rendering
- unnecessary rerenders
- large DOM trees
- long lists/tables without an appropriate strategy
- chart rendering cost
- oversized or unoptimized images
- font loading and layout shifts
- repeated network requests
- request waterfalls
- blocking data dependencies
- loading transitions and perceived latency
- hydration/client-boundary cost
- animation cost
- memory growth during long operational sessions

## Tables and large datasets

For large operational tables consider:

- server pagination
- windowing or virtualization
- stable row keys
- memoization only where measured/useful
- avoiding expensive cell renderers
- debounced or server-side search where appropriate
- column visibility instead of rendering everything

Do not introduce virtualization when dataset size and interaction complexity do not justify it.

## Charts

Limit expensive chart density.

Avoid rendering hidden or offscreen charts eagerly when lazy rendering is safe.

For live dashboards, control update frequency and avoid redrawing the entire view for small data changes.

## Fonts and media

Prefer:
- WOFF2
- needed weights only
- variable fonts where beneficial
- explicit image dimensions
- responsive image sizes
- lazy loading for non-critical media

Avoid font or image changes that introduce visible layout shift.

## Measurement

Use existing project tooling where available.

Useful evidence can include:
- browser Performance panel
- Lighthouse
- framework profiler
- bundle analyzer
- React profiler
- Core Web Vitals
- network waterfall
- application telemetry

Use project performance budgets when they exist.

## Performance budget

Prefer an existing project performance budget when one exists.

If no budget exists, do not invent universal thresholds. Instead establish:

- baseline measurement
- the surfaces/routes affected by the UI change
- project-specific risk tolerance
- acceptable before/after delta
- any regression that requires explanation

Useful budget dimensions can include:

- JavaScript/CSS transfer or bundle delta
- render/interaction cost
- Core Web Vitals where applicable
- table/chart update cost
- request count/waterfall
- memory growth in long-running operational sessions

A visual redesign should not introduce a meaningful unexplained performance regression.

## Perceived performance

UX performance includes:
- preserving context during local updates
- progressive loading states
- optimistic updates when safe
- avoiding full-page blocking for small actions
- showing background progress for long tasks
- keeping primary controls responsive

Never hide real latency with misleading UI.

## Report

State:
- what was measured or inspected
- bottlenecks found
- changes made
- before/after evidence when available
- unverified assumptions


## Runtime configuration performance

When appearance or preferences are loaded at runtime, review:

- configuration-fetch latency
- cache strategy and invalidation after publish
- theme/brand flash before configuration resolves
- server/client hydration mismatch
- full-app rerenders caused by local preference changes
- repeated asset/font downloads after theme changes
- large configuration payloads
- unnecessary blocking of first render for non-critical settings

Resolve critical theme values early enough to avoid visible instability where practical.

A user changing one local preference should not require rebuilding unrelated application state.
