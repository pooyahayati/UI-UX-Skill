# Specialist Routing Contract

This Skill can operate in two roles:

1. **Standalone UI/UX Head** — when the user invokes this Skill directly.
2. **Head-delegated UI/UX Specialist** — when a higher-level engineering Skill delegates UI/UX work to it.

The Skill may also route narrowly scoped work to lower-level specialist Skills. Specialist routing must reduce duplication and improve evidence; it must not create competing sources of authority.

## Authority hierarchy

When multiple Skills are active, use this precedence:

`Higher-level Engineering Head -> Production Dashboard UI/UX Head -> Lower-level Specialist`

A lower-level specialist MUST NOT silently override:

- approved product scope
- risk or approval requirements supplied by the higher-level Head
- architecture or security boundaries
- business rules or data semantics
- accepted design constraints supplied by this UI/UX Head

If a lower-level specialist discovers a conflict or material risk, return the conflict upward instead of resolving it by changing higher-level decisions.

## Standalone mode

When no higher-level Head contract is supplied, this Skill owns:

- UI/UX task framing
- UI/UX discovery and design-profile decisions
- UI/UX approval mode
- specialist selection
- UI implementation guidance
- UI validation and evidence
- UI-specific completion reporting

It still does not own unrelated backend, security, database, or product-scope changes.

## Head-delegated mode

When a higher-level Head supplies a delegation contract, treat supplied decisions as authoritative unless they are internally contradictory or unsafe.

Useful incoming fields are:

- Current Objective
- approved scope
- affected paths/surfaces
- project invariants
- accepted requirements
- acceptance criteria
- risk tier
- approval requirements
- working-tree boundaries
- architecture/security constraints
- required or recommended specialists
- requested output/handoff format

Do not repeat discovery that the higher-level Head has already completed. Do not reopen settled product or architecture decisions merely because this Skill would have chosen differently.

This Skill remains responsible for the UI/UX decisions inside the delegated boundary.

## Specialist classes

### Required specialist

A required specialist MUST be used when its trigger is active and the specialist is available/discoverable.

If it is unavailable:

1. do not pretend its workflow was executed;
2. continue only with work that does not require that specialist's judgment;
3. mark the specialist-dependent result as `Unverified` or `Blocked`;
4. do not declare the specialist-dependent part complete.

### Recommended specialist

Use when available and when its unique evidence materially improves the task. If unavailable, use the best safe fallback and report the limitation.

### Optional specialist

Use only when explicitly requested or when the task clearly benefits enough to justify the extra process.

## Current specialist registry

### Persian language and Persian-facing UI

**Specialist:** `persian-writing`

**Canonical source:**
`https://github.com/ali2000hos/persian-writing`

**Status:** REQUIRED when any trigger below is active.

Triggers:

- Persian is a supported product language.
- Persian is the primary interface language.
- The task creates, edits, reviews, or finalizes Persian user-facing copy.
- The interface contains material mixed Persian/English content.
- The task materially affects Persian RTL presentation or localization.
- The target product surface is Persian-facing and typography/text rendering is part of the change.

The specialist owns:

- Persian wording and register
- natural Persian phrasing
- orthography
- ZWNJ / نیم‌فاصله
- Persian ی / ک
- punctuation
- Persian digit conventions when appropriate
- Persian/English mixed-text correctness
- labels, buttons, field help, validation messages, errors, notices, empty states, and other Persian UI copy
- Persian language QA

This UI/UX Head retains ownership of:

- layout and information architecture
- design-system architecture
- component structure
- responsive behavior
- RTL/LTR layout architecture
- typography system and font-loading architecture
- theme and visual hierarchy
- interaction design
- accessibility at the product/UI level

When Persian-facing UI is in scope, do not mark Persian language QA complete unless `persian-writing` was used. If the specialist is unavailable, explicitly report:

`Persian language QA: Unverified — required specialist unavailable.`

The rest of the UI work may proceed when safe, but Persian-facing copy must not be represented as finalized.

### Browser runtime validation

**Specialist:** `browser-testing-with-devtools`

**Canonical source:**
`https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools`

**Status:** RECOMMENDED for browser-based UI work when the specialist is installed and runtime browser access is available.

Use it when live runtime evidence is important, including:

- layout or rendering defects
- responsive behavior
- console errors
- network behavior affecting UI
- state/hydration issues
- visual verification
- runtime performance investigation

This Skill defines what needs visual or interaction validation; the browser specialist supplies runtime evidence. Runtime evidence returns to this UI/UX Head and, when present, to the higher-level engineering Head.

## Specialist handoff contract

A lower-level specialist should receive only the context it needs.

Typical input:

- objective
- affected surfaces
- relevant constraints
- approved design direction
- acceptance criteria relevant to the specialist
- exact text/screen/state to inspect

Expected return:

- findings or decisions
- evidence
- affected surfaces/files when known
- unresolved risks
- checks performed/not performed
- explicit conflicts with higher-level constraints

## UI/UX result returned to a higher-level Head

When operating in Head-delegated mode, finish with a compact handoff that includes:

### UI/UX Specialist Result
- UI/UX decisions made
- affected surfaces/files
- higher-level constraints preserved
- lower-level specialists required/used/unavailable
- rendered/visual/accessibility evidence
- checks performed and not performed
- unresolved UI/UX risks
- remaining approvals
- required next action for the higher-level Head

Do not declare the entire software objective complete. The higher-level Head owns final integration, cross-domain verification, release decisions, and global completion.

## Repository/state ownership

When operating under a higher-level Head, follow its repository-purity and state-storage policy.

For `design-profile.md`:

- an approved, durable project design profile may be committed when it is meaningful project documentation;
- draft discovery notes, temporary audit output, screenshots, generated reports, and specialist scratch state should remain outside the product repository unless the project explicitly requires them;
- do not create durable documents merely to satisfy process.

## Conflict handling

When specialists disagree:

1. preserve higher-level approved constraints;
2. identify whether the disagreement is language, design, engineering, security, or product scope;
3. let the owning layer decide;
4. escalate unresolved cross-domain conflicts upward.

Examples:

- Persian wording question -> `persian-writing`
- RTL component layout -> this UI/UX Head
- authorization boundary -> higher-level engineering/security authority
- database/API semantics -> higher-level engineering Head
