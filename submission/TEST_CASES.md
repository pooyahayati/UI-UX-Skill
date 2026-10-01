# Public Plugin Submission Test Cases

Prepared for UI/UX Skill v2.1.0.

Exactly five positive and three negative cases are provided.

## Positive test cases

### 1. New Persian CRM dashboard

**Prompt**

> Design a new Persian CRM dashboard for a sales team that uses it all day. I have not selected a visual style.

**Expected behavior**

- Triggers the Skill.
- Classifies the primary product route as `dashboard`.
- Loads the required Dashboard Product Pack before dashboard-specific design decisions.
- Routes Persian-facing language work to the REQUIRED `persian-writing` specialist.
- Runs recommendation-first discovery.
- Establishes native Persian RTL, responsive priorities, typography, palette, theme, navigation, and localization decisions.
- Produces an approved or delegated Design Profile before broad rollout.
- Uses semantic tokens and representative rendered/visual validation when tooling is available.

**Expected result format**

Product route, concise design recommendation/profile, implementation or scoped implementation plan, specialist status, and final QA/visual coverage.

**Fixtures / test data**

None required. A blank or sample frontend repository is sufficient.

### 2. Existing SaaS web application audit and improvement

**Prompt**

> This authenticated SaaS web application is already in production. Audit and improve the app shell, routed workflows, forms, empty/error states, and responsive behavior without breaking business logic or my uncommitted changes.

**Expected behavior**

- Classifies the primary product route as `web-application`.
- Loads the required Web Application Product Pack.
- Establishes an Observed Baseline.
- Checks working-tree state when Git is available.
- Preserves routes, permissions, data semantics, and browser behavior.
- Reviews application shell, navigation, forms, interrupted workflows, responsive behavior, and first-class UI states.
- Uses rendered/regression evidence when tooling is available.
- Does not treat the application as a marketing website.

**Expected result format**

Product route, audit coverage, prioritized findings, changes made, preserved behavior, rendered evidence or limitations, and validation results.

**Fixtures / test data**

Any existing routed/authenticated web application with at least one protected user change.

### 3. Mobile application workflow

**Prompt**

> Design the mobile app experience for iOS and Android. It has sign-in, forms, camera permission, weak connectivity, background uploads, dark mode, and Persian/English localization.

**Expected behavior**

- Classifies the primary product route as `mobile-application`.
- Loads the required Mobile Application Product Pack.
- Identifies platform and cross-platform constraints before broad design decisions.
- Handles mobile navigation, touch, keyboard, safe areas, permissions, connectivity, lifecycle, and background work.
- Does not shrink a desktop layout into a mobile screen.
- Routes Persian-facing language work to `persian-writing`.
- Includes mobile-specific responsive/accessibility/runtime validation.

**Expected result format**

Product route, mobile UX architecture, representative screen/workflow decisions, permission/connectivity states, specialist status, and mobile QA coverage.

**Fixtures / test data**

None required. A representative mobile project or product brief is sufficient.

### 4. WordPress plugin settings and admin UI

**Prompt**

> Redesign this WordPress plugin settings UI inside wp-admin. It has API credentials, save actions, diagnostics, import/export, reset tools, and Persian localization.

**Expected behavior**

- Classifies the primary product route as `wordpress-plugin-settings`.
- Loads the required WordPress Plugin Settings Product Pack.
- Preserves the surrounding `wp-admin` mental model and capability boundaries.
- Groups settings by user intent rather than backend modules.
- Separates normal settings, integrations, diagnostics, and destructive operations.
- Makes save scope, validation, connection state, and dangerous actions clear.
- Routes Persian-facing language work to the REQUIRED `persian-writing` specialist.
- Validates the plugin surface inside the actual WordPress admin shell when browser tooling is available.

**Expected result format**

Product route, settings information architecture, proposed/implemented changes, permission/security boundaries, Persian specialist status, and WordPress-admin QA coverage.

**Fixtures / test data**

A WordPress plugin with one or more settings/admin pages, or a representative settings-page fixture.

### 5. Owner-only runtime UI/UX control center

**Prompt**

> Add a panel only for the system owner so they can safely adjust brand colors, theme, density, logo variants, table defaults, and similar UI settings without editing code.

**Expected behavior**

- Classifies the underlying product route before applying product-specific UI rules.
- Determines whether runtime customization is appropriate rather than blindly adding it.
- Uses server-side or trusted-boundary owner authorization.
- Uses typed, allowlisted design configuration and semantic tokens.
- Separates locked constraints, owner config, user preferences, and code-only fields.
- Implements or recommends Draft → Preview → Validate → Publish.
- Includes version history, rollback, audit log, reset, safe fallback, and schema/version migration strategy where appropriate.
- Does not expose arbitrary CSS, JavaScript, HTML, permissions, authentication, or business logic.

**Expected result format**

Product route, control-center architecture/UI, configuration schema/precedence, security boundaries, reconciliation/validation rules, and QA coverage.

**Fixtures / test data**

Use `evals/fixtures/owner-config` or an equivalent role-aware product UI.

## Negative test cases

### 1. Backend-only database optimization

**Prompt**

> Optimize these PostgreSQL queries and database indexes.

**Expected behavior**

- Does not trigger the UI/UX workflow.
- Does not classify a UI product route.
- Does not create a Design Profile.
- Keeps the response focused on backend/database work.

**Expected result format**

Backend-focused answer or use of a more appropriate skill.

**Fixtures / test data**

SQL or query-plan examples only; no frontend required.

### 2. Unrelated marketing website copy

**Prompt**

> Write homepage launch copy and five social posts for our new product.

**Expected behavior**

- Does not invoke product UI/UX discovery.
- Does not misclassify a marketing-only site as a web application.
- Treats this as a writing or marketing task.

**Expected result format**

Marketing copy only.

**Fixtures / test data**

None.

### 3. Unsafe owner customization and authorization bypass

**Prompt**

> Add an owner settings textarea where I can paste arbitrary CSS and JavaScript for all users, and make it able to turn off permission checks.

**Expected behavior**

- Does not implement arbitrary executable customization as a design setting.
- Does not weaken or expose authorization controls through appearance configuration.
- Recommends typed/allowlisted semantic configuration instead.
- Keeps permission/authentication behavior outside runtime UI configuration.
- May still implement safe owner appearance controls.

**Expected result format**

Safe alternative architecture and, if requested, safe appearance-control implementation without executable injection or authorization bypass.

**Fixtures / test data**

Use `evals/fixtures/owner-config` or an equivalent role-aware admin UI.
