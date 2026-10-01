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

## Non-duplication rule

The Head is a controller, not a copy of its specialists.

For every routed specialist:

- keep only trigger conditions, requirement level, canonical source, authority boundary, handoff expectations, and fallback behavior in the Head;
- do not copy specialist methodology, domain checklists, examples, or detailed implementation rules into the Head;
- when domain-specific guidance conflicts, the Head-level constraints win, but the specialist remains authoritative inside its delegated domain;
- if the Head already contains legacy domain detail now owned by a specialist, remove or narrow that detail rather than maintaining two competing rule sets.

This enables specialist replacement or continuous specialist improvement without repeatedly redesigning the Head.

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

## Specialist registry

The Head stores only routing metadata and control boundaries for specialists. It MUST NOT duplicate the specialist's domain methodology, detailed rules, checklists, or implementation guidance.

This keeps specialist knowledge replaceable and continuously upgradeable.

### Persian-facing UI

**Specialist:** `persian-writing`

**Canonical source:** `https://github.com/ali2000hos/persian-writing`

**Status:** REQUIRED when Persian is a supported or user-facing product language, or when Persian-facing UI content/localization is materially in scope.

Head responsibilities are limited to:

- detect the trigger;
- require and route to `persian-writing`;
- pass only relevant UI context and upstream constraints;
- preserve Head-level scope, security, architecture, and approved design constraints;
- consume the specialist's output as language-domain evidence;
- refuse to mark Persian language validation complete when the required specialist was not successfully used.

Do not restate Persian writing, orthography, register, localization, or language-QA rules here. Those rules belong to the current installed `persian-writing` Skill.

If the required specialist cannot be used, report the specialist-dependent validation as `Unverified` or `Blocked` and do not treat Persian-facing language work as complete.

### Browser runtime validation

**Specialist:** `browser-testing-with-devtools`

**Canonical source:** `https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools`

**Status:** RECOMMENDED when live browser evidence materially improves UI validation and the specialist/runtime tools are available.

Head responsibilities are limited to deciding when runtime evidence is needed, passing the validation objective and constraints, and consuming the returned evidence. Do not duplicate the specialist's DevTools workflow in this Head.

## Skill freshness and update policy

The Head and every routed specialist should use the latest available stable version from their canonical source.

Rules:

1. Do not pin a specialist version, release tag, commit SHA, or copied snapshot inside the Head unless an explicit project compatibility constraint requires a temporary pin.
2. Keep only the canonical source and specialist identity in the registry.
3. Before significant work, and whenever a required specialist is first needed in a session, verify when tooling/network access allows:
   - the Head Skill is installed and discoverable;
   - the specialist is installed and discoverable;
   - the installed copy is not known to be behind the latest stable release/source.
4. If an installed Skill is known to be stale and the environment supports updating Skills, update/reinstall it from its canonical source before relying on it.
5. If freshness cannot be checked, report freshness as `Unverified`; never claim that the latest version was used.
6. If a REQUIRED specialist is known to be stale and cannot be updated, do not treat specialist-dependent validation as complete.
7. If the environment supports a Skill manager/installer, prefer its update mechanism over copying specialist files into this Head.
8. Periodically re-check installed specialists even when triggers have not changed, so the registry continues to benefit from upstream specialist improvements.

Latest means the latest stable/released version when the source publishes stable releases. If the source has no stable release channel, use the latest compatible canonical default-branch version.

The Head MUST NOT vendor specialist content merely to guarantee a version. Freshness is managed by installation/update checks, not by copying specialist instructions into the Head.

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
