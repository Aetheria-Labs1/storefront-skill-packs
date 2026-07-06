# Food & Beverage — DTC Landing Pages — Knowledge Base

> This document contains expert knowledge for building Shopify landing pages.
> Upload this as a knowledge file in your Custom GPT configuration.

---

---

## STOREFRONT-CRAFT

# Storefront Craft Guide — Start Here

Load this skill first on any storefront page generation task.

---

## Architecture: Vibe-Code

Pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. No component JSON. No blueprint system. The AI generates HTML directly.

**VibePage schema:**
```json
{
  "head": { "title": "Page Title", "fonts": ["https://fonts.googleapis.com/..."] },
  "theme_css": ":root { --lx-accent-color: #4F46E5; ... }",
  "sections": [
    { "id": "hero", "html": "<section class='...'>...</section>", "css": ".custom { ... }", "js": "// vanilla JS" }
  ]
}
```

**Islands** = interactive React components hydrated at `data-island` markers in HTML:
```html
<div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
```

---

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

---

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

---

## CSS Variables (Brand Theming)

All sections use these CSS custom properties (set in `theme_css`):

| Variable | Purpose |
|---|---|
| `--lx-accent-color` | Primary brand/CTA color |
| `--lx-accent-color-hover` | Hover state |
| `--lx-text-color` | Primary text |
| `--lx-text-muted` | Secondary text |
| `--lx-bg-color` | Page background |
| `--lx-bg-surface` | Card/section background |
| `--lx-border-color` | Borders and dividers |
| `--lx-font-heading` | Heading font family |
| `--lx-font-body` | Body font family |

Use via `style="color: var(--lx-accent-color)"` or `style="font-family: var(--lx-font-heading)"`.

---

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

**Mediocre page:**
- Hardcoded colors instead of CSS vars
- Desktop-only layout
- Missing islands (raw HTML buttons instead of BuyBox)
- placeholder.co images shipped to production
- No animations or visual rhythm
- Trust badges missing

---

## Anti-Patterns (NEVER do these)

1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline gradients/colors
5. **No duplicate section IDs** — each must be unique kebab-case
6. **No `<script src="...">` in HTML** — use section `js` field for vanilla JS
7. **No framework code** — no React/Vue/Angular in section HTML (islands handle interactivity)
8. **Don't fake commerce** — always use BuyBox island for add-to-cart, never a plain button

---

## Section ID Naming

Use descriptive kebab-case: `hero`, `product-gallery`, `social-proof`, `ingredients`, `faq`, `sticky-cta`, `trust-badges`, `footer`. Never `section-1`, `section-2`.

---

## Island Rules

- `data-props` must be valid JSON in single-quoted attribute
- Only use valid island names (26 total — call `get_island_catalog` to see them)
- One `BuyBox` per page (multiple breaks cart state)
- One `CartDrawer` per page
- `StickyBar` needs `triggerOffset` — distance in px before it appears
- `ReviewCarousel` can use custom reviews array OR fetch from Shopify via productId

---

## Tailwind Usage

- CDN included in renderer — all utility classes available
- Use responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`
- Prefer utilities over custom CSS (only use section `css` for keyframes/animations)
- Use `clamp()` for fluid typography: `text-[clamp(2rem,5vw,4rem)]`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`

---

## Image Strategy

1. **Always check `search_design_library` first** — brand's uploaded assets are free and on-brand
2. **Use `list_products` for product images** — never generate fake product shots
3. **`generate_asset` for custom imagery** — hero backgrounds, lifestyle contexts, textures
4. **`edit_asset` for composites** — product-on-background, texture overlays
5. **Place URLs directly in HTML** — `<img src="${url}" />` or inline `style="background-image: url(...)"`
6. **Load `design-enrichment` skill** for full asset generation pipeline details


---

## WORKFLOW-ORCHESTRATION

# Workflow Orchestration — Execution Engine

Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.

---

## Flow Selection

```
What did the user provide?
│
├─ Ad creative (image URLs / screenshot)
│  → AD-TO-PAGE FLOW (analyze creative → extract style → generate matched page)
│
├─ Reference URL (competitor / inspiration)
│  → DESIGN-FIRST FLOW (extract_brand_design → use tokens as theme → generate)
│
├─ Brand brief only (name, industry, tone)
│  → STANDARD FLOW (context → assets → generate → validate → write)
│
├─ Existing page (wants edits)
│  → EDIT FLOW (read page → modify sections → validate → write)
│
├─ Product focus (PDP, collection)
│  → PRODUCT FLOW (list_products first → build around real product data)
│
└─ Multiple inputs (ad + products + brand)
   → STANDARD FLOW with enriched context
```

---

## Standard Flow (5 Phases)

### Phase 0: Context Gathering ✅ ALL PARALLEL

Fire simultaneously — no dependencies:

```
┌─ get_storefront_skills({ brief, page_type })    → system prompt + island catalog + schema
├─ get_design_md()                                 → brand voice/guidelines
├─ list_products(limit: 10)                        → product catalog (names, images, prices)
├─ search_design_library({ query: "hero" })        → existing brand assets
└─ get_connected_stores()                          → store_id (for publish later)
```

**Output:** Full context for generation — brand tokens, product data, asset URLs, island reference.

---

### Phase 1: Asset Generation ✅ PARALLEL PER SECTION

For each section that needs a custom image (hero backgrounds, lifestyle shots, textures):

```
┌─ search_design_library({ query: "hero background" })  → prefer existing over generating
│
├─ generate_asset({ prompt: "descriptive prompt here", style: "photography", purpose: "hero_bg", aspect: "landscape", brand_colors })
│  → returns { asset_id, url, width, height }
│
├─ [If compositing needed] edit_asset({ source_images: [product_url, bg_url], prompt: "Product on marble surface" })
│  → returns composited image URL
│
└─ view_asset(asset_id) → visually verify before using
```

**Decision tree for images:**
1. `search_design_library` first — if brand has relevant assets, USE THEM
2. If no good match → `generate_asset` (write your own descriptive prompt)
3. If need product-on-background → `edit_asset` with product image + generated/library background
4. If need transparent overlay → `generate_asset` with `transparent: true`

**Collect all image URLs before Phase 2.**

---

### Phase 2: HTML Generation (Agent writes VibePage)

Using context from Phase 0 + asset URLs from Phase 1:

1. Set `theme_css` from brand tokens (map flat columns → CSS vars)
2. Write each section's HTML using Tailwind classes + CSS vars
3. Place island markers where interactive commerce needed
4. Embed generated/library image URLs directly in `<img src="...">` and `background-image`
5. Add section `css` only for custom keyframes/animations
6. Add section `js` only for scroll-triggered reveals (IntersectionObserver)

---

### Phase 3: Validate ❌ SEQUENTIAL

```
validate_vibe_page({ page }) → { valid, errors, warnings }
```

If errors: fix the issues (usually JSON parsing in data-props, or invalid island names). Re-validate.

---

### Phase 4: Write + Preview ✅ SEQUENTIAL

```
write_vibe_page({ slug, page }) → { url, path, validation }
preview_vibe_page({ slug }) → { url }
```

Report the preview URL to the user.

---

## Ad-to-Page Flow

```
Phase 0: Context
├─ analyze_ad_creative({ image_urls, ad_format })  → visual signals, CTA, headline
├─ get_storefront_skills({ brief from ad analysis, page_type: "landing" })
└─ list_products()

Phase 1: Assets
├─ Use ad creative images directly where appropriate
├─ generate_asset for additional sections (testimonial bg, trust section bg)
└─ edit_asset to adapt ad images (crop, extend, composite)

Phase 2-4: Same as Standard Flow
```

---

## Design-First Flow (Reference URL)

```
Phase 0:
├─ extract_brand_design(url)           → extracted palette, fonts, spacing, tone
├─ get_storefront_skills(brief)
└─ list_products()

Phase 1: Use extracted tokens as theme_css base
Phase 2-4: Same as Standard Flow
```

---

## Edit Flow (Safe Iteration)

```
1. find_page({ query })                              → locate page by handle/title/UUID
2. get_page_content({ page_id })                     → read current sections + head
3. Identify which sections to modify
4. preview_section_update({ page_id, section_id, html })  → dry-run validation (repeat per section)
5. update_page_section({ page_id, section_id, html })     → commit change (bumps version)
6. check_page_integrity({ page_id, archetype })           → structural QA pass
7. [Optional] diff_page_versions({ page_id, version_a, version_b })  → review all changes
8. [If broken] rollback_page_version({ page_id, target_version })    → revert to prior version
```

**Key rules:**
- Always `preview_section_update` before `update_page_section` — catches validation errors without bumping version
- Run `check_page_integrity` after all edits complete — catches archetype violations (e.g. PDP without BuyBox)
- Use `diff_page_versions` to verify your changes look correct before publishing
- Use `rollback_page_version` if integrity check fails — creates a new forward version, preserves history

---

## Duplication Flow (Idempotent)

```
1. find_page({ query })                                     → locate source page
2. duplicate_page({ page_id, handle, idempotency_key })     → safe clone (retries won't create extras)
3. Edit sections on the duplicate (use Edit Flow above)
4. check_page_integrity({ page_id, archetype })             → final QA
```

**Idempotency key:** Pass a deterministic string (e.g. `"${handle}-v2-from-${source_handle}"`) so that retrying the same operation returns the existing duplicate instead of creating another.

---

## Parallelization Rules

| Can parallelize | Cannot parallelize |
|---|---|
| All Phase 0 context calls | Phase 1 needs Phase 0 results (brand_colors for asset gen) |
| Multiple generate_asset calls | validate must complete before write |
| Asset gen for different sections | edit_asset needs source image URLs first |

---

## Cost Control

- `search_design_library` before `generate_asset` — existing assets are free
- Use `quality: "medium"` for most assets, `"high"` only for hero images
- One hero image + one lifestyle shot usually enough for a PDP
- Landing pages: hero + 2-3 section backgrounds max
- Skip asset gen for sections using solid color/gradient backgrounds

---

## Page Type Defaults

### PDP Sections (6-8)
```
hero (product gallery + buybox) → trust-badges → benefits → ingredients → reviews → faq → sticky-cta → cart-drawer
```

### Landing Page Sections (7-10)
```
hero → trust-bar → problem/solution → features → before-after → testimonials → pricing → faq → cta → exit-intent
```

### Homepage Sections (5-7)
```
hero → featured-products → brand-story → social-proof → collections → newsletter → footer
```

### Collection Sections (4-6)
```
collection-header → filters → product-grid → featured-pick → trust-bar → newsletter
```

---

## Credit Costs

Always call `get_credits_balance` before expensive operations. If balance is 0, inform the user before proceeding.

| Tool | Cost | Notes |
|------|------|-------|
| `generate_asset` | credits | AI image generation |
| `edit_asset` | credits | AI image editing/compositing |
| `publish_vibe_page` | credits | Page generation (only on publish, not drafts) |
| `create_page_variation` | credits | A/B variant creation (requires Pro plan) |
| `create_ab_test` | credits | Experiment setup (requires Pro plan) |
| `update_page_section` | credits | Section regeneration |
| `validate_vibe_page` | FREE | Always validate before publishing |
| `check_page_integrity` | FREE | Structure/accessibility check |
| All read/list/get tools | FREE | No cost for browsing data |

**Preflight pattern:**
```
get_credits_balance → check cost → warn if insufficient → proceed or abort
```

