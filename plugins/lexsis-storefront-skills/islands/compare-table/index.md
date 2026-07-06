# CompareTable — Island Directory

Product comparison table for highlighting advantages over competitors or across product variants.

## Files

| File | Purpose |
|------|---------|
| `layouts/side-by-side.json` | 2-3 product columns, features as rows, sticky header |
| `layouts/feature-matrix.json` | Feature rows with checkmark/x indicators, winner highlighted |
| `layouts/compact.json` | Simplified 2-product comparison (ours vs theirs) |

## Quick Reference

- **Variants**: none (layout-driven)
- **Schema**: `vibe://schema/island/CompareTable`
- **Layouts**: `vibe://islands/compare-table/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place mid-to-lower page, after product introduction and before CTA
- Pair with: BuyBox (below table), TrustBadgeBar, FAQ
- Side-by-side works best with 2-3 products (scrolls horizontally on mobile)
- Feature-matrix is ideal for "us vs competitors" pages
- Compact variant is for focused head-to-head (landing pages, ads)
- Highlight the winning product with accent border (feature-matrix layout)
- Keep features list to 5-8 rows for scannability
