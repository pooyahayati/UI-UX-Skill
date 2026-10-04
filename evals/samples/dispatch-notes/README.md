# Authored Dispatch Notes comparison

This is **output**, not a raw forward-test fixture or an independent model result. It must never be copied into `evals/fixtures/sample-review` or included in a prepared prompt as an answer key. The original raw files remain unchanged. It is outside the distributable Skill/plugin package.

The maintainer authorized continuing R3 after its instruction/fixture contract integration. This bounded, fictional bilingual browser sample makes the design contract inspectable without a backend, new role, framework, admin panel, specialist installation or deployment.

## View locally

From the repository root, serve **only this directory** on loopback:

```bash
python -m http.server 8763 --bind 127.0.0.1 --directory evals/samples/dispatch-notes
```

- Comparable first directions: `http://127.0.0.1:8763/compare.html`
- Supported Persian comparison: `http://127.0.0.1:8763/compare-fa.html`
- Full-size A, English, light: `http://127.0.0.1:8763/?direction=a&language=en&theme=light&scenario=ready#visit`
- Full-size A, Persian, dark: `http://127.0.0.1:8763/?direction=a&language=fa&theme=dark&scenario=ready#visit`
- Full-size B, Persian, light: `http://127.0.0.1:8763/?direction=b&language=fa&theme=light&scenario=ready#visit`

English is default; Persian support is explicitly taken from the bilingual raw variant. Both themes exist for each direction. The comparison board's fixed desktop iframes are scaled thumbnails, not responsive/mobile evidence; open a full-size link for interaction and viewport testing.

Do not enter private/customer notes. Synthetic saves/completion are in-memory only; refresh clears them. Review controls select allowlisted test contexts, not persistent production settings. No network save/API, role enforcement, live appearance panel or permission guarantee exists. The local HTTP preview is development-only and must not be exposed publicly.

## Review the actual workflow

1. On narrow width, return to the list and open `VIS-204` again. The note survives same-tab navigation.
2. Edit the note, enable Fail next save, and Save draft. Observe busy/duplicate guard, retained exact input and durable failure feedback; retry normally.
3. Choose Read only, Loading and No assigned visits; restore Ready. These are labeled simulations, not backend permission/data checks.
4. Change theme/language/direction with an edited note; its value must not be replaced by translated seed text.
5. Try a blank note and completion without its checkbox; then complete using keyboard. Entered markup must display as literal text in the recorded result.
6. Inspect both themes/directions, mixed IDs, real fonts, long Persian copy and narrow/intermediate layouts. Separate actual checks from untested dimensions.

[DESIGN.md](DESIGN.md) is the draft r1/h1 reference. [QA.md](QA.md) records actual rendered/action evidence and gaps. [sample.json](sample.json) records identity/configuration, not approval. Source/asset tests protect links, real font/license bytes and separation from raw inputs; they do not render the UI or test model behavior.

Professional recommendation: A for frequent visit processing; B is a softer notebook treatment with equivalent tasks. **No direction selection, scoped visual approval or broad rollout has occurred.** Selection/refinement and revision-specific acceptance are the next gate; Skill-source acceptance alone is not fictional product-owner approval.
