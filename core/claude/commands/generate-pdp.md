---
description: Generate a product detail page optimized for conversions
allowed-tools: mcp__lexsis-ai__*
---

# /generate-pdp

Generate a product detail page optimized for conversions

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

### conversion-psychology

# Conversion Psychology — Storefront Design Intelligence
> When to load: ALWAYS. Read before generating any ecommerce page.
## The Conversion Stack (AIDA → Sections)
Map the AIDA framework to section order. Each stage requires specific psychology and placement.
## Above-the-Fold Rules
What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.
## Price Psychology Patterns
### Anchoring (strikethrough + current)
## Social Proof Hierarchy
Rank order by persuasive power (highest to lowest). Use this sequence in sections.
## Urgency & Scarcity
Three types. Each requires different implementation and psychology.
## Cognitive Load Management
Max 3 choices per section. More options = decision paralysis = abandonment.
## Trust Escalation Ladder
Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.
## CTA Psychology
Button copy is conversion science. Every word matters.
## Visual Hierarchy for Conversion
Eye-flow patterns direct attention to CTAs.
## Anti-Patterns (Conversion Killers)
| ❌ | Why | ✅ |
|----|-----|-----|
| Generic headlines ("Welcome to Our Store") | No hook, no benefit | "Get [Specific Benefit] in [Timeframe]" |
| Hidden prices ("Contact for Pricing") | Friction, distrust | Show price upfront (even if high) |
| Walls of text (5-paragraph descriptions) | Cognitive overload | Bullet points, max 3 benefits |
| Too many CTAs (3+ above fold) | Decision paralysis | 1 primary CTA, 1 optional secondary |
| Tiny mobile buttons (40px tap target) | Poor UX, missed clicks | 48px minimum (py-3 or py-4) |
| Auto-playing video with sound | Annoys users | Muted autoplay, click to unmute |
| No trust signals above fold | Credibility gap | Add star rating or customer count near CTA |
| Fake urgency (evergreen countdown) | Trust erosion | Real sale end dates or remove timer |
| Cluttered forms (8-field email capture) | Abandonment | Email only with `data-island="EmailCapture"` |
| Slow load times (5+ second hero load) | Bounce rate spike | Optimize images, lazy-load below fold |
| No mobile optimization (desktop-only) | Poor mobile UX | Responsive spacing, clamp() font sizes |
| Unclear value prop ("We're the best") | Generic, meaningless | "Save 10 hours/week with automated [task]" |
| No risk reversal (no guarantee) | Fear of loss | Risk reversal section before final CTA |
| Dead-end pages (no next step) | Lost momentum | Every section ends with CTA or link |
| Inconsistent branding (5 button styles) | Unprofessional | Consistent colors via CSS vars |
## Complete Page Recipes
### Recipe 1: Lead Gen (Email Capture)

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

# Product Detail Page (PDP) Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate high-converting product detail pages. BuyBox island is REQUIRED. Sticky CTA adds +12% CVR. Reviews placement adds +22% CVR. Variant swatches reduce bounce 15%.

## Triggers

"product page", "PDP", "product detail", "product landing", "product showcase"

## CRO-Backed Section Ordering

```
1. Hero (Split)         — product visual + benefit headline + CTA above fold
2. Product Gallery      — swipeable images, zoom on desktop
3. BuyBox + Variants    — price visible without scrolling (CRITICAL)
4. Benefits Grid        — 3-5 benefit cards with icons
5. Ingredients/Specs    — transparency builds trust (63% research ingredients before buying)
6. Reviews              — +22% CVR with real names/photos (place after claims)
7. Related Products     — cross-sell grid (Magnolia Bakery pattern)
8. FAQ                  — objection handling immediately before final CTA
9. Sticky CTA (mobile)  — +12% CVR, appears after scrolling past BuyBox
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
get_product(product_id) → title, variants, images, price, metafields
get_navigation          → navbar/footer links
list_products           → related products for cross-sell
```

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind CSS. Use `data-placeholder` where islands go:

