# Cross-Platform Mobile Design Rules

Use this local rule pack when one product or codebase targets multiple mobile platforms, including React Native, Flutter, Compose Multiplatform, .NET MAUI, or similar cross-platform stacks.

This is a design translation pack, not a framework implementation guide.

Core principle:

> Preserve the product and UX decisions; translate the platform idiom, not the pixels.

## Separate product truth from platform presentation

Classify every important decision as one of:

### Shared across platforms

Usually shared:

- product job;
- user roles;
- information architecture;
- core workflow sequence;
- business meaning;
- state model;
- content priority;
- brand identity and semantic tokens;
- validation rules;
- data trust and permission meaning.

### Platform-adapted

Often adapted:

- navigation chrome;
- back/dismiss behavior;
- sheets/dialogs;
- menus/context actions;
- system bars;
- keyboards/input behavior;
- permission presentation;
- motion;
- native controls;
- typography metrics;
- larger-screen patterns.

### Platform-exclusive

May be exclusive:

- platform-specific system integrations;
- hardware/capability-specific workflows;
- OS-exclusive widgets or navigation behavior;
- platform-specific account/payment/service features;
- desktop-class window behavior on supported devices.

Do not force a platform-exclusive behavior into the shared abstraction merely to keep screenshots identical.

## One design system, multiple presentations

Share semantic design intent such as:

- color roles;
- spacing scale;
- typography roles;
- elevation/surface intent;
- component purpose;
- interaction state vocabulary.

Allow platform presentation to diverge when native expectations improve usability.

The same semantic component does not have to be visually or behaviorally identical on every platform.

## Navigation translation

Preserve destination hierarchy and task relationships.

Translate navigation presentation according to platform and window context.

Examples:

- a top-level destination may appear in a platform-native tab structure on one platform and a different native navigation container on another;
- a detail flow may use different back/dismiss affordances while preserving the same hierarchy;
- tablet/large-screen layouts may expose multiple panes instead of repeating phone navigation.

Do not implement one platform's navigation chrome everywhere.

## Dialogs, sheets, and temporary tasks

Preserve the purpose of the task, not necessarily the container.

For each temporary flow, define:

- task scope;
- apply/cancel semantics;
- destructive behavior;
- dismiss behavior;
- resume behavior.

Then choose the appropriate native presentation on each platform.

## Permissions and system capabilities

The product reason for requesting a capability should remain shared.

The system flow, wording constraints, and recovery path may differ by OS.

Do not fake cross-platform consistency by replacing trustworthy system UI with custom copies.

## Typography and density

Preserve hierarchy and brand intent while allowing platform metrics, font rendering, text scaling, and density to adapt.

Validate large text independently on each platform.

Do not lock line heights or control heights to a single platform's measurements when they break native text scaling.

## Motion and gestures

Preserve the meaning of motion while allowing platform-native transition behavior.

Gesture shortcuts may differ by platform.

Do not require identical gestures where they conflict with system navigation or platform conventions.

## Shared component API caution

A shared component abstraction should encode product semantics, not erase platform capability.

Avoid abstractions that:

- expose every platform option in one bloated component;
- force lowest-common-denominator UI;
- make native accessibility harder;
- prevent adaptive platform behavior;
- preserve pixel identity at the expense of usability.

## Platform review matrix

For each important surface, record:

- shared UX decisions;
- iOS-specific adaptations;
- Android-specific adaptations;
- large-screen adaptations;
- capability-specific differences;
- known intentional visual differences.

This makes divergence explicit rather than accidental.

## Validation

Cross-platform QA must compare both:

### Shared invariants

- same product meaning;
- same core capabilities;
- equivalent validation/business outcome;
- equivalent content priority;
- equivalent accessibility goal.

### Platform fidelity

- native navigation/back expectations;
- system UI/insets;
- keyboard behavior;
- permissions;
- text scaling;
- gestures;
- large-screen behavior;
- accessibility services.

Do not treat screenshot similarity as proof of cross-platform quality.
