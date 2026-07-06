# Island Design Contract

Rules every island wrapper MUST follow. Violations = visual clashing between sections.

---

## Spacing

| Context | Class | Value |
|---------|-------|-------|
| Section wrapper vertical | `py-12 md:py-16 lg:py-20` | 48/64/80px |
| Between islands in same section | `space-y-6` or `gap-8` | 24/32px |
| Section heading to content | `mb-8 md:mb-12` | 32/48px |

Islands don't add outer margin. Wrapper controls position.

## Container Widths

| Island Type | Max Width | Class |
|-------------|-----------|-------|
| Full-bleed (hero, gallery bg) | none | `w-full` |
| Commerce (BuyBox, grid, cards) | 7xl (80rem) | `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` |
| Content (FAQ, text, email) | 3xl (48rem) | `max-w-3xl mx-auto px-4` |
| Navigation (nav, footer) | full | `w-full` (internal max-w-7xl) |
| Narrow content (testimonial quote) | 2xl (42rem) | `max-w-2xl mx-auto px-4` |

## Background Rhythm

```
Section 1 (hero):     --lx-bg-color or full-bleed image
Section 2:            --lx-surface-alt
Section 3:            --lx-bg-color
Section 4:            --lx-surface-alt
...alternate...
```

- Never 3+ consecutive sections with same background
- Hero always uses `--lx-bg-color` or image (never surface-alt)
- CTA banner sections: `--lx-accent-color` bg with white text (exception to alternating rule)

Apply via inline style: `style="background-color: var(--lx-surface-alt)"`

## Typography Hierarchy

| Level | Owner | Class | Font |
|-------|-------|-------|------|
| h1 | Hero section ONLY | `text-4xl md:text-5xl lg:text-6xl font-bold` | `--lx-font-heading` |
| h2 | Section headings | `text-2xl md:text-3xl lg:text-4xl font-bold` | `--lx-font-heading` |
| h3+ | Inside islands | Controlled by island — DO NOT OVERRIDE | — |

- One h1 per page (in hero)
- Section h2: centered by default (`text-center`), left-aligned in split layouts
- Supporting text below h2: `text-lg` + `--lx-text-muted` + `max-w-2xl mx-auto`
- Never set font-family in wrapper HTML — use CSS variables only

## Color Constraints

| Element | Allowed Colors |
|---------|---------------|
| Wrapper background | `--lx-bg-color`, `--lx-surface-alt`, transparent, or image |
| Text | `--lx-text-color` (primary), `--lx-text-muted` (secondary) |
| CTA buttons | `--lx-accent-color` bg + white text |
| Borders/dividers | `--lx-border-color` |
| Accent highlights | `--lx-accent-color` (links, badges, active states ONLY) |

NEVER use `--lx-accent-color` as a section background (except CTA banner sections).

## Responsive Rules

- Mobile-first: default styles = mobile, enhance with `sm:` → `md:` → `lg:`
- Grid layouts: `grid-cols-1 lg:grid-cols-2` (stack on mobile)
- Sticky elements: only above lg (`lg:sticky lg:top-24`)
- Full-bleed images: `aspect-[16/9] md:aspect-auto` (constrain mobile, natural desktop)
- Touch targets: min 44x44px on mobile
- Font sizes never below `text-sm` (14px) on mobile

## Animation Rules

- Use ONLY shared keyframes: `fadeUp`, `fadeIn`, `scaleIn`, `slideInLeft`, `slideInRight`
- Entrance timing: `animation: fadeUp 0.6s ease both`
- Stagger: `animation-delay: calc(var(--i, 0) * 100ms)` with `--i` set per item
- Never animate island internals — only wrapper/surrounding static HTML
- Reduce motion: animations should be subtle (< 20px translation, < 0.5s duration)

## Composition Rules

- Max 1 `BuyBox` per page
- Max 1 `DrawerShell` / `CartDrawer` per page (in hidden section)
- Max 1 `Navbar` / `SiteHeader` per page (first section)
- Max 1 `Footer` per page (last section)
- `TrustBadgeBar`: place within 1 scroll (200px) of primary CTA
- `StickyBar`: triggers when BuyBox scrolls out of viewport — place after BuyBox section
- `ReviewCarousel`: mid-page or after product details (never first section)

## Template Variables in Layout JSONs

Layouts use `{{VARIABLE}}` placeholders. Agent replaces before pasting:

| Variable | Source | Example |
|----------|--------|---------|
| `{{PRODUCT_ID}}` | `get_product` or `list_products` | `gid://shopify/Product/12345` |
| `{{PRODUCT_TITLE}}` | product.title | `Hydrating Serum` |
| `{{PRODUCT_PRICE}}` | product.price | `$29.99` |
| `{{BRAND_NAME}}` | `get_brand_kit` → name | `Glow Labs` |
| `{{CTA_TEXT}}` | page-type or industry skill | `Add to Cart` |
| `{{IMAGE_URL}}` | `search_design_library` or `generate_asset` | `https://cdn...` |
| `{{STORE_DOMAIN}}` | `get_connected_stores` | `mystore.myshopify.com` |