Hand-authored VibePage JSON persisted via `publish_vibe_page` still costs credits (it's the publish action, not the AI generation, that bills). Draft previews (`draft: true`) also consume credits.


---

## CONVERSION-PSYCHOLOGY

# Conversion Psychology — Storefront Design Intelligence

> When to load: ALWAYS. Read before generating any ecommerce page.

## The Conversion Stack (AIDA → Sections)

Map the AIDA framework to section order. Each stage requires specific psychology and placement.

### Short Page (5-7 sections) — Impulse / Low-consideration products

1. **Attention (1 section)**: Hero section
   - High-contrast gradient or bold product image
   - Benefit-driven headline (6-10 words)
   - `font-size: clamp(2.5rem, 5vw, 3.5rem)` for headline
   - Sticky CTA bar for persistent action

2. **Interest (2 sections)**: Value props + social proof stats
   - 3 icon-driven benefits max
   - Numbers: customer count, star rating, review count
   - `py-8 md:py-12` spacing

3. **Desire (2 sections)**: Reviews + transformation proof
   - Star-first review display, 3-6 reviews
   - Before/after images or testimonial carousel
   - `data-island="ReviewCarousel"` for dynamic trust

4. **Action (2 sections)**: CTA + footer
   - Urgency element (countdown or inventory indicator)
   - First-person CTA copy: "Get MY [benefit]"
   - `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`

### Medium Page (8-12 sections) — Considered purchase / New-to-brand

1. **Attention (1)**: Hero with video or interactive media
2. **Interest (3)**: Value props → logo carousel → stats
   - Logo carousel = trust transfer from known brands
   - Neutral background between hero and body
3. **Desire (5)**: Feature grid → testimonials → before/after → reviews → comparison table
   - 3-6 features with icons
   - Transformation proof with `data-island="BeforeAfter"`
   - Compare you vs. 2 alternatives (3 columns max)
4. **Action (3)**: FAQ → CTA → footer
   - Preemptive objection handling (5-8 questions)
   - `data-island="EmailCapture"` for fence-sitters
   - `data-island="FAQ"` for progressive disclosure

### Long Page (12-16 sections) — High-ticket / Complex products

1. **Attention (2)**: Hero + announcement bar
   - Free shipping threshold / promo in bar
2. **Interest (4)**: Value props → logo carousel → stats → press mentions
   - Layer authority progressively: claims → endorsements → proof
3. **Desire (7)**: Feature showcase → testimonials → case study → feature grid → reviews → comparison → risk reversal
   - Hero feature with `data-island="VideoPlayer"`
   - Full customer journey (problem → solution → result)
   - Guarantee + return policy badge-driven
4. **Action (3)**: FAQ → dual CTA → footer
   - Dual CTA: buy now / learn more
   - `data-island="BundleBuilder"` for upsells

**Section Order Rules:**
- Never reviews before value props (prove value before social proof)
- FAQ immediately before final CTA (remove last objection)
- Stats or logo carousel within first 3 sections for trust anchoring
- Footer always last (consistency signal)

---

## Above-the-Fold Rules

What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.

### PDP (Product Detail Page)

**Mandatory visible elements:**
- Product image (left 50-60% width, min 600px tall)
- Product title (max 2 lines)
- Price + compare_at_price (if discounted)
- Star rating + review count (clickable to reviews)
- Primary CTA button
- 1-2 trust badges (free shipping, guarantee)

**HTML pattern:**
```html
<section class="grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8">
  <div class="relative">
    <img src="/product.jpg" alt="Product" class="w-full h-auto rounded-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-6">
    <h1 class="text-4xl md:text-5xl font-bold leading-tight" style="color:var(--lx-text-color)">
      Premium Product Name
    </h1>
    <p class="text-lg md:text-xl opacity-80">One-line benefit promise that resonates</p>
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$89.00</span>
      <span class="text-lg line-through opacity-40">$129.00</span>
      <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">31% OFF</span>
    </div>
    <div class="flex items-center gap-2">
      <div class="flex">
        <span class="text-yellow-400">★★★★★</span>
      </div>
      <span class="text-sm opacity-70">(2,847 reviews)</span>
    </div>
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart — Free Shipping","showQuantity":true}'></div>
    <div class="flex gap-4 pt-4">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🚚</span>
        <span class="text-sm">Free Shipping</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-2xl">💯</span>
        <span class="text-sm">Money-Back Guarantee</span>
      </div>
    </div>
  </div>
</section>
```

### Landing Page (paid traffic)

**Mandatory visible:**
- Headline with specific benefit (not generic)
- Subline addressing pain point
- Hero image/video showing product in use
- Primary CTA (above fold)
- 1 trust signal (review stars or customer count)

**HTML pattern:**
```html
<section class="relative min-h-screen flex items-center justify-center text-center px-4 py-20" style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
  <div class="max-w-4xl mx-auto space-y-8">
    <h1 class="text-5xl md:text-7xl font-extrabold leading-none text-white">
      Get Flawless Skin in 30 Days
    </h1>
    <p class="text-xl md:text-2xl text-white/90">
      Without harsh chemicals or expensive treatments. Guaranteed.
    </p>
    <button class="px-10 py-5 text-xl font-bold rounded-lg transition-transform hover:scale-105" style="background:white;color:var(--lx-accent-color)">
      Start MY Transformation
    </button>
    <p class="text-white/80 text-sm">Join 47,000+ customers who transformed their skin</p>
  </div>
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Offer ends in:","urgencyThreshold":3600}'></div>
  <div data-island="SocialProofPopup" data-props='{"displayDuration":5000,"interval":15000,"maxPopups":3}'></div>
</section>
```

### Collection Page

**Mandatory visible:**
- Category headline + product count
- Filter bar (collapsible on mobile)
- First 4-6 products (2x3 grid desktop, 2 columns mobile)
- Sort dropdown
- Trust signal (delivery promise or return policy)

**Layout rule:** First product fold < 600px from top on desktop, < 800px on mobile.

---

## Price Psychology Patterns

### Anchoring (strikethrough + current)

Show original price crossed out. Minimum 20% discount to be credible, optimal 30-40%.

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$79.99</span>
  <span class="text-lg line-through opacity-40">$119.99</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">33% OFF</span>
</div>
<p class="text-sm mt-2 opacity-70">Save $40 today</p>
```

### Charm Pricing

End prices in .97, .95, or .99. Never .00 for mid-market ($50-$300). Use .00 only for premium ($500+).

**Examples:**
- Low-ticket (<$50): $29.97, $14.99
- Mid-ticket ($50-$300): $129.95, $79.97
- High-ticket ($300+): $999.00, $1,500.00

### Bundle Pricing (quantity breaks)

Show per-unit savings, not just total discount.

```html
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 1</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$59.99</p>
      <p class="text-sm opacity-70">$59.99 each</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border-2 rounded-lg relative transform scale-105" style="border-color:var(--lx-accent-color);box-shadow:0 20px 60px rgba(102,126,234,0.2)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">BEST VALUE</span>
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 3</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$119.99</p>
      <p class="text-sm opacity-70">$40.00 each — Save $60</p>
      <button class="w-full px-4 py-3 mt-4 rounded font-bold text-white" style="background:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 2</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$99.99</p>
      <p class="text-sm opacity-70">$50.00 each — Save $20</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
</div>
```

### Payment Splitting (Afterpay/Klarna)

Show "or 4 payments of $X" beneath price. Increases conversion 20-30% for $100+ items.

```html
<div class="space-y-2">
  <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$159.99</p>
  <p class="text-sm opacity-70">or 4 interest-free payments of $40.00 with <strong>Afterpay</strong></p>
</div>
```

### Decoy Pricing (3-tier)

Always show 3 options. Middle option is the target, positioned as "most popular".

```html
<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Basic</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$49.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Get Started
    </button>
  </div>
  <div class="p-8 rounded-lg relative transform scale-105" style="border:3px solid var(--lx-accent-color);box-shadow:0 20px 60px rgba(0,0,0,0.2)">
    <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 text-sm font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">MOST POPULAR</span>
    <h3 class="text-2xl font-bold mb-2">Pro</h3>
    <div class="flex items-baseline gap-2 mb-4">
      <p class="text-4xl font-bold" style="color:var(--lx-text-color)">$89.99</p>
      <p class="text-lg line-through opacity-40">$129.99</p>
    </div>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature C</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature D</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded font-bold text-white" style="background:var(--lx-accent-color)">
      Start Pro Trial
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Premium</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$149.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Everything in Pro</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature E</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature F</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Priority Support</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Go Premium
    </button>
  </div>
</div>
```

---

## Social Proof Hierarchy

Rank order by persuasive power (highest to lowest). Use this sequence in sections.

### 1. Numbers (stats bar)

Raw metrics. Most credible when specific and large.

```html
<section class="py-16 px-4" style="background:var(--lx-bg-surface)">
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-6xl mx-auto text-center">
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">247,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Happy Customers</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">4.8/5.0</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Average Rating</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">12,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">5-Star Reviews</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">94%</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Would Recommend</p>
    </div>
  </div>
</section>
```

**When to use:** First 3 sections. Anchor trust before storytelling.

### 2. Faces (testimonial cards)

Photos + quotes. Most effective for emotional products (beauty, wellness, lifestyle).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">What Our Customers Say</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface)">
        <div class="flex items-center gap-4 mb-4">
          <img src="/testimonials/sarah.jpg" alt="Sarah M." class="w-20 h-20 rounded-full" style="border:4px solid var(--lx-accent-color)" />
          <div>
            <p class="font-bold">Sarah M.</p>
            <p class="text-sm opacity-70">Verified Buyer</p>
            <div class="flex text-yellow-400">★★★★★</div>
          </div>
        </div>
        <p class="text-lg italic leading-relaxed opacity-90">
          "This completely changed how I approach skincare. I saw results in just 2 weeks."
        </p>
      </div>
      <!-- Repeat for more testimonials -->
    </div>
  </div>
</section>
```

**When to use:** After interest stage, before feature deep-dive. 3-6 testimonials max per section.

### 3. Logos (logo carousel)

Trust transfer from known brands. Works for B2B, press mentions, "as seen on".

```html
<section class="py-12 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-sm uppercase tracking-wide mb-8 opacity-70">Trusted by Leading Brands</p>
    <div class="flex justify-center items-center gap-12 flex-wrap">
      <img src="/logos/forbes.svg" alt="Forbes" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/techcrunch.svg" alt="TechCrunch" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/wsj.svg" alt="Wall Street Journal" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
    </div>
  </div>
</section>
```

**When to use:** Section 2-3. Before testimonials, after value props.

### 4. Quotes (review list)

Text-only reviews. Lowest impact but high volume works (10+ reviews).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">12,000+ 5-Star Reviews</h2>
    <div data-island="ReviewCarousel" data-props='{"autoplay":true,"reviewsPerView":3,"reviews":[{"rating":5,"text":"Exceeded expectations. Results were visible in days. Highly recommend.","author":"John D.","verified":true,"date":"2026-06-15"}]}'></div>
  </div>
</section>
```

**When to use:** Mid-page (sections 5-8). Pile-on after testimonials for reinforcement.

---

## Urgency & Scarcity

Three types. Each requires different implementation and psychology.

### 1. Real Scarcity (Inventory)

Only use if actually tracking inventory. False scarcity destroys brand trust.

```html
<div class="inline-flex items-center gap-2 px-4 py-2 rounded" style="background:#fff3cd;color:#856404">
  <span class="font-semibold">⚠️ Only 7 left in stock</span>
</div>
<div data-island="InventoryIndicator" data-props='{"threshold":10,"lowStockMessage":"Only {count} left in stock","outOfStockMessage":"Sold out — join waitlist"}'></div>
```

**When to use:** High-demand products, limited editions, seasonal items.

### 2. Deadline (Countdown)

Time-limited offers. Must have real expiration.

```html
<div class="sticky top-0 z-50 py-3 px-4 text-center text-white font-semibold text-sm" style="background:#c9302c">
  🔥 Summer Sale: 30% Off Ends in
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"","urgencyThreshold":3600}'></div>
  <a href="#shop" class="ml-4 underline">Shop Now</a>
</div>
```

**When to use:** Flash sales, product launches, abandoned cart recovery.

### 3. Exclusivity (Limited Access)

Member-only, waitlist, invite-only framing.

```html
<section class="py-20 px-4 text-center" style="background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto space-y-6">
    <h2 class="text-4xl font-bold" style="color:var(--lx-text-color)">Join the Waitlist</h2>
    <p class="text-lg opacity-80">Limited to 500 founding members. Next batch ships August 2026.</p>
    <div class="inline-block px-4 py-2 rounded-full text-sm font-semibold" style="background:#f0f0f0">
      127 spots remaining
    </div>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Reserve Your Spot"}'></div>
  </div>
</section>
```

**When to use:** Pre-launch, beta access, VIP tiers.

### Anti-Patterns (Fake Urgency)

| ❌ Don't | Why | ✅ Do |
|----------|-----|-------|
| Evergreen countdowns (timer resets on refresh) | Users notice, trust tanks | Use real sale end dates, or remove timer |
| "Only 2 left!" for digital products | Obvious lie | Use enrollment caps ("Only 50 spots in this cohort") |
| "Sale ends tonight" every night | Cried wolf effect | Run real weekly/monthly sales with calendar |
| SocialProofPopup with fake names | "John from New York just bought" on loop | Only use if pulling real order events from API |

---

## Cognitive Load Management

Max 3 choices per section. More options = decision paralysis = abandonment.

### Feature Grid (3 features, not 7)

**Good (3 features):**
```html
<section class="py-16 px-4">
  <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
    <div class="text-center space-y-4">
      <span class="text-5xl">⚡</span>
      <h3 class="text-xl font-bold">Fast Results</h3>
      <p class="opacity-80">See improvements in 7 days or less</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">🛡️</span>
      <h3 class="text-xl font-bold">Risk-Free</h3>
      <p class="opacity-80">60-day money-back guarantee</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">❤️</span>
      <h3 class="text-xl font-bold">Love It</h3>
      <p class="opacity-80">Join 47,000+ happy customers</p>
    </div>
  </div>
</section>
```

**If you have 6+ features:** Split into 2 sections (benefits vs. technical specs).

### CompareTable (3 columns max, 5-8 rows)

```html
<div data-island="CompareTable" data-props='{"columns":[{"name":"Competitor A","highlight":false},{"name":"You","highlight":true},{"name":"Competitor B","highlight":false}],"rows":[{"feature":"Feature 1","values":["❌","✅","❌"]},{"feature":"Feature 2","values":["✅","✅","❌"]},{"feature":"Feature 3","values":["❌","✅","✅"]}]}'></div>
```

### Progressive Disclosure (Tabs/FAQ)

Use islands for deep info. Don't dump paragraphs.

```html
<div data-island="Tabs" data-props='{"tabs":[{"label":"How It Works","content":"..."},{"label":"Ingredients","content":"..."},{"label":"Shipping","content":"..."}]}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"How long does shipping take?","answer":"2-3 business days."}]}'></div>
```

---

## Trust Escalation Ladder

Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.

### Sequence:

1. **Browse encouragement** (no commitment)
   - Hero: "Explore our collection"
   - Value props: "See why 47,000+ customers love us"

2. **Email capture** (small commitment)
   - Offer: "Get 10% off your first order"
   - Placement: Section 3-5
   - `data-island="EmailCapture"`

3. **Cart confidence** (medium commitment)
   - `data-island="BuyBox"` with "Add to Cart"
   - Show: trust badges, free shipping, easy returns

4. **Purchase trigger** (high commitment)
   - Final CTA: "Complete your order"
   - Add: `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`
   - Show: risk reversal (guarantee)

---

## CTA Psychology

Button copy is conversion science. Every word matters.

### First-Person Labels

**Bad (second-person):**
- "Get Started"
- "Buy Now"
- "Download the Guide"

**Good (first-person):**
- "Start MY Free Trial"
- "Add to MY Cart"
- "Send ME the Guide"

**Why it works:** First-person creates ownership before purchase.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Start MY Transformation
</button>
```

### Benefit-Driven Copy

**Bad (action-only):**
- "Submit"
- "Continue"
- "Next"

**Good (action + benefit):**
- "Get My Discount"
- "Unlock Free Shipping"
- "Claim My Spot"

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Claim My 30% Off
</button>
```

### Contrast Principle

CTA button must have 4.5:1 contrast ratio against background (WCAG AA). Use high-chroma colors.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg shadow-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 4px 12px rgba(102,126,234,0.4)">
  Add to Cart
</button>
```

**Color pairs (high contrast):**
- Blue CTA on white: `#667eea` / `#ffffff`
- Red CTA on dark: `#c9302c` / `#1a1a1a`
- Green CTA on light: `#28a745` / `#f9fafb`

### Button Hierarchy

**Primary (main action):**
```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Buy Now — $89
</button>
```

**Secondary (alternative action):**
```html
<button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
  Learn More
</button>
```

**Ghost (low-commitment):**
```html
<button class="px-6 py-3 rounded-lg hover:bg-opacity-10" style="color:var(--lx-accent-color)">
  View Details
</button>
```

**Link (minimal friction):**
```html
<a href="#learn-more" class="underline" style="color:var(--lx-accent-color)">
  Learn More
</a>
```

### Dual CTA (high + low commitment)

Offer high-commitment + low-commitment options.

```html
<div class="flex gap-4 justify-center">
  <button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
    Buy Now — $89
  </button>
  <button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
    Learn More
  </button>
</div>
```

**When to use:** High-ticket products ($300+), complex products needing education.

---

## Visual Hierarchy for Conversion

Eye-flow patterns direct attention to CTAs.

### Focal Points (element styles)

Use scale, color, and whitespace to create hierarchy.

**Headline (most important):**
```html
<h1 class="text-5xl md:text-7xl font-extrabold leading-tight mb-4" style="color:var(--lx-text-color)">
  Transform Your Skin in 30 Days
</h1>
```

**Subline (secondary):**
```html
<p class="text-xl md:text-2xl leading-relaxed mb-8" style="color:var(--lx-text-muted)">
  Clinically proven formula with visible results in just 2 weeks
</p>
```

**CTA (action):**
```html
<button class="px-10 py-5 text-xl font-bold rounded-lg shadow-2xl transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 8px 24px rgba(102,126,234,0.5)">
  Get Started
</button>
```

### Whitespace for Emphasis

Surround CTAs with empty space (min 2rem padding).

```html
<section class="py-20 px-4">
  <!-- CTA content -->
</section>
```

---

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

---

## Complete Page Recipes

### Recipe 1: Lead Gen (Email Capture)

**Goal:** Maximize email signups for nurture sequence.

