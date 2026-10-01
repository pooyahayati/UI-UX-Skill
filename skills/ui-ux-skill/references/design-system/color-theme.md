# Design System Color and Theme

Use when defining color roles, themes, contrast behavior, semantic status, or owner-configurable palettes.

## Color architecture

Use:

`Primitive Palette -> Semantic Color Roles -> Component/State Roles`

Do not let components consume arbitrary palette values when semantic roles exist.

## Core semantic roles

A product may define roles such as:

- surface.canvas
- surface.default
- surface.muted
- surface.raised
- text.primary
- text.secondary
- text.disabled
- text.inverse
- border.default
- border.strong
- action.primary
- action.secondary
- focus.ring
- status.success
- status.warning
- status.danger
- status.info

Extend only when meaning is stable.

## Theme contexts

Treat these as separate resolution contexts when supported:

- Light
- Dark
- High Contrast / Forced Colors

Do not define Dark as a simple inversion of Light.

Do not assume user-agent forced colors behave like a designer-authored high-contrast palette.

## Theme resolution

Semantic token meaning should remain stable across themes.

For example:

`text.primary` remains primary readable text in every theme even though the resolved color changes.

Components should not switch raw colors manually by theme if the semantic token layer can resolve them.

## User preference and product policy

Where the product allows it, resolve theme preference predictably.

Potential order:

1. locked product constraint
2. allowed owner policy
3. user preference
4. system preference
5. safe default

Do not let theme preference alter authorization or information visibility.

## Color scheme integration

On the web, consider platform/browser color-scheme integration for native controls and browser UI where appropriate.

Do not claim complete Dark support merely because page backgrounds change.

## Forced colors

When forced-colors mode applies:

- preserve semantic meaning without relying on authored colors;
- avoid disabling forced-color adjustment except for narrowly justified elements;
- verify focus, selection, borders, and controls remain identifiable.

Do not fight user high-contrast settings for brand fidelity.

## Contrast

Contrast validation should include:

- text;
- interactive controls;
- focus indicators;
- component boundaries where necessary for identification;
- disabled/read-only presentation;
- semantic statuses.

Do not assume one passing color pair makes an entire theme accessible.

## Status color

Status must not depend on color alone.

Pair color with:

- text;
- icon/shape;
- pattern or structural meaning where useful.

Do not use the same semantic color for unrelated concepts.

## Charts

Chart palettes should distinguish:

- categorical series;
- sequential data;
- diverging data;
- semantic status/reference lines.

Provide non-color cues or accessible data alternatives where needed.

Do not recycle application status colors as arbitrary chart categories.

## Owner-configurable palettes

Owner configuration should map to validated semantic roles or approved presets.

Do not expose unrestricted raw component colors as owner settings.

When brand colors cannot meet interaction contrast requirements, preserve brand identity in non-critical surfaces and resolve accessible action/focus roles separately.

## Validation

Test:

- Light;
- Dark;
- high contrast/forced colors when applicable;
- hover/focus/active/selected;
- disabled/read-only;
- statuses;
- charts;
- forms/tables;
- logo/media treatment;
- owner palette override and invalid fallback;
- RTL/LTR where color is paired with directional content.
