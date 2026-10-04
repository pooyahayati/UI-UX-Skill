# Dispatch Notes — benchmark design handbook

## Identity and governance

- Sample revision: r1
- Handbook revision: h1
- Updated: 2026-10-04. Single writer: current coding agent; benchmark acceptance remains with the repository maintainer, not an invented fictional stakeholder.
- Canonical sample-relative path: `DESIGN.md`. Lifecycle: `draft`. Last approved baseline: none. Direction selection, sample approval and broad rollout authority: none.
- This authored output demonstrates the candidate R3 contract. It is not a raw eval input, fresh independent model result, a new real product or approval evidence. Fictional `OWNER_NOTES.md` events are deliberately not applied.
- Engineering guidance: inspected current Vibe `1.3.1` and installed UI `3.1.1`; candidate handbook/sample contracts inspected in this repository at R3 merge `b069bd16e1170028fd987af804197d2d3732f752`. No candidate Skill was installed.

## Product and audience

Source: [raw brief](../../fixtures/sample-review/BRIEF.md) and its explicitly selected [bilingual variant](../../fixtures/sample-review/variants/bilingual.md). Primary route: browser `web-application`; no secondary route. Native HTML/CSS/JavaScript, no framework or backend. Existing roles: technician and coordinator. Only technician editing is exercised; coordinator authorization is not implemented or tested.

Approved hypothetical feature scope: assigned-visit list, visit details, draft/completion notes. Phone technicians must read the instruction, enter a note and understand its save/completion state; coordinators review notes on desktop. List, detail, note and result/recovery expose this job without inventing a login or analytics homepage. Excluded: billing, analytics, GPS, chat, AI, new roles, admin backend, persistence, deployment.

Active UI guidance: web-application and its navigation/state, workflows/data, interaction/access modules; shared navigation, forms, feedback, state/recovery, accessibility, responsive, hierarchy and low-motion contracts; semantic tokens, typography, color/themes, density/layout, component states and responsive variants. Other Product Packs were inspected only for initial whole-Skill compatibility, not activated. Persian copy used existing `persian-writing`; input/output safety used existing `security-and-hardening`. No agent or external design specialist was added.

## UX foundation and requirement coverage

| Brief requirement | Surface / state | Verification and actual limit |
| --- | --- | --- |
| Assigned visit and long next instruction | Same `VIS-204`, site, schedule and instructions in A/B | Visible desktop comparison; real Persian expansion; synthetic data |
| Read details, edit note, save draft | Detail and labeled note field | Taken browser actions: busy guard, failed save, exact note preservation and retry |
| Mark complete | Explicit finished-work checkbox, completion action and recorded note | Keyboard action, consequence/prerequisite feedback and literal recorded text; no server transition |
| Phone technicians | Single-pane list/detail below 760px, hash return path | Observed 390px and narrow 320px; actual phone OS/IME not tested |
| Both themes and supported languages | Orthogonal appearance/direction contexts | Both A/B × English/Persian × light/dark observed at desktop; focused high-risk mobile coverage, not every Cartesian state |

Notes remain in this tab across list/detail and review setting changes. Draft save and completion are in-memory simulations with no server request. Refresh clears them as disclosed. Only unsaved edits warn on leaving; there is no durable offline/sync promise. `loading`, `empty` and `access` are visibly labeled harness simulations, recovered by choosing Ready. Read-only presentation is not a security boundary.

## Preferences, references and assumptions

No real owner reference images, brand assets, research or taste preferences were supplied for this benchmark. Protected synthetic brief choices: balanced density, text labels on primary actions and unchanged product name. Professional recommendation is inferred from repeated visit work, not measured task-time uplift. The two directions propose foundation treatment; neither is selected.

## Languages, directions and formats

