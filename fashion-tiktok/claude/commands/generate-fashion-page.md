---
description: Generate a fashion/streetwear landing page with editorial layouts and lookbook grids
allowed-tools: mcp__lexsis-ai__*
---

# /generate-fashion-page

Generate a fashion/streetwear landing page with editorial layouts and lookbook grids

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

### fashion-expertise

# Fashion & Apparel — Storefront Blueprint Design Intelligence
> **When to load**: Product vertical is fashion, clothing, apparel, shoes, accessories, streetwear, athleisure, or basics. Auto-loads via `vibe://skills/vertical-fashion`.
## The Fashion Page Philosophy
Fashion pages sell **aspiration and identity**, not fabric specs. The page IS the lookbook. Every section should answer **"who will I become wearing this?"**
## VibePage Architecture
Fashion pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. NOT JSON schema.
## Section Sequences (by page type)
### Single Product PDP (8-10 sections)
## Island HTML Patterns
### ProductGallery + VariantSwatches + SizeGuide Stack
## Typography
**DRAMATIC size contrast = editorial feel.**
## Color & Backgrounds
**Monochrome is king. Black + white + ONE accent.**
## Hero Patterns
### Full-Bleed Editorial Hero
## Lookbook Grid (Asymmetric)
**Editorial-style asymmetric grid with CSS Grid:**
## Social Proof / Reviews
**UGC-first, with customer measurements:**
## Anti-Patterns (Fashion Page Killers)
### 1. Product-on-white-only (No Lifestyle)
**Bad**: Only flat-lay white-background shots.  
**Fix**: Lead with on-model editorial. Flat-lays secondary.
## Complete Fashion PDP Blueprint
**Full VibePage JSON for a premium fashion PDP:**
## Summary
Fashion pages are **editorial, image-forward, minimal**. Photography does 80% of the work.

### tiktok-traffic

# TikTok & Short-Form Video → Landing Page — Storefront Design Intelligence
> When to load: Page is being generated for TikTok ad traffic, Instagram Reels traffic, YouTube Shorts traffic, or any short-form video platform.
## Philosophy
**3-second hook or death.** Visitors from TikTok were interrupted mid-scroll. They weren't searching — they were swiping entertainment. Your page has 3 seconds before the back button.
## Mobile-Only Reality
**Every decision flows from mobile-first constraints:**
## Section Sequence (TikTok Formula)
**6-8 sections MAX. Each section = one decision closer to purchase.**
## Hero Patterns
### Pattern 1: Video-First Hero
## Video Integration
**VideoPlayer island placement hierarchy:**
## The TikTok Native Aesthetic
**Raw beats polished.** UGC-style content outperforms studio photography 2-3x for TikTok traffic. Make it feel creator-made.
## Social Proof (TikTok-Style)
**Format principle:** Make it look screenshotted from TikTok/Instagram comments, not designed by marketing.
## CTA Strategy
**Single CTA, repeated everywhere.** Do not confuse with multiple competing actions. One primary CTA on entire page.
## Urgency (When to Use It)
**TikTok traffic = impulse audience.** They arrived mid-scroll, not mid-search. Urgency triggers work exceptionally well.
## Content Rules
**Maximum lengths:**
- Headline: 5 words (4 ideal)
- Subline: 12 words (8-10 ideal)
- Review quote: 80 characters
- FAQ answer: 40 words
- CTA button: 4 words
## Anti-Patterns (TikTok Landing Page Killers)
### 1. Long Pages (>8 Sections)
## Complete Blueprint
### Full 6-Section TikTok Landing Page (VibePage JSON)

### animation-system

