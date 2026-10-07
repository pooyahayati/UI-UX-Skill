# Website Accessibility, Localization, Privacy, and QA

Load only after the active product route includes `website` and accessibility, privacy/consent, localization/RTL, edge states, or final website validation is in scope.

This module contains existing Website Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

## Accessibility

Read `../../shared/accessibility-interaction.md` for the cross-product interaction floor and `../../accessibility.md` for QA/evidence.

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

Read `../../shared/state-recovery.md`.

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
