# Product Routing

Classify UI/UX work by product type before loading product-specific knowledge.

Machine-readable source of truth:

`../product-types.json`

## Required sequence

1. inspect the request and available product/repository evidence;
2. determine one primary product route;
3. add a secondary route only when the current deliverable genuinely spans another product surface;
4. load only the `required_references` for active routes;
5. let each active Product Pack route its own internal modules;
6. read `../shared-rules.json` and `shared-product-rules.md`, then load only scope-relevant Shared Rules;
7. load Design System modules only when the task materially needs them;
8. evaluate specialist triggers independently.

Do not read Product Packs or internal product modules merely to classify the product. Classification uses the request, repository/product evidence, and registry triggers/exclusions.

## Product isolation

Inactive product knowledge is out of scope.

For a single-route task:

- do not load another Product Pack;
- do not load another product's local modules;
- do not preload local module maps from the global registry;
- do not apply another product's conventions by analogy when the active Product Pack already defines the behavior.

The global registry identifies products and their required top-level Product Packs only. Internal Dashboard modes, Mobile platform packs, WordPress surfaces, Website modules, and Web Application modules are routed from their parent Product Pack after activation.

This isolation reduces context without weakening product-specific quality.

## Multiple product routes

Use multiple routes only when the current deliverable genuinely spans multiple product surfaces.

Examples:

- public marketing/content surface plus signed-in application area: route each affected surface as `website` or `web-application`;
- SaaS application with an analytics dashboard: primary `web-application`, secondary `dashboard` only for the dashboard surface;
- WordPress plugin containing a monitoring workspace: primary `wordpress-plugin`, secondary `dashboard` only when dashboard semantics materially apply;
- web product with a companion mobile app: route affected web and mobile surfaces independently.

Always identify one primary route for the current deliverable. Do not activate a secondary route because a product merely contains that technology elsewhere.

## Authority

Use this precedence:

`Higher-level Engineering Head -> UI/UX Head invariants -> Active Product Pack -> Shared Product UI Rule -> Design-system defaults -> Lower-level Specialist within its delegated domain`

A Product Pack owns product/platform/host/domain specialization. Shared Rules own stable cross-product contracts. A lower-level specialist is authoritative only inside its delegated domain.

No lower layer may weaken accessibility, security, authorization, truthful-state, data-integrity, or approved upstream constraints.

## Generic fallback

`generic-product-ui` is fallback-only.

Use it only when the task is product UI work, no registered product type fits, and the current scope can be handled safely with shared UI/UX rules.

Do not force an unrelated Product Pack onto an unknown product.

## Handoff

For significant work, record:

- primary product route;
- secondary routes, if any;
- evidence used for classification;
- Product Packs and local modules actually loaded;
- Shared Rules and Design System modules actually loaded;
- product-specific validation performed;
- relevant modules intentionally not loaded;
- unresolved product-type ambiguity.

Do not claim product-aware validation for a Product Pack or module that was not loaded and exercised.
