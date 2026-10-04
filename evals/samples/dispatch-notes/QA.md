# Dispatch Notes r1 / h1 — actual review record

Reviewed 2026-10-04 by the current coding agent using the Codex in-app browser against an isolated loopback preview. This is source-author-managed rendered/functional evidence, **not fresh independent model conformance, research with technicians or owner approval**. Sample revision: r1. Handbook revision: h1. Selection/approval: pending.

## Rendered coverage

| Context | Observed method / artifact | Scope |
| --- | --- | --- |
| A/B × English/Persian × light/dark, ready desktop | Eight initial captures at requested 1280×1000 viewport; accessibility snapshots; native four-panel boards in both languages | Top-level RTL full-page capture is clipped/offset by the tool and is not trustworthy whole-page evidence; boards show the actual RTL iframe layout. Not every state in every combination |
| A, Persian, dark, mobile 390×844 | Ready and actual failed-save captures, taken edit/save/retry and navigation actions | High-risk long RTL recovery; horizontal page overflow absent |
| B, English, light, mobile 390×844 | Actual keyboard completion/literal-markup result and refreshed ready view | Different direction/language; tab-only reset observed, no persistence claim |
| B, Persian, light, 320×900 | Full-page capture and actual DOM overflow assertion | Long-copy narrow reflow without horizontal page overflow; not a 200% browser-zoom test |
| B, Persian, light/dark, intermediate 768×1000 | Capture, DOM overflow assertion and keyboard-focus screenshot | Two panes still fit; Tab from note reaches visible save focus |
| Four semantic A/B × theme palettes | Read actual rendered custom-property values and calculate seven relevant text pair contrasts per context | Minimum observed sampled text ratio 5.56:1; no full accessibility conformance claim |

Each comparison board renders four identical ready-state desktop iframe viewports at 1280×1400, then scales them uniformly for side-by-side inspection. English remains default; the separate Persian board reviews the supported language. Thumbnails do not provide mobile, full-size readability or workflow evidence by themselves. The top-level RTL full-page screenshot tool shifted content and clipped the right edge despite DOM bounds inside the viewport. Those initial captures are retained as capture failures, not a visual pass. Native viewport/action observations and the actual iframe boards are separate evidence; no image pixels were edited to disguise this limitation. A requested taller top-level override still reported 1000px actual height, so no taller top-level validation is claimed.

## Actual functional observations

Twenty-eight direct browser/DOM assertions passed across the exercised path, with no model benchmark involved:

- Saving becomes busy and blocks duplicate activation, then simulated failure preserves the **exact** entered Persian note and restores retry. Failure is not mislabeled as invalid input. Retry produces explicit tab-only simulated draft success.
- Read-only simulation blocks save; Ready restores it and the previous truthful save feedback. Loading and empty remain distinct and visible even on a mobile visit deep link.
- Actual list/detail navigation preserves the tab draft. Theme/language/direction changes preserve user-entered text, rather than substituting seed translations.
- Blank/whitespace notes are rejected with an associated invalid state. Completion requires explicit finished-work confirmation.
- Space on the native checkbox and Enter on completion produce a simulated recorded note, disable editing and return meaningful focus. Entered `<img ...>` text remains literal; no image node is created in the result.
- Reload clears simulated completion/notes and returns the seed, matching the visible disclosure. 320px and 768px RTL views have no horizontal page overflow. Tab from note reaches Save with visible focus.
- Seven sampled semantic text pairs in each of four rendered palettes exceed 4.5:1. This does not cover every hover/focus/control boundary or forced-color state.

Two defects found during implementation were corrected **before these checks/captures**: temporary read-only feedback no longer overwrites the previous saved feedback; loading/empty cannot hide both mobile panes when the hash points to the detail. Regression observations exercised both cases. Current rendered/action inputs are bound by the external source manifest; later source changes require relevant rechecks.

## Real font evidence and limits

