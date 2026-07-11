# TrustBadgeBar — Island Directory

Displays trust signals (shipping, returns, guarantees) as icon+text badges in compact layouts.

## Files

| File | Purpose |
|------|---------|
| `layouts/horizontal-icons.json` | Row of badges centered with border-top/bottom dividers |
| `layouts/vertical-stack.json` | Stacked vertically for sidebar placement next to BuyBox |
| `layouts/inline.json` | Single-line text-only badges for compact below-CTA placement |

## Quick Reference

- **Variants**: default, compact, inline
- **Required prop**: `badges` (JSON array of `{icon, text}`)
- **Schema**: `vibe://schema/island/TrustBadgeBar`
- **Layouts**: `vibe://islands/trust-badge-bar/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place within 200px (1 scroll) of primary CTA per contract rules
- `horizontal-icons` — standalone section, good between BuyBox and reviews
- `vertical-stack` — inline within BuyBox sidebar column (not a standalone section)
- `inline` — directly below BuyBox CTA button (not a standalone section)
- Default badges: `[{"icon":"truck","text":"Free Shipping"},{"icon":"refresh-cw","text":"30-Day Returns"},{"icon":"shield-check","text":"Secure Checkout"}]`
