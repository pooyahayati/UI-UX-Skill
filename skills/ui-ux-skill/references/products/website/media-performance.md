# Website Responsive Media and Performance

Load only after the active product route includes `website` and responsive behavior, media, performance, progressive enhancement, third-party scripts, or motion is in scope.

This module contains existing Website Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

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

## Motion

Read `../shared/motion.md`.

Website specialization:

- non-user-triggered motion should be rare and purposeful;
- avoid scroll hijacking and reveal animation required to access content;
- decorative background motion must not harm reading or performance;
- public-site animation should not delay discovery or conversion.

A website does not become more premium simply by moving more.
