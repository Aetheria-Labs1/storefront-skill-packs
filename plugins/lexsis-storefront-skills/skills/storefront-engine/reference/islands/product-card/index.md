# ProductCard — Island Directory

Individual product display unit. Used standalone, in grids, or inside carousels.

## Files

| File | Purpose |
|------|---------|
| `layouts/default.json` | Vertical card: image top, info below |
| `layouts/horizontal.json` | Image left, info right (for lists) |
| `layouts/compact.json` | Small thumbnail + title + price + quick-add |

## Quick Reference

- **Component**: ProductCard
- **Category**: commerce
- **Props**: 12 (product, variant, showBadge, showRating, showQuickAdd, imageAspect, hoverEffect, priceFormat, compareAt, badgeText, linkBehavior, cardRadius)
- **Variants**: default, horizontal, compact
- **Schema**: `vibe://schema/island/ProductCard`
- **Layouts**: `vibe://islands/product-card/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: QuickAdd (overlay), VariantSwatches (inline), ProductCarousel (as child)
- Use in CSS Grid for collection pages (grid-cols-2 md:grid-cols-3 lg:grid-cols-4)
- Horizontal variant for cart drawers, upsell lists, wishlist pages
- Compact variant for mini-cart items, search results
