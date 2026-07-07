---
name: cart-composition
description: DrawerShell + Atomic Islands
---

# Cart V2 Composition — DrawerShell + Atomic Islands

How to compose a rich, customizable cart drawer using Cart V2 atomic islands. Load when generating PDP or landing pages for stores with `cart_v2` enabled.

---

## When to Use Cart V2 vs V1

- **Cart V1 (CartDrawer):** Simple stores, no customization needed. One island, done.
- **Cart V2 (DrawerShell):** Premium brands wanting custom cart design, conditional upsells, progress bars, discount inputs. Full design freedom.

**Check:** If store has `cart_v2` in purposes → use Cart V2. Set `head.use_cart_v2 = true`.

---

## Required Structure

Every Cart V2 page MUST have:

```html
<section class="hidden">
  <div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open"}'>
    <!-- Your custom layout here -->
    <div data-island="CartLines" data-props='{"showQuantity":true,"showRemove":true}'></div>
    <div data-island="CartSummary" data-props='{}'></div>
    <div data-island="CartCheckoutButton" data-props='{"text":"Checkout"}'></div>
  </div>
</section>
```

**Minimum required islands inside DrawerShell:**
1. `CartLines` — shows cart items
2. `CartCheckoutButton` — checkout CTA

**Validation will FAIL without these.**

---

## Available Cart Islands

### Core (required)

| Island | Purpose |
|---|---|
| `CartLines` | Line items with qty controls |
| `CartSummary` | Subtotal/taxes/total |
| `CartCheckoutButton` | Checkout CTA button |

### Enhancements (optional)

| Island | Purpose |
|---|---|
| `CartProgressBar` | Free shipping progress |
| `CartDiscountInput` | Promo code input |
| `CartCrossSell` | Product recommendations |
| `CartAnnouncement` | Conditional messaging |
| `CartOrderNote` | Order notes / gift messages |
| `CartCountdown` | Urgency timer |

### Reusable (from page islands)

`TrustBadgeBar`, `CountdownTimer`, `PaymentOptions` — work inside DrawerShell unchanged.

---

## DrawerShell Modes

```jsonc
{
  "mode": "drawer-right",       // desktop default
  "responsive": {
    "mobile": "bottom-sheet"    // mobile: slide-up with drag handle
  }
}
```

Options: `drawer-right`, `drawer-left`, `bottom-sheet`, `modal`, `fullscreen`, `dropdown`

---

## Composition Patterns by Vertical

### Beauty / Skincare PDP

```html
<section class="hidden">
  <div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open","width":"420px"}'>
    <div class="p-4 border-b bg-gradient-to-r from-pink-50 to-rose-50">
      <div data-island="CartProgressBar" data-props='{"threshold":7500,"message":"Add {remaining} more for a FREE mini!","completedMessage":"You unlocked a FREE mini! Added to cart."}'></div>
    </div>
    <div class="flex-1 overflow-y-auto p-4">
      <div data-island="CartLines" data-props='{"layout":"compact","showQuantity":true,"showRemove":true}'></div>
    </div>
    <div class="p-4 border-t" id="routine-upsell" class="hidden">
      <div data-island="CartCrossSell" data-props='{"source":{"type":"shopify_recs"},"heading":"Complete Your Routine","max":2,"showQuickAdd":true}'></div>
    </div>
    <div class="p-4 border-t">
      <div data-island="CartDiscountInput" data-props='{"placeholder":"Promo code"}'></div>
    </div>
    <div class="p-4 border-t bg-gray-50">
      <div data-island="CartSummary" data-props='{"showTax":false}'></div>
      <div data-island="CartCheckoutButton" data-props='{"text":"Checkout","style":"filled"}'></div>
    </div>
    <div class="px-4 pb-4">
      <div data-island="TrustBadgeBar" data-props='{"badges":[{"icon":"leaf","label":"Clean Beauty"},{"icon":"shield","label":"Dermatologist Tested"},{"icon":"truck","label":"Free Shipping $75+"}]}'></div>
    </div>
  </div>
</section>
```

### Fashion / Apparel PDP

```html
<section class="hidden">
  <div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open"}'>
    <div class="p-4 border-b">
      <div data-island="CartCountdown" data-props='{"duration":900,"message":"Cart reserved for {time}","expiredMessage":"Items may sell out — checkout now"}'></div>
    </div>
    <div class="flex-1 overflow-y-auto p-4">
      <div data-island="CartLines" data-props='{"layout":"full","showQuantity":true,"showRemove":true,"showImage":true}'></div>
    </div>
    <div class="p-4 border-t">
      <div data-island="CartCrossSell" data-props='{"source":{"type":"manual","product_ids":["gid://shopify/Product/ACCESSORY1","gid://shopify/Product/ACCESSORY2"]},"heading":"Style It With","max":3,"layout":"horizontal"}'></div>
    </div>
    <div class="p-4 border-t bg-black text-white">
      <div data-island="CartSummary" data-props='{"showShipping":true}'></div>
      <div data-island="CartCheckoutButton" data-props='{"text":"CHECKOUT","style":"filled"}'></div>
    </div>
  </div>
</section>
```

