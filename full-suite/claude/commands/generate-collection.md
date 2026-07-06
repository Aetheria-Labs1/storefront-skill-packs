---
description: Generate a collection/category page with filterable product grid
allowed-tools: mcp__lexsis-ai__*
---

# /generate-collection

Generate a collection/category page with filterable product grid

## Prerequisites

Connect the Lexsis AI MCP server:
```json
{
  "mcpServers": {
    "lexsis-ai": {
      "type": "http",
      "url": "https://mcp.trylexsis.com/mcp",
      "headers": { "Authorization": "Bearer <your-api-key>" }
    }
  }
}
```

## Loaded Knowledge

### storefront-craft

# Storefront Craft Guide — Start Here
Load this skill first on any storefront page generation task.
## Architecture: Vibe-Code
Pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. No component JSON. No blueprint system. The AI generates HTML directly.
## Skills Map
| Skill | Purpose | Load when... |
|---|---|---|
| `craft-guide` | This file — architecture, flow, quality bar | Always first |
| `workflow-orchestration` | Tool sequencing, parallelization, flow selection | Always — load after craft-guide |
| `conversion-psychology` | Universal persuasion: pricing, urgency, trust, CTA psychology | Always — load for any ecommerce page |
| `animation-system` | CSS animations, scroll-reveal, headline effects | Adding motion to sections |
| `visual-craft` | Typography, spacing, color, micro-interactions | Polishing visual quality |
| `design-enrichment` | AI image generation + compositing pipeline | Need custom images/textures |
| `premium-patterns` | Proven high-converting section patterns in HTML | Building hero, trust, CTA sections |
| `island-patterns` | Per-island wrapper HTML + combination recipes | Using commerce/engagement islands |
| **Verticals** | | |
| `vertical-beauty` | Beauty/skincare: ingredient storytelling, before/after, editorial | Beauty, skincare, haircare, fragrance |
| `vertical-supplements` | Supplements: dark mode, clinical proof, comparison, urgency | Vitamins, protein, nootropics, fitness |
| `vertical-fashion` | Fashion: editorial layouts, lookbook grids, dramatic type | Clothing, shoes, accessories, streetwear |
| `vertical-food` | Food/bev: sensory photography, warm palettes, subscription | Food, coffee, snacks, meal kits |
| `vertical-luxury` | Luxury: restraint, whitespace, minimal sections, quiet CTAs | Jewelry, watches, designer, AOV>$300 |
| `vertical-home` | Home: room context, dimensions, material stories | Furniture, decor, candles, textiles |
| **Traffic Sources** | | |
| `traffic-source-meta` | Meta ads: message match, mobile-first, trust stacking | Facebook/Instagram ad landing pages |
| `traffic-source-google` | Google: intent matching, info density, CompareTable, FAQ | Google Ads/SEO landing pages |
| `traffic-source-tiktok` | TikTok: 3-sec hook, video-first, UGC aesthetic, 6-8 sections | TikTok/Reels/Shorts traffic |
| **Workflows** | | |
| `reference-pdp-remix` | Competitor PDP deconstruction and rebuild | Rebuilding a reference URL for your brand |
## Generation Flow (Overview)
```
1. get_storefront_skills({ brief, page_type }) → system prompt, island catalog, schema
2. [Optional] search_design_library() → find existing brand assets
3. [Optional] generate_asset(prompt, style, purpose) → get image URLs
4. Agent generates VibePage JSON (HTML+Tailwind per section)
5. validate_vibe_page({ page }) → structural + security check
6. write_vibe_page({ slug, page }) → persist to renderer
7. preview_vibe_page({ slug }) → get preview URL
```
## CSS Variables (Brand Theming)
All sections use these CSS custom properties (set in `theme_css`):
## Quality Bar
**Great page:**
- Mobile-first (works at 375px, enhances at lg:)
- Uses CSS vars for all brand colors/fonts (no hardcoded hex)
- Proper heading hierarchy (h1 → h2 → h3)
- Islands for all interactive commerce (BuyBox, Cart, Reviews)
- Generated/library images — no broken placeholder URLs in production
- Smooth scroll reveal on key sections
- Trust signals near purchase points
- Sticky add-to-cart on PDP
## Anti-Patterns (NEVER do these)
1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline gradients/colors
5. **No duplicate section IDs** — each must be unique kebab-case
6. **No `<script src="...">` in HTML** — use section `js` field for vanilla JS
7. **No framework code** — no React/Vue/Angular in section HTML (islands handle interactivity)
8. **Don't fake commerce** — always use BuyBox island for add-to-cart, never a plain button
## Section ID Naming
Use descriptive kebab-case: `hero`, `product-gallery`, `social-proof`, `ingredients`, `faq`, `sticky-cta`, `trust-badges`, `footer`. Never `section-1`, `section-2`.
## Island Rules
- `data-props` must be valid JSON in single-quoted attribute
- Only use valid island names (26 total — call `get_island_catalog` to see them)
- One `BuyBox` per page (multiple breaks cart state)
- One `CartDrawer` per page
- `StickyBar` needs `triggerOffset` — distance in px before it appears
- `ReviewCarousel` can use custom reviews array OR fetch from Shopify via productId
## Tailwind Usage
- CDN included in renderer — all utility classes available
- Use responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`
- Prefer utilities over custom CSS (only use section `css` for keyframes/animations)
- Use `clamp()` for fluid typography: `text-[clamp(2rem,5vw,4rem)]`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`
## Image Strategy
1. **Always check `search_design_library` first** — brand's uploaded assets are free and on-brand
2. **Use `list_products` for product images** — never generate fake product shots
3. **`generate_asset` for custom imagery** — hero backgrounds, lifestyle contexts, textures
4. **`edit_asset` for composites** — product-on-background, texture overlays
5. **Place URLs directly in HTML** — `<img src="${url}" />` or inline `style="background-image: url(...)"`
6. **Load `design-enrichment` skill** for full asset generation pipeline details