**VibePage structure (abbreviated):**
```json
{
  "head": {
    "title": "Get the Ultimate Skincare Guide",
    "fonts": ["https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap"]
  },
  "theme_css": ":root { --lx-accent-color: #667eea; --lx-text-color: #1a1a1a; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class='py-20 px-4 text-center' style='background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)'><div class='max-w-3xl mx-auto space-y-6'><h1 class='text-5xl md:text-6xl font-extrabold text-white'>Get the Flawless Skin Guide</h1><p class='text-xl text-white/90'>Learn how to achieve radiant skin in 30 days. Free download.</p><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Send Me the Guide\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class='py-16 px-4'><div class='grid md:grid-cols-3 gap-8 max-w-5xl mx-auto'><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Science-Backed Methods</h3><p class='opacity-80'>Proven techniques from dermatologists</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Natural Ingredients</h3><p class='opacity-80'>No harsh chemicals or side effects</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>30-Day Results</h3><p class='opacity-80'>See visible improvements in one month</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><div class='grid grid-cols-2 gap-8 max-w-4xl mx-auto text-center'><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>47,000+</p><p class='text-sm uppercase mt-2 opacity-70'>Downloads</p></div><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>4.9/5</p><p class='text-sm uppercase mt-2 opacity-70'>Rating</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class='py-20 px-4 text-center'><div class='max-w-2xl mx-auto space-y-6'><h2 class='text-4xl font-bold' style='color:var(--lx-text-color)'>Ready to Get Started?</h2><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Download Now — It\\'s Free\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 2: Direct Purchase (Low-ticket <$100)

**Goal:** Impulse buy, minimal friction.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8'><div><img src='/product.jpg' class='w-full rounded-lg'/></div><div class='flex flex-col justify-center space-y-6'><h1 class='text-5xl font-bold' style='color:var(--lx-text-color)'>Premium Serum</h1><p class='text-xl opacity-80'>Transform your skin in 30 days</p><div class='flex items-baseline gap-3'><span class='text-3xl font-bold' style='color:var(--lx-text-color)'>$79.99</span><span class='text-lg line-through opacity-40'>$119.99</span><span class='text-xs font-semibold px-2 py-1 rounded-full text-white' style='background:var(--lx-accent-color)'>33% OFF</span></div><div data-island='BuyBox' data-props='{\"productId\":\"gid://shopify/Product/123\",\"ctaText\":\"Add to Cart — Free Shipping\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 3: High-AOV ($500+)

**Goal:** Build trust for expensive purchase.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='relative min-h-screen flex items-center justify-center px-4' style='background:url(/hero.jpg) center/cover'><div class='max-w-3xl text-center space-y-6 text-white'><h1 class='text-6xl font-extrabold'>Enterprise CRM Platform</h1><p class='text-2xl'>Trusted by Fortune 500 companies</p><button class='px-8 py-4 text-lg font-bold rounded-lg' style='background:white;color:var(--lx-accent-color)'>Schedule a Demo</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "logos",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><p class='text-center text-sm uppercase tracking-wide mb-8 opacity-70'>Trusted by Industry Leaders</p><div class='flex justify-center gap-12 flex-wrap'><img src='/logos/company1.svg' class='h-10 opacity-60'/><img src='/logos/company2.svg' class='h-10 opacity-60'/><img src='/logos/company3.svg' class='h-10 opacity-60'/></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

**End of conversion-psychology.md**


---

## FOOD-EXPERTISE

# Food & Beverage DTC — Storefront Design Intelligence

> When to load: Product vertical is food, beverages, snacks, meal kits, coffee, tea, specialty food.

## Philosophy

Food pages sell with the SENSES. The visitor should almost taste/smell the product through the screen. Photography is 80% of the conversion. Every section should trigger appetite or curiosity.

Design must feel: **warm, inviting, appetizing, honest**. Like a farmer's market stall or a well-curated specialty store, not a supermarket shelf.

Key insight: food buyers are driven by:
1. **Appetite** (visual appeal, make them hungry)
2. **Values** (sourcing, ingredients, sustainability)
3. **Convenience** (subscription, bundles, easy reorder)
4. **Community** (reviews, recipes, shared experiences)

The golden rule: if the visitor can't imagine the taste/smell/texture from your hero section, you've lost them. Food is the most sensory-driven vertical in ecommerce.

Pages = **raw HTML + Tailwind CSS + CSS custom properties + React islands**.

## Architecture

**VibePage format:**
```json
{
  "head": {
    "title": "Rich, Bold, Unforgettable Coffee",
    "description": "...",
    "keywords": ["coffee", "single-origin", "organic"]
  },
  "theme_css": ":root { --lx-accent-color: #6F4E37; --lx-text-color: #2C1810; ... }",
  "sections": [
    {
      "id": "hero",
      "html": "<section>...</section>",
      "css": "",
      "js": ""
    }
  ]
}
```

**CSS custom properties:**
- `var(--lx-accent-color)` — primary brand color
- `var(--lx-text-color)` — body text
- `var(--lx-text-muted)` — secondary text
- `var(--lx-bg-color)` — page background
- `var(--lx-bg-surface)` — card/surface background
- `var(--lx-border-color)` — border color
- `var(--lx-font-heading)` — heading font family
- `var(--lx-font-body)` — body font family

**React islands:**
BuyBox, ProductGallery, BundleBuilder, SubscriptionToggle, ReviewCarousel, SocialProofPopup, TrustBadgeBar, FAQ, VideoPlayer, Tabs, ProductCarousel, CountdownTimer, EmailCapture, QuantityBreaks

Islands are hydrated via: `<div data-island="Name" data-props='{"key":"value"}'></div>`

**Tailwind CSS:** All utilities available. Responsive design via breakpoints (`sm:`, `md:`, `lg:`, `xl:`).

---

## Section Sequences

### Single Product (coffee, hot sauce, artisan snack)

**8-10 sections. Sensory-first flow:**

1. **Hero** — Appetizing full-width image (macro pour, steam, drizzle, bite). Headline describes TASTE or EXPERIENCE.
2. **Value Props** — 3 taste/quality pillars (icons + short text).
3. **Origin Story** — Large immersive section with farm/source imagery. Build trust through transparency.
4. **How to Use** — Recipe inspiration, preparation methods (3-4 tiles).
5. **Reviews** — Taste-focused reviews with photo uploads.
6. **Subscription** — BuyBox + SubscriptionToggle island, show savings.
7. **Nutrition Tabs** — Tabs island (Ingredients | Nutrition | Allergens | Sourcing).
8. **Trust Stats** — Social proof numbers.
9. **Final CTA** — Lifestyle shot with one-click add-to-cart.

**Islands:** BuyBox (with SubscriptionToggle), ReviewCarousel, Tabs, TrustBadgeBar

---

### Subscription Box (meal kit, snack box, coffee club)

**10-12 sections. Value-first, convenience-focused:**

1. **Hero** — Unboxing moment (flat-lay of box contents).
2. **How It Works** — 3-step explainer.
3. **What's Inside** — Product grid for this month's box.
4. **Customization** — Dietary filters, frequency selector.
5. **Pricing Plans** — QuantityBreaks island (1/3/6/12-month tiers).
6. **Sourcing Story** — Farm partners, quality curation.
7. **Reviews** — Subscription longevity reviews.
8. **Press Mentions** — Logo carousel.
9. **FAQ** — Skip/pause, cancellation, allergens.
10. **Final CTA** — "Start Your Subscription" with risk-free messaging.

**Islands:** BundleBuilder (if build-your-own-box), SubscriptionToggle, QuantityBreaks, ReviewCarousel, FAQ

---

### Variety Pack / Bundle

**8-10 sections. Discovery-first, flavor exploration:**

1. **Hero** — Spread/flat-lay of all flavors.
2. **Flavor Grid** — Each flavor gets a tile (photo + name + taste description).
3. **Build-Your-Own** — BundleBuilder island with visual selector.
4. **Savings Display** — QuantityBreaks island (3/6/12-pack tiers).
5. **Flavor-Specific Reviews** — Group by product.
6. **Pairing Suggestions** — Lifestyle photos, recipe ideas.
7. **FAQ** — Flavor recommendations, freshness.
8. **Cross-Sell** — ProductCarousel island.

**Islands:** BundleBuilder, QuantityBreaks, ReviewCarousel (flavor-segmented), ProductCarousel, Tabs

---

### Brand Story / Farm-to-Table

**6-8 sections. For sourcing stories, founder journey, sustainability:**

1. **Hero** — Founder or farm photo (warm, authentic).
2. **Origin Story** — Large immersive section with farm/source imagery.
3. **Commitments** — 4-tile sustainability/quality grid.
4. **Community Testimonials** — Values alignment focus.
5. **Certifications** — Logo carousel (USDA Organic, Fair Trade, etc.).
6. **Impact Stats** — Environmental/social impact numbers.
7. **Final CTA** — "Shop Our Story" with product link.

---

## Island Combinations

**The Food DTC Conversion Stack:**

### BundleBuilder
For variety packs, build-your-box subscriptions, flavor samplers. Visual selector with dynamic pricing.

```html
<div class="max-w-5xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Build Your Custom 6-Pack
    </h2>
    <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
      Choose your favorite flavors
    </p>
  </div>
  <div data-island="BundleBuilder" data-props='{"products":[{"id":"espresso","name":"Espresso Blend","image":"espresso.jpg","price":12},{"id":"light","name":"Light Roast","image":"light.jpg","price":12},{"id":"dark","name":"Dark Roast","image":"dark.jpg","price":12},{"id":"decaf","name":"Decaf","image":"decaf.jpg","price":12}],"minSelection":6,"maxSelection":6,"bundlePrice":66,"savings":6}'></div>
</div>
```

---

### SubscriptionToggle
For recurring delivery. Toggle between one-time and subscription with savings prominently displayed.

```html
<div class="max-w-2xl mx-auto px-6 py-20">
  <div class="bg-white rounded-2xl shadow-lg p-8">
    <div class="flex items-center justify-center gap-6 mb-6">
      <img src="PRODUCT_IMAGE" alt="Coffee bag" class="w-48 h-48 object-cover rounded-lg" />
      <div>
        <h3 style="font-family:var(--lx-font-heading);font-size:1.75rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem">
          Ethiopian Yirgacheffe
        </h3>
        <p style="font-size:1rem;color:var(--lx-text-muted);margin-bottom:1.5rem">
          Single-origin, small-batch roasted
        </p>
        <div data-island="SubscriptionToggle" data-props='{"oneTimePrice":24,"subscriptionPrice":19.20,"savingsPercent":20,"frequencies":["Every 2 weeks","Every 1 month","Every 2 months"]}'></div>
      </div>
    </div>
  </div>
</div>
```

---

### QuantityBreaks
For bulk savings (3-pack, 6-pack, 12-pack). Tiered pricing cards with "Best Value" badge.

```html
<div class="max-w-5xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Stock Up & Save
    </h2>
  </div>
  <div data-island="QuantityBreaks" data-props='{"tiers":[{"quantity":3,"price":36,"perUnit":12,"savings":6},{"quantity":6,"price":66,"perUnit":11,"savings":12,"badge":"Best Value"},{"quantity":12,"price":120,"perUnit":10,"savings":24}]}'></div>
</div>
```

---

### ReviewCarousel
Taste and flavor-focused reviews. Filter by product/flavor. Highlight photo reviews.

```html
<div class="max-w-6xl mx-auto px-6 py-20" style="background:var(--lx-bg-surface)">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Loved by 12,847 Coffee Enthusiasts
    </h2>
  </div>
  <div data-island="ReviewCarousel" data-props='{"productId":"coffee-ethiopian","filterOptions":["5-star","Photo reviews","Verified purchase"],"highlightKeywords":["delicious","fresh","authentic","best"]}'></div>
</div>
```

---

### Tabs (Nutritional Transparency)
For ingredients, nutrition facts, allergens, sourcing story.

```html
<div class="max-w-4xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Transparency Matters
    </h2>
  </div>
  <div data-island="Tabs" data-props='{"tabs":[{"label":"Ingredients","content":"<div class=\"space-y-4\"><div class=\"flex items-center gap-2 text-sm\"><svg class=\"w-5 h-5 text-green-600\">...</svg>Certified Organic</div><div class=\"flex items-center gap-2 text-sm\"><svg class=\"w-5 h-5 text-green-600\">...</svg>Fair Trade</div><p class=\"mt-4\">100% Arabica Coffee Beans from Ethiopia</p></div>"},{"label":"Nutrition","content":"<table class=\"w-full text-sm\"><tr><td>Calories</td><td>5</td></tr><tr><td>Caffeine</td><td>95mg</td></tr></table>"},{"label":"Allergens","content":"<p>Contains: None</p><p class=\"text-xs text-gray-500 mt-2\">Processed in a facility that handles tree nuts</p>"},{"label":"Sourcing","content":"<p>Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers. Harvested at 1,800-2,200 meters elevation.</p>"}]}'></div>
</div>
```

---

### ProductCarousel
For cross-sells and pantry completion.

```html
<div class="max-w-6xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Complete Your Pantry
    </h2>
  </div>
  <div data-island="ProductCarousel" data-props='{"products":[{"id":"grinder","name":"Coffee Grinder","image":"grinder.jpg","price":49},{"id":"mug","name":"Ceramic Mug","image":"mug.jpg","price":18},{"id":"pourover","name":"Pour Over Kit","image":"pourover.jpg","price":34},{"id":"beans","name":"Espresso Blend","image":"beans.jpg","price":24}]}'></div>
</div>
```

---

### TrustBadgeBar
Certifications and trust signals. Place near BuyBox or after hero.

```html
<div class="max-w-6xl mx-auto px-6 py-12 border-y" style="border-color:var(--lx-border-color)">
  <div data-island="TrustBadgeBar" data-props='{"badges":[{"icon":"organic","label":"USDA Organic"},{"icon":"fairtrade","label":"Fair Trade"},{"icon":"nongmo","label":"Non-GMO"},{"icon":"vegan","label":"Vegan"},{"icon":"glutenfree","label":"Gluten-Free"}]}'></div>
</div>
```

---

### FAQ
For objection handling. Cover shipping freshness, allergens, subscription management.

```html
<div class="max-w-3xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Frequently Asked Questions
    </h2>
  </div>
  <div data-island="FAQ" data-props='{"questions":[{"q":"How should I store my coffee?","a":"Store in an airtight container in a cool, dry place. Avoid refrigeration."},{"q":"What is the caffeine content?","a":"Approximately 95mg per 8oz cup."},{"q":"Can I change my subscription frequency?","a":"Yes, you can skip, pause, or adjust frequency anytime in your account."},{"q":"What is your freshness guarantee?","a":"We roast to order and ship within 24 hours. All coffee is roasted within 7 days of delivery."}]}'></div>
</div>
```

---

## Typography & Color

### Typography

Warm and approachable. **Rounded sans-serif or friendly serif for headlines.**

**Weights:** 500-700 (medium to bold). Food isn't tech — avoid thin weights (300) and ultra-bold (800+).

**Sizes:**
- **Hero headline:** `clamp(2.25rem, 5vw, 4rem)` (36px → 64px)
- **Section headlines:** `clamp(1.75rem, 3.5vw, 3rem)` (28px → 48px)
- **Subline:** `clamp(1rem, 2vw, 1.25rem)` (16px → 20px), line-height: 1.6-1.7
- **Eyebrow:** `clamp(0.875rem, 1.5vw, 1rem)` (14px → 16px), letter-spacing: `0.05em`

**Font pairing suggestions:**
- **Warm modern:** Inter (body) + Fraunces (headlines, friendly serif)
- **Artisan/craft:** Source Sans 3 (body) + Playfair Display (headlines, editorial serif)
- **Fun/snack brand:** DM Sans (body) + Quicksand (headlines, rounded sans)
- **Premium/luxury:** Crimson Text (body + headlines, elegant serif) or Cormorant (headlines) + Lato (body)

---

### Color & Backgrounds

Warm palette ALWAYS. Derive from food/ingredient colors:

- **Coffee/chocolate:** rich browns (#4A2C2A, #6F4E37), cream (#F5EDE4), burnt orange (#D2691E)
- **Tomato/sauce:** deep red (#C1440E), terracotta (#E07A5F), warm white (#FFFDF7)
- **Avocado/health:** sage green (#88A096), olive (#6B8E23), off-white (#FAFAF5)
- **Honey/bakery:** golden yellow (#F4A460), amber (#FFBF00), warm beige (#F5E6D3)
- **Berry/fruit:** deep purple (#6A0572), raspberry (#E30B5C), blush pink (#FFB6C1)
- **Organic/earth:** khaki (#C3B091), clay (#B87333), natural linen (#FAF0E6)

**NEVER:**
- Clinical white (#FFFFFF) — too sterile
- Tech blue (#0066FF) or neon (#00FFFF)
- Pure black (#000000) — use warm dark brown (#2C1810)

**Example theme_css:**

```css
:root {
  --lx-accent-color: #6F4E37;
  --lx-text-color: #2C1810;
  --lx-text-muted: #5C4A42;
  --lx-bg-color: #FFFDF7;
  --lx-bg-surface: #F5EDE4;
  --lx-border-color: #E5D7CB;
  --lx-font-heading: 'Fraunces', serif;
  --lx-font-body: 'Inter', sans-serif;
}
```

---

## Hero Patterns

### Food Photography Hero

```html
<section class="relative min-h-[80vh] flex items-end" style="background:var(--lx-bg-color)">
  <img src="IMAGE_URL" alt="Coffee pour" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
  <div class="relative z-10 max-w-3xl mx-auto text-center pb-16 px-6 text-white space-y-4">
    <p class="text-xs uppercase tracking-[0.15em] opacity-80">Single Origin • Small Batch</p>
    <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600">
      Your Morning Ritual, Perfected
    </h1>
    <p style="font-size:clamp(1rem,2vw,1.25rem);line-height:1.6;opacity:90">
      Rich, bold Ethiopian Yirgacheffe with notes of blueberry and dark chocolate
    </p>
    <button class="px-8 py-4 rounded-lg font-semibold bg-white text-black text-sm hover:bg-gray-100 transition">
      Shop Coffee →
    </button>
  </div>
</section>
```

---

### Flat-lay Grid Hero

```html
<section class="relative min-h-[90vh] flex items-center justify-center" style="background:var(--lx-bg-color)">
  <img src="FLATLAY_IMAGE" alt="All five flavors spread" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/30"></div>
  <div class="relative z-10 max-w-4xl mx-auto text-center px-6 text-white space-y-6">
    <p class="text-sm uppercase tracking-[0.15em] opacity-90">Variety Pack</p>
    <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,6vw,4.5rem);font-weight:700">
      Discover Your New Favorite
    </h1>
    <p style="font-size:clamp(1.125rem,2.5vw,1.5rem);line-height:1.5;max-width:40rem;margin:0 auto">
      Five bold flavors in one sampler pack. Crunchy, satisfying, and made with real ingredients.
    </p>
    <button class="px-10 py-5 rounded-lg font-semibold text-base" style="background:var(--lx-accent-color);color:white">
      Shop the Sampler
    </button>
  </div>
</section>
```

---

## Subscription Section

```html
<section class="py-24 px-6" style="background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Never Run Out
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Subscribe and save 20% on every delivery
      </p>
    </div>
    
    <div class="bg-white rounded-2xl shadow-xl p-10 max-w-2xl mx-auto">
      <div class="flex flex-col md:flex-row items-center gap-8">
        <img src="PRODUCT_IMAGE" alt="Coffee bag" class="w-64 h-64 object-cover rounded-xl" />
        <div class="flex-1">
          <h3 style="font-family:var(--lx-font-heading);font-size:1.5rem;font-weight:600;color:var(--lx-text-color);margin-bottom:1rem">
            Ethiopian Yirgacheffe
          </h3>
          <div data-island="SubscriptionToggle" data-props='{"oneTimePrice":24,"subscriptionPrice":19.20,"savingsPercent":20,"frequencies":["Every 2 weeks","Every 1 month","Every 2 months"],"defaultFrequency":"Every 1 month"}'></div>
          <p class="text-xs text-gray-500 mt-4">Skip or cancel anytime. No commitment.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Bundle Builder

```html
<section class="py-24 px-6" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Build Your Perfect Pack
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Choose 6 bags and save $12
      </p>
    </div>
    
    <div data-island="BundleBuilder" data-props='{
      "products": [
        {"id":"espresso","name":"Espresso Blend","description":"Bold & Intense","image":"espresso.jpg","price":12},
        {"id":"light","name":"Light Roast","description":"Bright & Fruity","image":"light.jpg","price":12},
        {"id":"dark","name":"Dark Roast","description":"Smoky & Rich","image":"dark.jpg","price":12},
        {"id":"decaf","name":"Decaf","description":"Smooth & Mellow","image":"decaf.jpg","price":12},
        {"id":"cold-brew","name":"Cold Brew Blend","description":"Sweet & Refreshing","image":"cold-brew.jpg","price":12},
        {"id":"french-roast","name":"French Roast","description":"Deep & Robust","image":"french.jpg","price":12}
      ],
      "minSelection": 6,
      "maxSelection": 6,
      "bundlePrice": 66,
      "savings": 6
    }'></div>
  </div>
</section>
```

---

## Nutritional Transparency