- Copied unmodified existing Vazirmatn Regular/Bold TTF assets. Name metadata identifies version 33.003 and SIL OFL 1.1. Included the copyright/license from the [official matching font release](https://github.com/rastikerdar/vazirmatn/blob/v33.003/OFL.txt).
- Regular SHA256: `b69fd4c680b8f3f225feabcc655a2c585d97627b8f5f5c0f9985e894069f3a56`.
- Bold SHA256: `f635fdbea28f265de395ba83b4b1570dcf2f58d13c65469e61903b1c2d2ae723`.
- Local server recorded HTTP 200 for both actual font requests. Browser observed-resource inventory lists both font files; visible Persian joining, real 400/700 hierarchy and mixed `VIS-204` / `HVAC-A2` were inspected. There are no external font services.
- The read-only browser bridge does not expose usable FontFace/per-glyph attribution. Its `document.fonts` view returned an empty inventory despite the observed real font resources, so that view is **not** treated as font-resolution proof. Asset re-bundling also failed because the preview blocks fetch with `connect-src 'none'`; this is not relabeled a successful download. Original font bytes and HTTP/resource evidence remain available.
- The development server's implicit `favicon.ico` request returned 404; no favicon/identity redesign was in scope. No relevant script error appeared in the inspected browser log.

## Retained artifacts and repeatability

Source lives in this directory and can be rerun using [README](README.md). Captures and generated check/palette/source manifests remain outside source control at the local operations path `../.roadmap-ops/r3-rendered/` relative to repository root:

- `comparison-r1.jpg` — actual four-panel English comparison board.
- `comparison-fa-r1.jpg` — actual four-panel supported-Persian comparison board.
- `comparison-fa-final-r1.jpg` — visually inspected successful native whole-board recapture from final normalized source after the recovery described below; use this for handoff.
- `{a,b}-{en,fa}-{light,dark}-desktop-r1.jpg` — eight initial desktop captures; top-level RTL full-page versions have the disclosed capture clipping limitation.
- `b-fa-dark-desktop-viewport-r1.jpg`, `b-fa-dark-desktop-full-v2-r1.jpg` — native viewport versus repeated failed full-page capture, not a corrected full-page result.
- `a-fa-dark-mobile-ready-r1.jpg`, `a-fa-dark-mobile-error-r1.jpg`.
- `b-en-light-mobile-ready-r1.jpg`, `b-en-light-mobile-completed-r1.jpg`.
- `b-fa-light-narrow-r1.jpg`, `b-fa-light-intermediate-r1.jpg`.
- `observed-checks.json`, `palette-evidence.json`, `source-manifest.json` — actual assertions, observed values and input identity, not product approval receipts.

These host-local evidence artifacts are not bundled with the distributable Skill. Missing copies on another host remain unavailable; reproduce rather than infer from a filename. The static CI sample tests cover local asset/link integrity, revision identity and raw-input separation only. They do not replay browser actions.

Initial final-recapture attempts reported unavailable. After resetting the temporary viewport, a fresh native viewport observation showed the page again. A subsequent native full-page capture was visibly inspected before being saved under the new `comparison-fa-final-r1.jpg` name. The saved JPEG was independently parsed at 1264×1791 with nonconstant image channels; a local image-viewer display anomaly is not relabeled an empty file. This recovered board matches final normalized source; the top-level RTL capture limitation remains. The retained English board predates its added Persian-review link while its product frames are unchanged. The source manifest records that chronology, not an uninterrupted capture success. Temporary viewport overrides were reset at handoff.

## Source checks and input-safety review

Twenty local regression/integrity tests and eight repository validators passed. JavaScript syntax passed. The Persian linter on the entire JavaScript file produced 30 findings about code quotation/ASCII syntax; it was not applied as a code formatter. Checking only the extracted Persian string copy through stdin returned zero findings. The first asset test incorrectly treated virtual `#list`/`#visit` routes as scroll anchors; the test now distinguishes declared entry-page hash routes while still checking real anchors, local paths and font bytes.

Security review was limited to this local harness: query/control enums are allowlisted, notes are bounded and rendered via text nodes, actual injected markup stayed literal, duplicate saves are blocked, and the HTML meta policy disallows external resources and connections. There is no package dependency installation, account, personal data, server API, upload or admin permission boundary here. Meta CSP and loopback serving are not a production security-header/authentication review or certification. Never enter private notes into the sample.

## Unperformed checks and remaining gate

No real backend save, authentication, coordinator role, authorization, durable/offline storage, native phone/IME, screen-reader session, full zoom matrix, OS forced-colors/reduced-motion test, user usability study, field performance measurement or admin appearance governance was performed. Reduced-motion/forced-color source handling exists but is not OS-rendered validation. No accessibility certification, task-time improvement, deploy/release or installed-candidate behavior is claimed.

Both directions remain proposals. The maintainer must explicitly select/delegate a **benchmark** direction for focused refinement and then provide revision-specific scoped acceptance if this example is the chosen R3 gate. That cannot approve a fictional customer's production product or unseen screens. R3 remains In progress; R4 is not started.