### island-patterns

# Island Patterns — Wrapper HTML & Combination Recipes
How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.
## Island Embedding Rules
1. `data-island` attribute = exact island name (case-sensitive)
2. `data-props` = valid JSON in **single-quoted** attribute value
3. One `BuyBox` per page (multiple breaks cart state)
4. One `CartDrawer` per page (place in first section or separate section)
5. Islands hydrate client-side — surrounding HTML renders immediately (SSR)
6. Never put islands inside other islands
7. Always wrap in a containing section with proper spacing
## Commerce Islands
### BuyBox — Primary Purchase Action
## Social Proof Islands
### ReviewCarousel — Customer Reviews
## Content Islands
### FAQ — Accordion Questions
## Engagement Islands
### IngredientExplorer — Interactive Ingredients
## Common Combinations
### PDP Core (minimum viable PDP)
## Data-Props Formatting Rules
1. **Single quotes** around attribute value: `data-props='...'`
2. **Double quotes** inside JSON: `{"key":"value"}`
3. **No apostrophes** in text values — use `'` or rephrase
4. **No line breaks** in data-props — must be one line
5. **Numbers without quotes**: `{"qty":2,"discount":10}`
6. **Booleans without quotes**: `{"autoPlay":true}`
7. **Arrays**: `{"items":[{...},{...}]}`
## PDP Template Recipes
### DTC Beauty PDP
## New PDP Islands (v2)
### ProductHero — Split-Layout PDP Hero
## Navigation Islands — Hydration Mode (Preferred)
Navigation islands (Navbar, Footer, SiteHeader) support **hydration mode**: you generate ANY HTML/CSS, then place `data-lx-*` tags on functional elements. The island attaches behavior (cart state, mobile toggle, newsletter) without touching your design.

## Workflow

# Collection / Category Page Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate browsable product listing pages. Grid-focused with EditorialProductGrid island. Quick-add buttons add +15% add-to-cart from grid. Consistent card aspect ratios prevent layout shift. Mid-grid promotional cards every 6-8 products drive AOV.

## Triggers

"collection page", "category page", "product grid", "shop all", "PLP", "product listing"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation + breadcrumb (REQUIRED island)
2. Hero Banner         — collection title + description (max 300px desktop, 200px mobile)
3. Filter/Sort Bar     — collapsible sidebar desktop, bottom sheet mobile
4. Product Grid        — EditorialProductGrid island (the star of the page)
5. Mid-Grid Promo      — promotional card every 6-8 products
6. Social Proof        — compact trust bar below grid
7. Newsletter          — compact single-line signup
8. Footer              — full nav + payment icons (REQUIRED island)
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details   → workspace ID, plan tier
get_connected_stores    → store domain, Shopify data
get_brand_kit           → logo, fonts, colors, voice, border radius
get_design_md           → brand brief, design philosophy, don'ts
```

Then page-specific:
```
get_navigation          → navbar/footer links, collection hierarchy, breadcrumb
list_products           → all products in target collection (titles, prices, images, variants, tags)
```

Critical extractions from `list_products`:
- Product count (determines pagination: "Load More" at 12+ products)
- Available filter dimensions: price range, product type, color, size, tags
- Variant data per product (for color swatches on cards)
- Sale/compare-at prices (for badge display)

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate full page as plain HTML + Tailwind. Mark island positions:

```html
<!-- SiteHeader placeholder -->
<div data-placeholder="SiteHeader" class="h-16 border-b">
  Navigation + breadcrumb renders here
</div>

<!-- Product Grid placeholder -->
<div data-placeholder="EditorialProductGrid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 min-h-[600px]">
  Product cards render here
</div>

<!-- Footer placeholder -->
<div data-placeholder="Footer" class="bg-gray-900 text-white py-12">
  Footer renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Grid is the STAR — hero banner stays short (max 300px desktop, 200px mobile)
- Tighter section padding than other page types: `py-8 md:py-12`
- Consistent card aspect ratios (1:1 or 3:4) with `object-fit: cover`
- Product titles truncated to 2 lines max (prevent layout break)
- Price always visible on card (never hidden behind interaction)

