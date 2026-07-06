# Cart System — Island Directory

Composed cart drawer using DrawerShell + CartLines + CartCheckoutButton + CartProgressBar + CartSummary (Cart V2).

## Files

| File | Purpose |
|------|---------|
| `layouts/drawer-right.json` | Standard right-side slide-out drawer |
| `layouts/bottom-sheet.json` | Mobile bottom sheet pattern |
| `layouts/mini-cart.json` | Dropdown mini-cart (compact, no full drawer) |

## Quick Reference

- **Variants**: DrawerShell (none), CartLines (compact, full), CartCheckoutButton (filled, outline), CartProgressBar (none), CartSummary (none)
- **Required prop**: `DrawerShell.triggerId` (element ID that opens drawer)
- **Schema**: `vibe://schema/island/DrawerShell`, `vibe://schema/island/CartLines`, `vibe://schema/island/CartCheckoutButton`, `vibe://schema/island/CartProgressBar`, `vibe://schema/island/CartSummary`
- **Layouts**: `vibe://islands/cart-system/layouts/{name}`
- **Contract**: follows `_contract.md`

## Composition

- Max 1 DrawerShell per page (in a hidden section)
- CartProgressBar sits at the top of the drawer (shows free shipping threshold)
- CartLines fills the scrollable middle area
- CartSummary + CartCheckoutButton anchor to the bottom
- DrawerShell is triggered by BuyBox or Navbar cart icon — ensure `triggerId` matches
- The entire section uses `class="hidden"` since it is invisible until triggered
- Template vars: `{{FREE_SHIPPING_THRESHOLD}}` (cents), `{{CTA_TEXT}}`