```html
<section class="py-24 px-6" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        What's Inside
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Transparency matters
      </p>
    </div>
    
    <div data-island="Tabs" data-props='{
      "tabs": [
        {
          "label": "Ingredients",
          "content": "<div class=\"space-y-4\"><div class=\"flex flex-wrap gap-3 mb-6\"><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Certified Organic</span><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Fair Trade</span><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Single Origin</span></div><p class=\"text-base\" style=\"color:var(--lx-text-color)\">100% Arabica Coffee Beans from Ethiopia</p><p class=\"text-sm mt-3\" style=\"color:var(--lx-text-muted)\">Roasted in small batches in Portland, Oregon</p></div>"
        },
        {
          "label": "Nutrition",
          "content": "<table class=\"w-full text-sm\"><tbody><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Serving Size</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">8 fl oz (237mL)</td></tr><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Calories</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">5</td></tr><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Caffeine</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">95mg</td></tr><tr><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Fat</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">0g</td></tr></tbody></table>"
        },
        {
          "label": "Allergens",
          "content": "<div class=\"space-y-4\"><p class=\"text-base font-medium\" style=\"color:var(--lx-text-color)\">Contains: None</p><p class=\"text-sm mt-4\" style=\"color:var(--lx-text-muted)\">Processed in a facility that also handles tree nuts</p><div class=\"flex flex-wrap gap-2 mt-6\"><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Gluten-Free</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Dairy-Free</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Vegan</span></div></div>"
        },
        {
          "label": "Sourcing",
          "content": "<div class=\"space-y-4\"><p class=\"text-base\" style=\"color:var(--lx-text-color)\">Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers.</p><p class=\"text-base mt-4\" style=\"color:var(--lx-text-color)\">Harvested at 1,800-2,200 meters elevation, processed naturally, and shipped directly to our roastery in Portland.</p><div class=\"mt-6 p-4 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><p class=\"text-xs uppercase tracking-wider font-semibold mb-2\" style=\"color:var(--lx-text-muted)\">Certifications</p><div class=\"flex flex-wrap gap-2\"><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\">USDA Organic</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800\">Fair Trade</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-amber-100 text-amber-800\">Rainforest Alliance</span></div></div></div>"
        }
      ]
    }'></div>
  </div>
</section>
```

---

## Social Proof for Food

```html
<section class="py-24 px-6" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-sm uppercase tracking-wider font-semibold mb-2" style="color:var(--lx-accent-color)">Loved by Thousands</p>
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Join 12,847 Happy Customers
      </h2>
      <div class="flex items-center justify-center gap-2 mt-4">
        <div class="flex">
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
        </div>
        <span class="text-sm font-medium" style="color:var(--lx-text-color)">4.9 out of 5</span>
      </div>
    </div>
    
    <div data-island="ReviewCarousel" data-props='{
      "productId": "coffee-ethiopian",
      "filterOptions": ["5-star", "Photo reviews", "Verified purchase"],
      "highlightKeywords": ["delicious", "fresh", "authentic", "best", "amazing", "perfect"]
    }'></div>
  </div>
</section>
```

---

## Photography

**CRITICAL:** Food is a visual vertical. Photography makes or breaks conversion.

### Photography Angles

1. **Overhead flat-lay** — Ingredients spread out. Shows abundance. Perfect for: variety packs, meal kit "what's inside".
2. **45-degree hero angle** — Product in use (mug, plate). Creates appetite. Perfect for: hero sections, lifestyle moments.
3. **Macro texture** — Extreme close-up (pour, drizzle, steam). Triggers sensory response. Perfect for: parallax sections, product detail.
4. **Ingredient heroes** — Raw materials (coffee cherries, tomatoes on vine). Shows quality. Perfect for: origin stories, farm-to-table.
5. **Preparation moments** — Action shots (pouring, stirring, chopping). Shows how to use. Perfect for: recipe sections, how-to.
6. **Unboxing** — Subscription box opened, products arranged. Shows value. Perfect for: subscription landing pages.

### Asset Generation Keywords

**For coffee/beverages:**
- "Overhead shot of steaming coffee cup on rustic wooden table, morning light, minimalist aesthetic"
- "Macro close-up of coffee beans being poured, shallow depth of field, warm tones"
- "Pour-over coffee setup with gooseneck kettle, artisan aesthetic, soft natural light"

**For snacks/packaged food:**
- "Flat-lay of colorful snack variety pack, vibrant packaging, scattered arrangement, white background"
- "Close-up of crunchy snack texture, appetizing macro shot, warm lighting"
- "Hand holding snack bag outdoors, lifestyle moment, natural setting"

**For meal kits/fresh food:**
- "Overhead flat-lay of fresh ingredients for meal kit, vibrant vegetables, recipe card visible"
- "Plated finished meal, restaurant-quality presentation, garnished, natural light"
- "Hands chopping vegetables on wooden cutting board, cooking process, warm kitchen"

**For sauces/condiments:**
- "Sauce drizzle on dish, macro shot, appetizing texture, shallow depth of field"
- "Hot sauce bottles arranged on rustic shelf, warm lighting, artisan aesthetic"
- "Close-up of sauce texture in bowl, vibrant color, food photography style"

---

## Anti-Patterns

These mistakes will tank conversion:

1. **Small food images** — Food must be 600px+ on desktop. Thumbnails don't trigger appetite.
2. **Clinical/sterile layouts** — All-white backgrounds look like a pharmacy. Add warmth.
3. **Missing texture/appetite cues** — No steam, drizzle, pour shots, close-ups = no sensory response.
4. **No sourcing story** — Food buyers care WHERE food comes from. Omitting origin = missed trust-building.
5. **Generic product-on-white** — Stock-looking shots with no context scream "commodity".
6. **Cold color palettes** — Blues, teals, grays are wrong for food. Use warm tones.
7. **Tech-style typography** — Ultra-thin fonts (200-300) feel cold. Use 400-600 weights.
8. **No preparation/recipe context** — Visitors need to imagine USING the product.
9. **Hiding nutrition info** — Health-conscious buyers need ingredients, allergens, macros.
10. **Subscription without clear savings** — Savings MUST be immediately visible, not hidden.
11. **Stock food photography** — Generic, perfect images scream "fake". Use real product photos.
12. **Too many flavors without guidance** — 12 flavors with no bestseller/sampler = decision paralysis.
13. **No freshness messaging** — Communicate "roasted this week", "made to order", "ships within 24 hours".
14. **Ignoring dietary filters** — No allergen info or vegan/gluten-free badges = losing customer segments.
15. **Weak CTAs** — "Buy Now" is boring. Use specific: "Shop [Flavor]", "Try the Sampler", "Build Your Box".

---

## Complete Blueprint: Premium Coffee PDP

```json
{
  "head": {
    "title": "Rich, Bold Ethiopian Yirgacheffe Coffee | Single-Origin",
    "description": "Premium single-origin Ethiopian Yirgacheffe coffee with notes of blueberry and dark chocolate. Roasted fresh weekly. Subscribe and save 20%.",
    "keywords": ["coffee", "single-origin", "ethiopian coffee", "organic coffee", "fair trade"]
  },
  "theme_css": ":root { --lx-accent-color: #6F4E37; --lx-text-color: #2C1810; --lx-text-muted: #5C4A42; --lx-bg-color: #FFFDF7; --lx-bg-surface: #F5EDE4; --lx-border-color: #E5D7CB; --lx-font-heading: 'Fraunces', serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[80vh] flex items-end\" style=\"background:var(--lx-bg-color)\"><img src=\"coffee-hero.jpg\" alt=\"Coffee pour\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent\"></div><div class=\"relative z-10 max-w-3xl mx-auto text-center pb-16 px-6 text-white space-y-4\"><p class=\"text-xs uppercase tracking-[0.15em] opacity-80\">Single Origin • Small Batch</p><h1 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600\">Your Morning Ritual, Perfected</h1><p style=\"font-size:clamp(1rem,2vw,1.25rem);line-height:1.6;opacity:90\">Rich Ethiopian Yirgacheffe with notes of blueberry and dark chocolate</p><button class=\"px-8 py-4 rounded-lg font-semibold bg-white text-black text-sm hover:bg-gray-100 transition\">Shop Coffee →</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class=\"py-20 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-5xl mx-auto\"><div class=\"grid grid-cols-1 md:grid-cols-3 gap-12\"><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M10 3.5a1.5 1.5 0 013 0V4a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-.5a1.5 1.5 0 000 3h.5a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-.5a1.5 1.5 0 00-3 0v.5a1 1 0 01-1 1H6a1 1 0 01-1-1v-3a1 1 0 00-1-1h-.5a1.5 1.5 0 010-3H4a1 1 0 001-1V6a1 1 0 011-1h3a1 1 0 001-1v-.5z\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Single-Origin Ethiopia</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">From the Yirgacheffe region, 2,000m elevation</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z\" clip-rule=\"evenodd\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Small-Batch Roasted</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">Roasted fresh weekly in Portland, Oregon</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M9 2a1 1 0 000 2h2a1 1 0 100-2H9z\"></path><path fill-rule=\"evenodd\" d=\"M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z\" clip-rule=\"evenodd\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Tasting Notes</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">Blueberry, dark chocolate, caramel finish</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "origin-story",
      "html": "<section class=\"relative min-h-[500px] flex items-center\" style=\"background:var(--lx-bg-color)\"><img src=\"farm.jpg\" alt=\"Ethiopian coffee farm\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/40\"></div><div class=\"relative z-10 max-w-3xl mx-auto text-center px-6 text-white space-y-4\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600\">Grown at 2,000 Meters in Yirgacheffe</h2><p style=\"font-size:clamp(1rem,2vw,1.25rem);line-height:1.65;max-width:40rem;margin:0 auto\">Sourced from the Abebech Women's Cooperative, where 200 smallholder farmers cultivate coffee with care and tradition.</p></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "subscription",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Never Run Out</h2><p style=\"font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem\">Subscribe and save 20% on every delivery</p></div><div class=\"bg-white rounded-2xl shadow-xl p-10 max-w-2xl mx-auto\"><div class=\"flex flex-col md:flex-row items-center gap-8\"><img src=\"product.jpg\" alt=\"Coffee bag\" class=\"w-64 h-64 object-cover rounded-xl\" /><div class=\"flex-1\"><h3 style=\"font-family:var(--lx-font-heading);font-size:1.5rem;font-weight:600;color:var(--lx-text-color);margin-bottom:1rem\">Ethiopian Yirgacheffe</h3><div data-island=\"SubscriptionToggle\" data-props='{\"oneTimePrice\":24,\"subscriptionPrice\":19.20,\"savingsPercent\":20,\"frequencies\":[\"Every 2 weeks\",\"Every 1 month\",\"Every 2 months\"],\"defaultFrequency\":\"Every 1 month\"}'></div><p class=\"text-xs text-gray-500 mt-4\">Skip or cancel anytime. No commitment.</p></div></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div class=\"text-center mb-12\"><p class=\"text-sm uppercase tracking-wider font-semibold mb-2\" style=\"color:var(--lx-accent-color)\">Loved by Thousands</p><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Join 12,847 Happy Customers</h2></div><div data-island=\"ReviewCarousel\" data-props='{\"productId\":\"coffee-ethiopian\",\"filterOptions\":[\"5-star\",\"Photo reviews\",\"Verified purchase\"],\"highlightKeywords\":[\"delicious\",\"fresh\",\"authentic\",\"best\"]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "transparency",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">What's Inside</h2></div><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"label\":\"Ingredients\",\"content\":\"<div class=\\\"space-y-4\\\"><div class=\\\"flex flex-wrap gap-3 mb-6\\\"><span class=\\\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\\\">✓ Certified Organic</span><span class=\\\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\\\">✓ Fair Trade</span></div><p class=\\\"text-base\\\">100% Arabica Coffee Beans from Ethiopia</p></div>\"},{\"label\":\"Nutrition\",\"content\":\"<table class=\\\"w-full text-sm\\\"><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Serving Size</td><td class=\\\"py-3 text-right font-medium\\\">8 fl oz</td></tr><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Calories</td><td class=\\\"py-3 text-right font-medium\\\">5</td></tr><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Caffeine</td><td class=\\\"py-3 text-right font-medium\\\">95mg</td></tr></table>\"},{\"label\":\"Allergens\",\"content\":\"<p>Contains: None</p><p class=\\\"text-xs text-gray-500 mt-2\\\">Processed in a facility that handles tree nuts</p>\"},{\"label\":\"Sourcing\",\"content\":\"<p>Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers. Harvested at 1,800-2,200 meters elevation.</p>\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Frequently Asked Questions</h2></div><div data-island=\"FAQ\" data-props='{\"questions\":[{\"q\":\"How should I store my coffee?\",\"a\":\"Store in an airtight container in a cool, dry place. Avoid refrigeration.\"},{\"q\":\"What is the caffeine content?\",\"a\":\"Approximately 95mg per 8oz cup.\"},{\"q\":\"Can I change my subscription frequency?\",\"a\":\"Yes, you can skip, pause, or adjust frequency anytime in your account.\"},{\"q\":\"What is your freshness guarantee?\",\"a\":\"We roast to order and ship within 24 hours. All coffee is roasted within 7 days of delivery.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class=\"py-20 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-8 text-center\"><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">500K+</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Bags Shipped</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">4.9★</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Average Rating</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">Fresh</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Roasted Weekly</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">100%</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Certified Organic</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "final-cta",
      "html": "<section class=\"relative min-h-[400px] flex items-center justify-center\"><img src=\"cta.jpg\" alt=\"Coffee mug on table\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/30\"></div><div class=\"relative z-10 text-center px-6 text-white space-y-6\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600\">Your Morning Ritual, Perfected</h2><button class=\"px-10 py-5 rounded-lg font-semibold text-base bg-white text-black hover:bg-gray-100 transition\">Order Now</button></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary: The Food Page Playbook

1. **Lead with appetite** — Hero image must be large, appetizing, sensory (macro shots, steam, drizzle, texture).
2. **Warm everything** — Colors (browns, golds, reds, greens), lighting (morning sun, soft shadows), typography (friendly, readable).
3. **Tell the origin story** — Where it comes from matters. Build trust through transparency.
4. **Make it large** — Food images 600px+ on desktop. Never thumbnails.
5. **Subscriptions sell** — For consumables, show savings prominently, reduce commitment fear ("skip/cancel anytime").
6. **Nutrition transparency** — Tabs for ingredients, allergens, sourcing. Health-conscious buyers need this.
7. **Social proof = taste proof** — Reviews must emphasize flavor, freshness, repeat purchase. Photo reviews prioritized.
8. **Spacing is generous** — 80-96px between sections. Let food breathe.
9. **BundleBuilder for variety** — Visual selector, dynamic pricing, savings callout.
10. **Avoid coldness** — No clinical white, no tech blue, no thin fonts, no small images.

This is the blueprint for food pages that convert.


---

## META-TRAFFIC

# Meta Ads → Landing Page — Storefront Design Intelligence

> **When to load**: Page generated from Meta (Facebook/Instagram) ad creative.  
> **Auto-loads as**: `vibe://skills/traffic-source-meta`

---

## The #1 Rule: Message Match

Meta traffic arrives **interrupted** — they were scrolling feed, not searching. The #1 conversion killer is message discontinuity between ad and landing page.

### Exact Match (Best for Direct Response)
Ad headline: "Finally, a yoga mat that doesn't slip during downward dog"  
Page headline: "Finally, a yoga mat that doesn't slip during downward dog"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
  Finally, a yoga mat that doesn't slip during downward dog
</h1>
<p class="text-lg mt-3" style="color:var(--lx-text-muted)">
  Join 47,000+ yogis who switched to the GripFlow™ non-slip surface
</p>
```

### Evolved Match (Best for Product Pages)
Ad headline: "The yoga mat your feet won't slide on"  
Page headline: "Meet the GripFlow™ Yoga Mat"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
  Meet the GripFlow™ Yoga Mat
</h1>
<p class="text-xl mt-4" style="color:var(--lx-text-muted)">
  The non-slip surface that keeps you locked in—even in hot yoga
</p>
```

### Visual Continuity
If the ad shows **product on pink background** → hero must match:

```html
<section class="relative min-h-[85vh] flex items-center" 
  style="background:linear-gradient(to bottom, #FFE5F0 0%, #FFFFFF 100%)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- Product hero content -->
  </div>
</section>
```

If the ad shows **bold sans-serif headline** → page font must match:

```css
:root {
  --lx-font-heading: 'Inter', system-ui, sans-serif;
}
```

**Ad CTA color = page CTA color:**

```css
:root {
  --lx-accent-color: #FF6B6B;  /* Extracted from ad creative */
}
```

---

## Mobile-First Reality

**85%+ of Meta ad traffic is mobile.** Every design decision must pass the "thumb-zone test."

### Typography for Mobile
All text uses fluid sizing:

```html
<!-- Hero headline -->
<h1 style="font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;letter-spacing:-0.02em;font-weight:700">
  Your yoga mat won't slip anymore
</h1>

<!-- Subline -->
<p style="font-size:clamp(1.125rem,3vw,1.375rem);line-height:1.4;margin-top:1rem">
  The GripFlow™ surface stays locked—even in hot yoga
</p>

<!-- Body copy -->
<p style="font-size:clamp(1rem,2.5vw,1.125rem);line-height:1.6">
  No more adjusting your hands mid-flow. No more slipping in downward dog.
</p>
```

### Spacing for Mobile
Use `clamp()` for all vertical spacing:

```html
<section style="padding-top:clamp(2rem,8vw,5rem);padding-bottom:clamp(2rem,8vw,5rem)">
  <!-- Section content -->
</section>
```

### Tap Targets & Thumb Zone
**All CTAs: min 44px height, large tap area**

