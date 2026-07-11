# BeforeAfter — Island Directory

Transformation comparison island. Shows before/after states via slider, side-by-side, or toggle.

## Files

| File | Purpose |
|------|---------|
| `layouts/slider.json` | Draggable slider divider between before/after images |
| `layouts/side-by-side.json` | Two images next to each other with labels |
| `layouts/toggle.json` | Single image area with button toggle between states |

## Quick Reference

- **Variants**: slider, side-by-side, toggle
- **Required prop**: `before` (object with `src`, `label`)
- **Schema**: `vibe://schema/island/BeforeAfter`
- **Layouts**: `vibe://islands/before-after/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: Testimonials, ProductDetails, BuyBox
- Place mid-page to demonstrate product transformation results
- Works well below a hero and above social proof
- Never use more than 2 BeforeAfter islands on a single page
