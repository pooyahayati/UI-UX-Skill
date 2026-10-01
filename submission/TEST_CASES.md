# Public Plugin Submission Test Cases

Prepared for UI/UX Skill v1.4.0.

Exactly five positive and three negative cases are provided.

## Positive test cases

### 1. New Persian CRM dashboard

**Prompt**

> Design a new Persian CRM dashboard for a sales team that uses it all day. I have not selected a visual style.

**Expected behavior**

- Triggers the Skill.
- Inspects available project evidence first.
- Runs recommendation-first discovery.
- Establishes native Persian RTL, responsive priorities, typography, palette, theme, navigation, and localization decisions.
- Produces an approved or delegated Design Profile before broad rollout.
- Uses semantic tokens and reusable component architecture.
- Uses representative rendered/visual validation for broad rollout when tooling is available.

**Expected result format**

A concise design recommendation/profile followed by implementation or a scoped implementation plan, plus final QA/visual coverage.

**Fixtures / test data**

None required. A blank or sample frontend repository is sufficient.

### 2. Existing live dashboard audit and improvement

**Prompt**

> This dashboard is already in production. Audit and improve the UI/UX without breaking business logic or my current uncommitted changes. Validate broad visual changes with before/after evidence.

**Expected behavior**

- Establishes an Observed Baseline.
- Checks working-tree state when Git is available.
- Reports audit coverage.
- Prioritizes findings by severity, impact, scope, confidence, and fix type.
- Distinguishes measured/observed/user-provided/inferred evidence.
- Reviews hard-coded presentation and design-system changeability.
- Implements safe improvements while preserving functional contracts.
- Uses representative visual-regression evidence when capture tooling is available.
- Does not claim visual validation when rendered capture is unavailable.

**Expected result format**

Audit coverage, prioritized evidence-based findings, changes made, preserved behavior, before/after visual evidence or stated limitations, validation results, and remaining risks.

**Fixtures / test data**

Use `evals/fixtures/existing-dashboard` or an equivalent existing frontend with at least one protected user change.

### 3. Owner-only runtime UI/UX control center

**Prompt**

> Add a panel only for the system owner so they can safely adjust brand colors, theme, density, logo variants, table defaults, and similar UI settings without editing code.

**Expected behavior**

- Determines whether runtime customization is appropriate rather than blindly adding it.
- Uses server-side or trusted-boundary owner authorization.
- Uses typed, allowlisted design configuration and semantic tokens.
- Separates locked constraints, owner config, user preferences, and code-only fields.
- Implements or recommends Draft → Preview → Validate → Publish.
- Includes version history, rollback, audit log, reset, safe fallback, and schema/version migration strategy where appropriate.
- Defines preference reconciliation when owner constraints invalidate user settings.
- Does not expose arbitrary CSS, JavaScript, HTML, permissions, authentication, or business logic.

**Expected result format**

Architecture and UI implementation for the control center, configuration schema/precedence, security boundaries, reconciliation/validation rules, and QA coverage.

**Fixtures / test data**

Use `evals/fixtures/owner-config` or an equivalent role-aware dashboard.

### 4. Persian RTL table with technical LTR content

**Prompt**

> Improve this Persian admin table. It contains emails, domains, versions, IDs, dates, currency, sorting, filters, pagination, and mobile overflow.

**Expected behavior**

- Uses native RTL structure.
- Isolates technical LTR strings.
- Reviews logical CSS, sticky columns, pagination, sorting, mobile behavior, and localization formatting.
- Does not blindly mirror analytical or directional semantics.
- Includes accessibility checks.
- Considers Saved Views/column preferences when repeated use justifies them.

**Expected result format**

Targeted findings and implementation changes with RTL/LTR, personalization, and mobile QA notes.

**Fixtures / test data**

Use `evals/fixtures/rtl-table` or an equivalent mixed-direction table.

### 5. Personalized operational analytics and Data Trust UX

**Prompt**

> Improve this operational analytics dashboard for frequent users. Add useful saved views and preferences, and make data freshness, timezone, filters, stale/partial data, and KPI definitions clear.

**Expected behavior**

- Separates owner defaults from user preferences.
- Allows only appropriate preferences.
- Defines preference persistence, reset, reconciliation, migration, and safe fallback.
- Clarifies data freshness, last-updated time, timezone, filter scope, stale/partial/sync-failure states, and metric definitions.
- Preserves role and authorization boundaries.
- Uses evidence/metrics to describe how the change should be validated.
- Reviews responsive, accessibility, and performance implications.

**Expected result format**

Implemented personalization/Data Trust improvements, configuration precedence, validation/evidence plan, role/permission notes, and QA coverage.

**Fixtures / test data**

Use `evals/fixtures/analytics-dashboard` or an equivalent dashboard with KPI/filter/freshness states.

## Negative test cases

### 1. Backend-only database optimization

**Prompt**

> Optimize these PostgreSQL queries and database indexes.

**Expected behavior**

- Does not trigger the dashboard UI/UX workflow.
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

- Does not invoke dashboard UI/UX discovery.
- Does not propose dashboard redesign.
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