```html
<!-- Primary CTA -->
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold transition-colors"
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white">
  Get yours now
</button>

<!-- Sticky CTA (thumb zone) -->
<div data-island="StickyBar" data-props='{
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "60-day guarantee"
}'></div>
```

---

## Section Sequence (The Meta Formula)

This is the **proven sequence for cold Meta traffic** (no brand familiarity, interrupted state):

### 1. Hero (Message Match + Immediate Trust)
**Why first**: 3-second decision window.

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-2xl mx-auto text-center space-y-5">
    <!-- Trust bar (immediate) -->
    <div class="flex justify-center items-center gap-2 text-sm">
      <div class="flex">
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="font-semibold" style="color:var(--lx-text-color)">4.9/5 from 12,847 reviews</span>
    </div>

    <!-- Headline (message match) -->
    <h1 class="font-bold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
      Your yoga mat won't slip anymore
    </h1>

    <!-- Subline -->
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTA -->
    <button class="px-8 py-4 rounded-lg font-semibold" 
      style="background:var(--lx-accent-color);color:white">
      Get yours now
    </button>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Yoga Mat" 
      class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

### 2. Trust Strip (Immediately After Hero)
**Why second**: Meta traffic has ZERO brand equity.

```html
<section class="py-8 border-b" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- shield icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">60-Day Guarantee</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Love it or return it</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- truck icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Free Shipping</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">On all US orders</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- star icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">12,847 5-Star Reviews</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Rated Excellent</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- award icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Featured in Yoga Journal</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Best Mat 2025</p>
      </div>
    </div>
  </div>
</section>
```

### 3. Problem Agitation
**Why third**: Twist the knife before showing solution.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Sick of yoga mats that work against you?
    </h2>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Slipping during downward dog</h3>
        <p style="color:var(--lx-text-muted)">You adjust your hands 5 times per flow</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Sweaty palms = zero grip</h3>
        <p style="color:var(--lx-text-muted)">Hot yoga becomes a safety hazard</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Cheap mats fall apart</h3>
        <p style="color:var(--lx-text-muted)">You've replaced yours 3 times already</p>
      </div>
    </div>
  </div>
</section>
```

### 4. Solution (The Reveal)
**Why fourth**: Now they're primed.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto px-4">
    <div class="text-center mb-12">
      <h2 class="font-bold mb-4" 
        style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
        Meet the GripFlow™ Yoga Mat
      </h2>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        Engineered to solve every problem you just nodded at
      </p>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <!-- Feature 1 -->
      <div class="text-center space-y-4">
        <img src="texture-closeup.jpg" alt="GripFlow surface" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">GripFlow™ Non-Slip Surface</h3>
        <p style="color:var(--lx-text-muted)">
          Proprietary texture that gets grippier as you sweat
        </p>
      </div>

      <!-- Feature 2 -->
      <div class="text-center space-y-4">
        <img src="thickness-demo.jpg" alt="6mm cushion" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">6mm Cushion Core</h3>
        <p style="color:var(--lx-text-muted)">
          Knee-saving thickness without sacrificing stability
        </p>
      </div>

      <!-- Feature 3 -->
      <div class="text-center space-y-4">
        <img src="durability.jpg" alt="Lifetime warranty" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">Lifetime Durability</h3>
        <p style="color:var(--lx-text-muted)">
          Won't peel, crack, or fade—backed by lifetime warranty
        </p>
      </div>
    </div>
  </div>
</section>
```

### 5. Social Proof (Overcome Skepticism)
**Why fifth**: Flood them with proof.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      47,000+ yogis upgraded their practice
    </h2>

    <div class="grid md:grid-cols-3 gap-6">
      <!-- Review 1 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "I've tried 8 different mats. This is the only one that doesn't slip during hot yoga. The grip actually gets better when I sweat. Insane."
        </p>
        <div class="flex items-center gap-3">
          <img src="sarah-avatar.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Sarah M.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "Replaced my Manduka after 5 years. Should've done it sooner. The cushion is perfect—my knees don't hurt anymore."
        </p>
        <div class="flex items-center gap-3">
          <img src="mike-avatar.jpg" class="w-10 h-10 rounded-full" alt="Mike T." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Mike T.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny"
        </p>
        <div class="flex items-center gap-3">
          <img src="emma-avatar.jpg" class="w-10 h-10 rounded-full" alt="Emma L." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Emma L.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 6. Stats & Authority
**Why sixth**: Quantify the transformation.

```html
<section class="py-16 border-y" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-5xl mx-auto px-4">
    <div class="grid md:grid-cols-3 gap-8 text-center">
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">47K+</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Happy Customers</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">4.9/5</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Average Rating</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">99%</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Recommend to Friends</p>
      </div>
    </div>
  </div>
</section>
```

### 7. FAQ (Objection Handling)
**Why seventh**: Address the 5 questions stopping them.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-3xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Questions?
    </h2>

    <div data-island="FAQ" data-props='{
      "items": [
        {
          "question": "What's your return policy?",
          "answer": "60-day money-back guarantee. If you don't love it, return it for a full refund—no questions asked."
        },
        {
          "question": "How long does shipping take?",
          "answer": "All orders ship within 24 hours. Free 2-3 day shipping in the US."
        },
        {
          "question": "Is this really better than Manduka/Liforme?",
          "answer": "The GripFlow™ surface is proprietary. It's physics-tested to grip better as you sweat—other mats get slippery."
        },
        {
          "question": "What if I don't like it?",
          "answer": "Full refund within 60 days. We'll even cover return shipping."
        },
        {
          "question": "Do you have different colors/sizes?",
          "answer": "Yes! Available in 5 colors and 2 sizes (standard + XL). All colors have the same GripFlow™ surface."
        }
      ],
      "style": "minimal"
    }'></div>
  </div>
</section>
```

### 8. Final CTA (Last Chance)
**Why eighth**: They scrolled this far—remove all friction.

```html
<section style="padding:clamp(3rem,8vw,5rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto px-4 text-center space-y-6">
    <h2 class="font-bold" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Your last slippery yoga mat
    </h2>
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who upgraded to GripFlow™
    </p>
    <button class="w-full sm:w-auto px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Get my mat now
    </button>
    <div class="flex justify-center items-center gap-4 text-sm" style="color:var(--lx-text-muted)">
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- shield --></svg>
        60-day guarantee
      </span>
      <span>•</span>
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- truck --></svg>
        Free shipping
      </span>
    </div>
  </div>
</section>
```

---

## Hero Patterns for Meta Traffic

### Pattern 1: Social Proof Hero
**Best for**: High-review-count products

```html
<section class="relative min-h-[85vh] flex items-center px-4" style="background:white">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-semibold uppercase tracking-wide" style="color:var(--lx-accent-color)">
      Rated #1 Yoga Mat of 2025
    </p>

    <!-- Trust stars (prominent) -->
    <div class="flex justify-center items-center gap-2">
      <div class="flex">
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="text-lg font-bold" style="color:var(--lx-text-color)">4.9/5 stars (12,847 reviews)</span>
    </div>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em">
      The mat that finally grips
    </h1>

    <!-- Subline -->
    <p style="font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get yours now
      </button>
      <button class="px-8 py-4 rounded-lg font-semibold border" 
        style="border-color:var(--lx-border-color);color:var(--lx-text-color)">
        Watch 60-sec review
      </button>
    </div>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Mat" class="w-full max-w-lg mx-auto rounded-lg" />

    <!-- Trust badges -->
    <div class="flex flex-wrap justify-center gap-6 text-sm pt-4">
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- users --></svg>
        <span>47,000+ customers</span>
      </span>
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- shield --></svg>
        <span>60-day money-back guarantee</span>
      </span>
    </div>
  </div>
</section>
```

### Pattern 2: Video Hero
**Best for**: Demo-heavy products

```html
<section class="relative min-h-[90vh] flex items-center" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4 space-y-6">
    <!-- Video -->
    <div data-island="VideoPlayer" data-props='{
      "video_url": "grip-test-demo.mp4",
      "autoplay": true,
      "loop": true,
      "muted": true,
      "controls": true,
      "aspect_ratio": "16:9"
    }'></div>

    <!-- Content below video -->
    <div class="text-center space-y-4">
      <h1 class="font-bold leading-[1.1]" 
        style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
        Watch it grip in real-time
      </h1>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        The surface that gets better as you sweat
      </p>
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get my GripFlow mat
      </button>
      <div class="flex justify-center gap-4 text-sm pt-2">
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <span>4.9/5 stars</span>
        </span>
        <span>•</span>
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4"><!-- truck --></svg>
          <span>Free 2-day shipping</span>
        </span>
      </div>
    </div>
  </div>
</section>
```

### Pattern 3: UGC-Style Hero
**Best for**: Facebook, high authenticity

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:#FAFAFA">
  <div class="max-w-5xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-center">
      <!-- Real customer photo -->
      <img src="customer-selfie-with-mat.jpg" alt="Customer photo" 
        class="w-full rounded-lg shadow-lg" />

      <!-- Content -->
      <div class="space-y-5">
        <h1 class="font-semibold leading-[1.15]" 
          style="font-family:var(--lx-font-body);font-size:clamp(1.75rem,5vw,3rem)">
          "This mat changed my practice"
        </h1>
        <p class="text-lg" style="color:var(--lx-text-muted)">
          — Sarah M., verified customer (+ 46,999 others)
        </p>
        <button class="w-full md:w-auto px-8 py-4 rounded-lg font-semibold" 
          style="background:var(--lx-accent-color);color:white">
          Try it risk-free
        </button>
        <div class="flex flex-wrap gap-4 text-sm pt-2">
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
            <span>60-day guarantee</span>
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
            <span>4.9/5 from 12,847 reviews</span>
          </span>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Pattern 4: Countdown Urgency Hero
**Best for**: Sales/launches

```html
<section class="relative min-h-[85vh] flex items-center px-4" 
  style="background:linear-gradient(to bottom, #FEF3C7 0%, #FFFFFF 100%)">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-bold uppercase tracking-wide" style="color:#B45309">
      Limited Time: Launch Sale
    </p>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
      40% off ends tonight
    </h1>

    <!-- Subline -->
    <p class="text-xl" style="color:var(--lx-text-muted)">
      The GripFlow mat at its lowest price ever
    </p>

    <!-- Countdown -->
    <div data-island="CountdownTimer" data-props='{
      "end_time": "2026-12-31T23:59:59Z",
      "headline": "Sale ends in:",
      "style": "minimal",
      "size": "large"
    }'></div>

    <!-- CTA -->
    <button class="px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Claim my 40% off
    </button>

    <!-- Product image -->
    <img src="product-hero.jpg" alt="GripFlow Mat" class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

---

## Trust Stacking (Critical for Cold Traffic)

Meta traffic has **ZERO brand familiarity**. Trust must be immediate, overwhelming, and specific.

### The Trust Stack (All 3 Layers)

#### Layer 1: Hero Trust Bar
```html
<div class="flex flex-wrap justify-center gap-4 text-sm">
  <span class="flex items-center gap-2 font-semibold">
    <div class="flex">
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    </div>
    <span>4.9/5 (12,847 reviews)</span>
  </span>
  <span class="flex items-center gap-2 font-semibold">
    <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
    <span>60-Day Guarantee</span>
  </span>
</div>
```

#### Layer 2: Persistent Trust Badge Bar
```html
<div data-island="TrustBadgeBar" data-props='{
  "position": "top_sticky",
  "badges": [
    {"icon": "star", "text": "4.9/5 (12,847)", "color": "gold"},
    {"icon": "shield_check", "text": "60-Day Guarantee", "color": "blue"},
    {"icon": "truck", "text": "Free Shipping", "color": "green"},
    {"icon": "award", "text": "Yoga Journal Pick", "color": "purple"}
  ],
  "layout": "scroll",
  "background": "white"
}'></div>
```

#### Layer 3: Social Proof Popup
```html
<div data-island="SocialProofPopup" data-props='{
  "position": "bottom_left",
  "events": [
    {"type": "purchase", "name": "Sarah from NYC", "product": "GripFlow Mat", "time": "2 min ago"},
    {"type": "review", "name": "Mike from LA", "rating": 5, "time": "5 min ago"},
    {"type": "purchase", "name": "Emma from Austin", "product": "GripFlow Mat", "time": "8 min ago"}
  ],
  "interval": 8000,
  "show_delay": 3000,
  "style": "minimal"
}'></div>
```

### Trust Signal Hierarchy

**Tier 1 (Hero)**: Star rating + review count, customer count, guarantee  
**Tier 2 (Trust Strip)**: Free shipping, press mentions, security badges  
**Tier 3 (Section 5)**: Detailed testimonials with photos, before/after, expert endorsements

---

## Social Proof (UGC > Polished)

Meta traffic trusts **authentic > polished**.

### UGC-Style Reviews (Facebook)
```html
<div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid #E5E7EB">
  <!-- Stars -->
  <div class="flex">
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
  </div>

  <!-- Review text (casual tone) -->
  <p style="color:#1F2937;font-size:0.9375rem;line-height:1.5">
    okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny
  </p>

  <!-- Author -->
  <div class="flex items-center gap-3">
    <img src="customer-selfie.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
    <div>
      <p class="font-semibold text-sm">Sarah M.</p>
      <p class="text-xs" style="color:#6B7280">Verified Buyer • New York, NY</p>
    </div>
  </div>

  <!-- Optional: customer photo with product -->
  <img src="review-photo-in-use.jpg" class="w-full rounded-lg mt-3" alt="Customer photo" />
</div>
```

### Specific Numbers > Vague Claims

❌ "Thousands of happy customers"  
✅ "47,482 customers (and counting)"

❌ "Highly rated"  
✅ "4.9/5 stars from 12,847 verified reviews"

❌ "Fast shipping"  
✅ "Ships in 24 hours • Arrives in 2-3 days"

---

## CTA Strategy (Single Goal, Repeat 3x)

### The Rule: One Conversion Goal
All CTAs point to the same action.

**Single product**: "Get my GripFlow mat"  
**Multi-product**: "Shop yoga mats"  
**Lead gen**: "Get my free guide"

### Benefit-Driven CTA Copy

❌ Generic: "Shop now" / "Buy now"  
✅ Benefit-driven:
- "Get my GripFlow mat"
- "Solve my slipping problem"
- "Try it risk-free"
- "Claim my 40% off"

### CTA Placement (3x Rule)

**CTA #1: Hero**
```html
<button class="px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get my GripFlow mat
</button>
```

**CTA #2: After Social Proof**
```html
<div class="text-center space-y-4">
  <h3 class="font-bold text-2xl">Ready to upgrade?</h3>
  <button class="px-8 py-4 rounded-lg font-semibold" 
    style="background:var(--lx-accent-color);color:white">
    Get yours now
  </button>
  <p class="text-sm" style="color:var(--lx-text-muted)">60-day guarantee • Free shipping</p>
</div>
```

**CTA #3: Sticky Bar**
```html
<div data-island="StickyBar" data-props='{
  "position": "bottom",
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "Free shipping • 60-day guarantee"
}'></div>
```

### Mobile CTA Sizing
```html
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold" 
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white;font-size:1rem">
  Get yours now
</button>
```

---

## Urgency for Meta Traffic (Use Sparingly)

### When to Use Urgency
✅ Real sale with deadline  
✅ Limited inventory (< 50 units)  
✅ Launch window  
✅ Seasonal cutoff

❌ Fake scarcity  
❌ Persistent urgency

### CountdownTimer
```html
<div data-island="CountdownTimer" data-props='{
  "end_time": "2026-12-31T23:59:59Z",
  "headline": "Sale ends in:",
  "style": "minimal",
  "show_labels": true,
  "size": "large"
}'></div>
```

### Inventory Indicator
```html
<div data-island="InventoryIndicator" data-props='{
  "threshold": 50,
  "text": "Only {count} left in stock",
  "style": "warning"
}'></div>
```

---

## Mobile Patterns

### Container Padding
```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Content -->
</div>
```

### Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Grid items -->
</div>
```

### Full-Width CTA on Mobile
```html
<button class="w-full sm:w-auto px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get yours now
</button>
```

### Stack on Mobile
```html
<div class="flex flex-col sm:flex-row gap-4">
  <button>Primary CTA</button>
  <button>Secondary CTA</button>
