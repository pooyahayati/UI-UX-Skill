# Material navigation

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to each row. Active Product navigation/wayfinding rules own routes, hierarchy,
history and permissions. Material does not grant authority to change them.

| Component | Purpose / anatomy / presentation | Representative example / implementation observation |
| --- | --- | --- |
| App bar | Current-page identity: container, title, optional back/menu control and essential actions. Pick supported compact/flexible presentation by task and content, not a giant decorative header. | Visit detail shows its title and a meaningful back destination. Material Web roadmap lists top app bar unbuilt; custom existing header may be themed, not renamed an official implementation. |
| Navigation bar | Stable equal-level destinations: item target, label/icon and current-location indicator. Current official overview recommends compact/medium contexts and 3–5 destinations; not every product needs a bottom bar. | Visits, schedule and account keep identity between screens. Material Web lists navigation bar unbuilt; new flexible design is not inferred library coverage. |
| Rail / drawer | Alternative destination presentation: container, labeled items, current indicator, optional groups and modal trigger. Choose persistent/expanded/temporary behavior only where the product hierarchy and space justify it. | Wider work surface uses the same visits route set in a rail; temporary drawer on compact layout only if that is the approved product behavior. Both unbuilt in Material Web roadmap. |
| Tabs | Peer views within a context: tab list, labeled tabs, active indicator and associated panels. Use supported primary/secondary appearance without disguising major route hierarchy as tabs. | Visit detail switches between notes and history while preserving each state. Baseline tabs documented in Material Web; route-linked controls may instead require link semantics. |

## Per-component behavior and recovery

- **App bar:** back/menu names remain meaningful; collapsed/scroll treatments
  never hide the only escape or lose keyboard focus. Long titles may wrap where
  supported, with page identity still available to assistive technology.
- **Navigation bar:** current destination is separate from focus/pressed and is
  programmatically conveyed. Badges never replace destination names. Do not
  randomly shuffle or remove routes to fit a smaller viewport.
- **Rail / drawer:** presentation changes preserve active route and reading order.
  A modal drawer needs focus containment, Escape/dismissal and trigger restoration;
  a persistent rail must not trap focus. Unauthorized destinations stay protected
  by real routing/access rules, not just visibility.
- **Tabs:** selected state/panel relationships and appropriate keyboard selection
  behavior follow the existing accessibility contract. Do not auto-activate slow
  remote work on every arrow key; preserve loading/error/retry and unsaved state.

## Responsive, language, theme and controls

Choose transitions from existing breakpoints and actual route/label fit. Bar,
rail and drawer are alternatives, not three mandatory new layouts. Avoid bottom
bar/keyboard/sticky action overlap; tab overflow remains keyboard/touch reachable.
Use logical start/end, deliberate directional arrows, correct current state and
actual translated label widths; no label-less RTL redesign or mandatory second locale.

Surfaces, selected indicators/text and focus use approved roles in both themes.
Owner controls may change prepared appearance/density/icon assignments, not routes,
permission checks, focus model or transition logic. Motion communicates a context
change and supports reduced motion without blocking navigation.

Official sources: [app bars](https://m3.material.io/components/app-bars/overview),
[bar](https://m3.material.io/components/navigation-bar/overview),
[rail](https://m3.material.io/components/navigation-rail/overview),
[drawer](https://m3.material.io/components/navigation-drawer/overview),
[tabs](https://m3.material.io/components/tabs/overview).
Bar overview read live 2026-10-06; app-bar official indexed text reviewed; remaining
links observed in live catalog. Baseline availability:
[provider roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
For exact web support, use [stack fit](../material-stack-fit.md).
