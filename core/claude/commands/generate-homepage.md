---
description: Generate a brand homepage with navigation and collections
allowed-tools: mcp__lexsis-ai__*
---

# /generate-homepage

Generate a brand homepage with navigation and collections

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

### visual-craft

# Visual Craft — Typography, Spacing, Color & Polish
Techniques for making vibe-code pages look premium. Load when polishing visual quality.
## Typography Hierarchy
### Fluid Sizing (clamp)
## Spacing Rhythm
### Section Padding
## Color Usage
### Accent Application
## Image Treatment
### Rounded + Shadow (product cards)
## Micro-Interactions
### Button States
## Glass Morphism
```html
<div class="backdrop-blur-md rounded-2xl p-6 border border-white/20" style="background:rgba(255,255,255,0.1)">
  Frosted glass card
</div>
```
## Grain/Noise Texture
```css
.grain::before {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  pointer-events: none;
}
```
## Responsive Patterns
### Grid Collapse

## Workflow

# Brand Homepage Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate brand-first homepages. Navigation-driven, multi-CTA, storytelling-focused. Category grid adds +18% engagement. Featured products carousel drives discovery. Navbar + Footer islands REQUIRED.

## Triggers

"homepage", "home page", "main page", "front page", "store home"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation (REQUIRED island)
2. Hero                — brand lifestyle visual + value prop CTA
3. Categories Grid     — +18% engagement vs flat product list
4. Bestsellers         — featured products carousel (social proof via "popular")
5. Brand Story         — editorial mid-page (founder, mission, craft)
6. Testimonials        — 3 reviews with real names/photos (+22% CVR)
7. Trust Bar           — press logos + certifications (3-5 max)
8. Newsletter          — email capture with incentive ("10% off first order")
9. Footer              — full nav columns + legal + social (REQUIRED island)
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details   → workspace ID, plan tier
get_connected_stores    → store domain, Shopify data
get_brand_kit           → logo, fonts, colors, voice, brand story
get_design_md           → brand brief, design philosophy, positioning
```

Then page-specific:
```
get_navigation          → header nav links, footer columns, collection hierarchy
list_products           → identify bestsellers, new arrivals, featured items
```

`get_navigation` is CRITICAL for homepages — it provides the full site structure.

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate full page as plain HTML + Tailwind. Mark island positions:

```html
<!-- Navbar placeholder -->
<div data-placeholder="SiteHeader" class="h-16 border-b border-gray-200">
  Navigation renders here
</div>

<!-- Product grid placeholder -->
<div data-placeholder="EditorialProductGrid" class="min-h-[400px] grid grid-cols-2 md:grid-cols-4 gap-4">
  Product cards render here
</div>

<!-- Footer placeholder -->
<div data-placeholder="Footer" class="bg-gray-900 text-white py-12">
  Footer renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Multiple CTAs to DIFFERENT destinations (explore, shop, learn — not all same link)
- Full-width hero (lifestyle imagery, not product-only)
- Max-width 7xl for content sections
- Mobile: hamburger nav, single column, touch-friendly targets (48px min)

## Phase 2B — Island Mapping

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **Navbar / SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **Footer** (REQUIRED) | Section 9 | `get_navigation` → footer links, social |
| EditorialProductGrid | Section 4 | `list_products` → bestsellers array |
| EmailCapture | Section 8 | provider, listId, incentive |

```html
<!-- SiteHeader -->
<div data-island="SiteHeader" data-props='{"logo":{"src":"...","alt":"Brand"},"links":[{"label":"Shop","href":"/collections/all"},{"label":"About","href":"/pages/about"}],"cartEnabled":true}'></div>

<!-- Footer -->
<div data-island="Footer" data-props='{"logo":{"src":"..."},"columns":[{"title":"Shop","links":[...]},{"title":"About","links":[...]}],"social":[{"platform":"instagram","url":"..."}],"newsletter":true}'></div>
```

Use `vibe://schema/island/SiteHeader` and `vibe://schema/island/Footer` for exact props.

## Award-Winning Homepage Patterns

### Marine Layer Style (Editorial + Transactional Hybrid)
- Dual-path hero segmentation: "New for Him" / "New for Her"
- "This Just In" horizontal scroll carousel between editorial sections
- Quick-add from grid: hover reveals size selector (reduces clicks to purchase)
- Curated "shops within the shop" (Espresso Edit, Hemp Shop)
- 365-day return policy in announcement bar
- Color swatch visibility on grid cards
- Free shipping threshold in cart drawer

### Orbea Style (Full-Bleed Cinematic)
- Full-viewport video hero with brand manifesto overlay
- Category grid with dramatic overlay text
- Progressive product disclosure through scroll
- Minimal text: 2-5 words per section headline
- Dark background, product provides color
- Geographic identity embedded in narrative

### DTC Wellness (Clean + Trustworthy)
- Soft, warm hero with lifestyle imagery
- Category pills for quick filtering
- Ingredient/process transparency section
- Doctor/expert endorsement mid-page
- Subscription CTA prominent
- Clean whitespace signaling premium positioning

## Homepage-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Category grid (vs flat list) | +18% engagement | Shopify 2026 |
| Featured products carousel | Discovery path creation | Marine Layer pattern |
| Social proof below fold | Acceptable (not critical above fold on homepages) | NNGroup |
| Multiple CTAs (different goals) | Expected on homepages (unlike LPs) | Conversion Rate Experts |
| Announcement bar (shipping/returns) | Reduces cart abandonment anxiety | Route 2026 |
| Newsletter with incentive | 10-15% signup rates | Industry avg |
| Editorial mid-page (brand story) | Increases time-on-site, reduces bounce | Awwwards analysis |

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: nav renders, hero visible, categories grid, footer complete
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL.
**Other IDEs:** "Preview: {url} — verify navigation works, collections display"

### Verification Checklist
- [ ] SiteHeader island renders with navigation links from `get_navigation`
- [ ] Hero communicates brand value prop in 3 seconds (not product-specific)
- [ ] Multiple CTAs go to DIFFERENT destinations (shop, about, collections)
- [ ] Category/collection grid links are functional
- [ ] Featured products show real data (real prices, real titles)
- [ ] Footer renders with all nav columns + social + payment icons
- [ ] Mobile: hamburger nav works, single column, touch-friendly
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Fonts loading (not system fallback)
- [ ] Heading hierarchy: single h1 in hero, h2 per section

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Page Feels Editorial, Not Catalog

The homepage is a BRAND experience. It should feel like a magazine cover, not a product spreadsheet:
- Generous whitespace between sections (py-16 md:py-24 minimum)
- Lifestyle photography > product-on-white
- Copy speaks to identity/values, not just features
- Collections named creatively (not just "Shirts" — "The Weekend Edit")
- Visual rhythm: alternate full-bleed and contained sections
- First and last impressions matter most (Serial Position Effect)


