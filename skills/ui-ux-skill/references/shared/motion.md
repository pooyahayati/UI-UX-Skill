# Motion and Transition Rules

Use when animation, transition, haptic, scroll effects, animated feedback, or reduced-motion behavior is materially in scope.

## Purpose before motion

Motion should communicate one or more of:

- spatial relationship;
- hierarchy;
- continuity;
- state change;
- direct manipulation;
- progress;
- confirmation;
- attention to a meaningful event.

Do not animate because the interface feels visually quiet.

## Repeated-task cost

Motion that is pleasant once can become friction when repeated all day.

Reduce or remove animation in:

- high-frequency operations;
- dense dashboards;
- data entry;
- repeated navigation;
- bulk workflows.

## Duration and interruption

Animations should not block the next task unnecessarily.

Users should not have to wait for decorative motion before interacting.

When a transition is interrupted by a new user action, the UI should reach a coherent state.

## Reduced motion

Respect reduced-motion preferences.

When motion carries meaning, provide a lower-motion alternative that preserves the information.

Do not simply disable a transition if doing so makes state changes incomprehensible.

## Loading motion

Loading indicators communicate waiting, not completion percentage unless measurement exists.

Avoid large animated loaders that dominate a surface while unrelated content remains usable.

## Scroll motion

Avoid scroll hijacking.

Use scroll-triggered animation sparingly.

Do not require animation to reveal content needed for reading/navigation.

## Attention

Animation can draw attention, so reserve repeated/high-salience movement for genuinely important change.

Do not make routine live updates pulse continuously.

Avoid flashing patterns that create accessibility risk.

## Haptics

On platforms that support haptics:

- use them to reinforce meaningful state/action;
- avoid haptic feedback for every tap;
- do not rely on haptics as the only feedback.

Platform packs define native haptic conventions.

## Direction and RTL

Do not blindly mirror motion if the transition represents:

- time;
- physical direction;
- data order;
- platform-native navigation semantics.

Mirror only when the interaction meaning is directional according to language/layout.

## Validation

Verify:

- first use;
- repeated use;
- interrupted transition;
- reduced-motion mode;
- loading/long-running state;
- live update behavior when applicable;
- RTL/LTR directional meaning.
