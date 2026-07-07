---
description: Generate or modify the Cart V2 drawer — add upsells, progress bars, conditional rules
allowed-tools: mcp__lexsis-ai__*
---

# /setup-cart

Generate or modify the Cart V2 drawer — add upsells, progress bars, conditional rules

## Workflow

# Cart V2 Composition — DrawerShell + Atomic Islands

How to compose a rich, customizable cart drawer using Cart V2 atomic islands. Load when generating PDP or landing pages for stores with `cart_v2` enabled.

---

## When to Use Cart V2 vs V1

- **Cart V1 (CartDrawer):** Simple stores, no customization needed. One island, done.
- **Cart V2 (DrawerShell):** Premium brands wanting custom cart design, conditional upsells, progress bars, discount inputs. Full design freedom.

**Check:** If store has `cart_v2` in purposes → use Cart V2. Set `head.use_cart_v2 = true`.

---

## Required Structure

Cart V2 pages set `head.use_cart_v2: true` ONLY — no cart section in the page sections array.

The cart drawer lives in **store config** (`pcx_store_config.cart_section_html`), shared across all pages. This means:

- One cart configuration applies to ALL pages in the store
- The renderer automatically injects the cart HTML after page sections at render time
- You manage the cart using `get_cart_config` and `update_cart_config` MCP tools
- Pages only need the flag in their head — the cart HTML is NOT part of the page blueprint

**Page head requirement:**
```jsonc
{
  "head": {
    "title": "...",
    "use_cart_v2": true
  }
}
```

**Store config structure** (managed via MCP tools):
```html
<div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open"}'>
  <!-- Your custom layout here -->
  <div data-island="CartLines" data-props='{"showQuantity":true,"showRemove":true}'></div>
  <div data-island="CartSummary" data-props='{}'></div>
  <div data-island="CartCheckoutButton" data-props='{"text":"Checkout"}'></div>
</div>
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


# Cart V2 Management — MCP Tool Reference

How to generate, update, and manage Cart V2 configurations via MCP tools. Use these when the user asks to set up, modify, or configure their cart drawer behavior.

---

## Architecture

```
pcx_store_config (store-level):
├── cart_mode          — "drawer-right" | "drawer-left" | "bottom-sheet" | "modal" | "fullscreen"
├── cart_section_html  — The full DrawerShell HTML (global cart for all pages)
├── cart_rules[]       — Conditional show/hide rules (evaluated at runtime)
└── commerce_config    — Settings (threshold, currency, width, animation, checkout_mode)

pcx_page.head (page-level override):
├── use_cart_v2: true  — Flag to use V2 instead of auto-injected V1
└── cart_rules[]       — Page-specific rule overrides (merge with store-level)
```

---

## Workflow (ALWAYS follow this order)

1. **READ** — Call `get_cart_config` to see current state (cart_section_html, cart_rules, commerce_config)
2. **PARSE** — Understand what elements exist, what rules are active
3. **MODIFY** — Add/remove elements or rules as needed
4. **VALIDATE** — Call `validate_cart_rules` if rules changed
5. **WRITE** — Call `update_cart_config` to persist changes

**NEVER** write cart HTML directly into page sections. **NEVER** inline a DrawerShell in the sections array.
The page only needs `head.use_cart_v2: true` — the renderer handles injection from store config.

---

## Tools

### `get_cart_config`

Read the current cart configuration for a store. ALWAYS call this before making modifications.

**Input:** `workspace_id` (optional — resolved automatically)

**Returns:**
```json
{
  "cart_mode": "drawer-right",
  "cart_section_html": "<div data-island=\"DrawerShell\" ...>...</div>",
  "cart_rules": [...],
  "commerce_config": {...}
}
```

Returns `null` for `cart_section_html` if cart has not been generated yet.

---

### `generate_cart_v2`

Generate the initial `cart_section_html` for a store. Call ONCE when Cart V2 is first enabled.

**API:** `PATCH /api/v1/storefront/stores/{store_id}/config`

**Payload pattern:**
```json
{
  "cart_mode": "drawer-right",
  "cart_section_html": "<div data-island=\"DrawerShell\" ...>...</div>",
  "commerce_config": {
    "free_shipping_threshold": 9900,
    "currency": "INR",
    "cart_style": { "mode": "drawer-right", "responsive": { "mobile": "bottom-sheet" }, "width": "420px", "animate": "spring" },
    "checkout_mode": "standard"
  }
}
```

**Template for cart_section_html:**
```html
<div data-island="DrawerShell" data-island-container data-props='{"mode":"{{MODE}}","responsive":{"mobile":"{{MOBILE_MODE}}"},"width":"{{WIDTH}}","animate":"{{ANIMATE}}","trigger":"cart:open"}'>
  <!-- Always visible -->
  <div data-island="CartProgressBar" data-props='{"threshold":{{THRESHOLD}}}'></div>
  <div data-island="CartLines" data-props='{"showQuantity":true,"showRemove":true}'></div>
  <div data-island="CartSummary" data-props='{}'></div>
  <div data-island="CartCheckoutButton" data-props='{"text":"Checkout"}'></div>

  <!-- Conditional elements (hidden by default, rules show them) -->
  <div id="cart-discount" class="hidden">
    <div data-island="CartDiscountInput" data-props='{}'></div>
  </div>
