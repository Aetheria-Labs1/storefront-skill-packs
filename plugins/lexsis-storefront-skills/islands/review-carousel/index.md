# ReviewCarousel — Island Directory

Displays customer reviews in various layouts: grid cards, horizontal scroll, or single featured quote.

## Files

| File | Purpose |
|------|---------|
| `layouts/card-grid.json` | 3-column grid of review cards (1-col mobile, 3-col desktop) |
| `layouts/horizontal-scroll.json` | Swipeable horizontal carousel with peeking edge cards |
| `layouts/featured-quote.json` | Single large featured review, centered, narrow container |

## Quick Reference

- **Variants**: default, compact, grid, minimal
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/ReviewCarousel`
- **Layouts**: `vibe://islands/review-carousel/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place mid-page or after product details (never first section)
- Pair with: BuyBox (above), TrustBadgeBar, PDPInfoCards
- `card-grid` works best on surface-alt backgrounds for card contrast
- `featured-quote` uses narrow max-w-2xl — ideal for between wider sections
- `horizontal-scroll` needs overflow-hidden parent — layout handles this
