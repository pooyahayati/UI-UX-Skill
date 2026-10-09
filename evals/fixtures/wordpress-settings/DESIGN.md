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
