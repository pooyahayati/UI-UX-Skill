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

## Shared rule loading

After this Product Pack is active, read `../shared-product-rules.md` and `../../shared-rules.json`.

For broad website work normally load:

- `../shared/navigation-wayfinding.md`
- `../shared/feedback-status.md`
- `../shared/state-recovery.md`
- `../shared/accessibility-interaction.md`
- `../shared/responsive-adaptation.md`
- `../shared/content-hierarchy-progressive-disclosure.md`

Also load:

- `../shared/forms-data-entry.md` when forms/lead generation are in scope;
- `../shared/destructive-high-impact-actions.md` for consequential account/consent/delete actions;
- `../shared/motion.md` when motion is materially in scope.

This Website Product Pack specializes those contracts for public-facing discovery, trust, content, conversion, SEO-aware structure, media, and performance. Do not duplicate the full Shared Rule here.

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

## Visual direction

A public website may be more expressive than an operational product, but visual direction must come from the actual brand, subject matter, audience, and content.

Before choosing a style, identify:

- brand posture;
- audience expectations;
- industry/material/subject cues;
- desired emotional tone;
- level of visual restraint;
- one memorable design idea worth emphasizing.

Avoid generated-template defaults that appear regardless of subject.

Examples of patterns that require justification rather than automatic use:

- centered gradient hero;
- repeated identical cards;
- excessive glass/blur;
- arbitrary bento grids;
- decorative metrics;
- unnecessary all-caps eyebrow labels;
- generic stock imagery;
- animation on every section.

Spend visual boldness selectively.

## Typography

Typography is both brand and information architecture.

Define:

- primary type family;
- optional display/secondary family;
- body size/line height;
- heading scale;
- max reading width;
- weights/styles with real semantic roles;
- Persian/Latin pairing when multilingual.

Prefer readable line lengths and deliberate hierarchy.

Avoid:

- using too many type families;
- tiny body copy to preserve composition;
- low-contrast body text;
- fixed-height text containers;
- decorative type treatments that weaken comprehension.

Text must survive zoom, translation, and longer localized strings.

## Calls to action

CTA hierarchy should reflect actual user intent and commitment.

Define:

- primary action;
- secondary action;
- navigational actions;
- low-commitment alternatives.

CTA labels should describe the result.

Prefer:

- "Request a quote"
- "Book a consultation"
- "View pricing"
- "Download the guide"

over vague labels such as:

- "Submit"
- "Learn more" everywhere
- "Get started" when the next step is unclear.

Do not make every link look like the primary CTA.

## Conversion UX

Conversion is a journey, not a button treatment.

Evaluate:

- visitor readiness;
- required evidence;
- commitment level;
- friction;
- uncertainty;
- alternatives;
- next-step clarity.

A conversion path should not require the visitor to surrender information before understanding what they receive.

Do not use:

- false urgency;
- fake scarcity;
- misleading defaults;
- disguised advertising;
- hidden opt-ins;
- confirm-shaming;
- intentionally difficult cancellation/contact paths.

## Forms and lead generation

Read `../shared/forms-data-entry.md` and `../shared/feedback-status.md`.

Website lead-generation specialization:

- ask only for information needed at the current commitment level;
- explain privacy/use context when collecting personal or sensitive information;
- align form length with visitor readiness and value offered;
- preserve the public conversion path after validation failure;
- make success state and response/next-step expectation explicit.

For multi-step lead forms, preserve progress and entered data and clarify when information is actually submitted.

Do not force visitors to provide contact details before they understand what they receive.

## Contact and support

Contact options should match the business and visitor need.

Where relevant, expose:

- phone;
- email;
- form;
- address;
- map/location;
- hours;
- service area;
- support channel;
- response expectation.

Do not bury essential contact information solely to force visitors through a lead form.

Repeated help/contact mechanisms should remain predictable across relevant pages.

## Trust and credibility

Trust should be evidence, not decoration.

Potential trust evidence includes:

- real identity;
- team/expert identity;
- physical location;
- service area;
- qualifications;
- certifications;
- case studies;
- customer/client evidence;
- verifiable testimonials;
- real work samples;
- process transparency;
- pricing context;
- guarantees/policies;
- support/contact clarity;
- privacy/security information when relevant.

Match trust evidence to the decision.

A medical, financial, legal, educational, local-service, SaaS, and portfolio website require different proof.

Never fabricate:

- customer counts;
- logos;
- testimonials;
- ratings;
- awards;
- certifications;
- case-study results;
- press mentions;
- staff identity.

## Testimonials, ratings, and social proof

Use social proof only when its origin and meaning are understandable.

Where possible, clarify:

- who the person/customer is;
- what relationship existed;
- what result/context the testimonial refers to.

Avoid walls of anonymous praise.

Do not use decorative five-star ratings without a real source.

## Case studies and proof

A case study should make the evidence legible.

Where relevant, distinguish:

- context/problem;
- constraints;
- work performed;
- evidence/result;
- timeframe;
- attribution.

Do not present correlation as causation.

Do not invent quantitative improvement.

## Pricing and commercial clarity

