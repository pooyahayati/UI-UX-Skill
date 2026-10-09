# WordPress settings components

Use only through [settings](settings.md) for plugin-owned settings/configuration
inside `wp-admin`. This is the owner's settings design convention, not a claim
that WordPress requires every plugin or administration screen to use this library.

Stable public `@wordpress/components` controls are required for new and authorized
redesigned settings, even a short form. Preserve existing option keys, storage,
Settings API/REST contracts and server-side permissions. Audit/narrow-fix authority
does not imply a full component migration.

Use semantic HTML for headings and layout. For an actual component gap, record
the need and compatible native composition; size alone is not a gap. Do not copy
experimental/private APIs or assume the newest handbook proves minimum-version
support. Verify the chosen controls/props in the real supported admin context.

Official implementation sources:

- [Components package and WordPress styles](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-components/)
- [Plugin-page integration example](https://developer.wordpress.org/news/2024/03/how-to-use-wordpress-react-components-for-plugin-pages/)

## Choose by data and task

| Need | Stable public candidate | Check before use |
| --- | --- | --- |
| Short free text, email or technical value | `TextControl` | Persistent `label`, controlled `value`/`onChange`, meaningful `help`, native input type/direction and associated errors |
| Boolean setting | `ToggleControl` or `CheckboxControl` | Controlled value, consequence and dependency explanation; do not erase a disabled dependent value |
| Small known choice set | `SelectControl` or `RadioControl` | Actual option labels/values and the current selection; avoid a custom dropdown |
| Save, retry, cancel or reset action | `Button` | Explicit action/scope, supported variant, busy/disabled semantics and duplicate-submit protection |
| Durable local status or validation summary | `Notice` | Severity, accessible announcement, persistence and links to affected fields; not toast-only recovery |
| Genuinely secondary settings | `PanelBody` | Meaningful title, initial open state and discoverable errors; primary options need not be collapsed |
| Consequential confirmation | `Modal` | Clear scope, title/close callback, initial/contained focus and return focus; use only when consequence warrants it |
| Async wait | `Spinner` with status text | Loading is not a completed or measurable-progress claim |

This is a task-oriented shortlist, not an exhaustive component catalog. Use
ordinary headings/sections for a short form; components do not require tabs or
cards. Read official component documentation only for controls actually needed.

## Compatibility and assets

Derive the minimum WordPress/PHP versions from the product. Record each selected
control, important props, minimum/current host versions, source verification date
and actual runtime result. Check the matching core implementation when current
handbook examples use newer props. Avoid `__experimental*`, private exports and
`__next*` opt-in behavior as the default compatibility strategy. A stable export
can still have version-specific styling or warnings; inspect rather than suppress.

An explicitly verified public styling-transition flag can be a bounded exception:
record its reason and test it on both supported hosts. The WPS specimen adopts
`__next40pxDefaultSize` and `__nextHasNoMarginBottom` on the applicable basic
controls after inspecting core 6.8/7.1.3 and their deprecation notices. This does
not permit experimental controls, unknown flags or warning suppression.

For a bundled build, use the existing stack and dependency-extraction tooling so
WordPress supplies its registered shared dependencies. Load the generated asset
metadata with the same built entry; do not ship another React runtime or assume an
editor screen loaded the dependencies already. For a small no-build script using
the public `wp.components`/`wp.element` globals, explicitly declare the handles
it uses in its maintained asset metadata. This is a valid bounded integration,
not a request to introduce Node tooling into every PHP plugin.

Enqueue scripts on the owned settings hook only, and make `wp-components` a style
dependency. Add translation loading for the actual script handle/domain when
using WordPress i18n. Deliver an installable built plugin to administrators; they
must not run its development build. Scope layout CSS to the owned surface using
logical properties and approved tokens; do not restyle the global admin shell.

For dialogs/popovers, inspect portal content outside the root: document language,
direction, inherited typography, component styles, z-index and focus. `Popover`
normally appends content to the body; use a verified `Popover.Slot` only if the
product needs a deliberate portal location. Root-only selectors cannot certify
portal styling. Never enable Gutenberg merely to make ordinary settings work.

## Preserve the submission contract

Components are presentation and interaction. Keep existing Settings API form
submission when it meets the product contract; use an existing async endpoint
only when appropriate. Do not invent REST routes, option-key migrations or a new
privilege model because controls render in React. Server capability checks,
nonces, validation/sanitization and truthful save outcomes remain required.

Follow [settings recovery](settings.md#save-model) for initial-load errors,
section preservation, edits during saving, uncertain commits and concurrent
administration. Stored-secret masking is not a connected-service success claim.

## Verification record

Official package/control/element documentation was checked 2026-10-10. Concrete
runtime support must be checked per product; this date is not a permanent version
pin or universal compatibility guarantee. The repository's WPS specimen targets
WordPress 6.8 and the execution-time stable 7.1.3 for the basic public controls
above. Its runtime evidence does not certify every component/prop in the library.

Additional official sources:

- [TextControl](https://developer.wordpress.org/block-editor/reference-guides/components/text-control/)
- [ToggleControl](https://developer.wordpress.org/block-editor/reference-guides/components/toggle-control/)
- [Button](https://developer.wordpress.org/block-editor/reference-guides/components/button/)
- [Notice](https://developer.wordpress.org/block-editor/reference-guides/components/notice/)
- [Panel](https://developer.wordpress.org/block-editor/reference-guides/components/panel/)
- [Modal](https://developer.wordpress.org/block-editor/reference-guides/components/modal/)
- [Element public runtime](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-element/)
- [Dependency extraction](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dependency-extraction-webpack-plugin/)

Library usage is not visual, accessibility or data-preservation acceptance. Apply
the existing settings interaction and host-context checks before completion.
