# Product Routing

UI/UX work MUST be classified by product type before product-specific design rules are applied.

The machine-readable source of truth is:

`../product-types.json`

## Required routing sequence

1. inspect the request and existing product/repository context;
2. determine the primary `product_type`;
3. add secondary product routes only when the task genuinely spans multiple product surfaces;
4. load every `required_references` entry for each active route;
5. apply shared UI/UX rules only after the product route is known;
6. apply specialist routing independently for language, runtime validation, or other specialist domains.

For new products and major redesigns, do not proceed with product-specific design decisions while `product_type` is unresolved.

For narrow changes to an existing product, infer the route from observable product/repository evidence when confidence is high. If the route is genuinely ambiguous and materially changes the design rules, surface the ambiguity instead of silently choosing a product model.

## Authority

Use this precedence:

`Higher-level Engineering Head -> UI/UX Head invariants -> Active Product Pack -> Shared UI/UX defaults -> Lower-level Specialist within its delegated domain`

A Product Pack specializes UI/UX behavior for its product class. It must not override upstream product scope, security, architecture, business rules, or approved constraints.

A lower-level Specialist remains authoritative inside its delegated domain, but cannot override Head-level or active Product Pack constraints outside that domain.

## Multiple product routes

A product can span more than one route.

Examples:

- a public website with a signed-in product area:
  - primary route depends on the current deliverable;
  - public marketing/content surface: `website`;
  - signed-in product surface: `web-application`;
  - do not apply app-shell conventions to the public site or website-conversion patterns to an authenticated workflow.
- a SaaS web application with an analytics dashboard:
  - primary: `web-application`
  - secondary: `dashboard`
- a WordPress plugin whose settings page contains a monitoring dashboard:
  - primary: `wordpress-plugin`
  - secondary: `dashboard`
- a web product with a companion mobile app:
  - route each affected surface independently;
  - do not apply mobile navigation conventions to the web application or vice versa.

Always identify one primary route for the current deliverable.

## Generic fallback

`generic-product-ui` is a temporary fallback, not a preferred product class.

Use it only when:

- the task is product UI work;
- no registered product type fits;
- the current scope is still safe to handle with shared UI/UX rules.

Do not force an unrelated Product Pack onto an unknown product.

When a new recurring product class appears, add a dedicated Product Pack instead of expanding the generic fallback indefinitely.

## Product route handoff

For significant work, record:

- primary product route
- secondary routes, if any
- evidence used to classify the product
- required Product Packs loaded
- any product-type ambiguity that remains
- product-specific validation performed

Do not claim product-aware validation when the required Product Pack was not loaded.
