# EditorialProductGrid — Island Directory

Curated product showcase with editorial layout and flexible column arrangements.

## Files

| File | Purpose |
|------|---------|
| `layouts/triple-center.json` | 3 products, center one featured/larger |
| `layouts/dual-side.json` | 2 products side by side with editorial text between |
| `layouts/collection-wall.json` | 4-column product wall (2 mobile, 4 desktop) |

## Quick Reference

- **Variants**: tripleCenter, dualSide, quad
- **Required prop**: `products` (array of product objects with `productId`)
- **Schema**: `vibe://schema/island/EditorialProductGrid`
- **Layouts**: `vibe://islands/editorial-product-grid/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: ProductHero (above), ReviewCarousel (below for social proof), StickyBar
- Use `--lx-surface-alt` background to contrast with hero section above
- Never place immediately after another grid island — insert editorial or testimonial between
- tripleCenter works best for hero-product + flanking variants; quad for collection browsing
