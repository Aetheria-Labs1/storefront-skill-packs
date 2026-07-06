---
description: Generate an SEO-optimized comparison/listicle page
allowed-tools: mcp__lexsis-ai__*
---

# /generate-listicle

Generate an SEO-optimized comparison/listicle page

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

## Workflow

# SEO Listicle / Comparison Page Generation

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`

Generate SEO-optimized long-form listicle and comparison pages (>2000 words) with proper heading hierarchy, anchor navigation, and embedded commerce islands.

## When to Use

- "Top 10 best [products] for [use case]"
- "[Brand A] vs [Brand B]" comparison pages
- "Best alternatives to [product]"
- "Product roundup" or "buyer's guide"
- Any search-intent page designed to rank and convert

## CRO Evidence (from CRO-RESEARCH-2026)

- Anchor nav (sticky TOC on desktop) increases time-on-page **+40%** — users jump between entries, reducing bounce
- Comparison table placed at page bottom captures "ready to buy" readers — they scroll past entries → land on table → decide
- Winner badge on recommended product drives **+25% CTR** over unbadged entries
- FAQ before final CTA handles objections at decision point (Serial Position Effect: last items best remembered)
- Real testimonials with names increase trust **+22% CVR** (Digital Applied 2026)
- E-E-A-T signals (author byline, last-updated date, methodology) correlate with higher search placement and user trust

## Generation Flow (5 Phases)

### Phase 0 — Context & SEO Research

```
get_workspace_details    → workspace ID, plan tier
get_connected_stores     → store domain, Shopify data
get_brand_kit            → logo, fonts, colors, voice
get_design_md            → brand brief, design philosophy
list_products            → full product catalog (select featured items)
get_navigation           → navbar/footer links for internal linking
```

Determine from user input:
- Primary keyword (h1 target)
- Product list (3-10 products to feature)
- Comparison criteria (price, features, use case, rating)
- Author name for E-E-A-T byline

### Phase 1 — Asset Discovery

For each product in the listicle:
1. `search_design_library` — find existing product/lifestyle imagery
2. `get_product(product_id)` — pull product images, price, description
3. `generate_asset` — only if no suitable imagery exists (style: `photography`, purpose: `product_lifestyle`)
4. `view_asset` — verify before embedding

Generate one hero asset for the page header (style: `editorial`, purpose: `hero_bg`, aspect: `landscape`).

### Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind first. Use `data-placeholder` where islands will go. Focus on layout, hierarchy, spacing, and typography. All colors via `--lx-*` CSS variables.

Write 8-12 sections:

**Section 1: Hero + E-E-A-T Signals**
- h1 matching primary keyword exactly
- Subtitle with freshness signal: "Updated [Month] [Year] — [N] products tested"
- Author byline with name, role, and avatar
- Last-updated date + methodology disclosure link
- Full-bleed background or gradient

```html
<section id="hero" class="relative py-20 md:py-28 px-6 bg-[--lx-bg-color]">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="font-[--lx-font-heading] text-4xl md:text-5xl font-bold text-[--lx-text-color] leading-tight">{Keyword-Matched Title}</h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4">Updated July 2026 — {N} products tested over {X} weeks</p>
    <div class="flex items-center justify-center gap-3 mt-6">
      <img src="{author_avatar}" alt="{Author Name}" class="w-10 h-10 rounded-full" />
      <div class="text-left">
        <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">{Author Name}</p>
        <p class="font-[--lx-font-body] text-xs text-[--lx-text-muted]">{Role} · {X} years in {category}</p>
      </div>
    </div>
  </div>
</section>
```

**Section 2: Sticky Table of Contents (Anchor Nav)**
- Desktop: sticky sidebar or horizontal sticky bar below header
- Ordered list linking to each `#product-N` section ID
- "Jump to verdict" shortcut at end
- CRO: anchor nav increases time-on-page +40%

```html
<nav id="toc" class="sticky top-0 z-40 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-3 px-6 overflow-x-auto">
  <ol class="flex gap-6 max-w-5xl mx-auto text-sm font-[--lx-font-body] whitespace-nowrap">
    <li><a href="#product-1" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">1. {Name}</a></li>
    <li><a href="#product-2" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">2. {Name}</a></li>
    <!-- ... -->
    <li><a href="#verdict" class="font-semibold text-[--lx-accent-color]">Verdict</a></li>
  </ol>
</nav>
```

**Section 3: Introduction + Methodology**
- h2: "How We Chose the Best [Category]"
- 150-200 words: selection criteria, testing methodology
- Internal links to related pages via `get_navigation`
- Methodology disclosure builds E-E-A-T trust

