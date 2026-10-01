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

## Shared-rule boundary

After this Product Pack is active, read `../shared-product-rules.md` and load only Shared Product UI Rules that are materially in scope.

Do not duplicate the cross-product contracts here. This Product Pack owns only its product/platform/host specialization and any local sub-routing described below.
## Shared Mobile UX

### Navigation intent

Read `../shared/navigation-wayfinding.md`.

Mobile specialization:

- preserve predictable back/dismiss behavior;
- adapt destination presentation to platform/window context;
- avoid desktop sidebars or hover-dependent navigation transplanted unchanged;
- keep important actions discoverable without gesture-only dependence.

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

Read `../shared/forms-data-entry.md`.

Mobile specialization additionally owns:

- appropriate mobile input/keyboard semantics;
- autofill/password-manager/OTP behavior where applicable;
- keyboard avoidance;
- field progression;
- interruption-safe long-form behavior;
- reduced typing.

Do not let generic form rules override platform keyboard behavior.

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

Read `../shared/state-recovery.md`.

Mobile specialization additionally defines behavior across:

- background/foreground transitions;
- process termination where restoration is supported;
- app switching;
- interrupted uploads/downloads;
- local draft vs synchronized state.

Do not force a full restart after recoverable mobile interruption.

### Long-running work

Read `../shared/state-recovery.md` and `../shared/feedback-status.md`.

Mobile specialization must account for work continuing while the app is backgrounded or the user leaves the current screen.

Preserve truthful queued/running/completed/failed state and safe return paths.

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

Read `../shared/motion.md`.

Mobile specialization retains platform-native transition and haptic conventions.

Do not use haptics as the only feedback and respect reduced-motion settings.

### Accessibility goals

Read `../shared/accessibility-interaction.md` for the cross-product floor and `../accessibility.md` for QA/evidence.

Mobile specialization additionally validates:

- VoiceOver/TalkBack semantics;
- platform text scaling;
- touch reachability;
- switch/keyboard/pointer input where relevant;
- platform focus behavior;
- adaptive layouts at larger text sizes.

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
