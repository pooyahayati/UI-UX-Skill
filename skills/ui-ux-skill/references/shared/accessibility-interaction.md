# Accessibility Interaction Contracts

Use for all broad product design and whenever interaction accessibility is materially in scope.

This Shared Rule defines a cross-product accessibility floor. Product and platform packs may strengthen or specialize it; they must not weaken it.

Do not claim conformance without evidence and defined scope.

## Semantic-first rule

Prefer native semantic elements and platform controls when they correctly express the task.

Custom semantics create implementation obligations.

ARIA can expose semantics, but it does not automatically implement keyboard behavior.

Do not add ARIA roles that promise interactions the implementation does not provide.

## Keyboard access

Every essential interactive function should be operable without a pointer when the platform supports keyboard interaction.

Preserve:

- predictable Tab/Shift+Tab sequence;
- expected arrow-key behavior inside composite widgets;
- Escape/Enter/Space conventions where appropriate;
- browser/OS text-editing shortcuts;
- discoverable shortcuts for power-user features.

Do not trap focus except in a true modal interaction that requires containment.

## Focus visibility

Focused controls need a clearly visible indicator.

Do not remove the browser/platform focus indicator without replacing it with an equally or more visible one.

Focus must not be hidden behind sticky headers, toolbars, overlays, or scroll containers.

## Focus movement

Move focus only when a state transition requires it.

Examples:

- dialog opening;
- dialog closing/return;
- validation summary in a long failed form;
- route change where product semantics require a new reading position.

Do not steal focus for passive status updates.

## Selection vs focus

Selection, hover, active/current state, and keyboard focus are distinct.

Do not use one visual state to ambiguously represent multiple meanings.

## Names, labels, and descriptions

Interactive controls need understandable accessible names.

Provide descriptions when the name alone cannot communicate:

- consequence;
- input requirement;
- scope;
- state.

Icon-only controls require a meaningful accessible name.

## Status and live updates

Important dynamic status that is not otherwise discoverable should be programmatically available.

Avoid high-priority announcements for frequent low-value updates.

Do not flood screen-reader users during live dashboards or repeated background progress.

## Form errors

Detected errors should:

- identify the item;
- describe the problem in text;
- preserve valid input;
- provide correction guidance where possible.

Do not rely on color alone.

## Reflow, zoom, and text scaling

Interfaces should tolerate:

- browser zoom;
- larger text;
- translated string expansion;
- platform font scaling where applicable.

Avoid fixed-height containers that clip text.

Do not require two-dimensional scrolling for ordinary text/content when reflow is feasible.

Data visualizations/tables may require specialized alternatives instead of destructive reflow.

## Target size and spacing

Interactive targets should be large enough or sufficiently separated for reliable activation.

Treat minimum conformance as a floor, not an ideal target for important/frequent controls.

## Contrast and non-color meaning

Ensure meaningful contrast for:

- text;
- controls;
- boundaries when required to identify controls;
- focus indicators;
- status/selection.

Do not encode status, severity, trend, or required state only through color.

## Motion

Respect reduced-motion preferences.

Avoid flashing, unnecessary parallax, scroll hijacking, or repeated animation that interferes with reading or task completion.

Load `motion.md` for broader motion rules.

## Images and non-text content

Provide text alternatives when an image communicates content.

Decorative imagery should not create redundant noise for assistive technologies.

Dynamic charts need current-data alternatives; static alt text must not become stale and misleading.

## Dialogs and overlays

For true modal dialogs:

- move focus inside on open;
- contain keyboard focus while modal;
- provide a clear close/cancel path;
- restore focus meaningfully after close.

Do not mark content modal if users can still interact with background content.

## Custom widgets

For custom tabs, comboboxes, menus, grids, trees, listboxes, and similar widgets:

- use established interaction semantics;
- implement expected keyboard behavior;
- expose current state;
- preserve visible focus.

When native HTML solves the task, prefer it.

## Authentication

Do not make authentication depend unnecessarily on memory, puzzles, or forced transcription when assistive mechanisms such as password managers, paste, or alternative methods can support the user.

Security policy remains authoritative.

## Validation

For broad work, verify:

- keyboard-only essential path;
- visible/unobscured focus;
- semantic names/roles/states;
- form labels/errors;
- dialog focus;
- zoom/text scaling;
- reduced motion;
- non-color status;
- target practicality;
- screen-reader reading/status behavior where testable;
- RTL/LTR and translated strings where supported.

## Canonical guidance

When implementation details need verification, prefer current:

- WCAG 2.2;
- WAI-ARIA Authoring Practices Guide;
- platform accessibility guidance;
- native HTML semantics.

This file defines design/interaction expectations, not a claim of standards conformance.