Default language is English/LTR. Persian/RTL is supported only because the bilingual input explicitly selects it; not because the conversation is Persian. Both use self-hosted Vazirmatn Regular/Bold `33.003`, copied unmodified from the existing Persian skill assets. The font name/version/license metadata and the matching [official license](https://github.com/rastikerdar/vazirmatn/blob/v33.003/OFL.txt) were inspected. [Bundled license](fonts/OFL.txt) retains the notice; see the hashes in [QA](QA.md).

Browser font resource inventory and local HTTP 200 requests corroborate the real font assets; Persian shaping/mixed identifiers were visually inspected. Exact per-glyph font attribution is not available from this browser bridge; CSS naming alone is not the evidence. Only weights 400/700 ship; fallback is `sans-serif`, not a claim of verified fallback equivalence.

Visit/unit IDs and preserved English brand use `<bdi dir="ltr" lang="en">`; entered note uses `dir="auto"`. The synthetic weekday/time is translated with the same Tuesday/09:30 meaning. No calendar, timezone, currency or real scheduling policy is inferred. Persian prose uses Persian digits; identifiers remain unchanged.

## Visual foundation, components and states

Executable authority: [styles.css](styles.css), with shared semantic canvas/surface/text/action/focus/status roles and orthogonal A/B plus light/dark resolution. The handbook does not duplicate editable token values.

- A: structured task boundaries, restrained teal action semantics, inline-start instruction/visit cues and lower-radius surfaces. Recommended for frequent scanning and entry.
- B: calmer notebook surfaces, navy action semantics, block-start visit cue, rounder surface/control hierarchy and subtle elevation. Tradeoff: weaker hard separation than A; grouping relies more on spacing. Same workflow, content, balanced density, real fonts, text action labels and functionality; not a different scope or an intentionally inferior sketch.
- Shared roles: body/labels, captions, headings and technical identifiers; limited spacing and radius scales. Controls have logical spacing, visible focus and practical touch targets. No ornamental animation or chart/diagram because the approved job requires neither.
- Icons: one trusted, local, decorative outline notebook glyph plus mirrored directional arrows. Critical actions keep text. No uploaded SVG, external icon dependency, picker or runtime icon registry exists yet.
- Native controls expose relevant enabled/read-only/disabled/busy/invalid/success states. Error feedback is persistent, live and near the note. Status meaning is text, not color alone.

## Decisions, samples and approval

| Decision | State / source | Scope |
| --- | --- | --- |
| Product features/roles; balanced density; primary labels | Supplied synthetic brief, not real product-owner approval | Both directions, r1/h1 |
| English default, explicit Persian support and both themes | Supplied bilingual variant | Both directions, r1/h1 |
| Vazirmatn, A/B treatment, native browser implementation | Proposed professional recommendation | Benchmark only; no rollout |
| Direction selection and final sample approval | Unresolved; no actor/date/evidence invented | Requires an explicit real decision identifying benchmark scope and r1/h1 |

Executable samples: [index.html](index.html), configurations in [sample.json](sample.json), [default-language board](compare.html) and [supported-Persian board](compare-fa.html). Both directions use the same implementation and equivalent ready-state records in both themes. Scaled desktop board frames are not mobile screenshots. Review method, capture-tool limitations and actual actions are recorded in [QA.md](QA.md).

Current sample/handbook identity is r1/h1. There is no selected baseline, accepted revision or approval carried from fictional notes. Selection would permit bounded refinement, not unseen pages, backend implementation or production release. Approval of this authored example as Skill source would not by itself approve a fictional customer's product. Later material changes must identify the affected decisions and preserve any actually accepted prior baseline.

## Configurability and protected boundaries

| Parameter | Classification / source | Implementation status |
| --- | --- | --- |
| Roles, features, action meaning, access policy | Locked by brief / future real product requirements | Protected; actual backend authorization absent |
| Direction A/B, review theme/language/state/failure | Code-only benchmark harness in `app.js` | Allowlisted URL/control values; not persisted or an admin feature |
| Palette, font scale, spacing, surfaces | Proposed code-only semantic tokens in `styles.css` | Centralized actual consumers; no owner-published configuration |
| Semantic icon family/assignment | Proposed code-only local source | No admin picker or owner configuration yet |

There is no admin surface in this raw product; do not invent one. The broader approved roadmap's bounded appearance panel and icon controls remain R5/R6 work. A theme switch proves neither runtime governance nor draft/publish/rollback. No user/tenant preferences, history, schema migration, import or permission claims are made.

## Open questions, acceptance and next handoff

- Maintainer: choose/delegate one identified benchmark direction for refinement, then explicitly accept an observed r1/h1 or revised scoped sample; user feedback and approval are pending.
- Engineering lead: retain R3 In progress and R4 gated. R3 instruction/source evidence and authored rendering do not establish independent model conformance.
- Actual evidence: [QA](QA.md). Untested: real persistence/auth/roles, native devices/IME, screen-reader sessions, forced-colors/reduced-motion OS modes, full zoom matrix and unbuilt screens. No accessibility conformance or business uplift claimed.
- Change history: h1 initial draft and r1 initial executable directions; no prior approved document was overwritten or migrated. Next permitted work is focused feedback/refinement and scoped acceptance, not broad product rollout.
