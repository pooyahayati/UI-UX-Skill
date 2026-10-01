# Responsive and Adaptive Product UI

Use when layout, viewport, window size, orientation, zoom, touch/pointer input, or device adaptation is materially in scope.

Responsive design is product architecture, not a final CSS patch.

## Preserve task priority

When available space changes, preserve:

- primary task;
- important context;
- primary action;
- hierarchy;
- state;
- identity.

Do not preserve the desktop composition merely by shrinking it.

## Reflow decisions

For each region/component, choose intentionally whether it should:

- reflow;
- stack;
- wrap;
- collapse;
- move into a temporary surface;
- become a dedicated route/screen;
- switch from multi-pane to single-pane;
- remain horizontally scrollable;
- hide only if truly secondary.

Do not hide essential functionality just because width is limited.

## Breakpoints by failure, not device label

Choose layout transitions when the current layout stops working, not only because the viewport matches a popular device width.

Consider:

- text wrapping;
- control collision;
- reading width;
- table legibility;
- navigation capacity;
- touch target density;
- pane usefulness.

## Input modality

Do not assume:

- wide = mouse;
- narrow = touch.

Support the input methods the product/platform actually allows.

Avoid hover-only essential interaction.

## Text and localization

Layouts must tolerate:

- larger text;
- browser zoom;
- translation expansion;
- RTL;
- mixed-direction content.

Do not use fixed height to preserve visual symmetry when content can grow.

## Tables and dense data

Do not automatically convert every table into cards.

Choose based on the comparison task:

- prioritized columns;
- horizontal scroll;
- sticky identity column;
- expandable row;
- summary + detail;
- dedicated detail view.

Preserve cross-column comparison when it is essential.

## Navigation adaptation

Responsive navigation can change presentation but should preserve destination meaning and hierarchy.

Load `navigation-wayfinding.md`.

## Forms

On narrow layouts:

- preserve label/control relationships;
- keep errors visible;
- avoid two-column layouts that create confusing reading order;
- keep primary actions reachable.

Load `forms-data-entry.md`.

## Media

When media is important:

- preserve focal point;
- define crop/art direction;
- avoid layout shift;
- avoid oversized assets;
- maintain text readability over media.

Website Product Pack owns SEO/media-loading specifics.

## Orientation and resizing

For products that support rotation or resizable windows:

- preserve in-progress work;
- avoid resetting navigation/filter state;
- adapt layout without changing task meaning.

Mobile platform packs own OS-specific behavior.

## Zoom

Browser zoom or magnification should not cause:

- clipped essential content;
- inaccessible controls;
- overlapping fixed UI;
- hidden focus.

Horizontal scrolling may be appropriate for intrinsically two-dimensional content, not ordinary text.

## Validation

Test representative:

- narrow width;
- intermediate width;
- desktop/wide;
- large text/zoom;
- touch and keyboard/pointer as applicable;
- long translated strings;
- RTL/LTR;
- orientation/resizing when supported;
- dense data/table behavior.
