# Website Structure and Navigation

Load only after the active product route includes `website` and structure, navigation, page composition, or content hierarchy is in scope.

This module contains existing Website Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

## Primary objective

A website should help a visitor quickly answer:

- Where am I?
- Is this relevant to me?
- What is being offered or communicated?
- Why should I trust it?
- What evidence supports the claim?
- What should I do next?
- Where do I go if I need something else?

Do not design from decoration first.

Establish visitor intent, information architecture, content hierarchy, trust model, and conversion path before selecting visual treatments.

## Information architecture

Design the site around visitor intent, not internal organizational structure.

Before broad visual work, identify:

- top visitor questions;
- primary navigation destinations;
- secondary/support destinations;
- high-value content paths;
- conversion destinations;
- trust/legal/support surfaces;
- search needs;
- content taxonomy when content volume justifies it.

Prefer a small, understandable top-level structure over exposing every internal department or content category.

Avoid deep arbitrary menu nesting.

A visitor should be able to predict where a navigation item leads from its label.

## Navigation

Read `../shared/navigation-wayfinding.md` for the cross-product navigation contract.

Website-specific navigation must additionally resolve:

- primary and utility navigation;
- public information architecture;
- language switching when multilingual;
- search entry point when content volume warrants it;
- account/app entry point when the website connects to a signed-in product;
- sticky behavior only when it improves public-site wayfinding.

Use descriptive public-facing labels rather than internal organizational terminology.

Do not hide high-value public destinations solely to preserve visual minimalism.

### Mega menus

Use a mega menu only when information volume and hierarchy justify it.

A mega menu should group destinations meaningfully, remain keyboard/focus usable, work at zoom and smaller desktop widths, and have an intentional mobile replacement.

Do not turn a mega menu into an undifferentiated sitemap.

### Breadcrumbs

Use breadcrumbs when the public content hierarchy is deep enough that location context helps.

Breadcrumbs should represent a useful user-facing hierarchy, not blindly mirror URL segments.

Do not add breadcrumbs to shallow sites merely because they are an SEO pattern.

## Homepage architecture

The homepage should orient, qualify, prove, and route.

It does not need to explain everything.

A strong homepage usually answers, in a product-specific order:

1. what/who this is;
2. why it matters to the intended visitor;
3. what the visitor can do or explore;
4. why the visitor should trust it;
5. where to go next.

The exact sequence should follow visitor uncertainty, not a universal section template.

Avoid the default pattern of:

`Hero -> logo strip -> 3 cards -> feature grid -> testimonials -> CTA`

unless the content genuinely requires that structure.

## First viewport / hero

The first viewport has limited attention.

Choose the focal content deliberately.

It may be:

- a strong value proposition;
- the product itself;
- meaningful photography;
- proof/result;
- editorial statement;
- interactive demonstration;
- service/category choice;
- search/discovery entry point.

The hero does not always need:

- a large centered headline;
- two CTA buttons;
- a gradient;
- floating cards;
- decorative statistics.

Every first-viewport element should earn its space.

Keep the primary action clear without making secondary exploration impossible.

## Landing pages

A landing page should support one dominant intent.

Before design, establish:

- traffic source or visitor context when known;
- visitor awareness level;
- primary promise;
- primary objection;
- strongest available proof;
- conversion commitment level;
- required supporting information.

Match page length to the evidence needed for the decision.

Do not extend a page merely to imitate high-converting landing-page templates.

Do not hide necessary conditions, pricing context, exclusions, or consequences until after conversion.

## Service and detail pages

A service/detail page should answer more than "what is it?"

Where relevant, cover:

- who it is for;
- problem/context;
- scope;
- expected process;
- deliverables/outcomes;
- limitations;
- proof;
- pricing/pricing context;
- FAQ/objections;
- next step.

Place conversion opportunities where visitors have enough context to decide.

Do not repeat the same generic CTA after every section.

## Content and editorial pages

Optimize reading before decoration.

Resolve:

- article width;
- line length;
- text hierarchy;
- section navigation for long content;
- media placement;
- captions;
- code/data/table handling where relevant;
- author/date/update metadata when meaningful;
- related content;
- citations/source treatment when relevant.

Do not interrupt reading repeatedly with conversion banners, sticky overlays, or unrelated promotions.

For long pages, support scanning with meaningful headings rather than excessive visual section labels.

## Content hierarchy and scanning

Read `../shared/content-hierarchy-progressive-disclosure.md` for the cross-product hierarchy contract.

Website specialization:

- order sections around visitor questions and uncertainty;
- keep editorial/content pages readable before promotional;
- use public-facing headings that remain meaningful for scanning and semantic structure;
- let proof, media, CTA, and supporting content earn their prominence.

Do not convert every public content section into a rounded card or decorate hierarchy with badges/dividers that add no meaning.