## Phase 2B — Island Mapping

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **EditorialProductGrid** (REQUIRED) | Section 4 | `list_products` → products array |
| **Footer** (REQUIRED) | Section 8 | `get_navigation` → footer links |

```html
<!-- EditorialProductGrid -->
<div data-island="EditorialProductGrid" data-props='{"products":[{"id":"p1","title":"...","price":"$29.99","compareAtPrice":"$39.99","image":"...","secondImage":"...","variants":[{"color":"Black","swatch":"#000"},{"color":"White","swatch":"#fff"}],"badge":"Sale","quickAdd":true}],"columns":{"mobile":2,"tablet":3,"desktop":4},"quickAddEnabled":true,"promoCard":{"position":7,"title":"Buy 2, Get 1 Free","image":"...","href":"/collections/bundles"}}'></div>
```

Use `vibe://schema/island/EditorialProductGrid` for exact prop shape.

## Responsive Grid Columns

| Viewport | Columns | Card Min Width | Gap |
|----------|---------|----------------|-----|
| Mobile (< 640px) | 2 | ~160px | 12px |
| Tablet (640-1024px) | 3 | ~200px | 16px |
| Desktop (> 1024px) | 4 | ~280px | 20px |

## Product Card Anatomy

Every card MUST include:
1. **Image** — consistent aspect ratio (3:4 recommended), `object-fit: cover`
2. **Hover image** — second product image on hover (desktop only)
3. **Title** — truncated to 2 lines, `--lx-font-heading`
4. **Price** — always visible; if on sale: `<s>$39.99</s> $29.99` in accent color
5. **Color swatches** — small dots if product has color variants (max 5 visible + "+3")
6. **Quick-add button** — appears on hover (desktop) or always visible (mobile)
7. **Badge** — "New", "Sale", "Bestseller" positioned top-left

### Quick-Add Behavior (+15% add-to-cart from grid)
- Single-variant products: "Add to Cart" button adds directly
- Multi-variant products: "Choose Options" links to PDP
- On success: "Added!" micro-feedback animation (checkmark morph, 300ms)
- Never interrupt browsing with full-page redirects

## Mid-Grid Promotional Card

Insert after every 6-8 products (spans full grid width):
- Brand accent color background (`--lx-accent-color`)
- Promotional message: bundle deal, free shipping threshold, seasonal sale
- Single CTA button with contrasting color
- Different visual weight from product cards (clearly promotional, not confusable)

Example placements:
- Position 7: "Buy 2, Get 1 Free" bundle promo
- Position 14: "Free shipping on orders over $75" threshold nudge
- Position 21: "Subscribe & Save 20%" for consumables

## Filtering UX

### Desktop — Collapsible Sidebar
- Left sidebar (240px width) with filter groups
- Each group expandable/collapsible (accordion pattern)
- Active filters shown as removable chips above grid
- "Clear All" link when filters active
- Product count updates: "Showing 12 of 48 products"

### Mobile — Bottom Sheet
- "Filter" button in sticky bar triggers bottom sheet modal
- Full-screen overlay with filter groups
- "Apply Filters (12)" button shows result count
- "Clear" link in sheet header
- Sort dropdown: separate from filters, always accessible

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: grid renders, cards aligned, images consistent, quick-add visible
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL.
**Other IDEs:** "Preview: {url} — verify grid layout at 375px, 768px, 1280px"

### Verification Checklist
- [ ] Grid renders with correct column count per breakpoint
- [ ] All product images same aspect ratio (no layout jank)
- [ ] Prices visible on every card (including sale strikethrough)
- [ ] Quick-add buttons functional (hover on desktop, visible on mobile)
- [ ] Color swatches display correctly (not overflowing card)
- [ ] Mid-grid promo card visually distinct from product cards
- [ ] Filter bar sticky on scroll (desktop)
- [ ] Breadcrumb: Home > Collections > [Name] correct
- [ ] Mobile: 2-col grid, no horizontal overflow
- [ ] Brand colors via `--lx-*` variables applied

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Collection-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Quick-add buttons on grid | +15% add-to-cart | Shopify 2026 |
| Consistent card aspect ratios | Prevents CLS (must be <= 0.1) | Web.dev |
| Price visible on card | Table stakes (hidden price = lost sale) | Baymard |
| "Added!" micro-feedback | Peak-end rule — reward moment | Material Design 3 |
| Mid-grid promo card | AOV lift via threshold/bundle nudge | Marine Layer pattern |
| Hover second image | +engagement, reduces PDP bounce rate | Fashion industry std |
| 2-col mobile grid | Optimal for thumb browsing | Apple HIG (48px targets) |
| Short hero (< 300px) | Grid is the star — don't bury it | Baymard |
| Breadcrumb navigation | Reduces bounce, aids discovery | NNGroup |
| Load More (vs pagination) | Lower friction continuation | Infinite scroll without losing context |

## Section CSS Pattern

```html
<!-- Tighter padding for collection pages — grid density matters -->
<section id="collection-grid" class="py-8 md:py-12 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Grid content -->
  </div>
</section>
```