**Sections 4-N: Product Entries (one per product)**
- h2: "[Product Name] — Best for [Use Case]"
- Product image (alternating left/right layout per entry)
- 150-250 word mini-review
- h3 sub-sections for features where needed
- Pros/Cons as structured lists
- Key specs mini-table
- Star rating visual (CSS-only using `--lx-accent-color`)
- `data-placeholder="BuyBox"` where commerce island goes
- Winner badge (CRO: +25% CTR on recommended product):

```html
<section id="product-1" class="py-16 px-6 border-b border-[--lx-border-color]">
  <div class="max-w-4xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-start">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-[--lx-accent-color]/10 text-[--lx-accent-color] rounded-full text-xs font-semibold mb-3">
          <span>★</span> Editor's Choice
        </div>
        <span class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">#1 Pick</span>
        <h2 class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">{Product Name}</h2>
        <p class="text-sm text-[--lx-text-muted] mt-1">Best for: {use case}</p>
        <p class="mt-4 font-[--lx-font-body] text-[--lx-text-color]/80 leading-relaxed">{Review paragraph}</p>
        <div class="mt-4 grid grid-cols-2 gap-4">
          <div>
            <h3 class="font-semibold text-green-600 text-sm">Pros</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>+ {pro}</li></ul>
          </div>
          <div>
            <h3 class="font-semibold text-red-500 text-sm">Cons</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>- {con}</li></ul>
          </div>
        </div>
        <div data-placeholder="BuyBox" class="mt-6 p-4 border border-dashed border-[--lx-border-color] rounded">Add to cart island</div>
      </div>
      <div>
        <img src="{asset_url}" alt="{product name}" class="rounded-lg shadow-md w-full" />
      </div>
    </div>
  </div>
</section>
```

**Section N+1: Comparison Table**
- Full-width responsive table with feature matrix
- Highlight "Best Overall" / "Best Value" / "Best Premium" rows
- Mobile: horizontal scroll with sticky first column
- CRO: captures ready-to-buy readers who scrolled through all entries

**Section N+2: Verdict (Winner)**
- h2: "Our Top Pick"
- `data-placeholder="BuyBox"` for winning product
- Runner-up mention linking back to its anchor

**Section N+3: FAQ with Schema.org JSON-LD**
- h2: "Frequently Asked Questions"
- 5-8 questions targeting "People Also Ask" queries
- Embedded FAQPage structured data:

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}]}
</script>
```

**Section N+4: Related Content (Internal Linking)**
- 3-4 card grid linking to related listicles/collections
- Anchor text optimized for adjacent keywords

### Phase 2B — Island Mapping

Replace all `data-placeholder` divs with hydrated islands:

```html
<!-- Replace each placeholder -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"...","title":"Default"}]}}'></div>
```

Use `get_island_schema("BuyBox")` to confirm exact prop shape. Each product entry gets its own BuyBox island.

### Phase 3 — Validation

```
validate_vibe_page(page_data)
check_page_integrity(page_id)
```

SEO quality checks:
- Exactly one h1 tag (hero)
- h2 for each product entry, h3 for sub-features
- All anchor nav links resolve to section IDs
- FAQ schema JSON-LD is valid
- Total word count > 2000
- No duplicate section IDs

### Phase 4 — Publish & Verify

```
publish_vibe_page(page_data) → returns preview_url
```

**Visual Verification (REQUIRED):**

For Claude Code (Playwright MCP):
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
```

For Codex: use built-in browser to open preview_url and inspect.
For other IDEs: provide preview URL and instruct user to verify at 375px and 1280px.

**Checklist:**
- [ ] Sticky TOC visible and functional on desktop
- [ ] All anchor links scroll to correct sections
- [ ] Product images rendering (not broken placeholders)
- [ ] Winner badge visible on recommended product
- [ ] Comparison table scrollable on mobile (no overflow)
- [ ] BuyBox islands hydrated with real product data
- [ ] Brand colors applied via `--lx-*` variables
- [ ] FAQ accordion functional
- [ ] No horizontal scroll on mobile

## Quality Bar

- Total word count > 2000 across all sections
- Proper heading hierarchy: h1 (hero) → h2 (entries) → h3 (features)
- Sticky anchor nav with valid section ID targets
- Comparison table responsive (horizontal scroll on mobile, sticky first column)
- Each product entry has a working BuyBox island
- FAQ includes valid Schema.org FAQPage JSON-LD
- Winner badge on recommended product (+25% CTR)
- Author byline + last-updated date (E-E-A-T)
- Internal linking structure via `get_navigation`
- All `--lx-*` CSS variables (NOT `--color-*`)
- Mobile-first: readable at 375px width
- No fetch/XHR, eval, localStorage, @import, duplicate IDs


