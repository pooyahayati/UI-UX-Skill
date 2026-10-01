# iOS / Apple Mobile Design Rules

Use this local rule pack only when the active product route includes `mobile-application` and the current surface targets iOS or iPadOS.

These are UI/UX rules, not SwiftUI/UIKit implementation instructions.

## Native interaction model

Preserve Apple platform expectations unless the product has a deliberate and tested reason to diverge.

Design around:

- predictable hierarchical navigation;
- familiar back behavior;
- appropriate tab-based top-level navigation when destinations are peer-level and frequent;
- sheets for contained, temporary tasks;
- full-screen presentation only when the task genuinely needs full attention or immersion;
- system-native search, sharing, pickers, and contextual actions when they fit the task.

Do not reproduce Android-specific navigation chrome or web-app navigation patterns on iOS merely for cross-platform visual sameness.

## Layout, safe areas, and window adaptation

Treat safe areas and system-owned regions as first-class constraints.

Critical controls and primary information must remain usable around:

- status and system bars;
- home indicator;
- camera/sensor cutouts;
- Dynamic Island or equivalent system regions;
- software keyboard;
- split view / resizable windows on iPad where supported.

Design layouts to adapt rather than simply scale.

When width changes materially:

- allow adjacent regions to stack;
- allow detail content to move into a separate pane or screen;
- preserve readable line length;
- let controls and rows grow when text grows;
- avoid fixed-height containers that clip larger text.

## Dynamic Type and text growth

Assume users can substantially increase text size.

The layout must tolerate:

- multiline labels;
- taller controls and rows;
- stacked actions when horizontal space is insufficient;
- content reflow without overlap or truncation;
- meaningful hierarchy even when display text becomes large.

Do not treat text scaling as a QA-only concern.

## Navigation and back behavior

Users must understand where they are and what back navigation will do.

For deep flows:

- preserve meaningful hierarchy;
- avoid ambiguous close/back controls;
- do not use destructive back behavior;
- preserve in-progress work when safe;
- distinguish dismissing a modal task from navigating backward in the content hierarchy.

## Sheets, dialogs, and temporary tasks

Use temporary presentation for temporary work.

Make clear:

- whether changes are applied immediately or on confirmation;
- whether dismissal discards work;
- whether the task can resume;
- what the primary and cancellation actions are.

Avoid deeply nested modal stacks.

## Touch and gestures

Gestures should enhance direct manipulation, not hide essential functionality.

For gesture-only interactions:

- provide discoverable alternatives when the action is important;
- avoid conflicts with system navigation gestures;
- keep destructive gestures recoverable where practical;
- do not rely on hidden swipe actions for the only path to a critical command.

## Keyboard and data entry

Account for the on-screen keyboard as part of layout.

Ensure:

- focused fields remain visible;
- primary submit/next actions are not obscured;
- multi-step forms have intentional progression;
- appropriate input semantics reduce typing;
- valid input survives validation errors and temporary interruption;
- long forms can resume where the product supports drafts.

## iPad and larger-window behavior

Do not stretch a phone UI across a large window.

Consider:

- split navigation/content;
- list-detail layouts;
- supporting panes;
- persistent context where increased space improves the task;
- pointer/keyboard use for productivity workflows;
- multiple columns only when they improve comprehension.

When the app supports resizing or multitasking, validate intermediate widths rather than only phone and full-screen tablet extremes.

## Accessibility

Validate platform behavior for:

- VoiceOver semantics and reading order;
- Dynamic Type;
- sufficient contrast;
- visible focus where hardware keyboard/focus navigation is supported;
- reduced motion;
- control labeling;
- alternatives to gesture-only interactions.

Accessibility states must remain meaningful when the UI changes layout at larger text sizes.

## Motion and feedback

Use motion to communicate hierarchy, continuity, selection, and state changes.

Avoid motion that:

- delays common tasks;
- makes navigation feel unpredictable;
- obscures the final state;
- ignores reduced-motion preferences.

Haptics and animation should support meaning, not decorate every interaction.

## System capabilities

When using camera, photos, location, files, notifications, biometrics, sharing, or other system capabilities:

- request or invoke them in context;
- explain why the capability is needed;
- handle denial/cancellation;
- provide a recovery path where possible;
- do not mimic a successful system operation before the OS confirms it.

## Validation

For iOS/iPadOS surfaces, validate representative:

- compact and larger widths;
- large Dynamic Type;
- safe-area/system-region behavior;
- keyboard-visible form state;
- back/dismiss behavior;
- sheet/full-screen presentation;
- permission denied and recovery state when applicable;
- dark/light appearance when supported;
- VoiceOver/reduced-motion behavior where testable;
- iPad/multitasking layout when supported.

## Current platform references

When verification is needed, prefer current Apple Human Interface Guidelines rather than copied framework recipes.

Relevant canonical guidance includes:

- Apple Human Interface Guidelines — Layout
- Apple Human Interface Guidelines — Navigation and Search
- Apple accessibility guidance

This local pack remains the product's design authority; current official guidance should be used to refresh details when platform conventions materially change.
