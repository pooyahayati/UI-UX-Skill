# Android Mobile Design Rules

Use this local rule pack only when the active product route includes `mobile-application` and the current surface targets Android.

These are UI/UX rules, not Jetpack Compose/View implementation instructions.

## Android interaction model

Respect current Android and Material interaction expectations without forcing a generic visual template.

Preserve the product's brand and task model while adapting:

- navigation hierarchy;
- back behavior;
- system bars/insets;
- adaptive layout;
- touch and gesture interaction;
- system permissions and pickers;
- large-screen behavior.

Do not pixel-copy iOS navigation or presentation patterns onto Android.

## Edge-to-edge and system UI

Treat edge-to-edge layout as a design constraint.

Backgrounds and scrolling content may extend beneath system bars, but essential controls and touch targets must respect system insets.

Account for:

- status bar;
- navigation bar / gesture area;
- display cutouts;
- on-screen keyboard / IME;
- taskbar or window chrome on larger devices;
- multiple panes with different backgrounds.

Never place essential tap or drag targets where system gestures compete with them.

## Back and predictive back

Back behavior must be meaningful and predictable.

Design the navigation hierarchy so a back gesture can reveal a sensible previous destination.

Avoid:

- intercepting back without a clear user-facing reason;
- treating back as an arbitrary close button;
- losing drafts silently;
- returning to a state the user cannot understand.

Where current Android behavior exposes predictive back, transitions should accurately preview the destination or dismissal rather than contradicting the final result.

## Adaptive layouts

Treat Android as a range of windows, not a single phone canvas.

Design for:

- phones;
- tablets;
- foldables;
- resizable/multi-window contexts;
- desktop-windowing scenarios when the app supports them.

Adapt by:

- reflowing;
- revealing additional context;
- changing presentation;
- moving from bottom navigation to a navigation rail or other appropriate structure;
- introducing list-detail or supporting panes when useful.

Do not lock the product to portrait phone assumptions unless the product genuinely requires it.

## Navigation

Choose navigation according to available width, destination count, hierarchy, and frequency.

Navigation may legitimately change presentation across window sizes while preserving the same information architecture.

Do not:

- stretch bottom navigation across large screens;
- keep a drawer hidden when a persistent rail would materially improve repeated use;
- expose unrelated destinations merely because more space is available.

## Forms and keyboard

Design with the IME and keyboard transitions in mind.

Ensure:

- focused fields remain visible;
- actions remain reachable;
- content does not jump unpredictably;
- input types match expected data;
- errors preserve valid input;
- long workflows can resume after interruption where drafts are supported.

## Permissions and system capabilities

Request permissions at the moment the related feature becomes understandable.

Handle:

- first request;
- denial;
- repeated denial / system-controlled restrictions;
- settings recovery when needed;
- capability unavailable on the current device.

Never imply permission was granted until authoritative system state confirms it.

## Large-screen and pane patterns

When additional width improves the task, consider:

- list-detail;
- supporting pane;
- feed/primary content plus secondary context;
- persistent navigation;
- drag/drop or pointer affordances when relevant.

A large screen should expose useful context, not merely larger empty margins.

## Touch, gestures, and reachability

Essential actions must remain accessible without hidden gestures.

Avoid conflicts with edge navigation gestures.

When gesture shortcuts exist, provide visible alternatives for important operations.

## Accessibility

Validate:

- TalkBack semantics and order;
- text/font scaling;
- contrast;
- touch target practicality;
- focus behavior for keyboard/switch/pointer input where relevant;
- reduced motion;
- adaptive layouts at larger text sizes.

Do not assume accessibility only matters on handset layouts.

## Motion and feedback

Use motion to explain destination, hierarchy, expansion, and state change.

Transitions must remain consistent with back behavior and reduced-motion preferences.

Avoid ornamental motion that delays repeated tasks.

## Validation

For Android surfaces, validate representative:

- edge-to-edge/insets;
- gesture navigation and back behavior;
- predictive-back-compatible hierarchy where relevant;
- keyboard/IME visible state;
- permission denied/recovery;
- phone, tablet, and at least one intermediate/adaptive width;
- foldable/large-screen posture when supported;
- light/dark mode when supported;
- TalkBack/font-scaling behavior where testable;
- portrait/landscape or resizable behavior when supported.

## Current platform references

When verification is needed, prefer current Android Developers and Material guidance.

Relevant canonical guidance includes:

- Android adaptive layout guidance
- Android edge-to-edge and system-bars guidance
- Android predictive back guidance
- Android large-screen canonical layout guidance

This local pack remains the product's design authority; current official guidance should be used to refresh details when platform conventions materially change.
