# Comparable Samples and Scoped Design Approval

Use after enough discovery exists for a new product or broad redesign, before broad UI rollout. Discovery and activation belong to [discovery-and-profile.md](discovery-and-profile.md); durable authority belongs to [design-handbook.md](design-handbook.md). This reference owns sample comparison, refinement and approval evidence, not software feature scope or runtime settings.

## Select the smallest meaningful slice

Read the approved product requirements, actual audiences/roles, active Product Pack, current stack and draft handbook. Choose a small set of screens from the most important audience job: where the user starts, makes a consequential choice and sees the result/recovery. Explain why these surfaces expose the design decisions. Login, dashboards and analytics are not universal sample defaults.

Reuse supplied flows and constraints. A proposal for an unbuilt screen is not permission to add a feature, role, integration or data model. Synthetic content permits early design without a full backend, but visibly label sample data and hypothetical capabilities. Never copy customer data into public samples or present fictional metrics/testimonials as product facts. Separate scope decisions from appearance feedback.

## Compare coherent directions

Usually show two or three directions; use fewer/more only with a proportionate reason (for example, one approved baseline for a narrow correction). A direction is a coherent product-fit combination of hierarchy, typography, density, surfaces, controls, icons and restrained motion, not a random collection of decorative variants. Give a primary professional recommendation, its audience/workflow rationale and an important tradeoff. Let a novice choose through visible differences rather than token jargon.

Keep the principal workflow, feature scope, text, data, state, viewport and level of fidelity comparable. Do not make the preferred option look better by giving it shorter copy, stronger metrics, extra capabilities or a polished prototype against a rough sketch. Where a layout genuinely changes the workflow, explain that difference as a UX proposal needing its own decision. Theme and language variants are coverage of a direction, not separate directions.

Use the default product language and realistic text lengths with available actual fonts from the first samples. Include light and dark treatment for each direction at a comparable surface/state. For other supported languages, show representative real text in their actual direction, including mixed-script identifiers and long translations where relevant. Do not infer localization from the conversation. Route Persian content through the existing `persian-writing` specialist; use the active product's relevant typography, theme, responsive and accessibility rules, not another product's conventions.

Concept images can help with atmosphere or direction selection. Label them conceptual: they do not prove font shaping, responsive layout, focus, motion or interaction. Prefer the existing product's code-native/native preview when those qualities matter. Do not impose a framework, image generator, cloud service or full backend just to make a sample. A missing licensed/font asset is an explicit gap with a proposed substitute, not silently verified typography.

Present actual displayable artifacts with stable direction IDs/revisions and usable locations (inline preview, local preview path, screenshot or authorized artifact link). Text descriptions alone are not visual directions. Show both themes; make other supported directions inspectable without burying them behind an unexplained toggle. Record the actual viewing method and coverage. A file/build existing is not evidence that anyone viewed it.

## Select, refine and prove

Ask a focused question about the visible alternatives and the specific tradeoff. Allow a custom preference or explicit delegation of this identified choice. Preserve the owner's choice rather than replacing it with the recommendation. An unsubmitted default selection, silence, an image upload, "interesting" or implementation acceptance is not direction selection or visual approval.

Selection authorizes refinement of that direction within scope, not broad rollout. Before final approval, produce an executable representative sample using the current stack (a bounded local/native preview with synthetic data is sufficient). Do not wait for all software features. Exercise the selected direction on desktop and mobile/relevant native sizes, in both themes and representative supported languages/directions. Include relevant normal, loading, empty, error, success, disabled/access and recovery behavior; omit truly inapplicable states with a reason, never pretend a visual denial authenticates permissions.

Use a justified coverage matrix rather than a blind Cartesian product. At minimum make each required theme and direction visible, inspect the highest-risk combinations (for example, long RTL form error on mobile dark mode), and inspect real fonts, overflow/truncation, mixed text, contrast/focus, action meaning and reachable recovery. Verify an interaction by taking the action, not only by switching a mock state label. A simulated failure is useful if explicitly labeled; it is not proof of a backend's behavior. Accessibility and device claims remain bounded to the checks actually performed.

Record source/sample revision, actual font assets, run/view method, theme/language/viewport/state, observations, captures/locations and unresolved limitations. Font names in CSS are not proof the font loaded. Passing lint/build or source inspection cannot substitute for rendered proof. Use [qa-checklist.md](qa-checklist.md) and [visual-regression.md](visual-regression.md) when relevant.

Ask for feedback tied to specific parts (for example, spacing in the task list or mobile recovery), summarize the chosen changes, revise deliberately and keep unrelated accepted decisions. Avoid endless preference interviews. When rendering is unavailable, return permitted concepts/source and the exact missing check; retain pending approval/rollout and a recovery action. Do not claim the sample passes or demand installing a browser/tool without authority.

## Approval and revision boundary

Keep three decisions separate:

| Decision | What it means | What it does not mean |
| --- | --- | --- |
| Direction selection / scoped delegation | Refine the named direction and identified choices | All product features or final visual approval |
| Sample approval | Accept the identified rendered sample and matching handbook baseline within stated scope | Unseen states/pages/themes/languages or backend permission checks |
| Broad rollout authorization | Implement approved design within the engineering lead's software scope and gates | Release/deployment or unapproved new capabilities |

Before broad rollout, record actual approval/delegation evidence identifying the sample revision, matching handbook revision, actor/source/date (or explicit unknown), covered screens/choices and exclusions. Reuse explicit prior authority when it truly covers this baseline; never manufacture a new approval question for an already settled unchanged decision. If feedback is ambiguous about which revision or scope, clarify that material boundary only. A project maintainer approving Skill source is not a fictional sample product's owner approving its design.

Preserve the last approved baseline when a later sample or handbook revision changes. Mark affected choices pending and link the proposed revision; do not silently transfer old approval to new palette, font, navigation or workflow. Unchanged accepted choices retain their provenance. A compatible local detail can stay within delegated authority, with rationale; a material change needs new scoped approval. A changed handbook revision number alone neither invalidates every unchanged decision nor approves the changed ones.

Write the result into the canonical `DESIGN.md` using its existing samples/decisions/coverage sections. Link bulky review artifacts rather than creating a second approved design book. The sample and handbook must identify the same accepted design baseline. Keep proposed runtime settings distinct from implemented controls; a sample's theme switch is not an admin appearance panel.

## Handoff and completion

Return the recommended/comparable directions, selection source, executable selected revision and exact handbook baseline; actual themes/languages/sizes/states inspected; evidence and limits; accepted versus proposed choices; hypothetical capabilities; and remaining owner/engineering approval. Keep the main conversation concise while making samples accessible.

This gate is complete only for the stated slice when the visible samples, executable evidence and real scoped approval exist. Never turn approval of a few screens into acceptance of unbuilt pages, new features or future decisions. Continue development incrementally under the lead; later slices still need their own relevant validation.