### Supplements / Wellness PDP

```html
<section class="hidden">
  <div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open"}'>
    <div class="p-4 border-b bg-green-50">
      <div data-island="CartProgressBar" data-props='{"tiers":[{"threshold":5000,"label":"Free shipping"},{"threshold":10000,"label":"10% off"},{"threshold":15000,"label":"Free gift"}]}'></div>
    </div>
    <div class="flex-1 overflow-y-auto p-4">
      <div data-island="CartLines" data-props='{"layout":"compact","showQuantity":true}'></div>
    </div>
    <div class="p-4 border-t" id="subscribe-upsell" class="hidden">
      <div data-island="CartAnnouncement" data-props='{"message":"Subscribe & save 15% on every order","variant":"info"}'></div>
    </div>
    <div class="p-4 border-t">
      <div data-island="CartDiscountInput" data-props='{"placeholder":"Discount code"}'></div>
      <div data-island="CartOrderNote" data-props='{"placeholder":"Any dietary restrictions or notes?","maxLength":200}'></div>
    </div>
    <div class="p-4 border-t">
      <div data-island="CartSummary" data-props='{"showDiscounts":true}'></div>
      <div data-island="CartCheckoutButton" data-props='{"text":"Secure Checkout","style":"filled"}'></div>
    </div>
  </div>
</section>
```

---

## Conditional Rules

Rules control visibility of elements based on cart state. Place in `data-cart-rules` attribute on DrawerShell OR in page `head.cart_rules`.

### Rule Structure

```jsonc
{
  "id": "unique_rule_id",
  "conditions": {
    "op": "AND",
    "clauses": [
      { "field": "cart.subtotal", "op": "lt", "value": 9900 },
      { "field": "cart.item_count", "op": "gte", "value": 1 }
    ]
  },
  "action": {
    "type": "show",
    "target": "#element-id"
  },
  "priority": 10
}
```

### Available Fields

`cart.subtotal`, `cart.item_count`, `cart.total_quantity`, `cart.has_product_tag`, `cart.has_product_type`, `cart.has_product_id`, `cart.discount_applied`, `customer.segment`, `device.type`

### Operators

`eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `contains`, `in`, `not_in`, `exists`

### Actions

- `show` — reveal hidden element
- `hide` — hide visible element
- `swap_props` — override island props
- `add_class` — add CSS class

### Common Rule Patterns

**Free shipping nudge:**
```jsonc
{"id":"ship_nudge","conditions":{"op":"AND","clauses":[{"field":"cart.subtotal","op":"lt","value":7500}]},"action":{"type":"show","target":"#progress-bar"},"priority":100}
```

**Category-specific cross-sell:**
```jsonc
{"id":"skincare_upsell","conditions":{"op":"AND","clauses":[{"field":"cart.has_product_type","op":"eq","value":"Serum"}]},"action":{"type":"show","target":"#routine-upsell"},"priority":50}
```

**High-value cart messaging:**
```jsonc
{"id":"vip_msg","conditions":{"op":"AND","clauses":[{"field":"cart.subtotal","op":"gte","value":20000}]},"action":{"type":"show","target":"#vip-announcement"},"priority":80}
```

---

## CartCrossSell Sources

```jsonc
// AI-curated (static, fastest)
{"source": {"type": "manual", "product_ids": ["gid://shopify/Product/123"]}}

// Shopify recommendations (dynamic, based on cart)
{"source": {"type": "shopify_recs"}}

// From a collection
{"source": {"type": "collection", "collection_handle": "accessories"}}
```

---

## Anti-Patterns

- **Too many islands in cart** → drawer feels cluttered, slow to hydrate. Max 6-7 islands.
- **CartDrawer + DrawerShell on same page** → validation error. Pick one.
- **Missing `data-island-container`** → children hydrate immediately on page load (perf hit).
- **Conflicting rules** → two rules showing/hiding same element. Use priorities.
- **No CartLines or CartCheckoutButton** → validation blocks publish.
- **Rules without matching targets** → silent failure. Always verify `#id` exists in HTML.

---

## Head Config

Always set in page `head` when using Cart V2:
```jsonc
{
  "head": {
    "title": "...",
    "use_cart_v2": true
  }
}
```
