---
description: Generate a bundle builder page with discount tiers
allowed-tools: mcp__lexsis-ai__*
---

# /generate-bundle

Generate a bundle builder page with discount tiers

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

# Bundle Builder Page Generation

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`

Generate interactive bundle-builder pages with step-based UX, discount tier visualization, live price calculation, and progress indicators via the BundleBuilder island.

## When to Use

- "Create a build-your-own bundle page"
- "Box builder where customers pick 3-5 products"
- "Mix and match page with volume discounts"
- "Bundle deal landing page"
- Any page where customers assemble a multi-product bundle with tiered pricing

## CRO Evidence (from CRO-RESEARCH-2026)

- Progress bar toward next discount tier increases AOV **+18%** (Goal-Gradient Effect: motivation increases with proximity to goal)
- Showing savings as dollar amount (not just %) improves completion **+12%** ("You're saving $14.70" > "Save 15%")
- Pre-selected starter bundle for decision-fatigued users reduces choice paralysis (Hick's Law: decision time increases with options)
- "X bundles sold today" urgency counter leverages social proof without fake scarcity
- Sticky CTA + above-fold CTA combined = **+12% CVR** (Digital Applied 2026)
- Stack/bundle builders increase AOV **30-50%** (CRO-RESEARCH supplements data)
- Mobile sticky summary at bottom leverages Fitts' Law (infinite-width targets at screen edge)
- Free shipping threshold indicators in cart: "Add $15 more for free shipping" activates Goal-Gradient Effect

## Generation Flow (5 Phases)

### Phase 0 — Context Gathering

```
get_workspace_details    → workspace ID, plan tier
get_connected_stores     → store domain, Shopify data
get_brand_kit            → logo, fonts, colors, voice
get_design_md            → brand brief + guidelines
list_products            → bundleable products catalog
get_navigation           → navbar/footer links
```

Then fetch island schema:
```
get_island_schema("BundleBuilder") → props shape, config, slots
```

Determine from user input:
- Product pool (which products can be bundled)
- Minimum/maximum items per bundle (default: min 2, max 6)
- Discount tiers (default: 2 items = 10%, 3 = 15%, 4+ = 20%)
- Bundle theme/name (e.g., "Build Your Skincare Routine")

### Phase 1 — Asset Discovery

1. `search_design_library` — hero imagery, lifestyle shots showing bundles/boxes
2. `generate_asset` — hero background if none found (style: `photography`, purpose: `hero_bg`, aspect: `landscape`)
3. Product images come from `get_product(id)` for each bundleable item
4. `view_asset` — verify hero asset quality

### Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind first. Mark interactive zones with `data-placeholder`. All colors via `--lx-*` CSS variables.

Write 7 sections:

**Section 1: Hero (Savings Hook)**
- h1: "Build Your [Category] Bundle & Save Up to [max]%"
- Subtitle emphasizing mix-and-match + escalating savings
- Visual showing example bundle (3-4 product thumbnails fanned)
- Primary CTA: "Start Building" (anchor to product grid)
- CRO: savings amount in hero headline not just percentage (+12% completion)

```html
<section id="hero" class="relative min-h-[60vh] flex items-center justify-center px-6 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-br from-[--lx-accent-color]/10 via-[--lx-bg-color] to-[--lx-lavender]/10"></div>
  <div class="relative z-10 text-center max-w-3xl mx-auto">
    <p class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide font-[--lx-font-body] mb-4">Build Your Box</p>
    <h1 class="font-[--lx-font-heading] text-4xl md:text-6xl font-bold text-[--lx-text-color] leading-tight">
      Build Your Bundle<br/>
      <span class="text-[--lx-accent-color]">Save Up to 20%</span>
    </h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4 max-w-xl mx-auto">
      Mix and match your favorites. The more you add, the more you save.
    </p>
    <a href="#products" class="inline-block mt-8 px-8 py-4 bg-[--lx-accent-color] text-white font-semibold rounded-lg hover:bg-[--lx-accent-color-hover] transition-colors text-lg">
      Start Building
    </a>
  </div>
</section>
```

**Section 2: Step Progress Indicator**
- 3-step visual: Choose (active) → Review → Checkout
- Sticky on scroll (`position: sticky; top: 0; z-index: 30`)
- Current step uses `--lx-accent-color`, inactive uses `--lx-text-muted`
- Connecting lines between steps

```html
<nav id="progress" class="sticky top-0 z-30 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-4">
  <div class="max-w-4xl mx-auto flex items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-accent-color] text-white flex items-center justify-center text-sm font-bold">1</span>
      <span class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">Choose</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">2</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Review</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">3</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Checkout</span>
    </div>
  </div>
</nav>
```

**Section 3: Discount Tier Visualization**
- Visual tier ladder: 3 cards showing escalating savings
- Current tier highlighted with accent border + background tint
- "Add X more for next tier" nudge text
- Show dollar savings (not just %): CRO +12% completion
- CRO: progress bar toward next tier +18% AOV

```html
<section id="tiers" class="py-12 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-3xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl font-bold text-center text-[--lx-text-color] mb-8">The More You Add, The More You Save</h2>
    <div class="grid grid-cols-3 gap-4">
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-accent-color] bg-[--lx-accent-color]/5">
        <p class="text-3xl font-bold text-[--lx-accent-color]">10%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">2 items</p>
        <p class="text-xs text-[--lx-accent-color] mt-2 font-medium">Save ~$7</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">15%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">3 items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$14</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">20%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">4+ items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$24+</p>
      </div>
    </div>
  </div>