# Animation System — Vibe-Code Reference
CSS-only and vanilla JS animations for storefront pages. No framer-motion, no React — pure CSS keyframes + IntersectionObserver for scroll triggers.
## When to Animate vs Not
**Animate:**
- Hero headline on premium/editorial/bold brands
- Section entrances on scroll (fade-up, slide-in)
- Background gradients on dark/vibrant brands
- Stats/numbers counting up
- Floating decorative elements
## Section CSS: Keyframe Animations
Place in section `css` field. Scoped per section.
## Scroll-Triggered Reveal (Section JS)
Use section `js` field. IntersectionObserver fires animation on scroll.
## Headline Effects (CSS-only)
### Word-by-Word Fade
## Background Animations
### Gradient Shift (hero/CTA backgrounds)
## Micro-Interactions (Tailwind transitions)
### Button Hover
```html
<button class="transition-all duration-200 hover:scale-[1.02] hover:shadow-lg active:scale-[0.98]" style="background:var(--lx-accent-color)">
  Shop Now
</button>
```
## Brand Tone → Animation Mapping
| Tone | Level | Recommended |
|---|---|---|
| Luxury/Premium | Subtle, slow | Fade-in-up (0.8s), text-reveal, gradient-text |
| Playful/Bold | Energetic | Stagger, scale-in, floating elements, gradient-shift |
| Clinical/Minimal | Near-zero | Simple fade (0.4s) only |
| Editorial | Refined | Word-by-word, slide-left/right, underline-draw |
| Earthy/Organic | Gentle | Slow fade (1s), parallax, float |
| Tech/DTC | Snappy | Fast stagger (0.08s delay), scale-in |
## Performance Rules
1. Only animate `transform` and `opacity` — never `width`, `height`, `margin`
2. Add `will-change: transform` to heavily animated elements
3. Max 10 keyframe animations per page
4. Accessibility — always include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
5. Scroll observers: `{ passive: true }` and `threshold: 0.15`

## Workflow

# Storefront Page Generation

Generate high-quality Shopify landing pages using the Storefront Blueprint MCP tools.

## Generation Flow (5 Phases)

### Phase 0 — Context Gathering (run ALL in parallel)

```
get_workspace_details    → workspace context
get_connected_stores     → store ID, domain
get_brand_kit            → logo, fonts, colors, voice
get_theme_json           → design tokens (palette, typography, effects)
get_design_md            → brand brief + guidelines
list_products            → product catalog for commerce islands
get_navigation           → navbar/footer links
search_design_library    → existing brand assets
```

### Phase 1 — Asset Generation (parallel per section)

Decision tree per section:
1. `search_design_library` — check existing assets first (ALWAYS)
2. `generate_asset` — only if library has nothing suitable
3. `edit_asset` — composite/modify if needed
4. `view_asset` — verify result before using

### Phase 2 — HTML Generation

Write VibePage JSON with:
- Raw HTML + Tailwind CSS + CSS custom properties
- React islands for commerce (BuyBox, CartDrawer, ProductGallery)
- Responsive mobile-first design
- Brand CSS variables: `--color-accent`, `--color-text`, `--color-bg`, `--font-heading`, `--font-body`

### Phase 3 — Validation

Call `validate_vibe_page` — checks structure, ID uniqueness, islands, CSS/JS security.

### Phase 4 — Publish

Call `publish_vibe_page` with `draft: true` for preview, or `draft: false` for live.

## Page Type Templates

**Product Landing (PDP)** — 8 sections:
Hero → Product Showcase → Benefits → Social Proof → How It Works → FAQ → CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Features → Social Proof → Comparison → Pricing → FAQ → CTA → Footer

**Homepage** — 7 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Social Proof → Newsletter → Footer

## Quality Bar

- Mobile-first (test at 375px width)
- Use CSS custom properties for all brand colors/fonts
- Proper heading hierarchy (h1 → h2 → h3)
- Islands for any commerce interaction (add to cart, checkout)
- All images via asset tools (never hardcoded external URLs)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs, framework code

## Ad-to-Page Flow

When converting an ad creative to a landing page:
1. `analyze_ad_creative` — extract headline, claims, colors, tone
2. `match_persona_to_ad` — find target persona
3. `get_ad_creatives` — get full creative metadata
4. Continue with standard Phase 0-4 flow using extracted context


