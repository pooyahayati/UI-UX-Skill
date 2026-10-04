# Design handbook — synthetic appearance fixture

Status: proposed test fixture, not customer-approved product design.
Writer: engineering lead. Product route: web-application, no secondary route.
Authority: owner delegated practical choices for Skill validation, not a new product.

## Settled initial foundation

English/LTR/light primary. A quiet operational workspace, grouped owner controls,
explicit private-preview versus published state, responsive stacking and visible
keyboard focus. Real synthetic sample labels and data, not product metrics.
Prepared palettes preserve text/control contrast and non-color status names.
Typography uses locally available generic stacks; exact glyph identities/weights
need R7 evidence. Do not silently install or substitute a product font.

## Single value authority

Defaults, legal values, semantic resolution and setting consumers are owned by
`scripts/runtime_appearance.py`. The panel consumes its catalog, not copied default
values here. Runtime snapshots/drafts/history are in external SQLite, not this file.
Prepared original icon artwork, semantic roles, family capabilities and meaningful
fallbacks are owned by `scripts/runtime_icons.py`; configuration stores allowed
identifiers only. Shared/private/public/dialog consumers use the same SVG adapter.
Routine panel changes do not update this handbook or component source.

Owner configuration is tenant-scoped for the sample product and its owned preview.
Other tenants, authentication, routes, sample data meaning, focus/target/readability
floors and breakpoint logic remain locked. No user overrides are offered in R5;
do not invent a user-preference precedence implementation.

## Change and approval boundary

Primary sample review/corrections come first. Dark follows primary acceptance;
secondary locale/direction review requires confirmed need and scoped owner authority.
R5 prepares supported theme values; R7 records their actual integrated coverage.
R6 owns editable icon-family/semantic assignment, not arbitrary uploaded SVG.
The fixture offers prepared outline/solid families and plain/badged semantic uses;
these are demonstration choices, not mandated product libraries or style. Solid
stroke editing is disabled and its retained outline preference is dormant. Icon
defaults are staged locally without changing other settings or publishing them.

## Verification record

The [R5 executable checkpoint](../../../ROADMAP.md#r5-executable-checkpoint--2026-10-05)
and [fixture evidence](README.md#required-acceptance-and-recorded-limits) record scoped store/HTTP
tests and actual private-preview, publication, refresh/restart, dark, reset and rollback
observations. This record does not grant customer design approval or whole-stage
delivery acceptance. Runtime setting changes left this handbook unchanged; this later
evidence update is documentation, not manual synchronization of active values.
Source/build checks, actual HTTP storage/denial tests and browser rendering remain
separate evidence. Production authentication, device/screen-reader conformance and
exact installed OS fonts cannot be inferred from this synthetic fixture. QF04/QF05
remain required R7 checks on their original surfaces.
