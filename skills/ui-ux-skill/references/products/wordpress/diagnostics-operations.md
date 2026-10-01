# WordPress Plugin Diagnostics and Operations

Use this local rule pack when the active product route includes `wordpress-plugin` and diagnostics, status, Site Health, logs, support information, background jobs, maintenance, repair, or destructive operational actions are materially in scope.

## Status vs diagnostics vs logs

Separate:

- current status;
- health checks;
- diagnostics;
- raw logs;
- maintenance tools.

Do not place all technical information in one "Debug" page.

Most administrators need an actionable summary before raw detail.

## Status model

For important subsystems, communicate:

- healthy/ready;
- warning/degraded;
- error/blocked;
- checking;
- stale/unknown;
- disabled/not configured.

Do not use green/red color alone.

Use labels and explanations.

## Site Health integration

When a plugin has environment checks that fit the WordPress Site Health model, prefer integration with Site Health rather than inventing a duplicate health dashboard.

A Site Health test should:

- explain what is checked;
- explain why it matters;
- give an actionable remediation when possible;
- avoid alarming language for low-impact issues;
- run asynchronously when the test is slow or remote.

Do not turn promotional recommendations into Site Health failures.

## Plugin-local diagnostics

A plugin-local diagnostics page is useful when the plugin needs domain-specific operational detail that would overwhelm Site Health.

Organize diagnostics by user-actionability:

- user can fix now;
- host/admin must fix;
- remote service issue;
- developer/support detail.

Avoid presenting stack traces or raw arrays as the primary interface.

## Support information

When support export/copy is useful:

- separate safe system information from secrets/personal data;
- clearly indicate what will be copied/exported;
- allow review/redaction when practical;
- include relevant plugin/version/environment identifiers;
- avoid including credentials.

Do not tell users to paste unrestricted logs containing secrets or personal data into public support channels.

## Logs

If logs are user-visible:

- provide time/context;
- distinguish severity;
- allow filtering/search when volume warrants;
- explain retention;
- offer download/copy when useful;
- redact secrets;
- avoid loading huge log files synchronously into the admin page.

Raw logs are evidence, not the main UX.

## Background jobs

For sync, indexing, import/export, generation, cache rebuild, migration, cleanup, or scheduled tasks, define:

- queued;
- scheduled;
- running;
- progress when measurable;
- waiting/retrying;
- completed;
- partially completed;
- failed;
- cancelled;
- stale/stuck.

Show what the job affects.

Do not equate a request being accepted with the job being complete.

## Job control

Expose controls only when the backend supports them safely:

- retry;
- cancel;
- resume;
- restart;
- clear failed item;
- inspect details.

Disable or hide impossible actions.

Protect against duplicate execution.

For destructive retries/rebuilds, explain side effects.

## Cron and scheduling

When WordPress scheduling affects a feature:

- communicate that the work is scheduled/backgrounded;
- distinguish "scheduled" from "executed";
- explain delays when they are expected;
- surface overdue/stuck behavior when it materially affects the product.

Do not expose implementation jargon such as hook names as the primary status label unless the audience is explicitly technical.

## Maintenance and repair

Maintenance tools may include:

- rebuild index;
- regenerate assets;
- clear plugin cache;
- resync;
- repair data;
- rerun migration;
- remove orphaned data.

For every maintenance action, define:

- scope;
- expected duration;
- user-visible effect;
- reversibility;
- concurrency constraints;
- safe retry behavior.

Do not place destructive maintenance beside harmless utilities without visual separation.

## Data deletion and uninstall cleanup

Distinguish:

- deleting plugin-generated cache;
- deleting synced/derived data;
- deleting configuration;
- deleting user/content data;
- uninstall cleanup.

Use precise language.

For destructive data deletion:

- explain scope;
- clarify whether backups/exports exist;
- require deliberate confirmation;
- do not imply data is deleted if the system only schedules deletion.

## Progress and long-running UI

Avoid indefinite spinners.

For long work:

- allow navigation away when safe;
- persist status;
- provide last update/time;
- show completion/failure on return;
- provide a recovery path.

If exact percentage is unavailable, use truthful stage/status rather than fake progress.

## Operational notices

Use global admin notices only when the issue is important beyond the plugin page.

Examples may include:

- plugin unusable due to missing required configuration;
- critical migration blocked;
- site-wide integration failure requiring administrator action.

Keep low-risk operational messages local to the plugin screen.

## Accessibility

Operational UI should support:

- non-color status labels;
- keyboard access;
- live status announcements where appropriate;
- readable logs/tables;
- zoom/reflow;
- meaningful focus after actions;
- accessible progress indicators.

## Validation checklist

Test:

- healthy state;
- warning;
- hard failure;
- slow async check;
- remote-service failure;
- stuck background job;
- retry/cancel when supported;
- maintenance action;
- destructive data cleanup;
- support-info export;
- large log volume;
- narrow `wp-admin`;
- RTL/LTR where supported.
