# Real-World Mobile Application Fixture

Representative product: cross-platform field-service app for iOS and Android.

Primary route: `mobile-application`
Platforms: iOS + Android + cross-platform

Intentional issues:

- camera permission requested immediately on launch
- upload spinner has no queued/offline/resume state
- system back/dismiss semantics are identical on both platforms
- keyboard obscures form controls
- fixed spacing and font sizes ignore text scaling
- Dark theme is raw color inversion
- gesture-only destructive action has no alternative
- Persian/English mixed identifiers are not directionally isolated

Expected evaluation:

- load Shared Mobile UX + cross-platform + iOS + Android packs
- preserve platform-specific navigation/system UI behavior
- model permission, connectivity, background/resume states
- apply Shared forms/state/accessibility/motion rules
- apply design-system typography/theme/responsive/product variants
- route Persian language QA to persian-writing
