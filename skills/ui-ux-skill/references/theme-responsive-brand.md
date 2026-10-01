# Theme, Responsive, Brand, Icons, and Motion

## Brand audit

For existing products inspect:

- logo quality and legibility
- size, placement, and clear space
- Light/Dark variants
- responsive and collapsed variants
- favicon and app icons
- palette quality
- semantic color mapping
- typography fit
- icon consistency
- visual personality

Classify:

- treatment fix
- brand refresh
- identity redesign

Do not accidentally stretch, crop, recolor, or redraw an approved logo.

Actual identity replacement requires explicit user intent.

## Third-party asset licensing

Before committing or shipping external fonts, icons, illustrations, or brand assets:

- identify the source
- confirm redistribution and use terms
- prefer supplied or already licensed assets
- record attribution when required
- avoid copying protected brand material from unrelated products

## Palette

Audit whether colors:

- meet contrast needs
- separate interactive, neutral, and semantic roles
- work across enabled themes
- avoid unrelated accents
- remain understandable in tables, charts, and forms
- fit the intended product personality

Correct low-risk semantic-token problems directly when improvement was requested.

For a broad palette refresh, follow the selected autonomy mode.

Use semantic tokens instead of scattered raw colors.

## Theme

For new products and major redesigns, recommend Light + Dark unless product constraints justify one mode.

Do not create Dark mode through simple inversion.

Review independently:

- backgrounds and surfaces
- text
- borders
- focus
- hover, selected, and disabled
- status colors
- charts
- tables and forms
- dialogs and tooltips
- logo variants

## Responsive

Review:

- large desktop
- desktop
- laptop
- tablet
- mobile

Use existing breakpoints where sensible.

Responsive changes may affect:

- navigation
- grid and columns
- table fields
- filters
- actions
- forms
- charts
- secondary panels
- sticky regions
- dialogs
- information priority

Do not solve mobile by only shrinking fonts.

## Mobile tables

Choose based on task:

- priority columns
- expandable rows
- summary and detail
- horizontal scroll
- dedicated record view

Horizontal scroll can be superior when cross-column comparison matters.

## Navigation

Choose based on destination count, depth, frequency, expertise, and viewport:

- sidebar
- compact sidebar
- top navigation
- hybrid

Adapt intentionally on mobile.

## Icons

Prefer one coherent family.

Do not mix outline, filled, emoji, and multiple libraries without a deliberate system.

Icons should assist recognition, not replace critical labels.

## Motion

Use motion for state, hierarchy, continuity, or feedback.

Keep operational UI subtle.

Respect reduced-motion preferences.

Avoid animation that delays access.

## Surface and radius

Use controlled tokens.

Prefer hierarchy and borders before heavy shadows.

Reserve elevation for genuinely floating layers.


## Runtime theme and brand governance

When theme/brand settings are owner-configurable:

- map controls to semantic tokens or approved presets
- validate Light/Dark compatibility before publish
- validate contrast/focus/status semantics
- use allowlisted logo/font assets
- do not expose raw CSS or unrestricted URLs
- preserve safe defaults if configuration is invalid or unavailable
- respect user theme preference only when the owner/product allows it

A runtime palette control should change intended semantic roles consistently rather than patching individual components.
