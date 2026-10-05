// Native dialog owns inertness, Escape and the existing close/return path.
// Wrap Tab at the boundary so focus never loses its visible destination.
for (const dialog of document.querySelectorAll("dialog")) {
  dialog.addEventListener("keydown", event => {
    if (event.key !== "Tab" || !dialog.open || !dialog.matches(":modal")) return;
    const stops = [...dialog.querySelectorAll("button, input, select, textarea, a[href], [tabindex]")]
      .filter(node => !node.disabled && node.tabIndex >= 0 && node.getClientRects().length);
    if (!stops.length) return;
    const active = document.activeElement;
    const first = stops[0], last = stops[stops.length - 1];
    if (!dialog.contains(active) || (event.shiftKey ? active === first : active === last)) {
      event.preventDefault();
      (event.shiftKey ? last : first).focus();
    }
  });
}
