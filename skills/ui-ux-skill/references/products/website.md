# Website Product Pack

Use only when the active product route includes `website`.

This Product Pack applies to public-facing websites whose primary purpose is communication, discovery, trust, content consumption, lead generation, service/product presentation, or public information rather than performing ongoing authenticated application work.

Product design knowledge for websites is maintained locally in this repository. Do not depend on an external design Skill for website design.

Typical examples:

- company and corporate websites
- service-business websites
- personal-brand and portfolio websites
- blogs, magazines, and publications
- campaign and landing pages
- public informational websites
- SEO-driven content sites
- public product/brand websites

## Routing contract

After the `website` route is active:

1. read `../shared-product-rules.md` and select only Shared UI Rules required by the task;
2. load only the Website modules below that match the current scope;
3. load Design System modules only when reusable foundations, themes, tokens, states, or migration are materially involved;
4. do not load Dashboard, Web Application, Mobile, or WordPress Product Packs unless the deliverable genuinely spans those product surfaces.

The Website Product Pack is the only source of Website-specific routing. The global product registry must not expose these internal modules.

## Website vs web application

Use `website` when the primary experience is public-facing communication, discovery, content, trust, or conversion.

Use `web-application` when the primary experience is a stateful application used to perform ongoing work.

A product may contain both:

- public marketing/content site -> `website`
- signed-in product area -> `web-application`

Route each affected surface independently.

Do not apply application-shell conventions to a public website without a product reason.

Do not apply campaign/landing-page choreography to repeated-use application workflows.

## Website subtype and visitor job

Before broad design decisions, identify the dominant website subtype and the visitor's primary job.

Common website modes include:

### Corporate / organization

Primary jobs often include:

- understand what the organization does;
- establish legitimacy;
- understand capabilities;
- find contact/location/support;
- inspect proof, team, credentials, or case studies.

### Service business

Primary jobs often include:

- understand the service;
- determine fit;
- understand location/service area;
- evaluate trust;
- compare options;
- book, call, request a quote, or submit a lead.

### Product / brand site

Primary jobs often include:

- understand the product;
- see the product in context;
- understand differentiation;
- inspect proof;
- compare plans/options;
- start a trial, buy, contact sales, or enter the product.

### Personal brand / portfolio

Primary jobs often include:

- identify the person;
- understand expertise;
- inspect work/evidence;
- understand services or availability;
- contact, follow, book, or hire.

### Publication / content site

Primary jobs often include:

- discover relevant content;
- understand topic/category;
- read efficiently;
- navigate related content;
- search;
- subscribe or return.

### Campaign / landing page

Primary jobs often include:

- understand one focused offer/message;
- evaluate enough proof to act;
- complete one primary conversion path.

Do not force all website types into the same homepage template.

## Website decision brief

For significant work, establish:

- website subtype;
- primary visitor segments;
- primary visitor job;
- primary conversion;
- secondary conversion;
- content/proof strategy;
- navigation model;
- first-viewport objective;
- trust model;
- visual direction;
- typography posture;
- media/art-direction plan;
- responsive strategy;
- accessibility risks;
- performance risks;
- supported languages/directions;
- representative pages/states for validation.

The brief may be compact, but the design should not proceed as if these decisions do not exist.

## Local module routing

Load modules progressively:

- `website/structure-navigation.md` — information architecture, navigation, homepage/hero, landing/detail/editorial composition, content hierarchy.
- `website/conversion-trust.md` — visual direction, typography, CTA hierarchy, conversion, forms/leads, contact, trust/proof, pricing.
- `website/content-seo.md` — site search, SEO-aware information architecture, search-result presentation, structured data/breadcrumbs, internal linking.
- `website/media-performance.md` — responsive behavior, media/art direction, video, performance, third-party scripts, progressive enhancement, motion.
- `website/accessibility-localization-qa.md` — accessibility, privacy/consent, legal/footer, localization/Persian/RTL, edge pages, evidence, final Website QA.

For a narrow task, load the minimum matching module set. For broad Website design or redesign, load all modules that materially affect the requested deliverable.

## Shared-rule boundary

Cross-product behavior belongs to Shared Product UI Rules. Do not duplicate complete Shared Rules here or in Website modules.

Website modules retain only public-site specialization such as visitor discovery, trust, conversion, content/SEO structure, public navigation, responsive media, and Website-specific validation.

## Specialist boundary

Persian linguistic correctness remains owned by the required `persian-writing` specialist when Persian-facing UI is in scope. Website layout, directionality architecture, component behavior, and product semantics remain owned by this Skill.
