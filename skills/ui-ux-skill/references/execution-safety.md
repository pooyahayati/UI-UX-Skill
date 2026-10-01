# Execution Safety for Existing Projects

Use this reference before modifying an existing codebase.

## Working tree

If Git is available:

- inspect `git status --short` before changing files
- inspect relevant diffs before overwriting a file with existing modifications
- treat user-authored uncommitted work as protected
- do not use `git reset --hard`, destructive checkout, or `git clean -fd`
- do not revert unrelated edits
- do not mass-format unrelated files
- keep changes in reviewable batches

If Git is unavailable, inspect current file content and keep the same conservative behavior.

## Scope

Do not expand a UI task into unrelated architecture or backend work.

Avoid:
- unrelated dependency upgrades
- package-manager lockfile churn without cause
- broad naming refactors
- mass component rewrites when a local change works
- changing API contracts for visual convenience

## Functional contracts

Preserve unless explicitly authorized:

- authentication and authorization
- role visibility
- validation semantics
- data meaning
- routes and deep links
- saved preferences
- destructive-action semantics
- localization behavior
- API payload/response assumptions

## Production data and privacy

Prefer local, development, staging, fixtures, or anonymized data for UI inspection.

Do not:
- commit credentials, tokens, cookies, or secrets
- copy customer data into examples, screenshots, issues, or generated artifacts unnecessarily
- expose PII in public audit reports
- publish private repository content as evidence

Redact sensitive content from screenshots/reports when practical.

## Dependency and asset safety

Before adding a dependency, font, icon pack, image, or other third-party asset:

- confirm it is necessary
- prefer existing project assets
- verify license and redistribution suitability when it will be committed or shipped
- avoid unknown binaries or scripts
- avoid remote fonts when local/self-hosted assets are required

## High-risk changes

Treat these as strategic even when visually motivated:

- framework migration
- component-library replacement
- auth flow restructuring
- permission UI semantics
- destructive-action redesign
- major navigation changes
- actual brand identity replacement

Follow the user's autonomy mode and surface material tradeoffs.

## Completion

Report:
- files and surfaces changed
- important behavior preserved
- tests/checks run
- checks not run
- remaining risks


## Runtime configuration changes

When adding or changing owner/user configuration:

- inspect existing authorization and tenancy boundaries first
- do not store permission/security decisions in appearance configuration
- version configuration schemas
- provide migration/default behavior before removing or renaming fields
- preserve existing user preferences when compatible
- avoid destructive config rewrites without backup/version history
- test rollback/fallback before production rollout
- do not introduce arbitrary executable CSS/JavaScript/HTML as a shortcut for configurability

Treat configuration migration as production data migration when persisted records already exist.