When pricing is in scope, help visitors understand:

- unit/billing basis;
- what is included;
- important limits;
- plan differences;
- taxes/fees when material;
- trial/renewal implications;
- next step.

Do not design pricing to intentionally obscure the real cost.

If full pricing cannot be public, provide useful pricing context when possible rather than a context-free "Contact us."

## Search

Site search becomes important when users cannot reliably predict navigation or content volume is high.

Design search around:

- search scope;
- input prominence;
- result relevance;
- query persistence;
- no-result recovery;
- filtering/faceting when justified;
- typo/variant tolerance when supported;
- keyboard access;
- mobile behavior.

Do not add prominent search to a five-page site merely because large websites have it.

## SEO-aware information architecture

Website UX should support crawlable, understandable, user-facing structure.

Preserve or improve:

- descriptive page titles;
- one clear page topic;
- meaningful visible headings;
- logical heading hierarchy;
- descriptive link text;
- crawlable primary content;
- internal linking;
- stable useful URLs;
- canonical content decisions when within scope;
- useful breadcrumbs for deep hierarchies;
- meaningful image alternative text;
- content discoverability.

Search engines are not the audience; visitors are.

Do not distort headings, copy, or navigation merely to repeat keywords.

Do not hide essential content behind interaction that prevents ordinary access/discovery without a product reason.

## Search-result presentation

When content/SEO work is in scope, ensure the design/content system supports:

- descriptive document titles;
- a clear visual page title;
- useful snippets/meta descriptions where the content system allows them;
- site identity/favicons;
- canonical organization/business information;
- content-appropriate structured data where legitimately applicable.

Structured data must describe visible/real content.

Do not add schema merely because a rich-result type exists.

Do not promise that structured data will produce a rich result.

## Structured data and breadcrumbs

When technically in scope, prefer valid structured data that reflects real page content.

Potential website-level uses include:

- Organization / relevant subtype;
- LocalBusiness where applicable;
- Article for genuine article content;
- BreadcrumbList for useful hierarchy;
- other content-specific types only when the page actually qualifies.

Structured data implementation belongs to the implementation layer; this Product Pack defines when the information architecture and visible content support it.

## Internal linking

Internal links should help visitors discover related or next-step content.

Use:

- descriptive anchor text;
- contextual related links;
- category/topic relationships;
- useful next steps.

Avoid:

- repetitive keyword-stuffed links;
- huge unrelated footer link blocks;
- links added only for search engines;
- "click here" when a descriptive phrase is available.

## Responsive behavior

Read `../shared/responsive-adaptation.md`.

Website-specific responsive decisions must additionally preserve:

- first-viewport purpose;
- public navigation and language switching;
- reading width;
- CTA hierarchy;
- media focal point/art direction;
- comparison/pricing readability;
- footer/legal discoverability.

Do not preserve desktop spacing ratios mechanically or reorder content in a way that damages semantic/keyboard order.

## Responsive media and art direction

Media should adapt intentionally.

For significant images, establish:

- semantic purpose;
- intrinsic aspect ratio;
- focal point;
- desktop/mobile crop;
- text overlay safety;
- alternative text needs;
- whether the image is content or decoration.

Use responsive image techniques when implementation is in scope.

Do not ship oversized desktop images to every viewport by default.

Do not lazy-load the primary above-the-fold/LCP image merely because lazy loading is generally useful.

Reserve image dimensions/aspect ratios to reduce layout shift.

## Video and rich media

Use video only when it communicates something that static media cannot do as effectively.

Provide:

- controls where appropriate;
- captions/transcripts when speech/content requires them;
- reduced-motion/static fallback for nonessential autoplay motion;
- poster/fallback treatment;
- sensible loading strategy.

Avoid auto-playing sound.

Do not let decorative background video make content unreadable or materially degrade performance.

## Performance UX

Performance is part of website experience, especially for search/social/ad traffic and mobile networks.

Prioritize:

- fast access to primary content;
- stable layout;
- responsive interaction;
- efficient media;
- controlled font loading;
- minimal nonessential JavaScript;
- progressive enhancement;
- graceful behavior on slower devices/networks.

When performance measurement is in scope, use current Core Web Vitals guidance rather than stale hard-coded assumptions.

Current Core Web Vitals focus on:

- loading performance;
- interaction responsiveness;
- visual stability.

Prefer field/real-user evidence when available.

Lab results are useful for diagnosis but are not a substitute for field experience.

Do not claim performance improvement from visual inspection.

## Third-party scripts

Treat third-party scripts as product decisions because they can affect:

- performance;
- privacy;
- consent;
- security;
- layout stability;
- interaction responsiveness.

Challenge unnecessary:

- trackers;
- chat widgets;
- heatmaps;
- ad scripts;
- embedded social feeds;
- multiple tag managers;
- decorative third-party widgets.

Do not add a third-party script merely because a design template includes it.

## Progressive enhancement

Primary content and core navigation should remain understandable and usable when nonessential enhancement fails.

Use JavaScript for behavior that needs JavaScript.

Do not make basic content discovery depend on decorative client-side animation.

