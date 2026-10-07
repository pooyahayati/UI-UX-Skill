# Specialist Routing Contract

This Skill can operate in two roles:

1. **Standalone UI/UX Head** — when the user invokes this Skill directly.
2. **Head-delegated UI/UX Specialist** — when a higher-level engineering Skill delegates UI/UX work to it.

The Skill may also route narrowly scoped work to lower-level specialist Skills. Specialist routing must reduce duplication and improve evidence; it must not create competing sources of authority.

## Authority hierarchy

When multiple Skills are active, use this precedence:

`Higher-level Engineering Head -> UI/UX Head -> Lower-level Specialist`

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
- UI/UX discovery and design-handbook decisions
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

The machine-readable source of truth for specialist identity, requirement level, trigger, canonical repository, and install path is:

`../specialists.json`

The Head MUST NOT duplicate specialist methodology, domain checklists, examples, implementation rules, or pinned versions.

For a routed specialist:

- read the matching registry entry;
- evaluate its trigger;
- enforce its requirement level;
- pass only the context needed for the specialist's domain;
- preserve Head-level scope, security, architecture, approvals, and UI/UX constraints;
- consume the specialist result as domain evidence;
- mark specialist-dependent validation `Unverified` or `Blocked` when a required specialist cannot be used.

For Persian-facing UI, the registry marks `persian-writing` as REQUIRED.


The registry contains routing metadata only. Domain rules remain owned by the current specialist Skill.

## Skill freshness and update policy

The Head and every routed specialist should use the latest available stable version from their canonical source.

Rules:

1. Do not pin a specialist version, release tag, commit SHA, or copied snapshot inside the Head unless an explicit project compatibility constraint requires a temporary pin.
2. Keep only the canonical source and specialist identity in the registry.
3. Before significant work, and whenever a required specialist is first needed in a session, verify when tooling/network access allows:
   - the Head Skill is installed and discoverable;
   - the specialist is installed and discoverable;
   - the installed copy matches or is not known to be behind the current canonical upstream source.
   Use the environment's Skill manager when available; this repository also provides `scripts/validate_specialists.py` for explicit source/install checks.
4. If a REQUIRED Skill is missing or an installed Skill is known to be stale and the environment supports installing/updating Skills, install or update/reinstall it from the registry's canonical source before relying on it. Do not silently substitute Head-local domain rules for a missing required specialist.
5. If freshness cannot be checked, report freshness as `Unverified`; never claim that the latest version was used.
6. If a REQUIRED specialist is known to be stale and cannot be updated, do not treat specialist-dependent validation as complete.
7. If the environment supports a Skill manager/installer, prefer its update mechanism over copying specialist files into this Head.
8. Periodically re-check installed specialists even when triggers have not changed, so the registry continues to benefit from upstream specialist improvements.

Latest means the latest stable/released version when the source publishes stable releases. If the source has no stable release channel, use the latest compatible canonical default-branch version.

The Head MUST NOT vendor specialist content merely to guarantee a version. Freshness is managed by installation/update checks, not by copying specialist instructions into the Head.

An entrypoint match alone does not verify a specialist package. The repository checker binds the registry's package subtree to one current upstream commit and compares all required resource bytes, reporting entrypoint, package and freshness evidence separately. Strict checks inspect every named installation root. Missing/modified resources, unsupported links and unavailable reads cannot be called current. Local additions and Head edits remain preserved but are not automatically certified; use the managing Head's integration-aware check rather than overwriting its contract to obtain an exact match. The checker is read-only, and any repair/update still needs the actual host/user authorization. See the repository installation guide for checker limits and result meanings; do not infer a successful install from a successful source check.

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

## Bounded early-design agent handoff

For substantial early discovery/sample work, strongly recommend that the engineering lead delegate a bounded design assignment using this same Skill to keep the main coding conversation concise. This is an agent role, not a new external specialist or registry entry.

Proceed only when agent use is authorized and the capability exists. A recommendation is not permission to spawn an agent or create a separate user-owned chat. Otherwise the lead performs the same scoped work directly and reports that no subagent was used; do not make delegation itself a blocker.

The assignment identifies the product, audience/roles, approved goals/features, stack, default/supported languages and directions, existing assets/decisions, protected constraints, representative workflows, acceptance criteria, and exact owned paths. Name the canonical handbook path and baseline revision when established; use `design-handbook.md` for migration and preserve a valid legacy baseline until its consumers are verified rather than silently creating competing authorities.

Assign exactly one handbook writer for a given revision. Other agents return proposed changes instead of racing to edit shared decisions. Give only the permissions needed for the assignment; do not authorize unrelated dependencies, backend changes, publication, or broader software scope.

The return contains product-specific recommendations with rationale, truly open questions, sample locations/revisions when produced, proposed handbook changes, observed versus inferred assumptions, checks/evidence and limitations, conflicts, and approvals still needed. The lead checks scope, evidence and revision consistency and explicitly accepts or returns the result. Agent preference is not owner approval; sample approval is not feature-scope approval.

For subsequent slices, use [incremental decisions and handoffs](incremental-design-decisions.md) to pass the current approved baseline and genuinely new need, record affected decisions/settings/approvals, and reconcile a stale return before integration. A moved handbook revision is neither permission to overwrite it nor reason to repeat all discovery.

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

For canonical `DESIGN.md` and necessary legacy compatibility documents:

- a meaningful durable project handbook, including its initial draft and scoped approval history, belongs with product documentation under the project policy;
- temporary discovery scratch, audit output, screenshots, generated reports and specialist operational state remain outside the product repository unless explicitly required as product assets;
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
