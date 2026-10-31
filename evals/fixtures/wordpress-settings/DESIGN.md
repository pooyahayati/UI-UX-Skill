# WPS specimen design contract

Engineering fixture, not owner-approved product branding. Primary specimen: Persian/RTL, real WordPress admin, light host appearance. English is a compatibility test variant, not a requirement for real monolingual products. Dark mode is not a supported admin requirement here.

| Decision | Fixture criterion |
| --- | --- |
| Host | Keep core navigation, toolbar and other pages intact |
| Typography | Locally loaded Vazirmatn regular/bold in Persian; readable host defaults for English; no synthetic weights |
| Palette | Existing WordPress admin text/surface/border/action colors; no new brand or theme engine |
| Width | Owned content up to 880px, fields up to 560px, shrink within narrow host content |
| Scale | Body 16px, primary heading 24px/22px narrow, section heading 19px; help 14px |
| Spacing | Sections 24px/16px narrow; persistent labels and nearby help/errors; logical CSS |
| Simple form | Report title and notification toggle, no tabs or empty categories |
| Multi-topic | Report identity, delivery and secondary technical settings; section-specific save actions |
| Save placement | Below each section, explicit scope, reachable after reflow, non-overlapping labels |
| States | Initial/error, edit, saving, rejected, confirmed, unknown, conflict; preserve drafts |
| Dialog | Section-reset scope, keyboard containment/Escape/return, readable mixed-direction content |
| Acceptance | Actual normal/narrow captures and behavior; no universal device or screen-reader conformance claim |

Storage is the specimen's own synthetic option. It demonstrates CAS revision/conflict recovery; guidance must not prescribe a backend rewrite for an existing plugin. Endpoint values are displayed/stored, never fetched. Secrets used in tests are synthetic and excluded from returned state.

## R12 discovery and workspace extension

Reuse the above Persian-primary light-host foundation. The discovery variant adds
one labelled search and three wrapping section destinations, with current state
shown by text underline plus native button state. Native sections replace nested
PanelBody in this new layout; the old multi variant retains its tested disclosure.
Palette/width/spacing remain the observed WordPress baseline; bounded surface,
ink, muted, border, focus and radius tokens live only in the owned root. Radius is
8px; paragraphs use the intended 16px body size, help stays 14px. No animation,
global reset, new dependency or appearance engine is introduced.

Search/reveal and navigation share the existing draft state. Disabled recipient
focuses the labelled field-and-help wrapper, with one dependency explanation.
Technical input values remain LTR. Owner product approval is not inferred from
engineering acceptance of this synthetic fixture.

Compatibility: 2026-11-01 runtime observations on WordPress 6.8 and 7.1.3/PHP
8.3.35 verify the actual public TextControl, ToggleControl, SelectControl, Button,
Notice, Modal, Spinner, PanelBody and SearchControl exports. SearchControl uses
the same verified `__nextHasNoMarginBottom` styling-transition flag; legacy basic
controls keep their prior verified flags. The maintained no-build asset metadata
still supplies `wp-components`/`wp-element`; new local modules declare dependencies
through the owned enqueue hook. DataViews/DataForm/theme/UI packages are not used.
Existing core translations and local fixture copy are separate; no npm build or
generated asset metadata is claimed.

The optional workspace reuses those tokens and presents three task destinations:
report list/filter/detail, connection status with a link to configuration, and
background-work states. Details use the tested native Modal with focus return;
narrow layouts wrap filters/actions and use the actual viewport for dialog review.
Loading, no matches, queued/running/failed/retry/completed examples are explicitly
simulated. Configuration does not claim a healthy connection; a completion demo
does not claim confirmed server work. No jobs, external requests or customer
records are created. Final captures and exact source bindings are in the
[R12 runtime record](../../wordpress-settings/evidence/r12-browser-results.json).
