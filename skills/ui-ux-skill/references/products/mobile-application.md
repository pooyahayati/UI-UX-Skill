# Mobile Application Product Pack

Use only when the active product route includes `mobile-application`.

This Product Pack owns shared mobile UX rules and routes platform-specific design to local rule packs in this repository.

## Required mobile routing

Before major mobile design decisions, identify:

- target platforms: iOS, Android, or both;
- native vs cross-platform delivery model;
- primary device classes;
- orientation/resizable-window requirements;
- system capabilities in scope;
- offline/network assumptions;
- whether platform-specific divergence is expected.

Then load local rules as follows:

- iOS/iPadOS -> `mobile/ios.md`
- Android -> `mobile/android.md`
- one product/codebase spanning platforms -> `mobile/cross-platform.md`

For a cross-platform product targeting both iOS and Android, use:

`Shared Mobile UX -> Cross-platform rules -> iOS rules -> Android rules`

Do not use external design Skills for mobile product design. Platform design knowledge is maintained locally in this repository.

## Shared Mobile UX

### Navigation intent

Choose navigation based on task frequency, hierarchy, depth, and return behavior.

Keep back/dismiss behavior predictable.

Do not transplant desktop sidebars, hover-dependent interactions, or dense desktop tables into mobile unchanged.

Do not hide the only path to an important action behind an undiscoverable gesture.

### Touch and reachability

Primary actions and frequent controls must be practical for touch and repeated use.

Avoid tightly packed controls.

For important gesture shortcuts, provide a visible or otherwise discoverable alternative.

Consider one-handed use when it materially affects the workflow.

### Safe areas, system UI, and keyboard

Treat system-owned areas as layout constraints.

Account for:

- status/system bars;
- cutouts/notches;
- home/gesture areas;
- keyboards/IME;
- bottom navigation;
- sheets/dialogs;
- resizing and orientation when supported.

Focused inputs and primary actions must remain usable when the keyboard is visible.

### Mobile forms and data entry

Treat forms as workflows, not field collections.

Use:

- appropriate input semantics;
- clear field progression;
- useful defaults;
- autofill/password-manager/OTP support when applicable;
- preserved valid values after validation errors;
- explicit submit/save state;
- draft/resume behavior for long forms when loss would be costly.

Reduce unnecessary typing.

Do not obscure validation errors after the keyboard opens.

### Permissions

Request permissions in context when the user can understand the reason.

Design explicit states for:

- not requested;
- granted;
- denied;
- restricted/unavailable;
- recovery through system settings when needed.

Do not repeatedly pressure users to grant a denied permission.

Do not imply that capability is available until authoritative OS state confirms it.

### Connectivity and authoritative state

Design for the possibility that local UI state and server-authoritative state differ.

When relevant, define:

- offline state;
- weak/interrupted connectivity;
- queued local work;
- retry;
- cancellation;
- reconnect;
- stale local data;
- synchronization;
- synchronization failure;
- conflict resolution.

Clearly distinguish:

- saved locally;
- queued for sync;
- syncing;
- confirmed by server;
- failed.

### Session continuity and state restoration

Mobile work is frequently interrupted.

For meaningful in-progress work:

- preserve draft/input state when safe;
- define resume behavior after backgrounding;
- define behavior after process termination where the product can restore state;
- resume or explain interrupted uploads/downloads;
- preserve the user's place in long workflows;
- avoid forcing a full restart after recoverable interruption.

### Long-running work

For uploads, exports, imports, generation, media processing, or other long tasks:

- show queued/running/completed/failed state;
- show meaningful progress when measurable;
- support safe retry/cancel where the product allows;
- keep work understandable across app switches;
- do not report completion before authoritative confirmation.

### Deep links and return paths

When notifications, links, widgets, or external flows can open the app:

- route to a meaningful destination;
- restore enough context to understand why the user arrived there;
- handle inaccessible/expired destinations safely;
- avoid dropping the user on an unrelated home screen without explanation.

### Notifications and interruption

Use notifications to support meaningful return paths.

Define:

- what event merits interruption;
- where tapping returns;
- whether an action can safely occur from the notification;
- what happens when the underlying state has changed.

Do not use badges/notifications merely to manufacture engagement.

### Dense data on mobile

For complex data, prioritize task and hierarchy.

Prefer:

- summaries;
- progressive disclosure;
- dedicated detail screens;
- drill-down;
- purpose-built comparison;
- adaptive panes on larger devices.

Do not shrink a desktop grid into an unreadable phone table.

### Motion and haptics

Use motion and haptics to communicate:

- hierarchy;
- state change;
- confirmation;
- continuity;
- direct manipulation.

Avoid decorative motion in repeated workflows.

Respect reduced-motion preferences.

### Accessibility goals

Validate:

- screen-reader semantics and reading order;
- text scaling;
- contrast;
- touch target practicality;
- focus/navigation with assistive input when relevant;
- reduced motion;
- alternatives to gesture-only actions;
- adaptive layout at larger text sizes.

Accessibility is part of the design model, not a final patch.

## Platform-specific local rules

After applying Shared Mobile UX, load the applicable local pack:

### iOS / iPadOS

Read `mobile/ios.md`.

Use for Apple-specific navigation, safe-area behavior, Dynamic Type, iPad/resizable windows, VoiceOver, sheets, gestures, and other platform conventions.

### Android

Read `mobile/android.md`.

Use for edge-to-edge/system bars, predictive back, adaptive layouts, large screens/foldables, navigation adaptation, TalkBack, and Android-specific behavior.

### Cross-platform

Read `mobile/cross-platform.md`.

Use when one product or codebase spans platforms.

Preserve product/UX invariants while translating platform presentation rather than cloning pixels.

## Persian and mixed-language mobile UI

When Persian-facing language is in scope, the REQUIRED external `persian-writing` specialist owns Persian linguistic validation.

The Mobile Product Pack and its local platform packs retain ownership of layout, interaction, direction architecture, platform behavior, and mobile accessibility.

## Validation matrix

For mobile application work, validate representative:

- primary navigation;
- core workflow;
- keyboard/input flow;
- draft/resume behavior where relevant;
- permission state and recovery when relevant;
- offline/error/retry/sync states where relevant;
- long-running/background work where relevant;
- deep-link/notification return path where relevant;
- small and large supported windows;
- orientation/resizing when supported;
- active system theme modes;
- RTL/LTR where supported;
- accessibility behavior;
- lifecycle/resume behavior;
- platform-specific checks from every loaded local rule pack.

Do not claim mobile validation across a platform whose local pack was not loaded.