</div>
```

---

## Anti-Patterns (Meta Killers)

### ❌ Message Mismatch
**What**: Ad says "40% off" → page doesn't mention sale  
**Fix**: Ad headline = page headline

### ❌ Desktop-First Design
**What**: 85% mobile traffic hits tiny text, cramped spacing  
**Fix**: `clamp()` for all text, test on real iPhone

### ❌ No Social Proof Above Fold
**What**: Hero has zero trust signals  
**Fix**: Trust bar in hero. "4.9/5 from 12,847 reviews" immediately visible

### ❌ Multiple Competing CTAs
**What**: "Shop now" | "Learn more" | "Watch video" | "Compare"  
**Fix**: One goal. All CTAs → same action

### ❌ Slow-Loading Hero
**What**: 5MB image, 3+ second load  
**Fix**: < 200KB for hero. WebP format. Lazy-load below fold

### ❌ Asking for Email Too Early
**What**: EmailCapture popup 2 seconds after landing  
**Fix**: After social proof section, or exit-intent only

### ❌ Generic Stock Photos
**What**: Diverse-group-laughing-at-salad imagery  
**Fix**: Real product photos. Real customer photos. UGC > stock

### ❌ Burying the Price
**What**: No price until checkout  
**Fix**: Show price in hero or BuyBox. Transparency = trust

### ❌ No Mobile Sticky CTA
**What**: CTA only in hero. After scroll, no path to convert  
**Fix**: StickyBar after 50vh

### ❌ Over-Designing for Aesthetics
**What**: Parallax, auto-play videos, carousels  
**Fix**: Minimal animations. Fast > fancy

### ❌ No Guarantee
**What**: "Buy now" with no mention of returns  
**Fix**: "60-day money-back guarantee" everywhere

### ❌ Feature Dumping
**What**: "6mm TPE, dual-layer, eco-certified"  
**Fix**: "6mm cushion = your knees won't hurt." Translate features → benefits

---

## Complete VibePage Blueprint: Product Launch (New Product)

```json
{
  "head": {
    "title": "GripFlow™ Yoga Mat — The Mat That Won't Slip",
    "description": "Join 47,000+ yogis who solved their slipping problem. 60-day guarantee.",
    "fonts": [
      "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap"
    ]
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-text-color: #111827; --lx-text-muted: #6B7280; --lx-bg-color: #FFFFFF; --lx-bg-surface: #F9FAFB; --lx-border-color: #E5E7EB; --lx-font-heading: 'Inter', system-ui, sans-serif; --lx-font-body: 'Inter', system-ui, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh] flex items-center px-4\" style=\"background:white\"><div class=\"max-w-2xl mx-auto text-center space-y-6\"><p class=\"text-sm font-semibold uppercase tracking-wide\" style=\"color:var(--lx-accent-color)\">Rated #1 Yoga Mat of 2025</p><div class=\"flex justify-center items-center gap-2\"><div class=\"flex\"><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg></div><span class=\"text-lg font-bold\" style=\"color:var(--lx-text-color)\">4.9/5 stars (12,847 reviews)</span></div><h1 class=\"font-extrabold leading-[1.1]\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em\">The mat that finally grips</h1><p style=\"font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563\">Join 47,000+ yogis who solved their slipping problem</p><div class=\"flex flex-col sm:flex-row gap-4 justify-center\"><button class=\"px-8 py-4 rounded-lg font-semibold\" style=\"background:var(--lx-accent-color);color:white\">Get yours now</button></div><img src=\"{{product_image_url}}\" alt=\"GripFlow Mat\" class=\"w-full max-w-lg mx-auto rounded-lg\"/><div class=\"flex flex-wrap justify-center gap-6 text-sm pt-4\"><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z\"/></svg><span>47,000+ customers</span></span><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><span>60-day money-back guarantee</span></span></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "trust-strip",
      "html": "<section class=\"py-8 border-b\" style=\"background:var(--lx-bg-surface);border-color:var(--lx-border-color)\"><div class=\"max-w-7xl mx-auto px-4\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-6 text-center\"><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">60-Day Guarantee</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Love it or return it</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path d=\"M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z\"/><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Free Shipping</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">On all US orders</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"gold\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">12,847 5-Star Reviews</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Rated Excellent</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Featured in Yoga Journal</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Best Mat 2025</p></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ],
  "islands": [
    {
      "type": "StickyBar",
      "props": {
        "trigger_scroll": "50vh",
        "cta_text": "Get my GripFlow mat",
        "price": "$79",
        "trust_badge": "60-day guarantee • Free shipping"
      }
    }
  ]
}
```

---

## TL;DR — The Meta Landing Page Checklist

✅ **Message match**: Ad headline → page headline  
✅ **Mobile-first**: `clamp()` for text/spacing, 44px tap targets  
✅ **Trust immediately**: Star rating + review count in hero  
✅ **Single CTA goal**: All buttons → same action  
✅ **CTA 3x minimum**: Hero, post-social-proof, sticky bar  
✅ **UGC > polished** (Facebook) OR **editorial > UGC** (Instagram)  
✅ **Social proof section**: 6-8 reviews with photos  
✅ **Urgency (if applicable)**: Real countdown, real inventory  
✅ **FAQ section**: Top 5 objections  
✅ **Load speed**: < 3 seconds on mobile  
✅ **Visual continuity**: Ad colors → page colors

**If any are missing, the page will underperform.** Meta traffic is unforgiving.


---

## VISUAL-CRAFT

# Visual Craft — Typography, Spacing, Color & Polish

Techniques for making vibe-code pages look premium. Load when polishing visual quality.

---

## Typography Hierarchy

### Fluid Sizing (clamp)

```html
<h1 class="font-bold leading-[1.1] tracking-tight" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,6vw,4.5rem)">
  Hero Headline
</h1>
<h2 class="font-semibold leading-tight" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3.5vw,2.5rem)">
  Section Heading
</h2>
<p class="text-base lg:text-lg leading-relaxed" style="color:var(--lx-text-color);opacity:0.75">
  Body copy with comfortable reading width
</p>
```

### Size Scale

| Element | Mobile | Desktop | Tailwind |
|---|---|---|---|
| Hero h1 | 2.5rem | 4.5rem | `text-[clamp(2.5rem,6vw,4.5rem)]` |
| Section h2 | 1.5rem | 2.5rem | `text-[clamp(1.5rem,3.5vw,2.5rem)]` |
| Card h3 | 1.125rem | 1.5rem | `text-lg lg:text-2xl` |
| Body | 1rem | 1.125rem | `text-base lg:text-lg` |
| Eyebrow | 0.75rem | 0.75rem | `text-xs uppercase tracking-[0.15em]` |
| Price | 1.5rem | 2rem | `text-2xl lg:text-3xl font-bold` |
| Caption | 0.8125rem | 0.875rem | `text-[13px] lg:text-sm` |

### Eyebrow Pattern

```html
<p class="text-xs uppercase tracking-[0.15em] font-medium mb-3" style="color:var(--lx-accent-color)">
  New Arrival
</p>
```

### Font Pairing Rules

- Heading: display/serif for luxury, geometric sans for modern, rounded sans for playful
- Body: always readable sans-serif (Inter, DM Sans, Source Sans)
- Never same font for both unless brand specifies
- Weight contrast: heading 700+, body 400

---

## Spacing Rhythm

### Section Padding

```html
<!-- Standard section -->
<section class="px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
  <div class="max-w-7xl mx-auto">...</div>
</section>

<!-- Tight section (trust bars, announcements) -->
<section class="px-4 sm:px-6 lg:px-8 py-6 lg:py-8">...</section>

<!-- Hero (extra breathing room) -->
<section class="px-4 sm:px-6 lg:px-8 py-20 lg:py-32 min-h-[70vh] flex items-center">...</section>
```

### Element Spacing

| Between | Gap | Tailwind |
|---|---|---|
| Eyebrow → Heading | 12px | `mb-3` |
| Heading → Body | 16px | `mt-4` |
| Body → CTA | 24-32px | `mt-6 lg:mt-8` |
| Cards in grid | 24px | `gap-6` |
| Section items | 48-64px | `space-y-12 lg:space-y-16` |
| Icon → Label | 8px | `gap-2` |

### Container Pattern

```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Content never touches edges -->
</div>

<!-- Narrow for text-heavy sections -->
<div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Comfortable reading width -->
</div>
```

---

## Color Usage

### Accent Application

- CTAs (buttons, links): `background: var(--lx-accent-color)`
- Eyebrows: `color: var(--lx-accent-color)`
- Active states: borders, underlines
- Badges: `background: var(--lx-accent-color); color: white`
- **Never** large background areas (overwhelming)

### Surface Layering

```html
<!-- Page bg → section bg → card bg (3 layers max) -->
<body style="background:var(--lx-bg-color)">
  <section style="background:var(--lx-bg-surface)">
    <div class="bg-white rounded-xl p-6 shadow-sm">Card</div>
  </section>
</body>
```

### Dark Sections (contrast rhythm)

```html
<section class="py-20" style="background:var(--lx-text-color);color:var(--lx-bg-color)">
  <!-- Inverted: dark bg, light text -->
  <h2 style="color:var(--lx-bg-color)">Headline</h2>
  <p style="opacity:0.7">Muted on dark</p>
  <button style="background:var(--lx-accent-color);color:white">CTA</button>
</section>
```

### Gradient Patterns

```html
<!-- Subtle accent gradient (hero/CTA) -->
<section style="background: linear-gradient(135deg, var(--lx-bg-color) 0%, var(--lx-bg-surface) 100%)">

<!-- Accent fade (badges, highlights) -->
<span style="background: linear-gradient(90deg, var(--lx-accent-color), transparent); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
```

---

## Image Treatment

### Rounded + Shadow (product cards)

```html
<div class="rounded-xl overflow-hidden shadow-md">
  <img src="..." class="w-full h-full object-cover aspect-[4/5]" alt="..." />
</div>
```

### Overlay Text on Image

```html
<div class="relative rounded-2xl overflow-hidden">
  <img src="..." class="w-full h-80 object-cover" />
  <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
  <div class="absolute bottom-6 left-6 text-white">
    <h3 class="text-xl font-bold">Title</h3>
  </div>
</div>
```

### Aspect Ratios

| Context | Ratio | Tailwind |
|---|---|---|
| Hero full-width | 16:9 or free | `aspect-video` or `min-h-[70vh]` |
| Product card | 4:5 | `aspect-[4/5]` |
| Square grid | 1:1 | `aspect-square` |
| Banner | 3:1 | `aspect-[3/1]` |
| Thumbnail | 1:1 | `aspect-square w-16 h-16` |

### Object-fit Rules

- Product images: `object-contain` (show full product)
- Lifestyle/hero: `object-cover` (fill space, crop edges)
- Logos: `object-contain max-h-8`

---

## Micro-Interactions

### Button States

```html
<button class="
  px-6 py-3 rounded-lg font-semibold text-sm
  transition-all duration-200
  hover:shadow-lg hover:scale-[1.02]
  active:scale-[0.98] active:shadow-sm
" style="background:var(--lx-accent-color);color:white">
  Add to Cart
</button>
```

### Card Hover

```html
<div class="
  rounded-xl p-6 border transition-all duration-300
  hover:-translate-y-1 hover:shadow-xl hover:border-transparent
" style="border-color:var(--lx-border-color)">
  Card content
</div>
```

### Link Underline Animation

```css
.link-animate { position: relative; }
.link-animate::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--lx-accent-color);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.3s ease;
}
.link-animate:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}
```

---

## Glass Morphism

```html
<div class="backdrop-blur-md rounded-2xl p-6 border border-white/20" style="background:rgba(255,255,255,0.1)">
  Frosted glass card
</div>
```

---

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

---

## Responsive Patterns

### Grid Collapse

```html
<!-- 3-col desktop → 1-col mobile -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- 2-col split → stack on mobile -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center">
```

### Hide/Show by Breakpoint

```html
<div class="hidden lg:block">Desktop only</div>
<div class="lg:hidden">Mobile only</div>
```

### Mobile-First Section Reorder

```html
<!-- Image first on mobile (visual), text first on desktop (scannable) -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
  <div class="order-2 lg:order-1">Text content</div>
  <div class="order-1 lg:order-2">Image</div>
</div>
```


---

## PREMIUM-PATTERNS

# Premium Patterns — High-Converting Section Templates

Copy-and-adapt HTML+Tailwind patterns for common high-converting sections. Load when building hero, trust, CTA, or social proof sections.

---

## Hero Patterns

### Centered Hero (universal)

```html
<section class="relative min-h-[80vh] flex items-center justify-center text-center px-4 overflow-hidden" style="background:var(--lx-bg-color)">
  <div class="max-w-3xl mx-auto space-y-6">
    <p class="text-xs uppercase tracking-[0.2em] font-medium" style="color:var(--lx-accent-color)">Eyebrow Text</p>
    <h1 class="font-bold leading-[1.1] tracking-tight" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,6vw,4.5rem)">
      Your Hero Headline Here
    </h1>
    <p class="text-lg lg:text-xl max-w-xl mx-auto" style="color:var(--lx-text-color);opacity:0.7">
      Supporting copy that reinforces the headline and builds desire.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center pt-4">
      <a href="#buy" class="px-8 py-4 rounded-lg font-semibold text-sm transition-all hover:scale-[1.02] hover:shadow-lg" style="background:var(--lx-accent-color);color:white">
        Primary CTA
      </a>
      <a href="#learn" class="px-8 py-4 rounded-lg font-semibold text-sm border-2 transition-all hover:scale-[1.02]" style="border-color:var(--lx-accent-color);color:var(--lx-accent-color)">
        Secondary CTA
      </a>
    </div>
  </div>
</section>
```

### Split Hero (image + text)

```html
<section class="grid grid-cols-1 lg:grid-cols-2 min-h-[80vh]">
  <div class="flex items-center px-6 lg:px-16 py-16 lg:py-0 order-2 lg:order-1">
    <div class="space-y-6 max-w-lg">
      <p class="text-xs uppercase tracking-[0.2em] font-medium" style="color:var(--lx-accent-color)">Category</p>
      <h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3.5rem)">
        Headline
      </h1>
      <p class="text-base lg:text-lg leading-relaxed" style="color:var(--lx-text-color);opacity:0.7">
        Body copy here.
      </p>
      <button class="px-8 py-4 rounded-lg font-semibold transition-all hover:shadow-lg" style="background:var(--lx-accent-color);color:white">
        Shop Now
      </button>
    </div>
  </div>
  <div class="relative order-1 lg:order-2 min-h-[50vh] lg:min-h-full">
    <img src="IMAGE_URL" alt="Hero" class="absolute inset-0 w-full h-full object-cover" />
  </div>
</section>
```

### Full-Bleed Image Hero

```html
<section class="relative min-h-[90vh] flex items-center overflow-hidden">
  <img src="IMAGE_URL" alt="" class="absolute inset-0 w-full h-full object-cover" aria-hidden="true" />
  <div class="absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-transparent"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-6 lg:px-16">
    <div class="max-w-xl space-y-6 text-white">
      <h1 class="font-bold leading-[1.05]" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,5vw,4rem)">
        Bold Statement
      </h1>
      <p class="text-lg opacity-90">Supporting text on dark overlay.</p>
      <button class="px-8 py-4 rounded-lg font-semibold bg-white text-black transition-all hover:scale-[1.02]">
        Explore
      </button>
    </div>
  </div>
</section>
```

---

## Trust Bar Patterns

### Horizontal Icons + Text

```html
<section class="py-6 border-y" style="border-color:var(--lx-border-color);background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto px-4 flex flex-wrap justify-center gap-8 lg:gap-12">
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 13l4 4L19 7"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">Dermatologist Tested</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">Free Shipping Over ₹999</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">30-Day Easy Returns</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">100% Secure Payment</span>
    </div>
  </div>
</section>
```

---

## Social Proof Patterns

### Rating Summary Bar

```html
<div class="flex items-center gap-3 py-4">
  <div class="flex">
    <!-- 5 filled stars -->
    <svg class="w-5 h-5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
    <!-- repeat 4 more times -->
  </div>
  <span class="text-sm font-semibold" style="color:var(--lx-text-color)">4.9</span>
  <span class="text-sm" style="color:var(--lx-text-color);opacity:0.6">Based on 2,847 reviews</span>
</div>
```

### Testimonial Card Grid

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-center font-bold mb-12" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.5rem)">
      What Our Customers Say
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Card -->
      <div class="bg-white rounded-xl p-6 shadow-sm">
        <div class="flex gap-1 mb-3">
          <!-- 5 stars SVG -->
        </div>
        <p class="text-sm leading-relaxed mb-4" style="color:var(--lx-text-color);opacity:0.8">
          "Review text here. Keep it authentic and specific."
        </p>
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center text-xs font-bold">PM</div>
          <div>
            <p class="text-sm font-medium">Priya M.</p>
            <p class="text-xs opacity-50">Verified Buyer</p>
          </div>
        </div>
      </div>
      <!-- Repeat cards -->
    </div>
  </div>
</section>
```

---

## CTA Patterns

### Sticky Bottom Bar (mobile)

```html
<section class="fixed bottom-0 left-0 right-0 z-50 lg:hidden p-4 border-t bg-white/95 backdrop-blur-sm" style="border-color:var(--lx-border-color)">
  <div class="flex items-center justify-between gap-3">
    <div>
      <p class="text-sm font-bold">₹1,299</p>
      <p class="text-xs opacity-50 line-through">₹1,799</p>
    </div>
    <button class="flex-1 py-3 rounded-lg font-semibold text-sm" style="background:var(--lx-accent-color);color:white">
      Add to Cart
    </button>
  </div>
</section>
```

### Urgency CTA Section

```html
<section class="py-12 px-4 text-center" style="background:var(--lx-accent-color)">
  <div class="max-w-2xl mx-auto space-y-4">
    <p class="text-white/80 text-sm font-medium uppercase tracking-wider">Limited Time Offer</p>
    <h2 class="text-white text-3xl lg:text-4xl font-bold" style="font-family:var(--lx-font-heading)">
      Get 20% Off Today Only
    </h2>
    <p class="text-white/70 text-lg">Use code WELCOME20 at checkout</p>
    <button class="mt-4 px-10 py-4 bg-white rounded-lg font-bold text-sm transition-all hover:scale-[1.02] hover:shadow-xl" style="color:var(--lx-accent-color)">
      Shop Now →
    </button>
  </div>
</section>
```

