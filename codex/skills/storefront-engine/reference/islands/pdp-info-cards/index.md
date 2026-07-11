# PDPInfoCards — Island Directory

Displays product information, benefits, or certifications as structured icon+text cards.

## Files

| File | Purpose |
|------|---------|
| `layouts/filled-grid.json` | 2x2 grid with filled surface-alt background cards |
| `layouts/dashed-row.json` | Horizontal row of dashed-border compact cards |
| `layouts/minimal.json` | Vertical list with icon+text, no card borders |

## Quick Reference

- **Variants**: filled, dashed, minimal, bordered
- **Required prop**: `cards` (JSON array of `{icon, title, description}`)
- **Schema**: `vibe://schema/island/PDPInfoCards`
- **Layouts**: `vibe://islands/pdp-info-cards/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place after BuyBox section or alongside product details
- `filled-grid` — standalone section, good for ingredients/benefits breakdown
- `dashed-row` — compact, works as sub-section below BuyBox for shipping/return/warranty
- `minimal` — narrow content width, ideal for simple feature bullets
- Pair with: BuyBox (above), ReviewCarousel (below), TrustBadgeBar
- Cards typically contain: shipping info, return policy, certifications, key ingredients, product benefits
