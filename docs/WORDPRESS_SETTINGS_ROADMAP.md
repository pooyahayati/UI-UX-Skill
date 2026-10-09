# WordPress Plugin Settings Roadmap

Planning date: 2026-10-09.

Purpose: require `@wordpress/components`, task-oriented settings organization, and reliable interaction behavior for plugin-owned WordPress settings pages, without changing any other product route.

The [WordPress settings tracker in the project roadmap](../ROADMAP.md#wordpress-settings-extension-wps) is the **single current status ledger**. This document defines scope, work, dependencies, and acceptance criteria. Stage descriptions and scenario inventories are plans, not evidence of implementation or successful evaluation.

## Authority and settled decisions

The owner authorized preparing this plan in English and integrating it into the Git project with an updated project roadmap. That authorization covers this documentation change and its integration, not implementation of the planned Skill changes.

The component-library decision is settled: stable public components from `@wordpress/components` are mandatory for newly designed and explicitly authorized redesigned plugin settings surfaces. Do not reopen that choice merely because a form is small.

A subsequent instruction to execute this roadmap activates WPS-0. It does not automatically authorize migration of a real plugin, host-software installation, further remote integration, release, deployment, or updating the installed Skill. Reuse actual authorization already present in the executing session rather than asking repeatedly.

Use one lead implementation agent. This plan does not authorize additional agents or messages to other chats. A main agent can discover the work through `ROADMAP.md`, read this plan, and start the next eligible stage once execution is authorized.

## Baseline and implementation entry point

- Repository: `pooyahayati/UI-UX-Skill`.
- Canonical Skill source: `skills/ui-ux-skill/`.
- Inspected baseline: `f937d2e666a08ffaaf2958b9554d4ec1a214c54c`, version `3.3.0`.
- The baseline is evidence, not a permanent version pin. Refresh the repository state, applicable instructions, and affected files at kickoff.
- Existing WordPress guidance already covers intent-based grouping, capability boundaries, explicit saving, error recovery, accessibility, and inspection inside `wp-admin`. Extend and connect those rules; do not duplicate their shared methodology.
- Preserve user-authored changes and unrelated worktrees. Choose a clean suitable checkout or isolated branch for implementation.
- R0-R8, R9, and R10 history and completion counts remain separate from WPS. Planning does not reopen or relabel their acceptance.

Before editing Skill behavior, the executing agent must read the current WPS tracker, this plan, applicable repository instructions, and the existing WordPress pack/settings module. Inspect the relevant shared rules through the existing router; they remain read-only for this workstream.

The existing stabilization policy remains active while execution is unstarted. At an owner-authorized WPS kickoff, record that instruction and its bounded scope in the WPS tracker. That instruction supplies a WordPress-settings-only exception; it does not broaden the historical correction or Material exceptions, permit other product changes, or authorize editing shared policy validators to make a check pass.

## Scope and activation boundary

Both conditions are required to activate the new behavior:

1. The active product route includes `wordpress-plugin`.
2. The affected surface is a plugin-owned settings/configuration page or section inside WordPress administration.

In-scope examples include general configuration, connection settings, display options, advanced settings, and configuration reset actions on that settings surface, when those features actually exist.

Out of scope:

- Public websites, landing pages, standalone dashboards, web applications, and mobile applications.
- Public-facing WordPress themes, storefronts, and other visitor-facing UI.
- Block-editor controls and editor extensions as a separate surface.
- WordPress's global navigation, toolbar, unrelated admin screens, and other plugins.
- Non-settings onboarding, diagnostics, operations, or Network Admin workflows merely because the same plugin contains them.
- Extending the requirement to every operational screen in a hybrid plugin.
- Global design-system, theme, personalization, shared-rule, or optional Material changes.

For a hybrid product, apply the mandate only to the settings surface. Reading the WordPress pack for diagnostics or operations must not automatically load the new settings-components guide.

### Existing products and technical obstacles

Audit-only work reports the gap without migrating the UI. A narrow corrective request preserves its authorized boundary and does not trigger a whole-page rewrite. When a new design or redesign is authorized, the mandate applies within that scope, including simple forms.

A demonstrated technical obstacle requires a concrete compatibility finding and a bounded resolution proposal. Do not silently substitute another component library, waive the mandate because the form is small, or migrate storage/permissions to make the visual change easier.

## File allowlist and protected surfaces

### Future Skill behavior changes

| Path | Permitted change |
| --- | --- |
| `skills/ui-ux-skill/references/products/wordpress-plugin.md` | Settings-specific activation and routing clarification; preserve all other WordPress surfaces |
| `skills/ui-ux-skill/references/products/wordpress/settings.md` | Component mandate, organization, layout selection, interaction contract, and settings-specific acceptance |
| `skills/ui-ux-skill/references/products/wordpress/components.md` | New bounded guide to stable components, compatibility, assets, and integration |

Expected read path:

`WordPress Product Pack -> wordpress/settings.md -> wordpress/components.md`

The settings module exposes the guide when component selection, settings design, implementation, or review materially needs it. Do not add a global entrypoint dependency or preload it for other products or non-settings WordPress work.

### Supporting changes

| Path | Permitted purpose |
| --- | --- |
| `evals/wordpress-settings/**` | Dedicated scenarios, scoped evaluation helpers, isolation checks, and acceptance records |
| `evals/fixtures/wordpress-settings/**` | Raw briefs and runnable WordPress-settings specimens; fixture-local dependencies only when needed |
| `docs/WORDPRESS_SETTINGS_ROADMAP.md` | This plan and its scoped acceptance detail |
| `ROADMAP.md` | WPS current state, tracker, next action, and links; preserve other workstream history and policy |

This planning integration changes only the two Markdown documents inside the Git project. Future implementation may use the allowlist above after kickoff.

Protected content includes `SKILL.md`, product/shared/design-system registries, shared rules, design-system modules, specialist routing, other product packs, other WordPress modules, Material guidance, existing cross-product fixtures/manifests, historical evaluations, packaging tools, CI workflows, the README, and version files.

Run existing checks and use other products' inputs read-only where relevant. Do not modify their expectations to accommodate the new requirement. Reuse shared evaluation tools without edits when compatible. Any preparation needed only by this suite belongs in its dedicated directory; do not claim an existing validator automatically covers a newly added suite.

If implementation requires a path outside this allowlist, record why, its impact, and the proposed scope adjustment before changing it. A failing shared check is evidence to investigate, not permission to weaken or expand shared policy.

## Required settings outcome

### Components and visual hierarchy

Use stable public `@wordpress/components` controls for standard settings inputs, actions, feedback, and applicable interactive panels. Importing one library button while recreating the rest of the standard controls is not compliance.

Semantic HTML remains appropriate for layout, headings, and simple structure. A genuine need without a suitable stable component may use bounded composition or a semantic native control with a recorded reason. This must not become an escape hatch from the mandate.

Verify each chosen component and prop against the supported WordPress versions at implementation time. Experimental/private APIs and suppressing compatibility warnings are not the default path.

Visual quality should come from readable typography, useful grouping, consistent spacing, and clear action hierarchy. Do not add tabs, cards, columns, shadows, or dialogs solely because the library makes them available. This work does not invent plugin dark mode or a new appearance-control panel.

### Settings organization and findability

Inventory actual settings by user purpose, frequency, dependencies, consequence, default/inherited value, and capability. Derive the groups from that inventory.

Use user-facing group names, not database tables, class names, or API routes. Do not create empty categories or use Advanced as a miscellaneous bucket.

Use plain sections for short pages, tabs for independent topics, and disclosure panels for genuinely secondary content. Keep essential options and active errors discoverable. Avoid nested tabs.

Add settings search only when actual volume and findability justify it. Do not prescribe the same category count, fixed set of tabs, or universal page template for every plugin.

### Interaction, saving, and recovery

Provide persistent labels, meaningful values, nearby guidance where needed, and clear consequences for important options. Explain prerequisites and disabled controls.

Choose a coherent save model. Distinguish initial/loading, modified, saving, successful, and failed states. Show success only after authoritative server confirmation.

Do not mask an initial-load failure with defaults that look like saved values. Control submission until valid current state is available. Preserve safe user input after failure and provide correction or retry.

Prevent unintended duplicate submission. Do not overwrite newer user edits with an earlier request's response. Handle navigation with unsaved changes according to the product's real save contract.

Associate errors with their fields, make errors in other tabs or collapsed groups discoverable, and do not make a transient toast the only way to understand the outcome.

Distinguish replacement/removal of stored secrets, clearing a normal value, resetting a field/section, restoring defaults, and deleting plugin data. UI visibility does not replace server-side capabilities, validation, sanitization, or request protection.

### Technical compatibility and host integration

Derive the minimum supported WordPress version from the product's requirements. Verify it and the stable version at execution time; the newest documentation does not prove a feature exists on the minimum version.

Use WordPress shared dependencies, the generated asset dependency metadata, and the component stylesheet correctly. Load plugin assets only on its own settings screen. Bound custom styling to the owned surface.

Check dialogs/popovers and content rendered outside the application root separately. Do not require the standalone Gutenberg plugin without a demonstrated product requirement.

The library mandate does not automatically change option keys, data storage, the Settings API submission contract, capabilities, or require a new REST API. Preserve those contracts unless a separate authorized change is necessary.

Build tooling belongs to development and packaging. Ordinary site administrators should receive a ready-to-install plugin, not a request to run its build. Specimen dependencies must remain fixture-local rather than becoming dependencies of the entire Skill repository.

### Localization, accessibility, and real admin context

Use the product's actual language/direction requirements. The owner's conversation language is not a product-language requirement. Use the existing `persian-writing` route for the Persian specimen.

Inspect long translations, technical LTR values in RTL text, keyboard order, focus, errors, zoom/reflow, and overlays inside real `wp-admin`. Source attributes or geometry alone do not establish working accessibility or visual acceptance.

Read existing Multisite guidance only when the product supports that context. This roadmap adds neither Multisite support nor a new privilege model.

## Execution packages

There are seven packages, WPS-0 through WPS-6. Their live statuses, active package, completion count, and next action belong only in the [project tracker](../ROADMAP.md#wordpress-settings-extension-wps).

### WPS-0: Baseline and bounded kickoff

**Prerequisite:** owner instruction to execute this roadmap.

**Work:** inspect current source, instructions, user changes, and the three behavior paths; record the base revision and hashes of protected files; prepare positive and negative scenario inputs before behavior edits. Record the narrowly authorized WPS scope in the project tracker.

**Output:** reproducible baseline, expected changed-file allowlist, and raw evaluation inputs in the dedicated suite.

**Exit:** no unrelated user change is adopted; required paths and tooling are understood; any policy/integration conflict is resolved within the authorized WordPress-only boundary or remains an explicit blocker. Planning integration is not evidence that this package ran.

### WPS-1: Mandate and routing

**Prerequisite:** accepted WPS-0.

**Work:** add the requirement and local guide reference; distinguish new design, authorized redesign, audit, and narrow correction; preserve all other WordPress routes.

**Output:** a bounded local read path without changes to the global Skill entrypoint.

**Exit:** new settings requests, including simple forms, activate the mandate. Non-settings WordPress and non-WordPress requests do not. Audit-only work does not cause migration.

### WPS-2: Organization and interaction

**Prerequisite:** accepted WPS-1.

**Work:** refine existing grouping, section/tab selection, progressive disclosure, dependent controls, saving, errors, and recovery rules. Add examples only when they clarify a real decision.

**Output:** observable contracts for finding a setting, understanding its effect, and saving reliably.

**Exit:** short inputs do not produce unnecessary navigation; multi-topic inputs follow user intent; errors remain findable and safe input survives failed saving. Shared form methodology is referenced rather than copied.

### WPS-3: Component and implementation guidance

**Prerequisite:** accepted WPS-2.

**Work:** document stable component selection/composition, version support, shared dependencies, styles, translation, and overlays. Preserve storage and authorization boundaries.

**Output:** a focused local guide with official sources and a verification date; code examples only where useful and compatibility-checked.

**Exit:** the mandate and existing scope/contract protections are consistent; examples do not depend on private or experimental APIs; no new repository-wide framework/tooling dependency is introduced.

### WPS-4: Runnable specimen inside WordPress

**Prerequisites:** accepted WPS-3 and an authorized local test environment.

**Work:** build an isolated specimen with bounded real settings, grouping, a dependent field, saving, and a reproducible failure path. Simple and multi-topic forms may be variants of one specimen.

**Output:** a documented runnable/installable specimen, exact environment versions, and valid captures of representative states. Use synthetic data.

**Exit:** observe the screen at normal and narrow admin widths; exercise load, edit, successful/failed saving, keyboard access, and overlays; inspect Persian/mixed-direction content in the Persian specimen.

A successful build, mock screenshot, or standalone page outside `wp-admin` does not complete this package. Record available evidence and leave the required criterion open if the environment is unavailable. Do not install host software without existing authorization.

### WPS-5: Behavioral evaluation and isolation

**Prerequisite:** accepted WPS-4.

**Work:** run the scenario inventory against the candidate; inspect loaded resources, decisions, and changes; run relevant existing structural checks; compare source and package content with the baseline.

**Output:** per-scenario outcomes with method, candidate revision, concrete evidence, and limitations. Preparing a prompt is not executing a model.

**Exit:** no unexplained failures in activation, the mandate, data preservation, capabilities, or isolation; protected files remain byte-identical. Distinguish real agent observations from text checks or manual source review.

A fresh independent session is preferred when authorized and available. This plan does not itself authorize spawning an agent or creating/messaging another chat. If evaluation uses the current session, record that limitation rather than claiming independence.

### WPS-6: Local acceptance and reviewable handoff

**Prerequisite:** accepted WPS-5.

**Work:** review wording and links, map requirements to evidence, inspect the final diff, build the candidate package outside product source using existing tooling, and verify packaged resource routes.

**Output:** reviewable local changes, scoped acceptance record, and precise readiness state.

**Exit:** all required earlier criteria hold; other product resources in the package match the baseline; source, runtime specimen, candidate package, and installed state are reported separately. Keep release/version changes outside this implementation scope.

A later requested publication or installation must satisfy the project's gates for that exact final target. Local completion is not publication.

## Planned acceptance scenarios

These are future tests, not completed results.

| ID | Starting point or action | Required observable outcome |
| --- | --- | --- |
| WP-01 | New settings page with a few simple fields | Stable library controls; no simplicity exemption and no unnecessary navigation |
| WP-02 | Multi-topic settings with essential and advanced options | Task-based grouping, visible priority, no nested tabs |
| WP-03 | Change an option on which another field depends | Clear dependency state/reason; no undocumented data deletion |
| WP-04 | Initial settings load fails | Recoverable error; defaults do not masquerade as saved data |
| WP-05 | Validation or network failure while saving | Preserve input, identify the problem, no false success, usable retry/correction |
| WP-06 | Duplicate submit, edit during saving, or leave with unsaved changes | Respect the save contract and preserve newer user intent |
| WP-07 | Limited capability, reset, and sensitive values | Actual capability enforcement, clear reset scope, no secret exposure |
| WP-08 | Minimum supported and current stable WordPress versions | Compatible controls/styles/shared dependencies without a hidden editor-plugin requirement |
| WP-09 | Narrow Persian admin, long labels, technical values, and an overlay | Readable direction, usable focus and keyboard interaction in real admin context |
| WP-10 | Audit or narrow correction of a legacy settings page | Report the mandate gap without an unauthorized full migration or storage change |
| ISO-01 | Separate website, web-app, dashboard, and mobile requests | No new WordPress guide loading, library mandate, or settings-layout requirement |
| ISO-02 | Public-facing WordPress UI change | No activation of the admin-settings mandate |
| ISO-03 | Diagnostics-only or operations-only plugin task | Existing route preserved; settings-components guide not imposed |
| ISO-04 | Hybrid plugin with settings and operational workspace | Apply the mandate only to settings; preserve other active surfaces |
| ISO-05 | Compare candidate source and package with the baseline | Behavior edits only in the three allowed paths; other resources byte-identical |

Isolation is not only a search for the package name. Inspect actual routing, resources read, and decisions for negative scenarios. Exact wording equality across model responses is not a useful invariant.

Structural tests, runtime inspection, agent evaluation, and real product-owner approval are different evidence types. Historical cross-product results cannot be relabeled as fresh results for this candidate.

## Validation and evidence

Use the relevant existing tools after inspecting their current interfaces:

- `scripts/validate_product_routes.py`
- `scripts/validate_resource_routes.py`
- `scripts/validate_shared_rules.py`
- `scripts/validate_eval_fixtures.py`
- `scripts/validate_release.py`
- `scripts/package_release.py`

Record actual arguments, input revision, exit status, and scope. Existing validators do not automatically cover this suite. Run dedicated scenarios separately; do not edit shared validators to manufacture coverage or a pass.

Keep generated builds, caches, temporary captures, and scan reports outside product source. Retain selected durable evidence with provenance under the dedicated evaluation directory. Other products' tests may run read-only; their fixtures and expected behavior must not be rewritten.

## Progress, escalation, and rollback

Update the WPS tracker in `ROADMAP.md` before an authorized stage. Record actual partial delivery, affected files, dependencies, dated acceptance, checks, limitations, and the next action. Keep this document as the detailed contract, not a second live tracker.

Allowed stage states: `Not started`, `In progress`, `Blocked`, `Completed`, and `Reopened`. An unstarted prerequisite does not itself make a future stage blocked. A missing required observation keeps its criterion open.

Reassess scope when a protected file must change, the mandate leaks to another route, the UI requires an unauthorized data/permission/storage change, or the target version lacks a required compatible component. Missing required evidence prevents acceptance; unrelated passes cannot close it.

Rollback is limited to the workstream's own changes on its working branch. Do not reset unrelated work, delete user changes, or modify the installed Skill as a rollback shortcut.

At handoff, report the branch, local/upstream revisions, ahead/behind state, dirty/committed/pushed state, relevant checks, and any real PR/merge identifiers. Report unavailable evidence explicitly. No new release, installation, or Graphify run is implied by this documentation-only integration.

## References and evidence limits

Refresh component-specific implementation facts during WPS-3. The tutorial is educational, not a production contract or proof of support on every WordPress version.

- [Official plugin-page tutorial](https://developer.wordpress.org/news/2024/03/how-to-use-wordpress-react-components-for-plugin-pages/)
- [Official components package](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-components/)
- [Shared dependency extraction](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dependency-extraction-webpack-plugin/)
- [Settings API](https://developer.wordpress.org/plugins/settings/settings-api/)
- [REST request authentication](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/)
- [Current WordPress Product Pack](../skills/ui-ux-skill/references/products/wordpress-plugin.md)
- [Current settings module](../skills/ui-ux-skill/references/products/wordpress/settings.md)
- [Existing evaluation method and limitations](../evals/README.md)
