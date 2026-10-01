# Real-World WordPress Plugin Fixture

Representative product: integration plugin with settings, credentials, diagnostics, background sync, reset, and Multisite support.

Primary route: `wordpress-plugin`

Intentional issues:

- settings grouped by backend module names
- API key presence is shown as "Connected" without verification
- every message uses a global admin notice
- reset label does not explain scope
- long sync uses a blocking spinner
- capability logic assumes Administrator rather than capabilities/network scope
- no distinction between site and network defaults
- plugin UI uses custom controls that ignore wp-admin sizing/focus
- raw colors bypass semantic tokens

Expected evaluation:

- load WordPress main pack plus settings/onboarding/diagnostics/multisite local packs as needed
- preserve wp-admin host mental model and real capability semantics
- distinguish credential storage, connection health, background job state, reset/delete/uninstall scope
- load relevant Shared feedback/state/destructive/accessibility rules
- use host-compatible Design System variants