</div>
```

---

### `update_cart_section`

Add or remove elements from `cart_section_html`. Always pair with a rule when adding hidden elements.

**Adding an upsell block:**
1. Parse current `cart_section_html`
2. Insert before `CartSummary`:
```html
<div id="upsell-{{ID}}" class="hidden">
  <div data-island="ProductCard" data-props='{"productId":"{{SHOPIFY_GID}}"}'></div>
</div>
```
3. Add corresponding rule (see `update_cart_rules`)
4. Save via PATCH

**Removing an element:**
1. Parse current `cart_section_html`
2. Remove the `<div id="{{ID}}">` block
3. Also remove the matching rule from `cart_rules`
4. Save via PATCH

---

### `update_cart_rules`

Add, modify, or delete rules in `cart_rules[]`.

**Rule structure:**
```json
{
  "id": "upsell-vitc-serum",
  "conditions": {
    "op": "AND",
    "clauses": [
      { "field": "cart.has_product_id", "op": "eq", "value": "gid://shopify/Product/123" }
    ]
  },
  "action": { "type": "show", "target": "#upsell-vitc-serum" },
  "priority": 10
}
```

**IMPORTANT: Always use product GIDs, not string types/tags.**

| Condition Field | Type | Use |
|----------------|------|-----|
| `cart.has_product_id` | string (GID) | Specific product in cart |
| `cart.has_variant_id` | string (GID) | Specific variant in cart |
| `cart.subtotal` | number (cents) | Cart value threshold |
| `cart.item_count` | number | Number of unique items |
| `cart.total_quantity` | number | Total quantity across all items |
| `cart.discount_applied` | boolean | Any discount active |
| `device.type` | "mobile" / "desktop" | Device targeting |

**Action types:**
| Type | Effect | Target |
|------|--------|--------|
| `show` | Remove `hidden` class | CSS selector (e.g., `#upsell-vitc-serum`) |
| `hide` | Add `hidden` class | CSS selector |
| `swap_props` | Merge new props into island | `[data-island="IslandName"]` |
| `add_class` | Add CSS class | CSS selector |

---

### `set_page_cart_overrides`

Write page-level rule overrides. Use when a specific landing page needs different cart behavior.

**API:** `PATCH /api/v1/storefront/pages/{page_id}`

**Payload:**
```json
{
  "head": {
    "use_cart_v2": true,
    "cart_rules": [
      { "id": "upsell-skincare", "disabled": true },
      { "id": "page-summer-offer", "conditions": {...}, "action": {...} }
    ]
  }
}
```

**Merge behavior:**
- Page rules with same `id` as store rules → override them
- `{ "id": "x", "disabled": true }` → suppresses store-level rule on this page
- New IDs → appended (active only on this page)

---

## Common Patterns

### Pattern 1: Upsell for specific product

User says: "When someone adds the Vitamin C Serum, recommend the Moisturizer"

1. Add hidden block to `cart_section_html`:
```html
<div id="upsell-vitc" class="hidden">
  <p class="text-xs font-medium px-4 pt-3">Complete your routine</p>
  <div data-island="ProductCard" data-props='{"productId":"gid://shopify/Product/789"}'></div>
</div>
```

2. Add rule:
```json
{
  "id": "upsell-vitc",
  "conditions": { "op": "AND", "clauses": [
    { "field": "cart.has_product_id", "op": "eq", "value": "gid://shopify/Product/123" }
  ]},
  "action": { "type": "show", "target": "#upsell-vitc" }
}
```

### Pattern 2: Free shipping progress

Already in the cart by default (CartProgressBar island). Rule shows it when below threshold:
```json
{
  "id": "free-shipping-bar",
  "conditions": { "op": "AND", "clauses": [
    { "field": "cart.subtotal", "op": "lt", "value": 9900 }
  ]},
  "action": { "type": "show", "target": "#free-shipping-bar" }
}
```

### Pattern 3: Disable upsell on specific page

Landing page for haircare should not show the skincare upsell:
```json
// In page.head.cart_rules:
{ "id": "upsell-skincare", "disabled": true }
```

### Pattern 4: Mobile-only discount field

```json
{
  "id": "mobile-discount",
  "conditions": { "op": "AND", "clauses": [
    { "field": "device.type", "op": "eq", "value": "mobile" }
  ]},
  "action": { "type": "show", "target": "#cart-discount" }
}
```

---

## Validation Rules

1. Every hidden element in `cart_section_html` MUST have a corresponding rule in `cart_rules` — otherwise it's permanently hidden (dead code).
2. Every rule's `target` MUST match an `id` attribute in `cart_section_html` — otherwise the rule does nothing.
3. Use product GIDs (`gid://shopify/Product/XXX`), never string labels for product matching.
4. Subtotal values are in **cents** (e.g., $50 = 5000, ₹99 = 9900).
5. Rule `id` should match the element `id` it targets (convention, not enforced).


