# Material content containers

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to every row; active Product content/data hierarchy remains authoritative.

| Component | Purpose / anatomy / suitable variants | Representative example / Material Web baseline observation |
| --- | --- | --- |
| Card | Related content: container, title/body, optional media and separate actions. Elevated/filled/outlined appearance reflects grouping, not a card for every sentence or metric. | One assigned visit groups location, schedule and a visible Open action. Card is listed unbuilt; roadmap also mentions an old preview, which does not prove a stable current export. |
| List | Scannable related items: group, item primary/secondary text, optional leading/trailing content and action. Use supported row presentations based on information hierarchy, not a default icon on every row. | Assigned visits ordered by the product's actual scheduling rules; long titles stay understandable. Baseline list documented; task-specific list-detail arrangement is custom composition. |
| Divider | Modest grouping boundary: line/spacing within content. Full or inset presentation reflects the existing layout; it cannot be the sole indication of meaning. | Separate visit summary from instructions without increasing interactive border emphasis. Baseline divider documented. |

## States / accessibility / recovery

Cards are static groups unless explicitly interactive. Whole-card activation must
not produce nested conflicting links/buttons; keep distinct actions reachable.
Loading/empty/unavailable/error content is truthful and task-specific, not a
generic skeleton masquerading as final data. Lists maintain order, item identity,
selection/current state where applicable, keyboard focus and context through
refresh/pagination; do not assign listbox semantics to an ordinary content list.
Virtualization requires its own accessible navigation/data-recovery evidence.
Decorative dividers need no focus or action; use structural headings/group
semantics rather than relying on a color line to describe relationships.

## Responsive, language, themes and controls

Cards fit content and reflow; lists prioritize key information without silently
dropping required data, and trailing actions stay touch/keyboard reachable.
Divider insets follow actual logical content alignment. Preserve actual reading
order, isolated identifiers and approved font/line-height under compact width,
zoom and RTL. Do not mirror numeric/time meanings because the container is RTL.

Use semantic surfaces/text and subtle separator roles separately from interactive
target boundaries; dark grouping cannot depend solely on disappearing shadows.
Prepared controls may alter supported density, radius, elevation, separators,
font roles and semantic icons, not content order, permissions, data freshness or
whether a card becomes interactive. Motion may indicate an update without hiding
content or requiring animation to understand it.

Tables, charts and diagrams remain **custom/product or provider-specific patterns**,
not an official M3 contract invented here. Use relevant Product data rules and
existing theme adapters, keeping legends/labels, scale meaning, keyboard/touch
alternatives and actual data states. Neither a Material card around a chart nor
a provider's DataGrid makes the chart/table an official M3 component.

Official sources: [cards](https://m3.material.io/components/cards/overview),
[lists](https://m3.material.io/components/lists/overview),
[divider](https://m3.material.io/components/divider/overview).
Card overview read live 2026-10-06; remaining links catalog-observed.
Availability: [provider roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
Recheck [stack fit](../material-stack-fit.md) for stable APIs; do not install previews by default.
