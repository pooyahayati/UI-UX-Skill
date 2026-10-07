# Runtime appearance fixture

R6 scoped acceptance is recorded in the
[roadmap](../../../ROADMAP.md#r6-delivery-acceptance--2026-10-05). Its fixture
evidence does not close R7/R8, original typography/native-confirmation gaps or
production integration. Candidate source acceptance and passing merge are
separate checks; no new release or installed package is implied.

Synthetic web application, not a production theme builder or authentication system.
Primary review: English, LTR, light. The owner delegated practical fixture choices;
this is not customer approval of a real product. R7 owns integrated dark/localized QA.

## Contract and threat boundary

Use Python stdlib/SQLite and native HTML/CSS/JavaScript. No installed dependency.
`DESIGN.md` records intent; the server catalog owns prepared defaults and bounds;
SQLite outside the repository owns complete published snapshots and private drafts.
Consumers use resolved tokens, including an independent SVG chart/diagram adapter.

The loopback-only harness creates random sessions for **server-selected synthetic
principals**: owner-a, owner-a-peer, owner-b, viewer-a. No principal/role/tenant request
field can grant authority. A random one-use access link establishes an HttpOnly,
SameSite=Strict, Secure cookie. Writes also require same-origin and session-bound
CSRF checks; Host is restricted. This is a local test harness, not production login,
TLS, account provisioning, rate-limited authentication, or security certification.
Never expose it to a network or use real customer data. Local HTTP secure-cookie
behavior must be verified in the chosen browser; do not weaken the cookie for it.

Assets: two available generic font stacks and prepared palettes/variants only.
No font uploads, arbitrary colors/code/URLs, imports or exports. OS glyph identity
is not proved by a font-family declaration. R6 extends the catalog with prepared
outline/solid icons, visible family/per-use choices and a central fixed SVG adapter.
Original artwork and family capabilities are in `scripts/runtime_icons.py`, not
owner-authored vector code or an installed library. The solid settings badge is
deliberately unavailable and resolves a meaningful outline fallback with visible
provenance. Accessible action labels and disclosure state pairs remain separate
from artwork; only back/closed-disclosure semantics are direction-mirrored.

### Observable lifecycle

- Each owner has a private saved draft and base published revision. Preview is
  explicitly private and never changes the public reader or other owner's draft.
- Saving a complete schema-3 draft is explicit. Validation errors preserve stored
  draft/published/history state. Saving over a changed draft requires its revision.
- Complete valid schema-1/2 stored snapshots/drafts normalize on read into schema 3,
  preserving every prior appearance value and original historical bytes. Missing,
  extra or invalid old fields are not silently repaired. New requests must supply
  the current complete schema; stale legacy clients need to reload the catalog.
  Rollback copies a valid normalized old snapshot into a new version. No startup
  write-back or silent reset occurs.
- Schema 3 adds baseline/material owned-surface treatment and inherit/serif heading
  role. Defaults preserve the old baseline/body font. Material-derived container,
  field, disclosure, diagram and overlay roles keep existing palette/size/spacing/
  shape/variant settings. Compact Material controls remain at least 48 CSS px;
  baseline compact controls retain 44 px. This custom prepared adapter does not
  certify M3/library conformity. Original icons remain independently configurable;
  Material Symbols is not installed. [R9.5 evidence](../../material/R9_5_RUNTIME.md)
  records actual coverage; R9.6 full mode readiness is separate.
- Size/color controls affect declared consumers while primary foreground/target
  floors remain locked. Solid stroke editing is disabled; the retained outline
  width is dormant and an outline fallback uses its prepared width. Icon-only
  defaults affect local icon choices only and require normal preview/save/publish.
- Publish consumes the exact saved draft revision and base active revision in one
  transaction. A stale base returns 409; it never overwrites another publication.
- Reload server state preserves current draft inputs, including unsaved changes,
  and their original base. A moved base or saved-draft revision disables ordinary
  save/publication and offers **Review and reconcile changes**. This reads the
  latest published snapshot and the owner's saved draft without writing either.
  The dialog shows published/input differences and saved-draft differences; every
  published/input difference requires an explicit keep-current or use-input choice.
  It does not infer intent from an unavailable historical base. Unchanged fields
  retain current values. **Save reviewed private draft** compares both observed
  revisions, saves privately, and still requires separate publication. Cancel
  keeps saved/local state. A new conflict or unknown write outcome preserves
  inputs and requires a refreshed comparison before another recovery save.
- Rollback preserves saved and unsaved draft inputs and uses the same recovery
  path. Discard/reset remain deliberate alternatives, not prerequisites for
  recovery. Full browser navigation can still lose unsaved inputs after its
  existing unload warning; this fixture does not add offline draft storage.
- Publication/rollback is not safe to blindly retry after a lost response: refresh
  active/history first. Rollback appends a new validated snapshot; history survives.
- Reset produces a private defaults draft, not a publication. Discard removes only
  the actor's draft. All actions enforce tenant/actor ownership server-side.
- History exposes validated snapshots and changed setting names against the
  preceding version. A corrupt baseline reports unavailable differences rather
  than inventing a comparison. Rejected authenticated-owner inputs add a bounded
  validation-failed audit event without retaining their raw values; appearance,
  drafts and version history remain unchanged.
- Published reads return one complete validated snapshot plus revision/provenance.
  Missing/invalid data falls back to latest valid history or defaults, never merges
  fragments or reads a private draft. Failed storage reads return safe defaults and
  an explicit degraded state; writes fail without a false success response.
- No cache hides the latest active snapshot; an already open reader refreshes
  explicitly. Values survive refreshing the browser and reopening the store.

### API shapes

All `/api/v1/tenants/{tenant}/...` responses are JSON. Errors have
`{"error":{"code":"...","message":"...","details":{...}}}` and appropriate
401/403/404/409/413/415/422/503 statuses. Unknown body fields and duplicate JSON keys
are rejected. Duplicate security/framing headers and absolute/malformed request
targets return structured 400 errors before a write. Request limit: 16 KiB;
content type: application/json; no CORS. History query fields are bounded and
blank/duplicate/unknown parameters are invalid. Persisted snapshots also use a
bounded strict decoder, so corruption cannot bypass the fallback contract.

| Resource | Method | Body / result |
| --- | --- | --- |
| `/published` | GET | `{revision, source, config, tokens}`; public, known tenant only |
| `/catalog` | GET | defaults and human control contracts; known tenant only |
| `/draft` | GET | authenticated owner only; private `{draftRevision, baseRevision, config}` or null |
| `/draft` | PUT | `{config, baseRevision, draftRevision}`; compare-and-save |
| `/draft` | DELETE | `{draftRevision}`; compare-and-discard |
| `/previews` | POST | `{config}`; validate/resolve only, no persistence |
| `/publications` | POST | `{draftRevision}`; consumes saved complete draft |
| `/resets` | POST | `{draftRevision, baseRevision}`; private defaults draft |
| `/rollbacks` | POST | `{revision, baseRevision}`; append prior valid config |
| `/history` | GET | owner only, `?limit=20&before=<revision>`; max 50, newest first |
| `/audit` | GET | owner only, bounded history of actions; no raw rejected input |

`GET /api/v1/session` returns only safe display scope, canEdit and CSRF token for
the existing random session, never its credential. An anonymous session returns
canEdit=false and no CSRF value. Untrusted actor/role/tenant body fields are invalid.

## Running

From a repository checkout, choose an explicit **external** empty state directory:

```sh
python scripts/runtime_appearance.py --state-dir /absolute/external/fixture-state --port 8772 --principal owner-a
```

The one-time browser link is written to `access.json` in that state directory; do
not commit/share it. Open that link locally, then use Design and Appearance. Reader
view is a separate route and always uses published values. Stop the server when
finished. Server binding is fixed to 127.0.0.1; non-loopback flags are not offered.
Tests use fresh temporary stores and actual HTTP boundaries, not production state.

### Recovery regression checks

Run `node scripts/test_runtime_recovery.mjs` for actual shipped handlers with a
modeled DOM/HTTP boundary and `python scripts/test_runtime_appearance.py` for
real persistence/HTTP checks. Both are wired into existing CI. Neither is a
substitute for the actual-browser acceptance below.

`node scripts/test_runtime_recovery_browser.mjs` runs the two-owner UI workflow
against a fresh loopback server and disposable database. It requires an already
available `playwright` module, Python and compatible Chromium browser; it never
installs/downloads them. Optional environment overrides: `PLAYWRIGHT_MODULE`
(module path), `PYTHON` (executable), `BROWSER_EXECUTABLE` (installed browser),
and `RECOVERY_ARTIFACT_DIR` (external screenshot directory). It uses isolated
browser contexts, retains no credentials in reports, and closes its browser/server
and removes only its own temporary store. This optional local browser runner is
not executed by CI and is not an additional shipped runtime dependency.

## Required acceptance and recorded limits

Denial must preserve protected state; draft privacy, full snapshot publish, stale
draft/base conflicts, immutable history/rollback/reset, restart, invalid/missing/
failed-load fallback, reader coherence and source-preserving no-code changes need
actual checks. Color, font, spacing and shape must visibly change representative
forms/tables, overlays/errors and SVG consumers through the real panel. Stage
acceptance requires those observations and lead review, not this list alone.

The [R5 executable checkpoint](../../../ROADMAP.md#r5-executable-checkpoint--2026-10-05)
records 17 actual test outcomes, representative rendered lifecycle evidence and
source-preserving changes. The required outcomes above describe the contract,
not a substitute for that evidence. The [subsequent scoped R5 acceptance](../../../ROADMAP.md#r5-delivery-acceptance--2026-10-05)
records final source/security/package checks and passing implementation CI; its
integration checkpoint remains separate. R6 icons, R7 integrated quality and R8 candidate evaluation are
not certified by this fixture. Synthetic search controls illustrate appearance,
not a production search implementation or actual customer approval.