---

## Pricing Patterns

### Price with Discount

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">₹1,299</span>
  <span class="text-lg line-through opacity-40">₹1,799</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">28% OFF</span>
</div>
```

### Bundle Pricing

```html
<div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
  <div class="border rounded-xl p-5 text-center" style="border-color:var(--lx-border-color)">
    <p class="text-sm font-medium mb-1">1 Bottle</p>
    <p class="text-2xl font-bold">₹1,299</p>
    <p class="text-xs opacity-50">₹1,299/unit</p>
  </div>
  <div class="border-2 rounded-xl p-5 text-center relative" style="border-color:var(--lx-accent-color)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 text-[10px] font-bold px-3 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">MOST POPULAR</span>
    <p class="text-sm font-medium mb-1">2 Bottles</p>
    <p class="text-2xl font-bold">₹2,199</p>
    <p class="text-xs opacity-50">₹1,099/unit • Save 15%</p>
  </div>
  <div class="border rounded-xl p-5 text-center" style="border-color:var(--lx-border-color)">
    <p class="text-sm font-medium mb-1">3 Bottles</p>
    <p class="text-2xl font-bold">₹2,999</p>
    <p class="text-xs opacity-50">₹999/unit • Save 23%</p>
  </div>
</div>
```

---

## Features/Benefits Pattern

### Icon Grid

```html
<section class="py-16 lg:py-24 px-4">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-xs uppercase tracking-[0.2em] mb-3" style="color:var(--lx-accent-color)">Why Choose Us</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.5rem)">Benefits That Matter</h2>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      <div class="text-center space-y-3">
        <div class="w-12 h-12 mx-auto rounded-xl flex items-center justify-center" style="background:var(--lx-bg-surface)">
          <svg class="w-6 h-6" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24">...</svg>
        </div>
        <h3 class="font-semibold">Benefit Title</h3>
        <p class="text-sm leading-relaxed" style="opacity:0.7">Short description of this benefit.</p>
      </div>
      <!-- Repeat 5 more -->
    </div>
  </div>
</section>
```

---

## Navigation Pattern

### Transparent → Solid on Scroll

HTML:
```html
<nav class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 nav-transparent" id="main-nav">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
    <a href="/" class="text-lg font-bold" style="font-family:var(--lx-font-heading)">Brand</a>
    <div class="hidden md:flex items-center gap-6">
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">Shop</a>
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">About</a>
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">Reviews</a>
    </div>
    <button class="p-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
    </button>
  </div>
</nav>
```

CSS:
```css
.nav-transparent { background: transparent; }
.nav-solid { background: var(--lx-bg-color); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
```

JS:
```javascript
(function() {
  var nav = document.getElementById('main-nav');
  if (!nav) return;
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      nav.classList.remove('nav-transparent');
      nav.classList.add('nav-solid');
    } else {
      nav.classList.remove('nav-solid');
      nav.classList.add('nav-transparent');
    }
  }, { passive: true });
})();
```


---

## ISLAND-PATTERNS

# Island Patterns — Wrapper HTML & Combination Recipes

How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.

---

## Island Embedding Rules

1. `data-island` attribute = exact island name (case-sensitive)
2. `data-props` = valid JSON in **single-quoted** attribute value
3. One `BuyBox` per page (multiple breaks cart state)
4. One `CartDrawer` per page (place in first section or separate section)
5. Islands hydrate client-side — surrounding HTML renders immediately (SSR)
6. Never put islands inside other islands
7. Always wrap in a containing section with proper spacing

---

## Commerce Islands

### BuyBox — Primary Purchase Action

**Always pair with surrounding context (title, price are in the BuyBox island itself):**

```html
<section class="px-4 sm:px-6 lg:px-8 py-8">
  <div class="max-w-2xl mx-auto">
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
  </div>
</section>
```

**PDP layout — Gallery + BuyBox side by side:**

```html
<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16">
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
    <!-- Left: Gallery -->
    <div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableZoom":true}'></div>
    <!-- Right: BuyBox -->
    <div class="lg:sticky lg:top-24 lg:self-start">
      <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
    </div>
  </div>
</section>
```

### CartDrawer — Slide-out Cart

Place once, typically in first section or a dedicated invisible section:

```html
<section class="hidden">
  <div data-island="CartDrawer" data-props='{"position":"right","freeShippingThreshold":99900}'></div>
</section>
```

Note: `freeShippingThreshold` is in cents (99900 = ₹999).

### Cart V2 — DrawerShell + Atomic Islands

For stores with `cart_v2` enabled, use DrawerShell instead of CartDrawer. Set `head.use_cart_v2 = true`. Full composition guide: load `cart-composition` skill.

```html
<section class="hidden">
  <div data-island="DrawerShell" data-island-container data-props='{"mode":"drawer-right","responsive":{"mobile":"bottom-sheet"},"trigger":"cart:open"}'>
    <div class="p-4 border-b"><div data-island="CartProgressBar" data-props='{"threshold":9900}'></div></div>
    <div class="flex-1 overflow-y-auto p-4"><div data-island="CartLines" data-props='{"showQuantity":true,"showRemove":true}'></div></div>
    <div class="p-4 border-t bg-gray-50">
      <div data-island="CartSummary" data-props='{}'></div>
      <div data-island="CartCheckoutButton" data-props='{"text":"Checkout"}'></div>
    </div>
  </div>
</section>
```

Required: `CartLines` + `CartCheckoutButton` inside DrawerShell. Never mix with old `CartDrawer`.

### StickyBar — Scroll-triggered Bottom CTA

```html
<section>
  <div data-island="StickyBar" data-props='{"productId":"gid://shopify/Product/123","showPrice":true,"triggerOffset":600}'></div>
</section>
```

`triggerOffset`: px from top before bar appears. Set to ~height of hero + BuyBox section.

### QuantityBreaks — Volume Discounts

Place directly below or beside BuyBox:

```html
<section class="px-4 sm:px-6 lg:px-8 pb-6">
  <div class="max-w-2xl mx-auto">
    <div data-island="QuantityBreaks" data-props='{"productId":"gid://shopify/Product/123","tiers":[{"qty":2,"discount":10,"label":"Buy 2 Save 10%"},{"qty":3,"discount":15,"label":"Buy 3 Save 15%"},{"qty":5,"discount":20,"label":"Buy 5 Save 20%"}]}'></div>
  </div>
</section>
```

### ProductCarousel — Cross-sells / Related

```html
<section class="py-12 lg:py-20 px-4 sm:px-6 lg:px-8" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.25rem,2.5vw,2rem)">
      You May Also Like
    </h2>
    <div data-island="ProductCarousel" data-props='{"productIds":["gid://shopify/Product/1","gid://shopify/Product/2","gid://shopify/Product/3","gid://shopify/Product/4"],"columns":4,"showQuickAdd":true}'></div>
  </div>
</section>
```

### ProductGallery — Image Gallery with Zoom

```html
<div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableZoom":true}'></div>
```

Layout options: `"grid"` (thumbnails below), `"stack"` (vertical scroll), `"carousel"` (swipe).

---

## Social Proof Islands

### ReviewCarousel — Customer Reviews

**With custom reviews (no Shopify fetch):**

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Testimonials</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">Loved by Thousands</h2>
    </div>
    <div data-island="ReviewCarousel" data-props='{"reviews":[{"author":"Priya M.","rating":5,"text":"Amazing results in just one week!","date":"2026-05-01"},{"author":"Ananya R.","rating":5,"text":"Best serum I have ever used.","date":"2026-04-15"},{"author":"Kavita S.","rating":4,"text":"Great for sensitive skin.","date":"2026-03-20"}],"autoPlay":true}'></div>
  </div>
</section>
```

**With Shopify product reviews (auto-fetch):**

```html
<div data-island="ReviewCarousel" data-props='{"productId":"gid://shopify/Product/123","autoPlay":true}'></div>
```

### TrustBadgeBar — Trust Signals

```html
<section class="py-4 border-y" style="border-color:var(--lx-border-color)">
  <div data-island="TrustBadgeBar" data-props='{"badges":[{"icon":"shield","label":"Secure Checkout"},{"icon":"truck","label":"Free Shipping"},{"icon":"refresh","label":"Easy Returns"},{"icon":"award","label":"Premium Quality"}]}'></div>
</section>
```

Available icons: `shield`, `truck`, `refresh`, `award`, `check`, `lock`, `heart`, `star`, `clock`, `leaf`.

### SocialProofPopup — Recent Activity Toasts

Place once (invisible section):

```html
<section class="hidden">
  <div data-island="SocialProofPopup" data-props='{"messages":[{"text":"Sarah from Mumbai just purchased","delay":3000},{"text":"Rohit from Delhi added to cart","delay":5000},{"text":"12 people viewing this now","delay":8000}],"position":"bottom-left","interval":8000}'></div>
</section>
```

---

## Content Islands

### FAQ — Accordion Questions

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Frequently Asked Questions
    </h2>
    <div data-island="FAQ" data-props='{"items":[{"question":"How do I use this product?","answer":"Apply 2-3 drops to clean skin morning and night."},{"question":"Is it suitable for sensitive skin?","answer":"Yes, dermatologist tested and hypoallergenic."},{"question":"When will I see results?","answer":"Most customers see improvement within 1-2 weeks."},{"question":"What is your return policy?","answer":"30-day hassle-free returns, no questions asked."}],"style":"accordion","openFirst":true}'></div>
  </div>
</section>
```

### Tabs — Tabbed Content

```html
<section class="py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <div data-island="Tabs" data-props='{"tabs":[{"label":"Details","content":"<p>Full product details and specifications.</p>"},{"label":"Ingredients","content":"<ul><li>Hyaluronic Acid</li><li>Niacinamide 5%</li><li>Ceramides</li></ul>"},{"label":"How to Use","content":"<ol><li>Cleanse face</li><li>Apply 2-3 drops</li><li>Follow with moisturizer</li></ol>"}],"style":"underline"}'></div>
  </div>
</section>
```

Style options: `"underline"`, `"pills"`, `"bordered"`.

### BeforeAfter — Comparison Slider

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Real Results
    </h2>
    <div data-island="BeforeAfter" data-props='{"before":{"src":"BEFORE_IMAGE_URL","label":"Day 1"},"after":{"src":"AFTER_IMAGE_URL","label":"Day 30"}}'></div>
  </div>
</section>
```

---

## Engagement Islands

### IngredientExplorer — Interactive Ingredients

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Transparency</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">What's Inside</h2>
    </div>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Hyaluronic Acid","description":"Multi-molecular weight complex","benefit":"Deep multi-layer hydration"},{"name":"Niacinamide 5%","description":"Vitamin B3 derivative","benefit":"Minimizes pores, evens tone"},{"name":"Ceramide Complex","description":"Skin-identical lipids","benefit":"Repairs moisture barrier"}],"layout":"interactive"}'></div>
  </div>
</section>
```

### CompareTable — Product Comparison

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Why We're Different
    </h2>
    <div data-island="CompareTable" data-props='{"products":[{"name":"Our Serum","features":{"Clean Ingredients":true,"Dermat Tested":true,"No Parabens":true,"Under ₹1500":true}},{"name":"Brand X","features":{"Clean Ingredients":false,"Dermat Tested":true,"No Parabens":false,"Under ₹1500":false}},{"name":"Brand Y","features":{"Clean Ingredients":true,"Dermat Tested":false,"No Parabens":true,"Under ₹1500":true}}],"features":["Clean Ingredients","Dermat Tested","No Parabens","Under ₹1500"],"highlightIndex":0}'></div>
  </div>
</section>
```

### EmailCapture — Lead Capture

```html
<section class="py-12 lg:py-16 px-4" style="background:var(--lx-accent-color)">
  <div class="max-w-xl mx-auto text-center">
    <h2 class="text-white text-2xl font-bold mb-2" style="font-family:var(--lx-font-heading)">Join the Club</h2>
    <p class="text-white/70 text-sm mb-6">Get 10% off your first order + early access to new launches.</p>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Get 10% Off","incentive":"10% off your first order","style":"inline"}'></div>
  </div>
</section>
```

### ExitIntent — Last-Chance Popup

Place once (invisible):

```html
<section class="hidden">
  <div data-island="ExitIntent" data-props='{"headline":"Wait! Don't leave empty-handed","body":"Use code EXIT15 for 15% off your first order","ctaText":"Claim My Discount","showOnMobile":true}'></div>
</section>
```

---

## Common Combinations

### PDP Core (minimum viable PDP)

```
1. ProductGallery + BuyBox (side-by-side on desktop)
2. TrustBadgeBar (immediately below)
3. Tabs (details/ingredients/usage)
4. ReviewCarousel
5. StickyBar (scroll-triggered)
6. CartDrawer (hidden)
```

### Landing Page Core

```
1. Hero section (HTML, no island)
2. TrustBadgeBar
3. Benefits section (HTML grid)
4. BeforeAfter or IngredientExplorer
5. ReviewCarousel
6. EmailCapture or BuyBox
7. FAQ
8. ExitIntent (hidden)
```

### Collection Page

```
1. Collection header (HTML)
2. ProductCarousel (featured picks)
3. Product grid with QuickAdd per card
4. TrustBadgeBar
5. EmailCapture (footer)
```

---

## Data-Props Formatting Rules

1. **Single quotes** around attribute value: `data-props='...'`
2. **Double quotes** inside JSON: `{"key":"value"}`
3. **No apostrophes** in text values — use `'` or rephrase
4. **No line breaks** in data-props — must be one line
5. **Numbers without quotes**: `{"qty":2,"discount":10}`
6. **Booleans without quotes**: `{"autoPlay":true}`
7. **Arrays**: `{"items":[{...},{...}]}`

### Escaping gotchas

```html
<!-- WRONG: apostrophe breaks parsing -->
<div data-props='{"text":"Don't miss out"}'></div>

<!-- RIGHT: avoid apostrophes -->
<div data-props='{"text":"Do not miss out"}'></div>

<!-- RIGHT: use HTML entity in surrounding HTML, not in props -->
```

---

## PDP Template Recipes

### DTC Beauty PDP

```
ProductGallery (vertical, listenForVariant:true)
├── VariantSwatches (color, image type)
├── SubscriptionToggle
├── BuyBox (listenForEvents:true, showVariantSelector:false)
├── DeliveryEstimate (variant:"inline")
├── TrustBadgeBar (compact)
├── PaymentOptions (variant:"inline", listenForEvents:true)
├── InventoryIndicator (variant:"badge", listenForEvents:true)
├── Tabs (underline)
├── ReviewCarousel
├── BundleBuilder (layout:"horizontal")
├── ProductCarousel ("You may also like")
├── StickyBar
├── CartDrawer
└── SocialProofPopup
```

### Fashion/Apparel PDP

```
ProductGallery (layout:"grid", listenForVariant:true)
├── VariantSwatches (color, image) + VariantSwatches (type:"size_grid", axis mode)
├── OptionResolver (productId)
├── SizeGuide
├── BuyBox (variant:"expanded", listenForEvents:true, showVariantSelector:false)
├── InventoryIndicator (variant:"text", listenForEvents:true)
├── DeliveryEstimate (variant:"card")
├── Tabs (style:"underline")
├── ReviewCarousel
├── BundleBuilder (title:"Complete the look", layout:"stacked")
├── ProductCarousel
├── StickyBar
├── CartDrawer
└── ExitIntent
```

### Supplements/Wellness PDP

```
ProductGallery (vertical)
├── VariantSwatches (flat, image type for flavors)
├── QuantityBreaks
├── SubscriptionToggle
├── BuyBox (listenForEvents:true)
├── PaymentOptions (variant:"expandable")
├── TrustBadgeBar (badges: GMP, vegan, lab-tested)
├── IngredientExplorer (layout:"interactive")
├── FAQ (style:"accordion")
├── ReviewCarousel
├── CompareTable (vs competitors)
├── BundleBuilder (title:"Stack for results")
├── StickyBar
├── CartDrawer
└── CountdownTimer (style:"simple", inline with price)
```

### Personalized Product PDP (Gifts/Jewelry)

```
ProductGallery (layout:"grid")
├── VariantSwatches (type:"text")
├── BuyBox (variant:"expanded", listenForEvents:true)
├── DeliveryEstimate (variant:"banner")
├── PaymentOptions (variant:"inline")
├── Tabs
├── ReviewCarousel
├── ProductCarousel ("Complete the gift set")
├── StickyBar
└── CartDrawer
```

### Island Communication on PDP

Key event flows for PDP islands:
- VariantSwatches → (variant:changed) → BuyBox, ProductGallery, InventoryIndicator, PaymentOptions
- OptionResolver → (variant:changed) → all listeners above (for multi-axis products)
- SubscriptionToggle → (subscription:changed) → BuyBox
- BundleBuilder → (bundle:add) → CartDrawer
- InventoryIndicator → (inventory:updated) → StickyBar, BuyBox

Always set `listenForEvents:true` on listener islands when they co-exist with emitters.

---

## New PDP Islands (v2)

### ProductHero — Split-Layout PDP Hero

Premium split-hero for PDPs. Media pane on one side, BuyBox on the other.

