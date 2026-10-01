# WordPress Plugin Onboarding and Integrations

Use this local rule pack when the active product route includes `wordpress-plugin` and onboarding, setup, external integrations, account connection, API credentials, or license activation is materially in scope.

## First successful outcome

Onboarding should optimize for the first meaningful product outcome, not for completing every optional setting.

Classify setup steps as:

- required now;
- required before a specific feature;
- optional;
- advanced;
- can be deferred.

Do not force users through configuration that is irrelevant to the first successful use.

## Wizard vs normal page

Use a setup wizard when:

- the steps have meaningful dependency/order;
- first-run failure would otherwise be confusing;
- configuration spans distinct decisions;
- progress/resume materially helps.

Prefer a normal settings page when:

- steps are independent;
- setup is short;
- experienced admins need direct access;
- the plugin is primarily a small extension.

Do not create a wizard merely to look polished.

## Resume and skip behavior

For multi-step setup:

- preserve completed steps;
- allow safe resume;
- indicate required vs optional;
- allow skip when the feature can function without the step;
- provide a direct path to full settings after setup;
- avoid trapping returning users in the wizard.

If setup partially succeeds, show what remains.

## Environment readiness

Before asking for configuration that depends on the environment, surface relevant prerequisites.

Examples:

- required extension/service;
- permalink/config state;
- HTTPS;
- cron/background processing;
- writable path;
- REST connectivity;
- minimum plugin/theme dependency;
- account entitlement.

Do not ask the user to enter credentials for a feature that cannot work in the current environment.

## Integration state model

For each external integration, distinguish:

- not configured;
- credentials entered but unverified;
- connecting;
- connected;
- connected with warning;
- expired/unauthorized;
- rate-limited/unavailable;
- disconnected;
- misconfigured.

Connection status is not the same as configuration completeness.

## Connection testing

A Test Connection action should:

- describe what is tested;
- show pending state;
- prevent accidental duplicate tests when relevant;
- report a useful result;
- distinguish auth failure from network/service failure;
- provide recovery.

Do not convert every remote error into "Invalid API key."

## OAuth / external authorization

For external authorization flows:

- explain what the user is connecting;
- preserve return context after external redirect;
- handle cancellation;
- handle expired state/nonce;
- handle account mismatch;
- show authoritative connected identity when available.

Do not simulate authorization success before the callback/server confirms it.

## API credentials

When manual credentials are required:

- label each credential accurately;
- explain where to obtain it;
- separate identifier from secret;
- preserve safe values across failed validation;
- mask stored secrets;
- allow replacement/revocation.

Avoid asking users to paste multiple opaque values without contextual help.

## Feature gating

If an integration enables features:

- explain which features become available;
- distinguish unavailable from disabled;
- do not show enabled-looking controls that cannot work;
- link recovery/configuration from blocked features where useful.

## License / account onboarding

When a license/account is required:

- explain why it is required;
- distinguish product licensing from service/API connection;
- show connected account/license identity where appropriate;
- show activation scope;
- provide clear deactivate/switch behavior.

Do not mix commercial upsell messaging into error recovery for a valid existing license.

## Data sync onboarding

If setup initiates import/sync/indexing:

- explain expected scope;
- indicate background vs blocking work;
- provide job status;
- allow safe continuation when background work is supported;
- explain what is usable before completion;
- surface failure and retry.

Do not leave the user on a spinner for long server-side work that continues after navigation.

## Sample data

Offer sample/demo data only when it helps users learn the product.

Make it obvious that data is synthetic.

Provide a clean removal path.

Do not mix sample data with production content without clear labeling.

## Completion

Completion should communicate:

- what is configured;
- what remains optional;
- the first useful next action;
- where settings can be revisited.

Avoid celebratory completion screens that provide no path into the product.

## Accessibility and localization

Onboarding must support:

- keyboard use;
- visible focus;
- meaningful progress semantics;
- text scaling;
- clear validation;
- translated string expansion;
- RTL where supported.

For Persian-facing copy, route linguistic QA to `persian-writing`.

## Validation checklist

Test:

- fresh install;
- skipped optional step;
- failed prerequisite;
- invalid credential;
- external auth cancellation;
- successful connection;
- resumed partial setup;
- background sync still running;
- completion/next action;
- narrow `wp-admin`;
- RTL/LTR when supported.
