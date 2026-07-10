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

## Product Resolution

Products array supports Shopify GID references. Renderer auto-fetches name/image/price from Shopify at hydration time.

### Unresolved (preferred — fresh data):
```json
{"products": [
  {"productId": "gid://shopify/Product/123"},
  {"productId": "gid://shopify/Product/456"}
], "features": [{"name": "Material", "values": ["Cotton", "Polyester"]}]}
```

### Resolved (static — backward compat):
```json
{"products": [
  {"name": "Basic", "image": "/basic.jpg", "price": "$29"},
  {"name": "Pro", "image": "/pro.jpg", "price": "$49"}
], "features": [...]}
```

**Resolution rule**: items with `productId` but no `name` get fetched → maps to `{name, image, price}`. Items already having `name` pass through. `features[]` is purely declarative — never resolved from Shopify.

## Composition

- Place mid-to-lower page, after product introduction and before CTA
- Pair with: BuyBox (below table), TrustBadgeBar, FAQ
- Side-by-side works best with 2-3 products (scrolls horizontally on mobile)
- Feature-matrix is ideal for "us vs competitors" pages
- Compact variant is for focused head-to-head (landing pages, ads)
- Highlight the winning product with accent border (feature-matrix layout)
- Keep features list to 5-8 rows for scannability
