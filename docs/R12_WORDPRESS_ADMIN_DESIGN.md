# R12: WordPress Admin Design and Settings Findability

## Objective and authority

Administrators should find a setting, understand its consequence and complete their task in a coherent, attractive, contemporary plugin interface. Component selection serves that outcome; importing a library alone is not acceptance.

**Owner decision, 2026-11-01:** prepare this plan and update the project roadmap from the agreed design direction. Authority currently covers planning/documentation only. Implementation, dependencies, test-host changes, commit/push/merge, release and local installation are not authorized by this decision. Earlier WPS/R11 delivery permissions remain limited to their completed work. A later instruction may authorize bounded execution without repeating settled design choices.

Live package states belong only in [ROADMAP.md](../ROADMAP.md#r12-wordpress-admin-design-and-settings-findability). All six packages are initially `Not started`; planning readiness is not implementation completion. Execute in order after authorization, with one lead writer and one active package. Record material decisions and stage evidence here or in one linked execution record, not a second competing tracker.

**Superseding implementation instruction, 2026-11-01:** the owner requested all six packages. [Authority and execution evidence](R12_EXECUTION.md#authority) retain this bounded authorization. The initial planning-only decision above is historical; delivery remains separately authorized.

## Baseline and protected scope

Planning baseline: released Skill 3.5.1; remote `main` checked at `0f708db4a2eb77f1524903bad1cf8ec1c1e91b15` on 2026-11-01. Existing guidance and fixtures already cover task-based settings, native controls, saving/recovery, responsive/RTL behavior and capability boundaries. R12 strengthens findability, page composition and verifiable visual quality; it is not a claim that every existing screen is broken.

- Preserve [the WordPress Product Pack](../skills/ui-ux-skill/references/products/wordpress-plugin.md), [settings behavior](../skills/ui-ux-skill/references/products/wordpress/settings.md) and the owner's [component convention](../skills/ui-ux-skill/references/products/wordpress/components.md): stable public `@wordpress/components` remains required for **new or explicitly redesigned plugin-owned settings**, including short forms.
- Classify settings, operational workspace and hybrid surfaces separately. This work includes plugin-owned lists/details, connection status and background-work screens, not WordPress core's Plugins list, global navigation/toolbar, unrelated admin screens, public storefronts or block-editor UI.
- A narrow fix or audit never authorizes redesign. A workspace may need richer composition, but its name alone does not activate shadcn/ui, Material, Motion or a framework migration. Existing stack, explicit owner choices and host constraints win.
- Preserve storage/option keys, Settings API/REST contracts, capabilities, nonces, secret handling, data meaning and lifecycle behavior. No UI-driven backend redesign, global CSS reset or duplicate React runtime.
- Reuse approved `DESIGN.md` decisions or an observed baseline. Review one primary-language/direction proposal first; supported/requested dark appearance follows the existing approval rules, and secondary language/layout is conditional. Do not mandate a dark toggle, bilingual product, new font approval or a new appearance-management panel for every plugin.
- Where appearance management is already in product scope, retain bounded font/color/icon/density controls and the existing validation/preview/publication rules. Changes must stay within the plugin-owned surface; arbitrary executable CSS/JS/HTML remains excluded.
- The old WPS/R11 reports, screenshots and behavioral outputs remain historical evidence, not files to relabel as a new run.

## Planned change boundaries

Only `ROADMAP.md` and this plan change during planning. The following are **future implementation targets**, not permission to edit them now.

| Area | Intended change / boundary |
| --- | --- |
| `skills/ui-ux-skill/references/products/wordpress-plugin.md` | Route settings vs internal operational surfaces and their relevant design checks; keep the settings-only library mandate. |
| `references/products/wordpress/settings.md` and `components.md` under the Skill root | Extend organization/findability and visual/component decisions without duplicating existing save/security contracts. |
| Conditional local resources under `references/products/wordpress/` | At most a focused findability guide and page-pattern guide if the content warrants them; link from the active local module, not the global entrypoint. Short additions may stay in existing guides. |
| Existing onboarding, diagnostics and multisite modules | Narrow cross-links or WordPress-specific specialization where needed; do not copy their established state/permission rules. |
| `evals/fixtures/wordpress-settings/` and `evals/wordpress-settings/` | Reuse the owned synthetic host and save/recovery behavior; add bounded discovery/operational specimens and successor evidence. No real customer data or production site. |
| Existing evaluation/roadmap/package validation and CI entrypoints | Add directly required regression cases and R12 status checks; preserve historical fixtures, negative checks and unrelated acceptance gates. Extend existing tools, not a new general evaluation framework. |
| README/evaluation instructions/release documentation | Update only changed claims and navigation at acceptance. No version bump or installed-Skill edit in this plan. |

Shared rules, global registries, unrelated Product Packs, Material/shadcn/motion policy and the generic handbook template remain unchanged unless a demonstrated cross-cutting need is separately scoped. Use their current contracts through existing routing.

## R12.1: Baseline and surface routing

**Entry:** explicit implementation instruction. **Output:** retained baseline, bounded task inventory and conditional local routing.

Inspect real settings/tasks before choosing tabs, cards or a sidebar. For each representative setting record user-facing name, intent/search aliases, group, frequency/consequence, dependency, capability, default/effective value, save scope and stable destination. Record operational tasks separately; do not invent categories or features to fill a template.

| ID | Acceptance |
| --- | --- |
| A1.1 | Short settings, multi-topic settings, operational workspace and hybrid examples select the correct local guidance. A non-settings screen does not automatically acquire the settings-only library mandate. |
| A1.2 | Audit/narrow-fix, public-site and unrelated dashboard requests preserve their scope; no automatic redesign, package installation or extra Product Pack. |
| A1.3 | Every inventoried setting/task has a justified destination and protected state/save contract. Existing WPS/R11 source/evidence bindings and affected evaluation cases are identified before changes. |
| A1.4 | The R12 counter, active/next package and dated evidence rules are checkable, including rejection of out-of-order/unsupported completion; existing historical roadmap tests remain effective. |

**Exit evidence:** reviewed inventory/routing examples, exact baseline and dependency map, targeted routing/status regressions. No layout is accepted merely because these documents exist.

## R12.2: Organization and findability

**Entry:** accepted R12.1. **Output:** task-oriented grouping, navigation and conditional search guidance with concrete interaction examples.

Use sections for short forms; independent topics may justify tabs or plugin-local navigation. Keep frequent actions visible, advanced options deliberately secondary and critical prerequisites/errors discoverable. Avoid tab-within-tab navigation and vague catch-all groups. Search is required when the actual inventory/findability assessment warrants it, not because every form needs a search box. It complements, rather than replaces, understandable grouping.

| ID | Acceptance |
| --- | --- |
| A2.1 | A reviewer can map representative user tasks to the intended group without knowing internal option keys. Short forms do not gain unnecessary tabs/sidebar/search. |
| A2.2 | Search matches permitted setting names, help and curated user-intent aliases; a synonym query reaches the relevant setting even when the label uses another term. Persian matching handles relevant character/spacing variants; clearing and no-result states are useful. Do not index secrets, user-entered values or unauthorized metadata. |
| A2.3 | Selecting a result opens the correct page/group/disclosure, visibly identifies the field and places keyboard focus appropriately. Search, section changes and back navigation preserve valid unsaved edits; never persist secrets into URLs or unapproved browser storage to achieve this. |
| A2.4 | Hidden-group validation errors remain reachable. Disabled/inherited settings explain their actual dependency/authority; permission-denied results cannot expose or mutate restricted configuration. Search keyboard selection, dismissal and focus return work. |

**Exit evidence:** raw task/query examples plus focused model/DOM checks and rendered keyboard checks on the real host. Demonstrate found/not-found/hidden/disabled/restricted paths and draft preservation, not merely a successful string match.

## R12.3: Visual foundations and components

**Entry:** accepted R12.2. **Output:** implementable visual decisions and task-appropriate, version-checked control selection.

Record palette/status meanings, typography, widths, spacing/density, icon treatment, borders, action hierarchy and normal/focus/error/disabled states in the existing handbook or fixture design record. Reuse tokens; the component library is not a universal page layout. Branding stays inside the plugin surface and includes portal/overlay behavior. Decorative cards, excessive whitespace, oversized headings and motion must earn their place through the product task, not a generic modern-dashboard template.

| ID | Acceptance |
| --- | --- |
| A3.1 | The rendered design can be traced to approved/proposed foundations; repeated controls and states are consistent. Labels, help and actions remain readable with realistic long content, narrow width and supported direction. Missing decisions are proposals, never fabricated owner approval. |
| A3.2 | Each selected control/important prop has a public-source reference, review date, actual minimum/current target and runtime-dependency decision. Verify provided exports, generated asset metadata, styles/translations and bounded enqueue scope; a newer installed package does not prove an older host supports it. |
| A3.3 | Add a conditional decision route for data-heavy lists/forms where useful, including evaluating `DataViews`/`DataForm`; do not mandate them for short forms or infer REST/stack migration. A library limitation yields a documented compatible alternative, not an untested import or silent policy override. |
| A3.4 | Optional WordPress semantic tokens/theme integration is version-verified and scoped. Current experimental/new libraries are not automatic replacements. Interactive decoration respects reduced/off preferences, and save/focus/status behavior does not depend on animation. |

**Exit evidence:** scoped design specification and component compatibility record, with actual target-host checks for adopted controls. Reuse existing native controls when they satisfy the task. Do not copy an exhaustive, quickly stale upstream component/token catalog into the Skill.

## R12.4: Rendered page patterns

**Entry:** accepted R12.3. **Output:** a compact, inspectable set of realistic examples and guidance for choosing/adapting them.

Build on the existing simple/multi-topic specimens. Cover distinct needs without forcing a separate page for each: settings organization/search, list/filter-to-detail/edit, connection state, and background-work status/recovery. Reuse known safe fixture actions; do not build a real external service or production job engine for demonstration. Every simulated action/state is labelled truthfully.

| ID | Acceptance |
| --- | --- |
| A4.1 | One representative primary-language/direction page is rendered and reviewed inside `wp-admin` before the pattern is generalized. It uses real-length product text and the chosen foundation; other patterns share that language of design without forcing identical layouts. |
| A4.2 | Desktop/narrow layouts include the real toolbar/menu/notices. Long labels/help, filters, primary actions, overlays and focused controls remain usable without clipping or unintended page overflow. Inspect purposeful data-table overflow separately. |
| A4.3 | Useful default/loading/empty/error/disabled/unsaved states are shown for the relevant workflow. List selection and scope, connection configuration vs health, and accepted background work vs completion are distinguishable. |
| A4.4 | Captures/demo entrypoints identify source revision, host, language, theme, viewport and state. Engineering visual review and fixes are recorded. Real product rollout still requires its scoped owner approval; hypothetical fixture appearance does not create a new mandatory customer approval cycle. |

**Exit evidence:** linked runnable entrypoints, trustworthy screenshots and reviewed behavior in the real synthetic admin host. Cover Persian/RTL and a supported LTR test context as Skill capability checks, not a requirement that every downstream product be bilingual. Only exercise dark appearance where supported/requested; retain the existing sequential approval model.

## R12.5: Behavioral and regression evaluation

**Entry:** accepted R12.4. **Output:** evidence that the Skill chooses appropriate patterns and the specimens support actual administrator tasks.

| ID | Acceptance |
| --- | --- |
| A5.1 | A fresh evaluator receives raw product/task information without an answer key and locates/changes representative settings, including an alias query and a hidden-group error. Record success, wrong turns, help needed and observed path/time where measured. An author-led walkthrough is not unassisted discovery; agent results are not human usability certification. |
| A5.2 | Common tasks complete without facilitator hints and without lost edits or incorrect saved values. Investigate repeated wrong destinations or failed discovery and revise before acceptance. Compare against a retained baseline if claiming reduced time/steps; do not invent a universal seconds/click quota or claim improvement from screenshots alone. |
| A5.3 | Required behavioral cases cover short-form restraint, complex findability, hybrid routing, audit-only scope, incompatible/new components and primary/dark/secondary boundaries. The actual response/artifact is reviewed against withheld criteria; recommendations and library references alone are not successful implementation. |
| A5.4 | Existing save/recovery, two-admin conflict, capability/nonce, reset/secret, keyboard and package/resource regressions remain effective. Extend checks only for changed/uncovered outcomes, including search transitions, aliases and permission filtering; do not replace them with keyword-only assertions. |
| A5.5 | Preserve original WPS/R11 reports and outputs. Changed protected source gets an exact-parent successor record with explicit changed-path scope and actual fresh checks, not rewritten historical hashes or blanket exclusions. Refresh affected consumed-source behavioral cases (including WordPress-sensitive UI-foundation cases); added resource inventory/version changes must also satisfy the existing candidate/preparation bindings. Never rebind an old output and call it a new run. |

**Exit evidence:** criterion-to-result mapping, actual independent outputs and runtime observations, candidate/source hashes, negative integrity tests and explicit unexecuted/unsupported contexts. Missing required host/runtime evidence stays open; unrelated passes cannot close it. Reuse unchanged valid observations only within their recorded scope.

## R12.6: Combined acceptance and handoff

**Entry:** accepted R12.5. **Output:** coherent, reviewable Skill changes ready for a separately authorized delivery action.

| ID | Acceptance |
| --- | --- |
| A6.1 | All A1–A5 required outcomes have relevant accepted evidence. The roadmap reports six completed packages only then, with dated links and no hidden required blocker; historical WPS/R11 scope remains intact. |
| A6.2 | Source routes, extracted standalone/plugin resource routes, full license notices and package integrity pass. New WordPress references are discoverable only through relevant routes; unrelated product behavior/mandatory libraries do not change. |
| A6.3 | README, evaluation instructions, roadmap and actual behavior agree. Report visual/usability evidence separately from source checks, model observations and owner approval. Keep temporary runs, credentials, scans and machine state outside product source. |
| A6.4 | Handoff records branch/revision, changes, tests, meaningful limitations and the next authorized action. No automatic version bump, push/merge, publication, active install or production deployment follows from implementation acceptance. |

After separate delivery authorization, reuse the established exact-head CI, merge/tag binding, native security scan, actual downloaded-artifact verification and managed-local-update/backup workflow. Choose a release version then; do not promise a version or release date in this plan.

## Verification entrypoints and evidence maintenance

Use the smallest relevant checks per stage; run the combined affected suite before acceptance. Existing entrypoints to inspect/reuse:

- `python -B scripts/test_roadmap_policy.py` and `python -B scripts/validate_release.py` for tracker/policy and metadata consistency. The current roadmap validator chiefly covers historical WPS; R12-specific status coverage belongs in R12.1, not a weakened historical test.
- `python -B evals/wordpress-settings/test_contracts.py`, `node evals/wordpress-settings/test_model.cjs` and `node evals/wordpress-settings/test_conflict.cjs` for source/evidence boundaries and protected save behavior.
- The real-admin runner documented in `evals/fixtures/wordpress-settings/README.md`; select owned synthetic hosts and fresh external output before execution, preserving unrelated containers/data.
- `python -B scripts/test_behavior_evaluation.py` and `python -B scripts/validate_eval_result.py evals/ui-foundations/r12-result.json --suite ui-foundations --accept --release-binding evals/r12-release-version.json` for current saved acceptance. R12-specific inputs/criteria must be retained separately from evaluator inputs; evolve the existing harness only where needed.
- `python -B scripts/validate_resource_routes.py`, existing package tests/consumer verification and official Skill quick validation for affected source and actual extracted artifacts.

Keep raw briefs, reviewer criteria, actual outputs and execution records distinct. Existing exact source checks will intentionally fail after relevant changes until a truthful successor is supplied. Missing checks are not passes; a forward-compatible evidence mechanism must retain rejection of stale, missing, contradictory and tampered records.

## Official references to refresh during implementation

These are decision sources, not installed dependencies or a permanent compatibility guarantee:

- [WordPress components](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-components/) and [plugin-page integration](https://developer.wordpress.org/news/2024/03/how-to-use-wordpress-react-components-for-plugin-pages/).
- [DataViews and DataForm](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dataviews/), when a data-heavy surface warrants them.
- [Version-aware design-system selection](https://developer.wordpress.org/block-editor/contributors/design/design-system-packages/) and [theme/token boundaries](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/).
- [Settings API](https://developer.wordpress.org/plugins/settings/settings-api/) and [dependency extraction](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dependency-extraction-webpack-plugin/).

Refresh only selected components against the product's supported runtime. Preserve the settled native-settings convention unless new material evidence and an explicit scoped decision justify changing it.
