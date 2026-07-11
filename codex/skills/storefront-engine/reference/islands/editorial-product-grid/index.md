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
- **Required prop**: `products` (array with `productId` per item)
- **Schema**: `vibe://schema/island/EditorialProductGrid`
- **Layouts**: `vibe://islands/editorial-product-grid/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Product Resolution

Products array supports **both** resolved and unresolved items. The renderer auto-fetches unresolved products from Shopify Storefront API at hydration time.

### Unresolved (preferred — fresh data at render time):
```json
{"products": [
  {"productId": "gid://shopify/Product/123", "featured": true},
  {"productId": "gid://shopify/Product/456"}
]}
```

### Resolved (static — backward compat):
```json
{"products": [
  {"id": "p1", "title": "Jacket", "price": "$89.00", "image": "https://..."}
]}
```

### Mixed (both in same array):
```json
{"products": [
  {"productId": "gid://shopify/Product/123", "featured": true},
  {"id": "p2", "title": "Static Product", "price": "$29.00", "image": "https://..."}
]}
```

**Resolution rule**: items with `productId` but no `title` get fetched. Items already having `title` pass through untouched. Layout hints (`featured`, etc.) are preserved after resolution.

## Composition

- Pair with: ProductHero (above), ReviewCarousel (below for social proof), StickyBar
- Use `--lx-surface-alt` background to contrast with hero section above
- Never place immediately after another grid island — insert editorial or testimonial between
- tripleCenter works best for hero-product + flanking variants; quad for collection browsing
