# Preference Reconciliation

Use this reference when owner configuration, user preferences, saved views, or schema changes can invalidate previously stored settings.

The product should preserve valid user intent without preserving invalid state forever.

## Resolution order

Resolve in this order:

1. locked product constraints
2. current design-system defaults
3. current published owner configuration
4. current allowed user preference schema
5. stored user preference
6. safe fallback

A stored preference is not automatically valid merely because it was valid previously.

## Reconciliation policy

For each stored preference:

### Preserve

Keep the value when:
- the field still exists
- the value remains allowed
- the user is still permitted to control it
- dependent resources still exist

### Migrate

Map the value when there is a defined migration.

Examples:

- renamed density preset
- renamed column key
- moved saved-view filter field
- theme enum change

Migrations should be explicit and versioned.

### Drop and fallback

Discard the stored value and use the current allowed default when:

- the option was removed
- the field became locked
- the asset no longer exists
- the user lost permission
- no safe migration exists

Do not let an invalid preference break the page.

### Inform when material

Notify the user only when the reconciliation materially changes their workflow, such as:

- a saved view lost a required column/filter
- a shared view is no longer accessible
- a preferred landing page was removed

Avoid noisy notices for harmless internal migrations.

## Saved views

Treat saved views as versioned structured data.

A saved view may reference:

- filters
- sort
- grouping
- columns
- date range
- density
- search scope

When the underlying schema changes:

- preserve valid fields
- migrate known renamed fields
- remove invalid fields
- mark the view partially migrated when meaning changed
- require review before republishing a shared/owner view if critical semantics changed

Do not silently reinterpret a filter into a different business meaning.

## Owner constraint changes

Example:

Owner previously allows:

```text
density = compact | balanced | comfortable
```

User chose:

```text
comfortable
```

Owner later allows only:

```text
compact | balanced
```

Resolution:

- user's stored value becomes invalid
- use owner/default fallback
- retain old raw value only if needed for migration/audit, not active rendering
- optionally notify user if the change is noticeable

## Permission changes

If a user loses access to a field/entity:

- remove it from active saved views
- do not reveal hidden values through old saved-view metadata
- prevent shared views from bypassing row/field permissions

Authorization is evaluated at use time, not only when the view was created.

## Multi-device and conflict behavior

If preferences synchronize across devices, define conflict behavior.

Prefer deterministic rules such as:

- server timestamp/version
- explicit merge for independent fields
- last-write-wins only for low-risk personal preferences

Do not use last-write-wins for security or shared-governance decisions.

## Reset

Support:

- reset one preference
- reset a saved view
- reset all personal presentation preferences

Reset should re-resolve against current owner/default configuration.

## QA scenarios

Test:

- removed enum option
- renamed field
- removed table column
- user loses permission
- owner disables user control
- old schema version
- corrupted stored preference
- shared view with invalid filter
- concurrent updates
- rollback of owner config