```html
<div data-island="ProductHero" data-props='{"images":[{"url":"/product-1.jpg","objectFit":"contain","objectPosition":"center"},{"url":"/product-2.jpg","objectFit":"cover"}],"layout":"splitLeft","thumbnails":"rail","thumbnailPosition":"left","navigation":"floatingArrows","transition":"fade","listenForVariant":true}'></div>
```

**Layout options:** `splitLeft` (media left 60%), `splitRight`, `fullHeight`, `stacked`
**ALWAYS PAIR WITH:** BuyBox in the adjacent grid cell. Use CSS grid in the containing HTML section to create the split.

### EditorialProductGrid — Related Products + Bundle

Mixed-type grid with center feature card for bundles or highlighted products.

```html
<div data-island="EditorialProductGrid" data-props='{"products":[{"id":"123","title":"Product A","price":"$29","image":"/a.jpg"},{"id":"456","title":"Product B","price":"$35","image":"/b.jpg"}],"featureCard":{"title":"Save 20%","subtitle":"Bundle & save","type":"bundle","cta":"Add Bundle"},"layout":"tripleCenter","showQuickAdd":true}'></div>
```

**Layout options:** `tripleCenter` (product | feature | product), `dualSide`, `quad`

### PDPInfoCards — Product Detail Cards

Information cards for product specs, taste profiles, pairings, certifications.

```html
<div data-island="PDPInfoCards" data-props='{"cards":[{"title":"Taste Profile","icon":"palette","items":["Bright citrus","Smooth finish","Medium body"]},{"title":"Pairs With","icon":"wine","items":["Dark chocolate","Aged cheese","Fresh berries"]}],"variant":"dashed","columns":2,"badgeRow":[{"icon":"leaf","label":"Organic"},{"icon":"shield","label":"Lab Tested"}]}'></div>
```

**Variant options:** `bordered`, `dashed`, `filled`, `minimal`
**ALWAYS PAIR WITH:** Place below ProductHero/BuyBox section, above reviews.

---

## Navigation Islands — Hydration Mode (Preferred)

Navigation islands (Navbar, Footer, SiteHeader) support **hydration mode**: you generate ANY HTML/CSS, then place `data-lx-*` tags on functional elements. The island attaches behavior (cart state, mobile toggle, newsletter) without touching your design.

### Why Hydration Mode?

- Complete design freedom — any layout, any CSS
- Only 2-5 behavior props (vs 15+ style props in legacy mode)
- Cart state auto-syncs — no prop management
- Publish validator enforces required tags — can't ship broken nav

### Navbar — Hydration Mode

**Required tags:** `data-lx-nav="root|cart-trigger|cart-count|mobile-trigger|mobile-panel"`

**Behavior props:** `sticky` (bool), `cartMode` ("drawer"|"link"), `transparent` (bool)

```html
<div data-island="Navbar" data-props='{"sticky":true,"cartMode":"drawer"}'>
  <nav data-lx-nav="root" class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-6 flex items-center justify-between h-16">
      <a href="/" data-lx-nav="logo">
        <img src="{{brand_logo}}" class="h-8" alt="{{brand_name}}" />
      </a>
      <nav class="hidden lg:flex items-center gap-8">
        <a href="/collections" data-lx-nav="link" class="text-sm font-medium">Shop</a>
        <a href="/about" data-lx-nav="link" class="text-sm font-medium">About</a>
      </nav>
      <div class="flex items-center gap-4">
        <button data-lx-nav="cart-trigger" class="relative p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18M16 10a4 4 0 01-8 0"/>
          </svg>
          <span data-lx-nav="cart-count" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-black text-white text-[10px] flex items-center justify-center" style="display:none"></span>
        </button>
        <button data-lx-nav="mobile-trigger" class="lg:hidden p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 12h18M3 6h18M3 18h18"/>
          </svg>
        </button>
      </div>
    </div>
    <div data-lx-nav="mobile-panel" class="hidden lg:hidden border-t px-6 py-4">
      <a href="/collections" class="block py-3 text-sm font-medium">Shop</a>
      <a href="/about" class="block py-3 text-sm font-medium">About</a>
    </div>
  </nav>
</div>
```

**CSS requirement** (include in section CSS):
```css
[data-lx-nav="mobile-panel"] { display: none; }
[data-lx-nav="mobile-panel"].lx-open { display: block; }
```

**Dropdowns (optional):**
```html
<div class="relative">
  <a href="/shop" data-lx-nav="dropdown-trigger">Shop ▾</a>
  <div data-lx-nav="dropdown-panel" class="absolute top-full mt-2 bg-white shadow-lg rounded-lg p-4">
    <a href="/collections/new" class="block py-2 text-sm">New Arrivals</a>
  </div>
</div>
```

**Hide cart (no cart-trigger/cart-count needed):**
```html
<div data-island="Navbar" data-props='{"sticky":true,"hideCart":true}'>
```

### Footer — Hydration Mode

**Required tags:** `data-lx-footer="root"`  
**Optional tags:** `newsletter-form`, `newsletter-input`, `newsletter-success`, `year`

```html
<div data-island="Footer" data-props='{"newsletterEndpoint":"https://api.example.com/subscribe"}'>
  <footer data-lx-footer="root" class="bg-gray-950 text-gray-300 py-16 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
      <div>
        <img src="{{brand_logo}}" class="h-8 mb-4 invert" alt="{{brand_name}}" />
        <p class="text-sm text-gray-400">{{brand_tagline}}</p>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Shop</h4>
        <a href="/collections" class="block text-sm py-1.5 text-gray-400 hover:text-white">All Products</a>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Newsletter</h4>
        <form data-lx-footer="newsletter-form" class="flex">
          <input data-lx-footer="newsletter-input" type="email" placeholder="your@email.com" class="flex-1 px-3 py-2 bg-gray-900 border border-gray-700 text-sm text-white rounded-l" />
          <button type="submit" class="px-4 py-2 bg-white text-black text-sm font-medium rounded-r">→</button>
        </form>
        <p data-lx-footer="newsletter-success" style="display:none" class="text-sm text-green-400 mt-2"></p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-10 pt-6 border-t border-gray-800 text-sm text-gray-500">
      © <span data-lx-footer="year"></span> All rights reserved.
    </div>
  </footer>
</div>
```

### SiteHeader — Hydration Mode

Combines announcement + navbar. Uses BOTH `data-lx-header` and `data-lx-nav` tags.

**Required tags:** `data-lx-header="root"` + same nav tags as Navbar

```html
<div data-island="SiteHeader" data-props='{"sticky":true,"cartMode":"drawer","messages":["Free shipping over $75","New summer collection"],"dismissible":true}'>
  <header data-lx-header="root" class="fixed top-0 w-full z-50">
    <div data-lx-header="announcement" class="bg-black text-white text-center py-2 text-xs relative">
      <span data-lx-header="announcement-text">Free shipping over $75</span>
      <button data-lx-header="announcement-dismiss" class="absolute right-3 top-1/2 -translate-y-1/2">✕</button>
    </div>
    <nav class="bg-white border-b">
      <!-- Same data-lx-nav tags as Navbar example above -->
    </nav>
  </header>
</div>
```

### Tag Reference

| Tag | Islands | Behavior |
|-----|---------|----------|
| `data-lx-nav="root"` | Navbar, SiteHeader | Sticky/scroll attaches here |
| `data-lx-nav="cart-trigger"` | Navbar, SiteHeader | Click → open CartDrawer or navigate |
| `data-lx-nav="cart-count"` | Navbar, SiteHeader | textContent auto-updated from $cartLines |
| `data-lx-nav="mobile-trigger"` | Navbar, SiteHeader | Click toggles mobile-panel .lx-open class |
| `data-lx-nav="mobile-panel"` | Navbar, SiteHeader | Toggle target for mobile menu |
| `data-lx-nav="dropdown-trigger"` | Navbar, SiteHeader | Hover shows dropdown-panel |
| `data-lx-nav="dropdown-panel"` | Navbar, SiteHeader | Shown/hidden on hover (same parent) |
| `data-lx-footer="root"` | Footer | Root element |
| `data-lx-footer="newsletter-form"` | Footer | Form submit → POST endpoint |
| `data-lx-footer="newsletter-input"` | Footer | Email input |
| `data-lx-footer="newsletter-success"` | Footer | Shown after successful submit |
| `data-lx-footer="year"` | Footer | textContent = current year |
| `data-lx-header="root"` | SiteHeader | Root + spacer via ResizeObserver |
| `data-lx-header="announcement"` | SiteHeader | Hidden on dismiss |
| `data-lx-header="announcement-text"` | SiteHeader | Rotates through messages[] |
| `data-lx-header="announcement-dismiss"` | SiteHeader | Click hides + persists to sessionStorage |

### Validation (Publish Blocks If Missing)

The publish validator enforces required tags when hydration mode detected:
- Navbar/SiteHeader: `root` + `cart-trigger` + `cart-count` + `mobile-trigger` + `mobile-panel`
- Footer: `root`
- Cart tags skipped if `hideCart: true` in props


---

# WORKFLOWS

## page-generation

# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide` and `vibe://skills/generation-protocol` first — they define the VibePage schema, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 0 — Context Gathering (run ALL in parallel)

```
get_workspace_details    → workspace ID
get_connected_stores     → store domain
get_brand_kit            → logo, fonts, colors, voice, border radius
get_design_md            → brand brief + design philosophy + don'ts
list_products            → product catalog (for commerce islands)
get_navigation           → navbar/footer links
search_design_library    → existing brand assets (hero images, lifestyle shots)
```

All 7 calls can run in parallel. Wait for all before proceeding.

### Phase 1 — Asset Preparation

Decision tree per section:
1. `search_design_library` — check existing assets FIRST (always)
2. `generate_asset` — only if library has nothing suitable
3. `edit_asset` — composite/modify if needed
4. `view_asset` — verify result before using in page

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 2A — Raw HTML Generation (No Islands)

Generate complete VibePage JSON with pure HTML + Tailwind CSS:
- Place `data-placeholder="IslandName"` divs where islands will go
- Focus entirely on visual design: layout, typography, color, spacing, imagery
- Apply brand CSS variables in `theme_css`
- Use Google Fonts URLs in `head.fonts`
- Write real copy (never Lorem Ipsum)
- Use asset URLs from Phase 1 in `<img>` tags

This renders instantly in any browser — iterate on design here.

### Phase 2B — Island Mapping

Replace placeholders with actual islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"v1","title":"Default","available":true}]}}'></div>
```

Use `vibe://schema/island/{name}` resource to get exact prop shapes for each island.

### Phase 3 — Validation

```
validate_vibe_page(page_json)
```

Fix any errors. Common issues: duplicate section IDs, invalid island names, missing required props, inline `<style>`/`<script>` tags.

### Phase 4 — Publish + Visual Verify

```
publish_vibe_page(slug, page, archetype, publish=false)  → preview_url
```

**Visual verification is REQUIRED before marking complete:**

| Agent | How to Verify |
|-------|--------------|
| Claude Code | `browser_navigate(preview_url)` → `browser_take_screenshot({fullPage: true})` → review screenshot |
| Codex | Use built-in browser to open preview_url |
| Cursor | Open preview_url in browser, take screenshot with available tool |
| No browser | Provide preview_url to user: "Open this to verify the page" |

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Mobile layout correct (375px viewport, no horizontal scroll)
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues → `update_page_section` → re-screenshot.
When satisfied → `publish_page(page_id)` to go live.

## Page Type Templates

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

## Quality Bar

- Mobile-first (375px viewport — test this)
- All brand colors via `--lx-*` CSS variables (never hardcoded hex in HTML)
- Proper heading hierarchy (single h1 in hero, h2 per section, h3 for sub-items)
- Islands for ALL commerce interactions (add-to-cart, checkout, cart drawer)
- All images from asset tools (never external URLs unless Shopify CDN)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Hero headline ≤ 8 words, visible without scrolling
- Use shared keyframes (fadeUp, fadeIn, scaleIn) — don't define new @keyframes unless truly unique

## Ad-to-Page Flow

When converting an ad creative to a landing page:
1. `get_ad_creatives` — get creative metadata
2. `analyze_ad_creative` — extract headline, claims, colors, tone, CTA
3. `match_persona_to_ad` — identify target audience
4. Continue with Phase 0-4 using extracted context
5. Ensure "scent continuity" — ad headline ≈ page hero headline


## design-assets

# Design Assets & Brand Management

Manage visual assets (search, generate, edit) and brand identity (kit, themes).

## Asset Pipeline (Priority Order)

Always follow this order — never generate when existing assets work:

### 1. Search First
```
search_design_library({ query: "lifestyle woman skincare" })
```
Returns existing brand assets (product shots, lifestyle, textures, SVGs).

### 2. Generate If Needed
```
generate_asset({
  prompt: "Minimalist skincare flatlay on marble surface, soft morning light",
  style: "photography",        // photography | illustration | 3d_render | editorial | abstract
  purpose: "hero_bg",          // hero_bg | product_lifestyle | card_bg | section_bg | icon | texture
  aspect: "landscape",         // landscape | portrait | square
  quality: "medium",           // low | medium | high
  brand_colors: ["#1a1a1a", "#f5f5dc"]
})
```

### 3. Edit/Composite
```
edit_asset({
  source_ids: ["asset_123", "asset_456"],
  prompt: "Place product bottle on the lifestyle background, natural lighting match",
  mode: "composite"            // composite | inpaint | style_transfer
})
```

### 4. Verify
```
view_asset(asset_id)
```
Visual verification before using in page.

## Style Selection Guide

| Brand Tone | Style |
|-----------|-------|
| Luxury/Premium | `photography` or `editorial` |
| Playful/Fun | `illustration` or `3d_render` |
| Tech/Modern | `abstract` or `3d_render` |
| Natural/Organic | `photography` |
| Artistic/Creative | `editorial` or `illustration` |

## Purpose → Aspect Ratio

| Purpose | Aspect | Typical Use |
|---------|--------|-------------|
| hero_bg | landscape | Full-width hero backgrounds |
| product_lifestyle | portrait/square | Product in context |
| card_bg | square | Grid cards, thumbnails |
| section_bg | landscape | Section backgrounds |
| icon | square | Small decorative elements |
| texture | square | Repeating patterns, overlays |

## Brand Kit Management

### Read Brand Identity
```
get_brand_kit()
```
Returns: logo, fonts (heading/body), colors (primary/secondary/accent), border radius, spacing scale, brand voice.

### List Available Themes
```
list_themes()
```
Returns: theme IDs, names, which is default.

### Update Theme
```
update_theme(theme_id, {
  fonts: { heading: "Inter", body: "Inter" },
  colors: { primary: "#000", accent: "#ff6b00" },
  border_radius: "8px"
})
```

## Design References

### Extract from URL
```
extract_brand_design({ url: "https://brand.com" })
```
Returns: palette, fonts, spacing, tone analysis.

## Cost Control

- `low` quality: fast, cheap — use for textures, backgrounds, placeholders
- `medium` quality: default — use for most section images
- `high` quality: expensive — use only for hero images and key product shots
- Budget: ~3-5 generated assets per page maximum
- Always `search_design_library` first to avoid unnecessary generation


## publishing

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `validate_vibe_page` — always validate before publishing
2. `publish_vibe_page` — persist to DB + storage
   - `draft: true` → preview URL only (not live on store)
   - `draft: false` → live on Shopify store

## Operations

### Publish (New Page)
```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { draft: false })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
publish_vibe_page(page_data, { draft: true })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
publish_page(page_id)
```
Makes a draft page live.

### Unpublish
```
unpublish_page(page_id)
```
Takes page offline but preserves it in DB.

### Duplicate
```
duplicate_page(page_id, { title: "New Title" })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
create_page_variation(page_id, { changes: {...} })
```
Creates variant for A/B testing.

## Prerequisites

- Store must be connected (`get_connected_stores`)
- Brand kit should exist for proper theming

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)


## page-editing

# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `list_pages` — find target page
2. `get_page` — read current page structure + HTML
3. Make changes (one of the operations below)
4. `validate_vibe_page` — verify changes are valid
5. Page auto-versions on each mutation

## Operations

### Update/Replace a Section

```
update_page_section(page_id, section_id, { html, css, settings })
```
- Can replace HTML entirely or patch specific parts
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_page_section(page_id, null, { html, css, settings, position })
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
remove_page_section(page_id, section_id)
```
- Irreversible — confirm with user first
- Auto-bumps version

### Reorder Sections

```
move_page_section(page_id, section_id, new_position)
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always `get_page` first to understand current structure
- Reference section IDs from the page data (don't guess)
- After editing, run `validate_vibe_page` before telling user it's done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout


## analytics

# Storefront Analytics & Experiments

Access page performance data and manage A/B experiments.

## Analytics Tools

### Page-Level Deep Dive
```
get_page_analytics(page_id)
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
get_analytics_timeseries({ metric: "conversions", period: "daily", range: "30d" })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
get_attribution({ page_id? })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
create_ab_test({
  page_id: "...",
  variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
})
```

### 2. Monitor Results
```
get_experiment_results(experiment_id)
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
scale_winner(experiment_id, { variant_id: "..." })
```
Scales winning variant to 100% traffic, marks experiment complete.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split — a variant may win on mobile but lose on desktop
- Use `get_attribution` to understand which traffic sources convert best
- Compare page analytics before/after changes to measure impact


