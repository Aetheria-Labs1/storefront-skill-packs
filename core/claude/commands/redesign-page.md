---
description: Redesign an existing page while preserving SEO and performance
allowed-tools: mcp__lexsis-ai__*
---

# /redesign-page

Redesign an existing page while preserving SEO and performance

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

# Page Redesign (Modernize/Refresh Existing Page)

Visually refresh an existing page using performance data to preserve what works and redesign what does not.

## Prerequisites

- Target page exists (published or draft)
- Brand kit up to date (may have changed since page creation)
- Page analytics available for performance-informed decisions

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
get_design_md()                  → brand brief, design philosophy, constraints
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
find_page({ query: "page name or slug" })
```
Or:
```
list_pages({ status: "published" })
```

Then load full page data:
```
get_page(page_id)
inspect_page_sections(page_id)
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
get_page_analytics(page_id)
```

Categorize each section:
- **KEEP** — high CVR, proven copy, minor visual polish only
- **REDESIGN** — same content, new layout/styling
- **REPLACE** — low-performing, rebuild approach
- **REMOVE** — adds friction, no conversion value

Key rule: NEVER redesign sections that are converting well. Analytics data overrides aesthetic preferences.

### Step 4 — Apply Section-by-Section Updates

For each section to change:
```
update_page_section(page_id, section_id, { html, css, settings })
```

For reordering (if scroll-depth data suggests better flow):
```
move_page_section(page_id, section_id, new_position)
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
validate_vibe_page(page_id)
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
diff_page_versions(page_id, { from: previous_version, to: current_version })
```

Present structural diff to user for approval before publishing.

### Step 7 — Publish Draft and Visual Verification

```
publish_page(page_id, { draft: true })
```

Returns `preview_url`.

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify."

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues found: `update_page_section` to fix, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
publish_page(page_id)
```

If redesign later hurts metrics: `rollback_page_version(page_id, version_id)` is available.

## Decision Points

| Question | Decision |
|----------|----------|
| Full rebuild or section-by-section? | >70% sections changing = full rebuild is faster |
| Keep copy or rewrite? | Keep unless analytics show messaging problems |
| Preserve section order? | Yes, unless scroll-depth shows clear drop-off pattern |
| Same section types or new? | Prefer new layouts for freshness; same types if copy fits |
| A/B test old vs new? | Recommend if page has >500 daily visitors |

## Quality Gates

- URL/slug PRESERVED (never change -- breaks SEO and ad links)
- Page title and meta description preserved unless explicitly requested
- High-CVR sections retain their copy and core structure
- New design matches current brand kit (`--lx-*` variables)
- Mobile responsiveness maintained or improved
- All existing islands remain functional
- Version history intact (rollback available)
- Page passes `validate_vibe_page` with zero errors


