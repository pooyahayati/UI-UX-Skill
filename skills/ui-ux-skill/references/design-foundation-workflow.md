# Sequential Samples and Scoped Design Approval

Use after enough discovery exists for a new product or broad redesign, before broad UI rollout. Discovery belongs to [discovery-and-profile.md](discovery-and-profile.md); durable authority belongs to [design-handbook.md](design-handbook.md). This reference owns staged visual review, not software feature scope or runtime settings.

## Start from settled foundations and the product job

Read approved requirements, audiences/roles, the active Product Pack, current stack and `DESIGN.md`. Reuse settled palette/color roles, actual font and typography scale, spacing/density, surfaces, controls, icons and motion constraints. Link their authoritative sources; do not substitute a new style while illustrating them. Resolve only material missing or conflicting foundations with a professional recommendation and focused owner question before the affected sample. A novice need not invent design values.

Choose the smallest meaningful screens from the principal job: where users start, make a consequential choice and see the result/recovery. Explain the choice. Login, dashboards and analytics are not universal defaults. Choose the primary viewport from the product, audience and usage (for example, phone-first technician web app versus a desktop-heavy workspace), not from the conversation or a universal device size. Record target sizes and inspect responsive behavior at relevant narrow, intermediate and wide sizes.

A proposed screen is not permission to add a feature, role, integration or data model. Synthetic content permits early design without a full backend; label synthetic data, simulated actions and hypothetical capabilities. Do not copy private customer data or invent product metrics. Keep scope decisions separate from appearance feedback.

## Phase 1 — One primary design, feedback, approval

Present one coherent professional proposal, using the product's primary language, actual direction and primary theme (normally light; preserve an established different default). Explain why the settled foundations and hierarchy fit the audience/job, and a relevant tradeoff. Multiple competing directions are not mandatory; offer an alternative only for a material unresolved choice or an explicit request. Do not add Persian/English, RTL/LTR or theme variants just to fill a comparison board.

Use realistic copy/lengths and available actual fonts. Present a displayable artifact with a stable sample ID/revision, its matching handbook revision, and a usable inline/local/authorized viewing location. Text descriptions alone are not visual samples. Concept images may communicate atmosphere but cannot prove typography, responsive layout, focus or interactions. Prefer the current stack's bounded code-native/native executable preview; no mandatory framework, generator, cloud service or full backend.

Ask focused feedback on visible details; summarize corrections, revise the same proposal and retain unrelated accepted choices. Do not wait for every software feature. Before asking for sample acceptance, inspect an executable representative slice at product-relevant responsive sizes with applicable normal, loading, empty, error, success, disabled/access and recovery states. Record omissions with reasons. If rendering/assets are unavailable, retain pending acceptance, explain the gap and propose a permitted recovery; source/build success is not rendered proof.

Record actual scoped approval of the corrected primary revision and matching handbook baseline. Silence, an unsubmitted default, an upload, "interesting", implementation acceptance or a recommendation is not visual approval. Only then advance to the derived dark-mode review.

## Phase 2 — Derived dark mode, feedback, approval

After primary approval, derive dark treatment from that exact baseline. Preserve typography, spacing, structure, semantic icons and workflow; adapt semantic colors and relevant surfaces/states for dark readability rather than introducing another brand or layout. Show the same important job/content at appropriate responsive sizes, collect corrections, inspect affected contrast/focus/actions/recovery and obtain separate revision-scoped dark approval. Record the parent primary baseline and affected handbook decisions.

Identify dark-mode requirements during discovery, but do not require simultaneous first-phase light/dark artifacts. An already approved primary dark treatment need not be duplicated; record that existing authority and resolve any other required theme without replacing it. Preserve existing production themes and constraints; conflicts require a scoped decision, not silent removal. A theme switch in a sample is not an implemented admin appearance panel.

## Phase 3 — Secondary language/direction only when needed and authorized

After dark review is accepted, inspect the product's language needs and ask the owner to confirm whether a secondary language/layout is required and authorize its named scope. A declared possible locale alone is not permission to start its design ahead of the preceding phases. Reuse explicit existing authority only if it covers this stage and baseline; do not repeat settled questions. For a monolingual product, record this phase as not applicable with the product-language source; do not create extra layouts.

For authorized secondary languages, adapt the accepted system using real copy/fonts and each actual LTR/RTL direction. Test relevant long translations, mixed-script identifiers, forms and responsive states; do not blindly mirror all icons/charts or create a conflicting design system. Route required Persian content through `persian-writing`. Obtain scoped approval of the revised secondary sample, identifying its primary/dark parent baselines. Do not add further locales, calendar changes or localization features without product scope. This staged proposal workflow never deletes existing production locales.

## Evidence and revision boundary

Use a justified coverage matrix for the current phase, not an upfront Cartesian product of future themes/locales. Record planned later coverage separately from actually inspected contexts. In the final covered slice, ensure every required approved theme/authorized locale is represented and inspect high-risk combinations. Verify actions by taking them, not merely selecting mock state labels. Simulated failures do not prove backend behavior; visual denial does not authenticate permissions.

Record source/sample revision, actual font assets or environment resolution, viewing/run method, theme/language/viewport/state, observations, captures and limitations. A font name in CSS does not prove it loaded. Accessibility/device claims stay within actual checks. Use [qa-checklist.md](qa-checklist.md) and [visual-regression.md](visual-regression.md) as relevant.

Keep proposal/refinement, sample approval and engineering rollout authority separate. Before broad rollout, record actual approval/delegation evidence: revision, matching handbook baseline, actor/source/date (or explicit unknown), covered screens/choices and exclusions. Primary approval never approves unseen dark/localized samples; any phase approval never adds software features or authorizes release/deployment.

Preserve the last approved baseline when revisions change. Mark materially affected choices pending, link the new proposal and assess dependent dark/localized samples for re-review; do not silently transfer old approval. Unchanged accepted choices retain provenance. A compatible detail can remain within explicit delegated authority; a changed revision number alone neither invalidates every decision nor approves changed ones.

Write phase status, feedback/corrections, parent baselines and evidence in canonical `DESIGN.md`. Link bulky artifacts rather than creating a second approved handbook. Keep proposed runtime settings distinct from implemented controls.

## Handoff and Skill evaluation

Return the single recommendation and foundation sources; current phase/sample/handbook revisions; actual responsive/state evidence and limits; accepted versus proposed choices; skipped secondary scope/reason; and next required owner/engineering decision. Keep the main conversation concise and samples accessible.

A real product's gate closes only for the stated slice with visible executable evidence and real scoped approvals. A Skill maintainer accepting instructions or fictional evaluation notes is not a customer approving a product design. Evaluate whether the agent follows the sequential gates using raw scenarios and honest observations; never require the maintainer to choose the taste of an unrelated demonstration to continue Skill development. Authored examples and structural tests are not independent model conformance.