```html
<div data-placeholder="BuyBox" class="min-h-[200px] border border-dashed border-gray-300 rounded-lg p-4">
  Buy panel renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Mobile-first responsive design (375px base)
- Hero height: 420-550px (Seton.de data: -11% bounce, +19% engagement)
- CTA buttons: min 48px height, use `--lx-accent-color`
- Price MUST be visible without scrolling
- Single h1 (product title), h2 per section

## Phase 2B — Island Mapping

Replace placeholders with actual islands. Use `vibe://schema/island/{name}` for prop shapes.

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **BuyBox** (REQUIRED) | Section 3 | `get_product` → variants, price, images |
| ProductGallery | Section 2 | `get_product` → images array |
| VariantSwatches | Section 3 | `get_product` → variant options |
| StickyCart | Section 9 | product title + price |
| ReviewCarousel | Section 6 | provider + productId |
| FAQ | Section 8 | items[{question, answer}] |

```html
<!-- BuyBox (REQUIRED) -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"v1","title":"30ml","price":"$29.99"},{"id":"v2","title":"60ml","price":"$49.99"}],"images":["url1","url2"]}}'></div>

<!-- StickyCart -->
<div data-island="StickyCart" data-props='{"product":{"title":"...","price":"$29.99"},"threshold":600}'></div>
```

## Niche Variants

### Beauty PDP
- Hero: dewy product shot with soft lighting, split-layout
- Ingredients section: hero actives with source/science, EWG/cruelty-free badges
- Before/after UGC gallery (+54% purchase intent — Nosto)
- Routine builder: "Your AM/PM ritual" (increases AOV via bundling)
- Texture close-ups reduce returns by setting sensory expectations

### Supplement PDP
- Clinical data section: study results with specific numbers ("23% improvement in 8 weeks")
- Dosage/serving info prominently displayed
- Third-party testing badges (NSF, USP, ConsumerLab) — significant trust lift
- Transformation timeline: "Week 1... Week 4... Week 12..."
- Subscribe & save with 15-25% discount anchoring
- NO aggressive countdown timers on health products (erodes trust)

### Fashion PDP
- Size guide section with model measurements + fabric details (reduces returns 20-30%)
- Two-image product cards (front + hover alternate view)
- "Complete the look" cross-sell section
- Color variant swatches visible on first viewport
- Free returns messaging prominent (82% say returns influence purchase)

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: BuyBox renders, price visible, variants selectable, mobile layout intact
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL and inspect.
**Other IDEs:** Provide URL: "Preview: {url} — verify at 375px mobile width"

### Verification Checklist
- [ ] BuyBox island hydrates (shows product, not empty div)
- [ ] Price visible without scrolling on mobile
- [ ] Variant selector works (swatches clickable)
- [ ] Sticky CTA appears after scrolling past BuyBox
- [ ] Product images render (not broken placeholders)
- [ ] Brand colors applied via `--lx-accent-color` (not default purple)
- [ ] Mobile: no horizontal scroll, single column stack
- [ ] CTA contrast ratio >= 4.5:1 (WCAG AA)

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Section CSS Pattern

```html
<section id="pdp-hero" class="py-16 md:py-24 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Content with --lx-* variables -->
  </div>
</section>
```

## Conversion Data Reference

| Tactic | Impact | Source |
|--------|--------|--------|
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Real testimonials with names/photos | +22% CVR | Digital Applied 2026 |
| Variant swatches (vs dropdown) | -15% bounce | CXL |
| Size guide presence | -20-30% returns | Baymard |
| Before/after UGC | +54% purchase intent | Nosto |
| Subscribe & save option | +30-50% AOV | Supplement industry avg |
| FAQ before final CTA | Objection handling at decision point | NNGroup |
| Price visible without scroll | Table stakes (abandonment if hidden) | Baymard |