Provide graceful fallback for:

- failed media;
- disabled/blocked third-party scripts;
- reduced motion;
- slow loading;
- unsupported enhancement.

## Accessibility

Read `../shared/accessibility-interaction.md` for the cross-product interaction floor and `../accessibility.md` for QA/evidence.

Website specialization must additionally validate:

- semantic landmarks and heading structure for public content;
- skip/navigation landmarks where appropriate;
- meaningful link purpose;
- accessible menus and public search;
- forms/lead conversion;
- image alternatives and media captions/transcripts;
- sticky public headers that do not obscure focus;
- public content at zoom/text expansion.

Do not claim WCAG compliance without sufficient evidence and defined scope.

## Menus and interactive navigation accessibility

For custom navigation interactions:

- preserve keyboard access;
- keep focus visible;
- avoid hover-only access;
- make expanded/collapsed state programmatically understandable;
- return focus predictably after temporary overlays/drawers;
- prevent sticky navigation from obscuring the focused element.

Mobile navigation should have a clear open/close model and should not trap focus incorrectly.

## Motion

Read `../shared/motion.md`.

Website specialization:

- non-user-triggered motion should be rare and purposeful;
- avoid scroll hijacking and reveal animation required to access content;
- decorative background motion must not harm reading or performance;
- public-site animation should not delay discovery or conversion.

A website does not become more premium simply by moving more.

## Privacy, consent, and preference UX

When consent/preferences are in scope:

- make choices understandable;
- avoid false equivalence or visual coercion;
- preserve access to essential content where legally/product-wise appropriate;
- provide a way to revisit preferences when required;
- distinguish necessary behavior from optional tracking;
- do not use dark patterns to increase consent.

Legal compliance depends on jurisdiction and implementation context; do not claim compliance from UI treatment alone.

## Legal, policy, and footer surfaces

Footer and legal navigation should help visitors find durable reference information.

Where relevant:

- privacy;
- terms;
- accessibility statement;
- returns/refunds;
- shipping;
- licensing;
- contact;
- company identity;
- social channels;
- language/region settings.

Do not turn the footer into an unstructured dump of every link.

## Localization, Persian, and RTL websites

When Persian-facing language is in scope, the REQUIRED external `persian-writing` specialist owns Persian linguistic validation.

This Product Pack retains ownership of:

- website information architecture;
- page composition;
- conversion UX;
- responsive behavior;
- direction architecture;
- content hierarchy;
- visual design;
- website accessibility.

For multilingual websites:

- keep language switching discoverable;
- use the correct page/part language metadata when implemented;
- preserve language-specific direction;
- isolate mixed-direction technical content;
- support longer/shorter localized strings;
- localize formats where relevant;
- maintain equivalent core navigation/conversion paths where appropriate;
- avoid forcing identical line breaks/layout proportions across languages.

Do not treat the RTL version as a mirrored screenshot.

## Error, unavailable, and edge pages

Read `../shared/state-recovery.md`.

Website-specific recovery should cover representative:

- 404/not found;
- unavailable/maintenance when applicable;
- failed public form submission;
- empty search results;
- removed/expired public content.

Every edge page should preserve useful public navigation and a recovery path.

A playful 404 page is not useful if it removes orientation and recovery.

## Website QA matrix

For significant website work, validate representative:

### Page coverage

- homepage;
- primary service/product/content page;
- at least one deeper page;
- navigation;
- footer;
- primary conversion flow;
- contact/support;
- search if present;
- legal/trust surface;
- 404/error recovery.

### Responsive coverage

- narrow mobile;
- wider mobile;
- tablet/intermediate width when layout materially changes;
- desktop;
- wide desktop if composition changes;
- browser zoom / larger text.

### Interaction coverage

- navigation/menu;
- forms;
- validation;
- success;
- error;
- keyboard-only path;
- focus visibility;
- reduced motion;
- interactive media.

### Content/SEO structure

- document title;
- main visible title;
- heading hierarchy;
- semantic landmarks;
- internal links;
- breadcrumbs where applicable;
- indexable primary content when SEO matters;
- structured-data eligibility only when applicable.

### Performance-sensitive behavior

- primary/LCP media;
- layout stability;
- responsive images;
- lazy-loading boundaries;
- font behavior;
- third-party scripts;
- interaction responsiveness.

### Localization

- each supported direction;
- representative long strings;
- mixed Persian/English content when relevant;
- language switch;
- localized navigation and conversion flow.

## Evidence and claims

Do not claim:

- improved conversion;
- SEO uplift;
- better Core Web Vitals;
- accessibility compliance;
- increased trust;
- faster performance;

without evidence appropriate to the claim.

Use design rationale for design decisions and measured evidence for performance/business claims.

## Current canonical references

When a detail may have changed, prefer current canonical guidance rather than copying third-party recipes.

Useful sources include:

- W3C Web Content Accessibility Guidelines (WCAG) 2.2
- Google Search Central documentation
- web.dev Core Web Vitals guidance
- MDN Web Docs for semantic HTML, responsive media, and browser behavior

External sources inform the local Product Pack; they do not become design dependencies.
