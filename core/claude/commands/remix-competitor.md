---
description: Rebuild a competitor page adapted to your brand
allowed-tools: mcp__lexsis-ai__*
---

# /remix-competitor

Rebuild a competitor page adapted to your brand

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

# Competitor Remix (Rebuild from Reference URL)

Capture a competitor page, decompose its structure, and rebuild it using the user's own brand identity, copy, and products. NEVER copy content -- only structural inspiration.

## Prerequisites

- User provides a reference URL
- Store connected and brand kit configured
- User's own product/content available to replace competitor's

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Capture Reference Design

```
capture_design_source({ url })
```

Screenshots the page and extracts structural layout data.

```
extract_brand_design({ url })
```

Pulls competitor's design DNA: color palette, typography, spacing rhythm, border radius, shadow depth, image treatment style, overall aesthetic (minimal, bold, editorial, etc.).

### Step 3 — Decompose into Section Map

Analyze captured page into numbered section breakdown:
```
1. Full-bleed hero — product centered, headline overlay, gradient wash
2. Trust badge row — 4 icons with micro-labels, centered
3. Split feature section — image left, text right, 50/50
4. Testimonial carousel — 3 cards, star ratings, photos
5. Product grid — 3 columns, hover zoom
6. FAQ accordion — 6 items, expandable
7. Final CTA — full-width, contrasting background
```

For each: note layout pattern, content type, approximate proportions, interactive elements.

### Step 4 — Map to Lexsis Capabilities

For each competitor section:
- Island available? Use `get_island_schema(island_name)` for prop shapes
- Static HTML+Tailwind section? (most common)
- Requires custom interactivity? Flag for JS sandbox

### Step 5 — Source User's Own Assets

```
search_design_library({ query: "<relevant product/category>" })
list_products({ limit: 10 })
```

Replace ALL competitor imagery with user's own assets. Generate new if needed:
```
generate_asset({ prompt: "...", style_reference: "brand_kit" })
```

CRITICAL: NEVER reference, hotlink, or reuse competitor images/copy/logos.

### Step 6 — Two-Phase Generation

**Phase A — Raw HTML + Tailwind (no islands)**

For each section from the decomposition:
- **Structure**: Keep competitor's layout pattern (grid, split, stacked)
- **Brand**: Replace ALL colors/fonts/spacing with user's `--lx-*` variables
- **Content**: Write original copy serving user's value proposition
- **Images**: User's own assets exclusively
- **CTAs**: Aligned with user's conversion goals

Set all brand tokens in `theme_css`:
```css
:root { --lx-accent-color: #...; --lx-font-heading: '...', serif; }
```

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

**Phase B — Island Mapping**

Replace placeholders with hydrated islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"...","answer":"..."}]}'></div>
```

### Step 7 — Validate and Publish Draft

```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { publish: false })
```

Returns `preview_url`.

### Step 8 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify alongside reference."

Checklist:
- [ ] ZERO competitor content carried over (no copy, images, logos)
- [ ] All colors from user's `--lx-*` variables (not competitor palette)
- [ ] Structural similarity recognizable but not pixel-perfect
- [ ] User's brand fonts loading (not system fallback)
- [ ] Mobile layout works independently
- [ ] Islands hydrated with user's own product data
- [ ] Original copy serves user's value proposition

If issues found: `update_page_section` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Keep exact structure or adapt? | Adapt: remove irrelevant sections, add where user has more to say |
| Which sections to skip? | Competitor-specific (their awards, team), navigation that does not fit |
| How close to follow? | Structural only -- proportions, flow, section types |
| Interactive elements? | Map to available islands; static equivalent if no island exists |

## Quality Gates

- ZERO competitor content (copy, images, logos, brand marks)
- Page uses exclusively user's `--lx-*` CSS variables
- All images are user's own or freshly generated
- All product references from user's own catalog
- Copy is original, serving user's value proposition
- Mobile layout independent (do not assume competitor's responsive approach)
- Page passes `validate_vibe_page` with zero errors