</section>
```

**Section 4: Product Selection Grid (BundleBuilder zone)**
- h2: "Choose Your Products"
- Responsive grid: 2 cols mobile, 3-4 cols desktop
- Each product card: image, name, individual price, "Add to Bundle" button
- Optional category filter tabs above grid
- `data-placeholder="BundleBuilder"` wrapping the grid
- CRO: pre-select a "starter bundle" for decision-fatigued users (Hick's Law)

```html
<section id="products" class="py-16 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl md:text-3xl font-bold text-[--lx-text-color] text-center mb-8">Choose Your Products</h2>
    <p class="text-center text-[--lx-text-muted] font-[--lx-font-body] mb-8">Select 2 or more items to unlock bundle savings</p>
    <div data-placeholder="BundleBuilder" class="border-2 border-dashed border-[--lx-border-color] rounded-xl p-8 min-h-[400px] flex items-center justify-center">
      <p class="text-[--lx-text-muted]">BundleBuilder island: product grid + live cart + tier progress</p>
    </div>
  </div>
</section>
```

**Section 5: Social Proof**
- "X bundles sold today" urgency counter (real data, not fake)
- 2-3 customer testimonials specific to bundles/value
- Star ratings with review excerpts
- UGC images of received bundles
- CRO: social proof after claims that raise skepticism (+22% with real names)

```html
<section id="social-proof" class="py-16 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-4xl mx-auto text-center">
    <p class="font-[--lx-font-body] text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">Trusted by Bundlers</p>
    <p class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">1,247 bundles built this week</p>
    <div class="grid md:grid-cols-3 gap-6 mt-12">
      <!-- Testimonial cards with real names, photos, star ratings -->
    </div>
  </div>
</section>
```

**Section 6: FAQ**
- h2: "Bundle FAQs"
- 4-6 questions: pricing, changes, minimums, shipping
- Schema.org FAQPage JSON-LD embedded
- CRO: FAQ before final CTA handles objections (Serial Position Effect)

**Section 7: Mobile Sticky Summary**
- Fixed bottom bar on mobile (hidden on desktop)
- Shows: item count, current savings, "View Bundle" button
- Leverages Fitts' Law: infinite-width target at screen edge

```html
<div class="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-[--lx-bg-color] border-t border-[--lx-border-color] p-4 shadow-lg">
  <div class="flex items-center justify-between">
    <div>
      <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">0 items selected</p>
      <p class="font-[--lx-font-body] text-xs text-[--lx-accent-color]">Add 2+ to save</p>
    </div>
    <button class="px-6 py-3 bg-[--lx-accent-color] text-white rounded-lg font-semibold text-sm">View Bundle</button>
  </div>
</div>
```

### Phase 2B — Island Mapping

Replace `data-placeholder="BundleBuilder"` with the hydrated island:

```html
<div data-island="BundleBuilder" data-props='{
  "products": [{"id":"gid://shopify/Product/1","title":"...","price":"$34.00","image":"..."}],
  "minItems": 2,
  "maxItems": 6,
  "discountTiers": [
    {"minQuantity": 2, "discountPercent": 10, "label": "Save 10%"},
    {"minQuantity": 3, "discountPercent": 15, "label": "Save 15%"},
    {"minQuantity": 4, "discountPercent": 20, "label": "Save 20%"}
  ],
  "layout": "grid",
  "columns": {"mobile": 2, "tablet": 3, "desktop": 4},
  "showProgress": true,
  "preselected": []
}'></div>
```

Use `get_island_schema("BundleBuilder")` to confirm exact prop shape before mapping.

### Phase 3 — Validation

```
validate_vibe_page(page_data)
check_page_integrity(page_id)
```

Additional checks:
- BundleBuilder island has valid product IDs from the store
- Discount tiers are logically sequential (higher qty = higher discount)
- Sticky elements (progress bar, mobile summary) don't overlap
- Price displays use consistent currency formatting
- Island props match schema from `get_island_schema`

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
- [ ] Hero CTA scrolls to product grid
- [ ] Step progress indicator sticky and visible
- [ ] Discount tier cards rendering with correct percentages
- [ ] BundleBuilder island hydrated (products visible, add buttons work)
- [ ] Mobile sticky summary bar visible on small viewports
- [ ] Brand colors applied via `--lx-*` variables
- [ ] No horizontal scroll on mobile
- [ ] Progress bar updates as items added (island handles this)
- [ ] Dollar savings shown alongside percentage

## Quality Bar

- BundleBuilder island correctly configured with valid product IDs and discount tiers
- Discount tier visualization shows both percentage AND dollar savings (+12% completion)
- Progress bar toward next tier visible (+18% AOV)
- Pre-selected starter bundle option for choice-paralyzed users
- Step progress indicator sticky and functional
- Mobile: sticky bottom summary bar, swipeable product grid (2-col)
- "X bundles sold today" social proof (real, not fabricated)
- All `--lx-*` CSS variables (NOT `--color-*`)
- Proper heading hierarchy (h1 hero, h2 per section)
- FAQ includes Schema.org FAQPage JSON-LD
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Minimum 2 items required before checkout CTA enables
- Currency formatting consistent throughout


