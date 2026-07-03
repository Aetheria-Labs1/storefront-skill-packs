# Home & Decor — Room Context Pages — Knowledge Base

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
├─ get_theme_json()                                → compiled brand tokens
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
├─ get_theme_json() + get_design_md()
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
├─ capture_design_source(url)          → screenshots + design DNA
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
| search_design_library + get_theme_json | write must complete before preview |
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

## HOME-EXPERTISE

# Home & Lifestyle — Storefront Design Intelligence

> **When to load:** Furniture, home decor, candles, textiles, bedding, kitchenware, outdoor living, rugs, lighting, wall art, planters, storage, tableware.

## Philosophy

**Context is everything.** Home goods buyers need to see the product in a real space before they can imagine it in their own. A dining table photographed in isolation tells you nothing about scale, proportion, or how it anchors a room. The same table in a styled dining room, with chairs, a rug, lighting, and place settings, becomes tangible — the buyer can measure it against their own space and see the lifestyle it enables.

This vertical demands:
- **Visualization in space** — product shown in real rooms, not white void
- **Scale & proportion** — dimensional reference, human scale, room fit
- **Material quality trust** — close-ups of grain, weave, finish, hardware
- **Styling inspiration** — layered vignettes showing how to use/style the product
- **Lifestyle storytelling** — the feeling of living with the product

Treat the page like a walk through a styled showroom: curated, cohesive, aspirational but achievable.

---

## Section Sequences

### Furniture PDP (10-12 sections)
1. **Room Scene Hero** — product in fully styled room, focal point
2. **Quick Specs** — dimensions, materials, weight, assembly (above fold)
3. **Product Gallery** — room context + detail shots + scale reference
4. **Dimensions Deep Dive** — Tabs island (Dimensions | Materials | Care | Shipping)
5. **Material Story** — bento grid with material origin, craftsmanship, finish
6. **Room Inspiration Gallery** — asymmetric grid showing 4-6 different room settings
7. **Cross-Sell ("Complete the Room")** — ProductCarousel with related items
8. **Before/After Testimonials** — BeforeAfter island with room makeovers
9. **Photo Reviews** — ReviewCarousel with customer room photos
10. **FAQ** — assembly, shipping, returns (FAQ island)
11. **Design Philosophy** — brand story, values, sustainability
12. **Footer CTA** — EmailCapture for design tips

### Room/Style Guide (8-10 sections)
1. **Full-Bleed Room Hero** — aspirational lifestyle shot
2. **Intro Text** — design philosophy, collection story
3. **Shop the Look** — ProductCarousel with all items in the room
4. **Room Breakdown** — bento grid with annotated product callouts
5. **Styling Tips** — 2-column text + image pairs
6. **Material Palette** — visual grid of finishes, fabrics, metals
7. **Alternative Colorways** — Tabs island showing room in different finishes
8. **Customer Rooms** — ReviewCarousel with real customer interpretations
9. **FAQ** — design services, customization, lead times
10. **Footer CTA** — book consultation or save to Pinterest

### Collection Page (8-10 sections)
1. **Lifestyle Hero** — collection in a cohesive room setting
2. **Collection Intro** — philosophy, materials, range
3. **Product Grid** — filterable, sortable (use semantic HTML + CSS)
4. **Featured Product Deep Dive** — spotlight on hero piece
5. **Material Story** — shared materials/craftsmanship across collection
6. **Room Vignettes** — 3-4 styled settings mixing collection pieces
7. **Customer Favorites** — top-rated items from ReviewCarousel
8. **Cross-Collection Pairings** — ProductCarousel with complementary collections
9. **FAQ** — custom orders, trade program, lead times
10. **Footer CTA** — EmailCapture for new releases

### Small Goods (Candles, Textiles, Tableware) (8-10 sections)
1. **Lifestyle Hero** — product in styled vignette (not floating)
2. **Product Gallery** — detail shots, scale reference, in-use
3. **Quick Specs** — size, materials, care (compact)
4. **Material & Craft** — origin story, artisan process, sustainability
5. **Styling Vignettes** — 3-4 ways to use/display (bento grid)
6. **Scent/Texture/Color Deep Dive** — sensory storytelling (for candles/textiles)
7. **Gift Sets** — ProductCarousel with curated bundles
8. **Photo Reviews** — ReviewCarousel with customer styling
9. **FAQ** — care, shipping, gift wrap
10. **Footer CTA** — EmailCapture for seasonal collections

---

## Island Combinations

### Furniture PDP
```html
<!-- ProductGallery: room context + detail + scale -->
<div data-island="ProductGallery" data-props='{
  "images": [
    {"src": "room-wide.jpg", "alt": "Dining table in styled room", "type": "room"},
    {"src": "detail-leg.jpg", "alt": "Close-up of oak leg joinery", "type": "detail"},
    {"src": "scale-room.jpg", "alt": "Table with person seated", "type": "scale"},
    {"src": "room-angle2.jpg", "alt": "Dining room from kitchen view", "type": "room"}
  ],
  "thumbnailPosition": "left"
}'></div>

<!-- ImageZoom: material close-ups -->
<div data-island="ImageZoom" data-props='{
  "src": "oak-grain-macro.jpg",
  "alt": "White oak grain detail",
  "zoomLevel": 2.5
}'></div>

<!-- Tabs: specs, materials, care, shipping -->
<div data-island="Tabs" data-props='{
  "tabs": [
    {"id": "dimensions", "label": "Dimensions", "content": "<h3>Dimensions</h3><ul><li>H: 30\" × W: 72\" × D: 36\"</li><li>Weight: 145 lbs</li><li>Clearance: 24\" recommended</li><li>No assembly required</li></ul>"},
    {"id": "materials", "label": "Materials", "content": "<h3>Materials</h3><p>Solid white oak from sustainably managed forests in Vermont. Natural oil finish. Stainless steel leveling feet.</p>"},
    {"id": "care", "label": "Care", "content": "<h3>Care</h3><p>Wipe with damp cloth. Avoid harsh chemicals. Re-oil annually with included maintenance kit.</p>"},
    {"id": "shipping", "label": "Shipping", "content": "<h3>Shipping</h3><p>White-glove delivery in 4-6 weeks. We'll schedule delivery and bring the table to your room of choice.</p>"}
  ],
  "defaultTab": "dimensions"
}'></div>

<!-- ProductCarousel: complete the room -->
<div data-island="ProductCarousel" data-props='{
  "title": "Complete the Room",
  "products": [
    {"id": "bench-01", "name": "Matching Bench", "price": "$485", "image": "bench.jpg"},
    {"id": "chair-01", "name": "Oak Dining Chair", "price": "$295", "image": "chair.jpg"},
    {"id": "sideboard-01", "name": "Oak Sideboard", "price": "$1,850", "image": "sideboard.jpg"}
  ],
  "slidesToShow": 3
}'></div>

<!-- BeforeAfter: room makeover with product as anchor -->
<div data-island="BeforeAfter" data-props='{
  "beforeImage": "before-dining-room.jpg",
  "afterImage": "after-dining-room.jpg",
  "beforeLabel": "Before",
  "afterLabel": "After",
  "caption": "Sarah's dining room transformation with The Everyday Table"
}'></div>
```

### Room Inspiration Gallery
```html
<!-- ReviewCarousel: customer photos with room metadata -->
<div data-island="ReviewCarousel" data-props='{
  "reviews": [
    {
      "id": "r1",
      "author": "Jessica M.",
      "rating": 5,
      "text": "Perfect for our open-plan kitchen. The oak warms up the whole space.",
      "images": ["customer-room-1.jpg"],
      "metadata": {"room": "Kitchen/Dining", "style": "Modern Farmhouse"}
    },
    {
      "id": "r2",
      "author": "David L.",
      "rating": 5,
      "text": "Seats 8 comfortably. The finish is bulletproof with two kids.",
      "images": ["customer-room-2.jpg", "customer-room-2b.jpg"],
      "metadata": {"room": "Dining Room", "style": "Transitional"}
    }
  ],
  "showPhotosOnly": false
}'></div>
```

---

## Typography & Color

### Typography
- **Headings:** Warm serif (Fraunces, Quincy CF, Canela) or geometric sans (Avenir Next, Graphik, Suisse Intl) at 400-500 weight
- **Body:** 15-17px, 1.6-1.7 line-height, never below 14px
- **Eyebrow:** 11-12px uppercase, 0.12em letter-spacing, muted color
- **Hierarchy:** Large product name (3-4rem), subdued descriptors (0.875rem), generous whitespace

### Color
**Warm neutrals only.** Home buyers are hyper-sensitive to color — stark white (#FFF) reads as cold/clinical and undermines the "warm home" feeling.

```css
:root {
  --lx-bg-color: #FAFAF8;       /* Warm off-white, not stark */
  --lx-bg-surface: #F7F5F2;      /* Slightly warmer for cards */
  --lx-text-color: #2C2C2C;      /* Warm black, not pure black */
  --lx-text-muted: #6B6B6B;      /* Warm gray for secondary text */
  --lx-border-color: #E8E6E1;    /* Warm border, not cool gray */
  --lx-accent-color: #8B7355;    /* Derived from product material (walnut brown, ceramic sage, linen beige) */
  --lx-font-heading: 'Fraunces', Georgia, serif;
  --lx-font-body: 'Avenir Next', -apple-system, sans-serif;
}
```

**Accent from product:** If oak furniture → warm brown accent. If ceramic → soft sage or clay. If linen → warm beige. Never generic blue/red.

---

## Hero Patterns

### Room Scene Hero (Furniture)
```html
<section class="relative min-h-[85vh]" id="hero">
  <img 
    src="ASSET[dining-room-wide-hero.jpg]" 
    alt="The Everyday Table in a sunlit dining room with oak chairs and linen curtains" 
    class="absolute inset-0 w-full h-full object-cover"
    loading="eager"
  />
  <!-- Gradient overlay for text legibility -->
  <div class="absolute inset-0 bg-gradient-to-r from-white/80 via-white/40 to-transparent"></div>
  
  <div class="relative z-10 flex items-center min-h-[85vh] px-6 lg:px-16">
    <div class="max-w-lg space-y-5">
      <p class="text-xs uppercase tracking-[0.12em]" style="color:var(--lx-text-muted)">
        Solid White Oak
      </p>
      <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:400;line-height:1.15;color:var(--lx-text-color)">
        The Everyday Table
      </h1>
      <p class="text-sm" style="color:var(--lx-text-muted)">
        72" × 36" × 30" • Seats 6-8 • No assembly required
      </p>
      <div class="flex gap-4 items-center">
        <span class="text-2xl font-medium" style="color:var(--lx-text-color)">$1,850</span>
        <a 
          href="#details" 
          class="inline-block text-sm font-medium border-b pb-1 transition-colors hover:opacity-70" 
          style="color:var(--lx-text-color);border-color:var(--lx-border-color)"
        >
          View Details →
        </a>
      </div>
    </div>
  </div>
</section>
```

### Lifestyle Hero (Small Goods — Candle)
```html
<section class="relative min-h-[75vh]" id="hero">
  <img 
    src="ASSET[candle-vignette-hero.jpg]" 
    alt="Cedarwood candle on styled shelf with books and ceramics" 
    class="absolute inset-0 w-full h-full object-cover"
  />
  <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/20 to-transparent"></div>
  
  <div class="relative z-10 flex items-end min-h-[75vh] px-6 lg:px-16 pb-12">
    <div class="max-w-md space-y-4">
      <p class="text-xs uppercase tracking-[0.12em] text-white/80">
        Hand-Poured Soy Wax
      </p>
      <h1 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3.5vw,2.5rem);font-weight:400;line-height:1.2;color:white">
        Cedarwood & Amber
      </h1>
      <p class="text-sm text-white/80">
        8 oz • 50-hour burn • Smokeless cotton wick
      </p>
      <div class="flex gap-4 items-center">
        <span class="text-xl font-medium text-white">$38</span>
        <a 
          href="#details" 
          class="inline-block text-sm font-medium border-b border-white/50 pb-1 text-white hover:opacity-70 transition-opacity"
        >
          Shop Now →
        </a>
      </div>
    </div>
  </div>
</section>
```

---

## Dimensions Section (NON-NEGOTIABLE)

**For furniture, dimensions MUST be in the first 2-3 sections.** Use the Tabs island with Dimensions as the default open tab.

```html
<section class="py-16 px-6 lg:px-16" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div data-island="Tabs" data-props='{
      "tabs": [
        {
          "id": "dimensions",
          "label": "Dimensions",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Dimensions</h3><ul class=\"space-y-2 text-sm\" style=\"color:var(--lx-text-muted)\"><li><strong>Height:</strong> 30 inches</li><li><strong>Width:</strong> 72 inches</li><li><strong>Depth:</strong> 36 inches</li><li><strong>Weight:</strong> 145 lbs</li><li><strong>Clearance:</strong> 24\" recommended around table</li><li><strong>Assembly:</strong> None required — delivered fully assembled</li></ul><p class=\"text-xs mt-4\" style=\"color:var(--lx-text-muted)\">Custom sizes available. <a href=\"#contact\" class=\"underline\">Contact us</a> for quote.</p></div>"
        },
        {
          "id": "materials",
          "label": "Materials",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Materials</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Solid white oak from sustainably managed forests in Vermont. Each plank is hand-selected for grain consistency. Natural oil finish (not polyurethane) for a matte, tactile surface. Stainless steel leveling feet with felt pads.</p></div>"
        },
        {
          "id": "care",
          "label": "Care",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Care Instructions</h3><ul class=\"space-y-2 text-sm\" style=\"color:var(--lx-text-muted)\"><li>Wipe spills immediately with a damp cloth</li><li>Avoid harsh chemicals and abrasive cleaners</li><li>Re-oil annually with the included maintenance kit (instructions provided)</li><li>Use placemats or trivets for hot items</li></ul></div>"
        },
        {
          "id": "shipping",
          "label": "Shipping",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Shipping & Delivery</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">White-glove delivery in 4-6 weeks. We'll call to schedule a delivery window, bring the table to your room of choice, unpack, and remove all packaging. Free shipping within the continental US. Alaska/Hawaii: contact for quote.</p></div>"
        }
      ],
      "defaultTab": "dimensions"
    }'></div>
  </div>
</section>
```

---

## Material Story Section

**The "why it costs what it costs" section.** Bento-style grid with material origin, craftsmanship, finish, and durability. Pair with ImageZoom for tactile close-ups.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        Crafted to Last Generations
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        Why we chose white oak, hand-joinery, and natural oil
      </p>
    </div>

    <!-- Bento Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
      <!-- Large image: oak forest -->
      <div class="lg:col-span-7 lg:row-span-2 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <img 
          src="ASSET[oak-forest-vermont.jpg]" 
          alt="White oak forest in Vermont" 
          class="w-full h-full object-cover min-h-[400px]"
        />
      </div>

      <!-- Text: origin -->
      <div class="lg:col-span-5 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Sustainably Sourced</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          Our white oak comes from family-owned forests in Vermont, certified by the Forest Stewardship Council. Each tree is tracked from forest to finish.
        </p>
      </div>

      <!-- Image: joinery close-up -->
      <div class="lg:col-span-5 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <div data-island="ImageZoom" data-props='{
          "src": "ASSET[mortise-tenon-joint.jpg]",
          "alt": "Mortise and tenon joinery detail",
          "zoomLevel": 2.5
        }'></div>
      </div>

      <!-- Text: craftsmanship -->
      <div class="lg:col-span-5 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Hand-Joined</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          Mortise-and-tenon joinery — the same technique used in 18th-century furniture. No screws, no glue failures. The table tightens over time.
        </p>
      </div>

      <!-- Text: finish -->
      <div class="lg:col-span-7 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Natural Oil Finish</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          We skip polyurethane in favor of Danish oil. The surface is matte, warm to the touch, and ages beautifully. Minor scratches can be buffed out with the included kit — no refinishing needed.
        </p>
      </div>

      <!-- Image: grain macro -->
      <div class="lg:col-span-5 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <div data-island="ImageZoom" data-props='{
          "src": "ASSET[oak-grain-macro.jpg]",
          "alt": "White oak grain close-up",
          "zoomLevel": 3
        }'></div>
      </div>
    </div>
  </div>
</section>
```

---

## Room Inspiration Gallery

**Asymmetric CSS Grid showing the product in 4-6 different room settings.** Critical for buyers who need to see versatility.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-color)">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        Styled Six Ways
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        From modern farmhouse to mid-century minimal
      </p>
    </div>

    <!-- Asymmetric grid -->
    <div class="grid grid-cols-4 lg:grid-cols-8 gap-4">
      <!-- Large: modern farmhouse -->
      <div class="col-span-4 row-span-2 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-modern-farmhouse.jpg]" 
          alt="Table in modern farmhouse dining room" 
          class="w-full h-full object-cover min-h-[500px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-sm font-medium">Modern Farmhouse</p>
          <p class="text-white/80 text-xs mt-1">With linen chairs and pendant lighting</p>
        </div>
      </div>

      <!-- Small: mid-century -->
      <div class="col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-midcentury.jpg]" 
          alt="Table in mid-century modern dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Mid-Century</p>
        </div>
      </div>

      <!-- Small: scandinavian -->
      <div class="col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-scandinavian.jpg]" 
          alt="Table in Scandinavian-style dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Scandinavian</p>
        </div>
      </div>

      <!-- Medium: industrial -->
      <div class="col-span-2 lg:col-span-3 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-industrial.jpg]" 
          alt="Table in industrial loft dining room" 
          class="w-full h-full object-cover min-h-[300px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Industrial</p>
        </div>
      </div>

      <!-- Medium: coastal -->
      <div class="col-span-2 lg:col-span-3 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-coastal.jpg]" 
          alt="Table in coastal-style dining room" 
          class="w-full h-full object-cover min-h-[300px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Coastal</p>
        </div>
      </div>

      <!-- Small: transitional -->
      <div class="col-span-2 lg:col-span-2 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-transitional.jpg]" 
          alt="Table in transitional dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Transitional</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Social Proof

**Photo reviews showing the product in REAL customer homes** (not staged). This is the most trusted content in the home vertical — buyers want to see the product after delivery, in imperfect lighting, in real rooms.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        In Your Homes
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        Real rooms, real reviews
      </p>
    </div>

    <div data-island="ReviewCarousel" data-props='{
      "reviews": [
        {
          "id": "r1",
          "author": "Jessica M.",
          "location": "Portland, OR",
          "rating": 5,
          "title": "Exactly what we needed",
          "text": "Perfect size for our open-plan kitchen. The oak warms up the whole space. We've had it for 6 months and it still looks brand new despite daily use with two kids.",
          "images": ["ASSET[customer-room-jessica.jpg]", "ASSET[customer-detail-jessica.jpg]"],
          "metadata": {"room": "Kitchen/Dining", "style": "Modern Farmhouse"},
          "verifiedPurchase": true,
          "date": "2026-05-12"
        },
        {
          "id": "r2",
          "author": "David L.",
          "location": "Austin, TX",
          "rating": 5,
          "title": "Worth every penny",
          "text": "We deliberated for weeks before buying. No regrets. The finish is bulletproof, seats 8 comfortably, and the craftsmanship is obvious. It's the anchor of our dining room.",
          "images": ["ASSET[customer-room-david.jpg]", "ASSET[customer-room-david-2.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Transitional"},
          "verifiedPurchase": true,
          "date": "2026-04-28"
        },
        {
          "id": "r3",
          "author": "Priya S.",
          "location": "Seattle, WA",
          "rating": 5,
          "title": "Finally, a table that fits our space",
          "text": "We have a narrow dining room and most tables are either too wide or too small. This is the Goldilocks table — 72\" is perfect. The delivery team was incredibly careful and professional.",
          "images": ["ASSET[customer-room-priya.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Mid-Century"},
          "verifiedPurchase": true,
          "date": "2026-03-15"
        }
      ],
      "showPhotosOnly": false,
      "slidesToShow": 1,
      "autoplay": false
    }'></div>
  </div>
</section>
```

---

## Photography

**Room context is non-negotiable.** Do not show furniture floating in a white void — it reads as cheap, despite the price point.

### Required shot types (in order of priority):
1. **Room-wide hero** — product as focal point in a fully styled room (rug, lighting, accessories, wall art)
2. **Scale reference** — product with a person seated/standing nearby (or known-size objects like books, plates)
3. **Detail shots** — joinery, grain, hardware, finish (macro lens, natural light)
4. **Alternate angles** — room from 2-3 different viewpoints
5. **In-use shots** — table set for a meal, candle lit, textiles draped/styled
6. **Material close-ups** — ImageZoom-ready macros of wood grain, fabric weave, ceramic glaze

### Asset keyword patterns:
- `room-wide-hero`, `room-angle-2`, `room-kitchen-view`
- `detail-leg-joinery`, `detail-oak-grain`, `detail-hardware`
- `scale-person-seated`, `scale-room-context`
- `styled-dining-table-set`, `styled-breakfast-nook`
- `customer-room-[name]`, `customer-detail-[name]`

### Anti-pattern:
Never use product photos with:
- Pure white backgrounds (reads as e-commerce commodity, not heirloom furniture)
- No scale reference (can't tell if it's 4 feet or 8 feet)
- Harsh studio lighting (looks artificial)
- Empty rooms (reads as "before" photo, not aspirational)

---

## Anti-Patterns

### 12 Home Page Killers

1. **No room context** — product floating in white void. NEVER.
2. **Missing dimensions above the fold** — buyers can't proceed without H×W×D.
3. **Tiny product images** — home buyers zoom obsessively. Use ImageZoom islands.
4. **Cold color palette** — stark white (#FFF), cool grays, blue accents. Reads as clinical/office, not home.
5. **Generic product photography** — no styling, no accessories, no life.
6. **Buried shipping/assembly info** — surprise fees or assembly requirements kill conversions.
7. **No material story** — "solid oak" means nothing without origin, finish, durability.
8. **No customer room photos** — staged rooms are aspirational, customer rooms build trust.
9. **Mobile-hostile specs** — dimensions in a dense paragraph instead of scannable list.
10. **No cross-sells** — buyers want to see the full room, not just one piece.
11. **Flat typography** — home is tactile. Use warm serifs, generous spacing, hierarchy.
12. **No scale reference** — table could be 4 feet or 12 feet. Show a person or known-size object.

### Warning Signs in Blueprint Prompts:
- "Minimalist design" → often means cold/sparse. Home needs warmth.
- "Lots of whitespace" → yes, but warm off-white (#FAFAF8), not stark.
- "Product gallery" → must specify room context shots, not just product-on-white.
- "Clean and modern" → risk of sterile. Clarify "warm modern" or "organic modern."

---

## Complete Blueprint Example

**Full VibePage JSON for Furniture PDP (Dining Table)**

```json
{
  "head": {
    "title": "The Everyday Table — Solid White Oak | [Brand Name]",
    "description": "Hand-crafted dining table in solid white oak. 72\" × 36\" × 30\". Seats 6-8. Mortise-and-tenon joinery. Natural oil finish. White-glove delivery in 4-6 weeks.",
    "og_image": "ASSET[og-everyday-table.jpg]"
  },
  "theme_css": ":root{--lx-bg-color:#FAFAF8;--lx-bg-surface:#F7F5F2;--lx-text-color:#2C2C2C;--lx-text-muted:#6B6B6B;--lx-border-color:#E8E6E1;--lx-accent-color:#8B7355;--lx-font-heading:'Fraunces',Georgia,serif;--lx-font-body:'Avenir Next',-apple-system,sans-serif}",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh]\"><img src=\"ASSET[dining-room-wide-hero.jpg]\" alt=\"The Everyday Table in sunlit dining room\" class=\"absolute inset-0 w-full h-full object-cover\" loading=\"eager\"/><div class=\"absolute inset-0 bg-gradient-to-r from-white/80 via-white/40 to-transparent\"></div><div class=\"relative z-10 flex items-center min-h-[85vh] px-6 lg:px-16\"><div class=\"max-w-lg space-y-5\"><p class=\"text-xs uppercase tracking-[0.12em]\" style=\"color:var(--lx-text-muted)\">Solid White Oak</p><h1 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:400;line-height:1.15;color:var(--lx-text-color)\">The Everyday Table</h1><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">72\" × 36\" × 30\" • Seats 6-8 • No assembly required</p><div class=\"flex gap-4 items-center\"><span class=\"text-2xl font-medium\" style=\"color:var(--lx-text-color)\">$1,850</span><a href=\"#details\" class=\"inline-block text-sm font-medium border-b pb-1 transition-colors hover:opacity-70\" style=\"color:var(--lx-text-color);border-color:var(--lx-border-color)\">View Details →</a></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "quick-specs",
      "html": "<section class=\"py-12 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-6 text-center\"><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Dimensions</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">72\" × 36\" × 30\"</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Material</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Solid White Oak</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Finish</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Natural Oil</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Delivery</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">4-6 Weeks</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product-gallery",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"src\":\"ASSET[table-room-wide.jpg]\",\"alt\":\"Dining table in styled room\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-leg.jpg]\",\"alt\":\"Oak leg joinery close-up\",\"type\":\"detail\"},{\"src\":\"ASSET[table-scale-person.jpg]\",\"alt\":\"Table with person seated\",\"type\":\"scale\"},{\"src\":\"ASSET[table-room-angle2.jpg]\",\"alt\":\"Dining room from kitchen view\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-grain.jpg]\",\"alt\":\"Oak grain macro\",\"type\":\"detail\"}],\"thumbnailPosition\":\"left\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "dimensions-tabs",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"id\":\"dimensions\",\"label\":\"Dimensions\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Dimensions</h3><ul class=\\\"space-y-2 text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\"><li><strong>Height:</strong> 30 inches</li><li><strong>Width:</strong> 72 inches</li><li><strong>Depth:</strong> 36 inches</li><li><strong>Weight:</strong> 145 lbs</li><li><strong>Clearance:</strong> 24\\\" recommended</li><li><strong>Assembly:</strong> None — delivered fully assembled</li></ul></div>\"},{\"id\":\"materials\",\"label\":\"Materials\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Materials</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Solid white oak from Vermont. Natural oil finish. Stainless steel leveling feet.</p></div>\"},{\"id\":\"care\",\"label\":\"Care\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Care</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Wipe with damp cloth. Re-oil annually.</p></div>\"},{\"id\":\"shipping\",\"label\":\"Shipping\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Shipping</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">White-glove delivery in 4-6 weeks.</p></div>\"}],\"defaultTab\":\"dimensions\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "material-story",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)\">Crafted to Last Generations</h2></div><div class=\"grid grid-cols-1 lg:grid-cols-12 gap-4\"><div class=\"lg:col-span-7 lg:row-span-2 relative overflow-hidden rounded-lg\"><img src=\"ASSET[oak-forest.jpg]\" alt=\"Vermont oak forest\" class=\"w-full h-full object-cover min-h-[400px]\"/></div><div class=\"lg:col-span-5 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Sustainably Sourced</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">FSC-certified Vermont oak.</p></div><div class=\"lg:col-span-5 relative overflow-hidden rounded-lg\"><div data-island=\"ImageZoom\" data-props='{\"src\":\"ASSET[mortise-tenon.jpg]\",\"alt\":\"Joinery detail\",\"zoomLevel\":2.5}'></div></div><div class=\"lg:col-span-7 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Natural Oil Finish</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Matte, warm, repairable.</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "room-gallery",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Styled Six Ways</h2></div><div class=\"grid grid-cols-4 lg:grid-cols-8 gap-4\"><div class=\"col-span-4 row-span-2 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-farmhouse.jpg]\" alt=\"Modern farmhouse\" class=\"w-full h-full object-cover min-h-[500px] transition-transform duration-500 group-hover:scale-105\"/><div class=\"absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent\"><p class=\"text-white text-sm font-medium\">Modern Farmhouse</p></div></div><div class=\"col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-midcentury.jpg]\" alt=\"Mid-century\" class=\"w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105\"/></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div data-island=\"ProductCarousel\" data-props='{\"title\":\"Complete the Room\",\"products\":[{\"id\":\"bench-01\",\"name\":\"Matching Bench\",\"price\":\"$485\",\"image\":\"ASSET[bench.jpg]\"},{\"id\":\"chair-01\",\"name\":\"Oak Dining Chair\",\"price\":\"$295\",\"image\":\"ASSET[chair.jpg]\"}],\"slidesToShow\":3}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "before-after",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-5xl mx-auto\"><div class=\"text-center mb-8\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Room Transformations</h2></div><div data-island=\"BeforeAfter\" data-props='{\"beforeImage\":\"ASSET[before-dining.jpg]\",\"afterImage\":\"ASSET[after-dining.jpg]\",\"caption\":\"Sarah's dining room with The Everyday Table\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">In Your Homes</h2></div><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"id\":\"r1\",\"author\":\"Jessica M.\",\"rating\":5,\"text\":\"Perfect for our open-plan kitchen.\",\"images\":[\"ASSET[customer-1.jpg]\"],\"verifiedPurchase\":true}],\"slidesToShow\":1}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"Is assembly required?\",\"answer\":\"No. The table is delivered fully assembled.\"},{\"question\":\"Can I customize the size?\",\"answer\":\"Yes. Contact us for a quote on custom dimensions.\"},{\"question\":\"What's your return policy?\",\"answer\":\"30-day returns. We'll arrange pickup and issue a full refund.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta-footer",
      "html": "<section class=\"py-20 px-6 lg:px-16 text-center\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-xl mx-auto\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:var(--lx-text-color)\">Get Design Tips in Your Inbox</h2><p class=\"mt-3 text-sm\" style=\"color:var(--lx-text-muted)\">Room styling ideas, new releases, and exclusive offers</p><div class=\"mt-6\"><div data-island=\"EmailCapture\" data-props='{\"placeholder\":\"Your email\",\"buttonText\":\"Subscribe\",\"successMessage\":\"Thanks! Check your inbox.\"}'></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Home & lifestyle pages succeed when they **transport the buyer into the space** — not just show them a product. Every section should answer: "What will this look like in my home? How will it feel? Will it fit? Is it worth the price?" Context, scale, material story, and real customer rooms are the four pillars. Skip any of them and conversions collapse.


---

## GOOGLE-TRAFFIC

# Google Ads & SEO → Landing Page — Storefront Design Intelligence

> **When to load:** Page designed for Google Ads (Search/Shopping/Display) or organic SEO traffic.

## Philosophy

Google traffic arrives with **INTENT**. They searched. They typed keywords. They're already interested — your job is to **answer immediately**.

Unlike social traffic (discovery-driven, emotional), Google visitors want:
- **Information density** — specs, comparisons, evidence
- **Validation** — reviews, certifications, guarantees
- **Clarity** — clear pricing, transparent shipping, no surprises
- **Speed** — fast answers, visible CTAs, minimal friction

**Not needed:** Emotional hooks, storytelling, lifestyle imagery above the fold. They're past awareness — they're evaluating.

**Core principle:** Answer their search query in the first 3 seconds or lose them.

---

## Intent-Based Architecture

Google traffic falls into **4 intent categories**. Each requires a different page structure:

### 1. Transactional Intent ("buy X", "X for sale", "X price")
**User goal:** Make a purchase decision now.  
**Page focus:** Product + price + trust signals + fast checkout.  
**Sections:** 8-10 total.

### 2. Comparison Intent ("X vs Y", "best X", "X alternatives")
**User goal:** Evaluate options before deciding.  
**Page focus:** CompareTable-led, feature grids, "why us" positioning.  
**Sections:** 10-12 total.

### 3. Informational Intent ("how X works", "what is X", "X benefits")
**User goal:** Learn before committing.  
**Page focus:** Educational content, detailed explanations, FAQs.  
**Sections:** 10-14 total.

### 4. Navigational Intent (brand name search)
**User goal:** Find your specific brand.  
**Page focus:** Affirm their choice, show product range, make buying easy.  
**Sections:** 6-8 total.

---

## Section Sequences (by Intent)

### Transactional (8-10 sections)
1. **Product+Price Hero** — image, price, rating, CTA
2. **TrustBadgeBar** — shipping, guarantee, certifications
3. **Key Benefits Grid** — 3-4 benefits with icons
4. **Social Proof** — reviews or testimonials
5. **Product Details** — specs, ingredients, what's included
6. **FAQ** — 8-10 objection-handling questions
7. **Pricing Tiers** (if applicable) — BuyBox or QuantityBreaks
8. **Final CTA** — StickyBar or repeated buy button
9. *Optional:* ProductCarousel (related items)
10. *Optional:* ReviewCarousel (detailed reviews)

### Comparison (10-12 sections)
1. **Comparison Hero** — positioning statement + visual
2. **CompareTable** — you vs 2 competitors, 5-7 rows
3. **Why We Win Grid** — 3-4 differentiators
4. **Evidence Section** — certifications, lab results, press
5. **Detailed Feature Breakdown** — Tabs or accordion
6. **Social Proof** — aggregated reviews
7. **FAQ** — comparison-specific questions ("why more expensive?")
8. **Pricing Display** — clear, with value anchoring
9. **Guarantee/Risk Reversal** — money-back, trial period
10. **Final CTA**
11. *Optional:* Case studies or before/after
12. *Optional:* Video explainer

### Informational (10-14 sections)
1. **Answer-First Hero** — direct answer to search query
2. **Educational Content** — how it works, step-by-step
3. **Visual Explainer** — diagram or video
4. **Benefits Deep Dive** — detailed, with evidence
5. **Scientific Backing** — studies, certifications
6. **Use Cases** — who it's for, scenarios
7. **FAQ** — 10-12 questions (educational + objections)
8. **Social Proof** — reviews focusing on outcomes
9. **Product Details** — what you're actually buying
10. **Comparison** — vs alternatives or status quo
11. **Pricing** — transparent, value-focused
12. **Guarantee**
13. **Final CTA**
14. *Optional:* Related content or resources

### Navigational (6-8 sections)
1. **Brand Hero** — logo, tagline, category
2. **ProductCarousel** — full range
3. **Why Us** — 3-4 key differentiators
4. **Social Proof** — aggregate reviews
5. **FAQ** — brand-specific questions
6. **Final CTA**
7. *Optional:* Company story (brief)
8. *Optional:* Press mentions

---

## Above-the-Fold Rules

**Transactional intent MUST show:**
- Product image (high quality, zoomable)
- Price (actual number, not "learn more")
- Star rating + review count
- Primary CTA ("Add to Cart", not "Learn More")
- Key trust signal (free shipping, guarantee)

**Comparison intent MUST show:**
- Clear positioning ("The #1 alternative to X")
- Visual indication of comparison (split hero or table preview)
- Primary differentiator ("30% more effective")

**Informational intent MUST show:**
- Direct answer to the likely query
- Clear content structure (headings visible)
- Scroll indicator ("Learn more ↓")

**Example: Info-Dense Transactional Hero**
```html
<section class="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16" style="background:var(--lx-bg-color)">
  <div>
    <img src="IMAGE_URL" alt="Product" class="w-full rounded-xl shadow-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-4">
    <div class="flex items-center gap-2">
      <div class="flex text-yellow-400">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
      </div>
      <span class="text-sm font-medium" style="color:var(--lx-text-muted)">4.8/5 from 4,847 reviews</span>
    </div>
    
    <h1 class="font-bold leading-tight" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      Premium Omega-3 Fish Oil — 2,847mg Per Serving
    </h1>
    
    <p class="text-base" style="color:var(--lx-text-muted)">
      Triple-strength formula • 90 softgels • 3-month supply
    </p>
    
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$34.99</span>
      <span class="text-xl line-through opacity-40" style="color:var(--lx-text-muted)">$49.99</span>
      <span class="text-xs px-2 py-1 rounded-full font-semibold" style="background:var(--lx-accent-color);color:white">30% OFF</span>
    </div>
    
    <p class="text-sm flex flex-col gap-1" style="color:var(--lx-text-muted)">
      <span>✓ Free shipping on all orders</span>
      <span>✓ 90-day money-back guarantee</span>
      <span>✓ Third-party lab tested</span>
    </p>
    
    <button class="w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white">
      Add to Cart — Free Shipping
    </button>
    
    <p class="text-xs text-center" style="color:var(--lx-text-muted)">
      In stock • Ships within 24 hours
    </p>
  </div>
</section>
```

---

## Hero Patterns

### Product+Price Hero (Transactional)

**Purpose:** Answer "what is it, how much, why trust you" in 3 seconds.

**Required elements:**
- High-quality product image (left on desktop)
- Star rating + review count (specific number, not "thousands")
- Product name + key benefit as H1
- Key specs or quantity (one line, scannable)
- Price (large, actual number) + compare-at price + discount badge
- 3 trust signals (shipping, guarantee, certification)
- Primary CTA (action-oriented: "Add to Cart", not "Shop Now")
- Stock/shipping status

```html
<!-- See example above -->
```

### Comparison Hero

**Purpose:** Immediately signal "we're better than X" and preview the proof.

```html
<section class="py-12 lg:py-20 px-4" style="background:linear-gradient(135deg, var(--lx-bg-surface) 0%, var(--lx-bg-color) 100%)">
  <div class="max-w-6xl mx-auto text-center">
    <div class="inline-block px-4 py-1 rounded-full text-sm font-semibold mb-4" style="background:var(--lx-accent-color);color:white;opacity:0.9">
      The #1 Alternative to Brand X
    </div>
    
    <h1 class="font-bold mb-4" style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)">
      30% More Effective. 40% Less Expensive.
    </h1>
    
    <p class="text-lg max-w-2xl mx-auto mb-8" style="color:var(--lx-text-muted)">
      Trusted by over 50,000 customers who switched from premium brands — same results, better value.
    </p>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-4xl mx-auto">
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">2,847mg</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">vs Competitor's 2,100mg</div>
      </div>
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">$0.39</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">per serving (vs $0.67)</div>
      </div>
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">4.8★</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">from 4,847 reviews</div>
      </div>
    </div>
  </div>
</section>
```

### Answer-First Hero (Informational)

**Purpose:** Give them the answer immediately, then earn the click to "learn more".

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto">
    <h1 class="font-bold mb-6 text-center" style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)">
      How Long Does It Take for Omega-3 to Work?
    </h1>
    
    <div class="p-6 rounded-xl mb-8" style="background:var(--lx-accent-color);color:white">
      <p class="text-xl font-semibold mb-4">Quick Answer:</p>
      <p class="text-lg leading-relaxed">
        Most people notice initial benefits within <strong>2-3 weeks</strong> (improved mood, focus). 
        Full cardiovascular and joint benefits typically appear after <strong>8-12 weeks</strong> of consistent use.
      </p>
    </div>
    
    <p class="text-lg mb-4" style="color:var(--lx-text-muted)">
      But the timeline depends on several factors. Here's everything you need to know:
    </p>
    
    <div class="flex justify-center">
      <svg class="w-6 h-6 animate-bounce" style="color:var(--lx-text-muted)" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </div>
</section>
```

---

## CompareTable Strategy

**The power island for Google comparison traffic.** When someone searches "X vs Y", they want a table. Give it to them.

**Rules:**
- **Max 3 columns** — you + 2 competitors (or "typical brand" + "cheap alternative")
- **5-7 rows** — key decision factors only, not feature dump
- **Win the majority** — be honest, but pick rows where you win or tie 4+ times
- **Specific numbers** — not "high quality", but "2,847mg per serving"
- **Visual wins** — checkmarks (✓), crosses (✗), or color-coded cells

**CompareTable island HTML:**
```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      How We Compare to Leading Brands
    </h2>
    
    <div data-island="CompareTable" data-props='{
      "columns": ["Our Brand", "Brand X (Premium)", "Brand Y (Budget)"],
      "highlightColumn": 0,
      "rows": [
        {
          "label": "Omega-3 Per Serving",
          "values": ["2,847mg ✓", "2,100mg", "1,200mg"]
        },
        {
          "label": "Price Per Serving",
          "values": ["$0.39 ✓", "$0.67", "$0.28"]
        },
        {
          "label": "Third-Party Tested",
          "values": ["✓ Yes", "✓ Yes", "✗ No"]
        },
        {
          "label": "Purity (Mercury)",
          "values": ["<0.09ppm ✓", "<0.10ppm", "Unknown"]
        },
        {
          "label": "Money-Back Guarantee",
          "values": ["90 days ✓", "30 days", "None"]
        },
        {
          "label": "Free Shipping",
          "values": ["✓ All orders", "Over $50", "✗ Never"]
        },
        {
          "label": "Average Rating",
          "values": ["4.8/5 (4,847) ✓", "4.6/5 (2,103)", "3.9/5 (847)"]
        }
      ]
    }'></div>
    
    <p class="text-center text-sm mt-6" style="color:var(--lx-text-muted)">
      Data last verified: June 2026. Competitor pricing based on publicly listed prices.
    </p>
  </div>
</section>
```

**When to use:**
- Any comparison intent ("X vs Y", "best X", "X alternative")
- Transactional pages in competitive markets (supplement, SaaS, electronics)
- After hero, before deep dive (section 2-3)

---

## Information Density

Google searchers **want substance**. Unlike social traffic (skim, scroll, bounce), they came to read.

**What this means:**
- **More text is OK** — 200-300 word paragraphs are fine if well-structured
- **Use headings liberally** — H2 every 2-3 paragraphs, H3 for sub-points
- **Bullet lists** — break up dense info (specs, benefits, features)
- **Tabs or accordions** — for deep content (ingredients, scientific backing, detailed specs)
- **FAQ with 8-12 questions** — not 4-5 (they have LOTS of questions)

**Bad example (thin):**
```
Our product is the best. Buy now!
```

**Good example (dense but scannable):**
```html
<section class="py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <h2 class="font-bold mb-6" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)">
      What Makes Our Formula Different
    </h2>
    
    <div class="space-y-6">
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">1. Triple-Strength Concentration</h3>
        <p class="leading-relaxed mb-3" style="color:var(--lx-text-muted)">
          Each serving delivers <strong>2,847mg of omega-3 fatty acids</strong> — including 1,647mg EPA and 1,200mg DHA. 
          That's 30-40% more than most "premium" brands, which means faster results and better value per dose.
        </p>
        <ul class="list-disc list-inside space-y-1" style="color:var(--lx-text-muted)">
          <li>EPA: Supports cardiovascular health and reduces inflammation</li>
          <li>DHA: Critical for brain function and cognitive health</li>
          <li>Optimal 4:3 EPA:DHA ratio backed by clinical research</li>
        </ul>
      </div>
      
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">2. Molecular Distillation for Purity</h3>
        <p class="leading-relaxed" style="color:var(--lx-text-muted)">
          We use a proprietary 5-step molecular distillation process to remove mercury, PCBs, and other contaminants. 
          Third-party lab results show <strong>less than 0.09ppm mercury</strong> — well below FDA limits and 
          competitive with pharmaceutical-grade fish oils.
        </p>
      </div>
      
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">3. Triglyceride Form (Not Ethyl Ester)</h3>
        <p class="leading-relaxed" style="color:var(--lx-text-muted)">
          Our omega-3s are in <strong>re-esterified triglyceride (rTG) form</strong>, which studies show is 
          up to 70% more bioavailable than the cheaper ethyl ester (EE) form used by most brands. 
          That means your body actually absorbs what you're paying for.
        </p>
      </div>
    </div>
  </div>
</section>
```

---

## FAQ as Conversion Tool

FAQ is not an afterthought — it's a **conversion section** for Google traffic.

**Why:** Their search queries = questions. Answer them = earn trust.

**Rules:**
- **8-12 questions minimum** (not 4-5)
- **Questions = their actual searches** — use Google autocomplete, People Also Ask, your support tickets
- **Mix types:**
  - Product-specific ("How much EPA/DHA per serving?")
  - Objection-handling ("Why more expensive than Brand X?")
  - Usage ("When should I take it?")
  - Trust ("Is it third-party tested?")

**FAQ island HTML:**
```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      Frequently Asked Questions
    </h2>
    
    <div data-island="FAQ" data-props='{
      "items": [
        {
          "question": "How much EPA and DHA does each serving contain?",
          "answer": "Each serving (2 softgels) contains 1,647mg EPA and 1,200mg DHA, for a total of 2,847mg of omega-3 fatty acids. This is 30-40% higher than most premium brands."
        },
        {
          "question": "Is your fish oil tested for mercury and contaminants?",
          "answer": "Yes. Every batch is third-party tested by an independent lab (ISO 17025 certified). Our mercury levels are consistently below 0.09ppm — well under FDA limits of 0.1ppm. Lab reports are available on request."
        },
        {
          "question": "Why is this more expensive than other fish oils?",
          "answer": "Three reasons: (1) Higher concentration (2,847mg vs typical 1,000-1,500mg), (2) Re-esterified triglyceride form (70% more bioavailable than cheap ethyl ester forms), (3) Rigorous purity testing. On a per-serving basis of absorbed omega-3, we are actually more cost-effective."
        },
        {
          "question": "How long until I see results?",
          "answer": "Most customers report improved mood and mental clarity within 2-3 weeks. Full cardiovascular benefits typically appear after 8-12 weeks of consistent daily use."
        },
        {
          "question": "What is the difference between triglyceride and ethyl ester forms?",
          "answer": "Ethyl ester (EE) is cheaper to produce but less bioavailable. Triglyceride (TG) and re-esterified triglyceride (rTG) forms are absorbed 50-70% better. We use rTG, which means more omega-3 reaches your cells per softgel."
        },
        {
          "question": "Do I need to take it with food?",
          "answer": "Yes. Omega-3s are fat-soluble, so taking them with a meal containing fat improves absorption by up to 3x. We recommend taking with breakfast or dinner."
        },
        {
          "question": "Is there a fishy aftertaste or burps?",
          "answer": "Our enteric-coated softgels dissolve in your small intestine (not stomach), which eliminates fishy burps. Over 90% of our customers report zero aftertaste."
        },
        {
          "question": "What is your return policy?",
          "answer": "90-day money-back guarantee. If you are not satisfied for any reason, return the bottle (even if empty) within 90 days for a full refund. No questions asked."
        },
        {
          "question": "How does this compare to krill oil?",
          "answer": "Krill oil has lower EPA/DHA content (typically 200-300mg vs our 2,847mg), making it 10x less cost-effective per mg of omega-3. While krill oil has phospholipid-bound omega-3s, our rTG form is comparably bioavailable at a fraction of the cost."
        },
        {
          "question": "Can I take this if I am on blood thinners?",
          "answer": "Omega-3s have mild blood-thinning properties. If you are on warfarin, aspirin, or other anticoagulants, consult your doctor before starting any omega-3 supplement."
        },
        {
          "question": "Is this safe during pregnancy?",
          "answer": "Omega-3s (especially DHA) are important during pregnancy for fetal brain development. However, you should always consult your OB-GYN before starting any supplement while pregnant or nursing."
        },
        {
          "question": "How should I store this?",
          "answer": "Store in a cool, dry place away from direct sunlight. Refrigeration is not required but can extend shelf life. Do not freeze."
        }
      ],
      "defaultOpen": 0
    }'></div>
  </div>
</section>
```

---

## Trust Signals

Google searchers are **validation-driven**. They want proof.

**Specific > vague:**
- ✗ "Thousands of happy customers"
- ✓ "4,847 verified reviews (4.8/5 average)"

**Verifiable > claimed:**
- ✗ "Highest quality"
- ✓ "Third-party tested by ISO 17025 lab (report available)"

**Quantified > general:**
- ✗ "Fast shipping"
- ✓ "Ships within 24 hours • Avg delivery: 3-5 days"

**TrustBadgeBar HTML (below hero):**
```html
<section class="py-6 px-4" style="background:var(--lx-bg-surface);border-top:1px solid var(--lx-border-color);border-bottom:1px solid var(--lx-border-color)">
  <div class="max-w-6xl mx-auto">
    <div data-island="TrustBadgeBar" data-props='{
      "badges": [
        {"icon": "shield-check", "label": "Third-Party Tested", "sublabel": "ISO 17025 certified lab"},
        {"icon": "truck", "label": "Free Shipping", "sublabel": "All orders • Ships in 24hrs"},
        {"icon": "refresh", "label": "90-Day Guarantee", "sublabel": "Full refund, no questions"},
        {"icon": "award", "label": "4.8★ Rating", "sublabel": "From 4,847 reviews"}
      ],
      "layout": "horizontal"
    }'></div>
  </div>
</section>
```

**Key trust signal types:**
1. **Reviews** — star rating + count + recent review snippets
2. **Certifications** — FDA-registered, GMP, NSF, third-party lab
3. **Guarantees** — money-back period, trial offers
4. **Shipping** — speed, cost, tracking
5. **Press/endorsements** — "As seen in X" (if true)
6. **Usage stats** — "50,000+ customers", "1M+ bottles sold"

---

## Pricing Display

**NEVER hide the price.** Google searchers came to evaluate — they will bounce if they can't see the price above fold.

**Rules:**
1. **Show the number** — not "Starting at", not "Learn more", but "$34.99"
2. **Above fold** — in hero or first 2 sections
3. **Anchoring** — show compare-at price if you have one ("$49.99" struck through)
4. **Per-unit for subscriptions** — "$1.17/day" or "$0.39/serving" alongside monthly price
5. **All-in cost** — "Free shipping" or "+$5.99 shipping" (no surprises)
6. **Payment options** — for high-ticket ($100+), show "or 4 payments of $X" (via PaymentOptions island)

**Pricing display HTML (standalone section):**
```html
<section class="py-12 px-4">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)">
      Simple, Transparent Pricing
    </h2>
    
    <div class="p-8 rounded-xl" style="background:var(--lx-bg-surface);border:2px solid var(--lx-accent-color)">
      <div class="mb-4">
        <span class="text-sm font-semibold px-3 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">BEST VALUE</span>
      </div>
      
      <div class="mb-2">
        <span class="text-5xl font-bold" style="color:var(--lx-text-color)">$34.99</span>
        <span class="text-xl ml-2 line-through opacity-40" style="color:var(--lx-text-muted)">$49.99</span>
      </div>
      
      <p class="text-lg mb-4" style="color:var(--lx-text-muted)">
        $0.39 per serving • 90 servings
      </p>
      
      <ul class="text-left space-y-2 mb-6 max-w-sm mx-auto" style="color:var(--lx-text-muted)">
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>2,847mg omega-3 per serving</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>Free shipping • No subscription required</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>90-day money-back guarantee</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>Ships within 24 hours</span>
        </li>
      </ul>
      
      <button class="w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white">
        Add to Cart
      </button>
    </div>
    
    <p class="text-sm mt-4" style="color:var(--lx-text-muted)">
      One-time purchase • Cancel or modify anytime
    </p>
  </div>
</section>
```

---

## SEO-Ready Structure

Google searchers often came via **organic search** — your page should be SEO-optimized by default.

**Heading hierarchy:**
- One H1 (page title, in hero)
- H2s for major sections (every 400-600 words)
- H3s for sub-sections

**Schema signals** (if applicable):
- Product schema (name, price, rating, availability)
- FAQ schema (automatically added by FAQ island)
- Review schema (aggregate rating)

**Content patterns:**
- **Answer the search query in H1** — "How Long Does Omega-3 Take to Work?" not "Welcome to Our Site"
- **First paragraph = direct answer** — Google often pulls this for featured snippets
- **Use the keyword naturally** — in H1, first paragraph, 2-3 H2s, image alt text
- **Internal links** — to related products, blog posts, category pages
- **External links** — to studies, certifications (builds trust with Google)

---

## Anti-Patterns

**12 Google landing page killers:**

1. **Hidden pricing** — "Contact for quote", "See pricing", "Learn more". Instant bounce.
2. **Emotional-first hero** — Lifestyle imagery + vague tagline. They came to evaluate, not dream.
3. **No comparison** — In competitive markets, failing to position vs alternatives = lost sale.
4. **Thin content** — 3 sections, 400 words total. They have questions; answer them.
5. **No FAQ** — Means you are hiding something or don't understand their concerns.
6. **Fake scarcity** — "Only 3 left!" (refreshes to "Only 3 left!" again). Destroys trust.
7. **No reviews** — Or only 5-star reviews with no detail. Suspicious.
8. **Vague specs** — "High quality", "Premium ingredients". What does that MEAN?
9. **Slow above-fold CTA** — Button is in section 4. They bounced in section 2.
10. **No guarantee** — Asking them to take all the risk. Reduces conversions 20-40%.
11. **Auto-play video** — Especially with sound. Rage quit.
12. **Newsletter popup on entry** — They just arrived. Let them read first.

---

## Complete Blueprints

### Blueprint 1: Transactional Product Page (Omega-3 Example)

```json
{
  "page_id": "omega3-google-transactional",
  "intent": "transactional",
  "traffic_source": "google_ads_search",
  "target_query": "buy omega 3 fish oil",
  
  "head": {
    "title": "Premium Omega-3 Fish Oil (2,847mg) — $34.99 | Free Shipping",
    "description": "Triple-strength omega-3 with 2,847mg per serving. Third-party tested for purity. 4.8★ from 4,847 reviews. 90-day guarantee. Free shipping.",
    "keywords": ["omega 3", "fish oil", "EPA DHA", "omega 3 supplement"]
  },
  
  "theme_css": ":root{--lx-accent-color:#0066CC;--lx-text-color:#1a1a1a;--lx-text-muted:#666666;--lx-bg-color:#ffffff;--lx-bg-surface:#f5f5f5;--lx-border-color:#e0e0e0;--lx-font-heading:'Inter',sans-serif;--lx-font-body:'Inter',sans-serif}",
  
  "sections": [
    {
      "id": "hero",
      "type": "product_info_hero",
      "html": "<section class=\"grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16\" style=\"background:var(--lx-bg-color)\"><div><img src=\"/images/omega3-bottle.jpg\" alt=\"Premium Omega-3 Fish Oil Bottle\" class=\"w-full rounded-xl shadow-lg\"/></div><div class=\"flex flex-col justify-center space-y-4\"><div class=\"flex items-center gap-2\"><div class=\"flex text-yellow-400\"><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg></div><span class=\"text-sm font-medium\" style=\"color:var(--lx-text-muted)\">4.8/5 from 4,847 reviews</span></div><h1 class=\"font-bold leading-tight\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Premium Omega-3 Fish Oil — 2,847mg Per Serving</h1><p class=\"text-base\" style=\"color:var(--lx-text-muted)\">Triple-strength formula • 90 softgels • 3-month supply</p><div class=\"flex items-baseline gap-3\"><span class=\"text-3xl font-bold\" style=\"color:var(--lx-text-color)\">$34.99</span><span class=\"text-xl line-through opacity-40\" style=\"color:var(--lx-text-muted)\">$49.99</span><span class=\"text-xs px-2 py-1 rounded-full font-semibold\" style=\"background:var(--lx-accent-color);color:white\">30% OFF</span></div><p class=\"text-sm flex flex-col gap-1\" style=\"color:var(--lx-text-muted)\"><span>✓ Free shipping on all orders</span><span>✓ 90-day money-back guarantee</span><span>✓ Third-party lab tested</span></p><button class=\"w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — Free Shipping</button><p class=\"text-xs text-center\" style=\"color:var(--lx-text-muted)\">In stock • Ships within 24 hours</p></div></section>"
    },
    {
      "id": "trust-bar",
      "type": "trust_badges",
      "html": "<section class=\"py-6 px-4\" style=\"background:var(--lx-bg-surface);border-top:1px solid var(--lx-border-color);border-bottom:1px solid var(--lx-border-color)\"><div class=\"max-w-6xl mx-auto\"><div data-island=\"TrustBadgeBar\" data-props='{\"badges\":[{\"icon\":\"shield-check\",\"label\":\"Third-Party Tested\",\"sublabel\":\"ISO 17025 certified lab\"},{\"icon\":\"truck\",\"label\":\"Free Shipping\",\"sublabel\":\"All orders • Ships in 24hrs\"},{\"icon\":\"refresh\",\"label\":\"90-Day Guarantee\",\"sublabel\":\"Full refund, no questions\"},{\"icon\":\"award\",\"label\":\"4.8★ Rating\",\"sublabel\":\"From 4,847 reviews\"}],\"layout\":\"horizontal\"}'></div></div></section>"
    },
    {
      "id": "benefits",
      "type": "benefits_grid",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-12\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Why Customers Choose Our Omega-3</h2><div class=\"grid grid-cols-1 md:grid-cols-3 gap-8\"><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M9 2a1 1 0 000 2h2a1 1 0 100-2H9z\"/><path fill-rule=\"evenodd\" d=\"M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm9.707 5.707a1 1 0 00-1.414-1.414L9 12.586l-1.293-1.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Triple-Strength Formula</h3><p style=\"color:var(--lx-text-muted)\">2,847mg per serving — 30-40% more than premium brands. Better value, faster results.</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Pharmaceutical-Grade Purity</h3><p style=\"color:var(--lx-text-muted)\">Molecular distillation removes mercury, PCBs. Third-party tested every batch.</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">70% Better Absorption</h3><p style=\"color:var(--lx-text-muted)\">Re-esterified triglyceride (rTG) form — not cheap ethyl ester. Your body absorbs more.</p></div></div></div></section>"
    },
    {
      "id": "reviews",
      "type": "social_proof",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">What Customers Are Saying</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"name\":\"Sarah M.\",\"rating\":5,\"text\":\"I have tried 4 different omega-3 brands over the years. This one actually works — my joint pain is 80% better after 6 weeks. Worth every penny.\",\"verified\":true},{\"name\":\"Michael T.\",\"rating\":5,\"text\":\"No fishy burps! And my doctor said my triglyceride levels dropped 47 points in 3 months. Switching from my old brand was the best decision.\",\"verified\":true},{\"name\":\"Jennifer K.\",\"rating\":5,\"text\":\"I am a pharmacist and very picky about supplements. The rTG form and third-party testing sold me. My whole family takes this now.\",\"verified\":true}],\"autoplay\":true,\"interval\":5000}'></div></div></section>"
    },
    {
      "id": "details",
      "type": "product_details",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"font-bold mb-6\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">What Makes Our Formula Different</h2><div class=\"space-y-6\"><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">1. Triple-Strength Concentration</h3><p class=\"leading-relaxed mb-3\" style=\"color:var(--lx-text-muted)\">Each serving delivers <strong>2,847mg of omega-3 fatty acids</strong> — including 1,647mg EPA and 1,200mg DHA. That's 30-40% more than most \"premium\" brands, which means faster results and better value per dose.</p><ul class=\"list-disc list-inside space-y-1\" style=\"color:var(--lx-text-muted)\"><li>EPA: Supports cardiovascular health and reduces inflammation</li><li>DHA: Critical for brain function and cognitive health</li><li>Optimal 4:3 EPA:DHA ratio backed by clinical research</li></ul></div><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">2. Molecular Distillation for Purity</h3><p class=\"leading-relaxed\" style=\"color:var(--lx-text-muted)\">We use a proprietary 5-step molecular distillation process to remove mercury, PCBs, and other contaminants. Third-party lab results show <strong>less than 0.09ppm mercury</strong> — well below FDA limits and competitive with pharmaceutical-grade fish oils.</p></div><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">3. Triglyceride Form (Not Ethyl Ester)</h3><p class=\"leading-relaxed\" style=\"color:var(--lx-text-muted)\">Our omega-3s are in <strong>re-esterified triglyceride (rTG) form</strong>, which studies show is up to 70% more bioavailable than the cheaper ethyl ester (EE) form used by most brands. That means your body actually absorbs what you're paying for.</p></div></div></div></section>"
    },
    {
      "id": "faq",
      "type": "faq",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"How much EPA and DHA does each serving contain?\",\"answer\":\"Each serving (2 softgels) contains 1,647mg EPA and 1,200mg DHA, for a total of 2,847mg of omega-3 fatty acids. This is 30-40% higher than most premium brands.\"},{\"question\":\"Is your fish oil tested for mercury and contaminants?\",\"answer\":\"Yes. Every batch is third-party tested by an independent lab (ISO 17025 certified). Our mercury levels are consistently below 0.09ppm — well under FDA limits of 0.1ppm. Lab reports are available on request.\"},{\"question\":\"Why is this more expensive than other fish oils?\",\"answer\":\"Three reasons: (1) Higher concentration (2,847mg vs typical 1,000-1,500mg), (2) Re-esterified triglyceride form (70% more bioavailable than cheap ethyl ester forms), (3) Rigorous purity testing. On a per-serving basis of absorbed omega-3, we are actually more cost-effective.\"},{\"question\":\"How long until I see results?\",\"answer\":\"Most customers report improved mood and mental clarity within 2-3 weeks. Full cardiovascular benefits typically appear after 8-12 weeks of consistent daily use.\"},{\"question\":\"What is the difference between triglyceride and ethyl ester forms?\",\"answer\":\"Ethyl ester (EE) is cheaper to produce but less bioavailable. Triglyceride (TG) and re-esterified triglyceride (rTG) forms are absorbed 50-70% better. We use rTG, which means more omega-3 reaches your cells per softgel.\"},{\"question\":\"Do I need to take it with food?\",\"answer\":\"Yes. Omega-3s are fat-soluble, so taking them with a meal containing fat improves absorption by up to 3x. We recommend taking with breakfast or dinner.\"},{\"question\":\"Is there a fishy aftertaste or burps?\",\"answer\":\"Our enteric-coated softgels dissolve in your small intestine (not stomach), which eliminates fishy burps. Over 90% of our customers report zero aftertaste.\"},{\"question\":\"What is your return policy?\",\"answer\":\"90-day money-back guarantee. If you are not satisfied for any reason, return the bottle (even if empty) within 90 days for a full refund. No questions asked.\"}],\"defaultOpen\":0}'></div></div></section>"
    },
    {
      "id": "final-cta",
      "type": "sticky_cta",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Try Risk-Free for 90 Days</h2><p class=\"text-lg mb-6\" style=\"color:var(--lx-text-muted)\">If you don't feel better in 90 days, return it for a full refund. No questions asked.</p><button class=\"px-12 py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — $34.99</button><p class=\"text-sm mt-4\" style=\"color:var(--lx-text-muted)\">Free shipping • Ships within 24 hours</p></div></section>"
    }
  ]
}
```

### Blueprint 2: Comparison Page

```json
{
  "page_id": "omega3-google-comparison",
  "intent": "comparison",
  "traffic_source": "google_ads_search",
  "target_query": "best omega 3 supplement comparison",
  
  "head": {
    "title": "Best Omega-3 Comparison: We Test 12 Brands | 2026 Results",
    "description": "Independent comparison of top omega-3 brands. See purity tests, EPA/DHA levels, price per mg, and real customer results. Updated June 2026.",
    "keywords": ["omega 3 comparison", "best omega 3", "fish oil review"]
  },
  
  "theme_css": ":root{--lx-accent-color:#0066CC;--lx-text-color:#1a1a1a;--lx-text-muted:#666666;--lx-bg-color:#ffffff;--lx-bg-surface:#f5f5f5;--lx-border-color:#e0e0e0;--lx-font-heading:'Inter',sans-serif;--lx-font-body:'Inter',sans-serif}",
  
  "sections": [
    {
      "id": "hero",
      "type": "comparison_hero",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:linear-gradient(135deg, var(--lx-bg-surface) 0%, var(--lx-bg-color) 100%)\"><div class=\"max-w-6xl mx-auto text-center\"><div class=\"inline-block px-4 py-1 rounded-full text-sm font-semibold mb-4\" style=\"background:var(--lx-accent-color);color:white;opacity:0.9\">The #1 Alternative to Nordic Naturals</div><h1 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)\">30% More EPA+DHA. 40% Less Expensive.</h1><p class=\"text-lg max-w-2xl mx-auto mb-8\" style=\"color:var(--lx-text-muted)\">Trusted by over 50,000 customers who switched from premium brands — same purity standards, better value.</p><div class=\"grid grid-cols-1 md:grid-cols-3 gap-4 max-w-4xl mx-auto\"><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">2,847mg</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">vs Nordic's 2,100mg</div></div><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">$0.39</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">per serving (vs $0.67)</div></div><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">4.8★</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">from 4,847 reviews</div></div></div></div></section>"
    },
    {
      "id": "compare-table",
      "type": "comparison_table",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">How We Compare to Leading Brands</h2><div data-island=\"CompareTable\" data-props='{\"columns\":[\"Our Brand\",\"Nordic Naturals\",\"Nature Made\"],\"highlightColumn\":0,\"rows\":[{\"label\":\"Omega-3 Per Serving\",\"values\":[\"2,847mg ✓\",\"2,100mg\",\"1,200mg\"]},{\"label\":\"Price Per Serving\",\"values\":[\"$0.39 ✓\",\"$0.67\",\"$0.28\"]},{\"label\":\"Form\",\"values\":[\"rTG (70% more bioavailable) ✓\",\"TG\",\"EE (ethyl ester)\"]},{\"label\":\"Purity (Mercury)\",\"values\":[\"<0.09ppm ✓\",\"<0.10ppm\",\"Not disclosed\"]},{\"label\":\"Third-Party Tested\",\"values\":[\"✓ Every batch\",\"✓ Yes\",\"✗ No\"]},{\"label\":\"Money-Back Guarantee\",\"values\":[\"90 days ✓\",\"30 days\",\"None\"]},{\"label\":\"Free Shipping\",\"values\":[\"✓ All orders\",\"Over $50\",\"✗ Never\"]},{\"label\":\"Average Rating\",\"values\":[\"4.8/5 (4,847) ✓\",\"4.6/5 (2,103)\",\"3.9/5 (847)\"]}]}'></div><p class=\"text-center text-sm mt-6\" style=\"color:var(--lx-text-muted)\">Data last verified: June 2026. Competitor pricing based on publicly listed prices.</p></div></section>"
    },
    {
      "id": "why-we-win",
      "type": "benefits_grid",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-12\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Why 50,000+ Customers Switched</h2><div class=\"grid grid-cols-1 md:grid-cols-3 gap-8\"><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">More Omega-3 Per Dollar</h3><p style=\"color:var(--lx-text-muted)\">At $0.39/serving for 2,847mg, you get <strong>7,300mg of absorbed omega-3 per dollar</strong> vs 3,100mg with Nordic Naturals.</p></div><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Same Purity Standards</h3><p style=\"color:var(--lx-text-muted)\">We use the same third-party labs as premium brands. Mercury <0.09ppm, PCBs undetectable. Lab reports available.</p></div><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">3X Longer Guarantee</h3><p style=\"color:var(--lx-text-muted)\">90-day money-back (vs 30-day industry standard). We want you to actually see results before committing.</p></div></div></div></section>"
    },
    {
      "id": "faq",
      "type": "faq",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Common Comparison Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"How can you be cheaper if you have more omega-3?\",\"answer\":\"We sell direct-to-consumer with no retail markup. Nordic Naturals pays 40-50% to retailers (Whole Foods, CVS). We pass those savings to you.\"},{\"question\":\"Is rTG form really better than regular TG?\",\"answer\":\"Both are good. rTG is molecularly identical to natural fish oil triglycerides but concentrated. Studies show 10-20% better absorption than TG, 50-70% better than EE (ethyl ester).\"},{\"question\":\"Why do you compare to Nordic Naturals specifically?\",\"answer\":\"They are the #1 premium brand and set the purity/quality standard. If we match or beat them on purity while offering 40% better value, it proves our quality.\"},{\"question\":\"How do I know your lab reports are real?\",\"answer\":\"Every bottle has a lot number. Email us with the lot number and we will send you the third-party lab report (COA) for that specific batch.\"}],\"defaultOpen\":0}'></div></div></section>"
    },
    {
      "id": "cta",
      "type": "final_cta",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Try the #1 Nordic Naturals Alternative</h2><p class=\"text-lg mb-6\" style=\"color:var(--lx-text-muted)\">90-day guarantee. If you don't prefer us, get a full refund.</p><button class=\"px-12 py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — $34.99</button></div></section>"
    }
  ]
}
```

---

## Summary

**Google traffic = intent-driven.** Answer their query immediately, then earn the conversion with evidence.

**Key principles:**
1. **Show price above fold** — always
2. **Information density** — they want substance
3. **CompareTable for comparison intent** — the power island
4. **FAQ 8-12 questions** — their search queries = your FAQs
5. **Trust signals specific + verifiable** — not vague claims
6. **SEO-ready structure** — H1 = search query answer

**Avoid:** Hiding price, emotional-first heroes, thin content, no comparison, fake scarcity, vague specs.

**When in doubt:** Ask "Does this answer their search query in 3 seconds?" If no, rewrite.


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

## DESIGN-ENRICHMENT

# Design Enrichment — AI Image Generation & Compositing

How to use `generate_asset`, `edit_asset`, and `view_asset` tools to create custom images for page sections. Load when a page needs custom imagery beyond what's in the design library.

---

## Decision Tree: Generate vs Reuse

```
Need an image for a section?
│
├─ search_design_library({ query: "hero lifestyle skincare" })
│  ├─ Found good match → USE IT (free, brand-consistent)
│  └─ No match or poor quality → GENERATE
│
├─ Product shot needed?
│  ├─ list_products() has product images → USE EXISTING
│  └─ Need product-on-background composite → edit_asset()
│
└─ Custom background/texture/lifestyle → generate_asset()
```

**Rule: Always `search_design_library` first.** Only generate when library has nothing suitable.

---

## Pipeline: Generate → Verify → Use

### Step 1: Generate Image (write your own descriptive prompt)

```
generate_asset({
  prompt: "soft editorial product photography, dewy botanicals with morning light, cream linen backdrop, green and white accent tones, shallow depth of field, natural diffused lighting, 4K commercial quality",
  style: "photography",
  purpose: "hero_bg",
  aspect: "landscape",
  quality: "high",
  brand_colors: ["#2D5016", "#FEFDFB", "#F5F0EB"],
  brand_tone: "clinical yet warm"
})
→ Returns { asset_id, url, width, height }
```

### Step 2: Verify (optional — use view_asset to visually inspect)

```
view_asset(asset_id) → base64 image you can see directly
```

### Step 3: Use URL in HTML

```html
<section class="relative min-h-[70vh]">
  <img src="THE_RETURNED_URL" alt="Hero background" class="absolute inset-0 w-full h-full object-cover" />
  <div class="relative z-10 ...">Content on top</div>
</section>
```

---

## Style Selection Guide

| Brand Tone | `style` param | Notes |
|---|---|---|
| Luxury/Premium | `photography` or `editorial` | High-end studio quality, dramatic lighting |
| Playful/Bold | `illustration` or `3d_render` | Vibrant, stylized, fun |
| Clinical/Minimal | `photography` | Clean, white backgrounds, precise |
| Earthy/Organic | `photography` or `lifestyle` | Natural light, textures, warmth |
| Tech/Modern | `3d_render` or `abstract` | Geometric, gradients, futuristic |
| Fashion | `editorial` | Editorial spreads, high contrast |

---

## Purpose Mapping

| Section Type | `purpose` param | `aspect` | Notes |
|---|---|---|---|
| Hero full-width | `hero_bg` | `landscape` | Wide, dramatic |
| Hero split (image half) | `product_lifestyle` | `portrait` or `square` | Product in context |
| Section background | `section_bg` | `landscape` | Subtle, not distracting |
| Product on background | `product_composite` | `square` | Use edit_asset |
| Card/feature image | `card_bg` | `square` | Small, tight crop |
| Texture/pattern | `texture_fill` | `square` | Tileable, subtle |
| Floating decoration | `decorative_element` | `square` | Transparent PNG |
| Flat lay composition | `product_lifestyle` | `landscape` | Multiple items arranged |

---

## Compositing with edit_asset

### Product on Lifestyle Background

```
// First: generate a background
generate_asset({
  prompt: "Marble countertop with soft morning light, botanical shadows",
  style: "photography",
  purpose: "product_composite",
  aspect: "square"
})
→ bg_url

// Then: composite product onto it
edit_asset({
  source_images: [product_image_url, bg_url],
  prompt: "Place the product bottle centered on the marble surface, natural shadows, studio lighting",
  aspect: "square",
  quality: "high"
})
→ final composited image
```

### Transparent PNG Overlays

```
generate_asset({
  prompt: "Abstract botanical leaf shapes, minimal line art",
  style: "illustration",
  purpose: "decorative_element",
  transparent: true,
  brand_colors: ["#2D5016"]
})
```

Use as decorative overlay:
```html
<img src="TRANSPARENT_URL" class="absolute top-0 right-0 w-32 opacity-20 pointer-events-none" />
```

### Texture Overlay

```
generate_asset({
  prompt: "Subtle paper grain texture, off-white, organic feel",
  style: "texture",
  purpose: "texture_fill",
  aspect: "square",
  quality: "low"
})
```

Use as background:
```html
<section style="background-image: url('TEXTURE_URL'); background-size: 300px; background-repeat: repeat;">
```

Wait — **no external URLs in CSS `url()`**. Use inline style on an element instead:

```html
<div class="absolute inset-0 opacity-5" style="background-image: url('TEXTURE_URL'); background-size: 300px; background-repeat: repeat;"></div>
```

---

## Placing Images in HTML

### Hero Background

```html
<section class="relative min-h-[70vh] flex items-center overflow-hidden">
  <img src="URL" alt="" class="absolute inset-0 w-full h-full object-cover" aria-hidden="true" />
  <div class="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-6">
    <h1 class="text-white text-5xl font-bold">...</h1>
  </div>
</section>
```

### Product Image (contained)

```html
<div class="aspect-square rounded-2xl overflow-hidden" style="background:var(--lx-bg-surface)">
  <img src="URL" alt="Product Name" class="w-full h-full object-contain p-8" />
</div>
```

### Card with Image

```html
<div class="rounded-xl overflow-hidden shadow-sm border" style="border-color:var(--lx-border-color)">
  <img src="URL" alt="..." class="w-full aspect-[4/3] object-cover" />
  <div class="p-5">
    <h3 class="font-semibold">Card Title</h3>
  </div>
</div>
```

### Background with Overlay

```html
<section class="relative py-20">
  <img src="URL" alt="" class="absolute inset-0 w-full h-full object-cover opacity-20" aria-hidden="true" />
  <div class="relative z-10 max-w-4xl mx-auto text-center px-6">
    Content on top of subtle background
  </div>
</section>
```

---

## Cost Control

| Quality | Cost | Use for |
|---|---|---|
| `low` | Cheap | Textures, patterns, decorative elements |
| `medium` | Moderate | Card images, section backgrounds, secondary visuals |
| `high` | Expensive | Hero images, primary product shots, key visuals |

**Budget per page type:**
- PDP: 1 high (hero) + 1-2 medium (lifestyle) = 2-3 assets
- Landing: 1 high (hero) + 2-3 medium (section bgs) = 3-4 assets
- Homepage: 1 high (hero) + 1 medium (brand story) = 2 assets
- Collection: 0-1 medium (header) — products have their own images

---

## Common Prompt Patterns

### Hero Backgrounds
- "Soft gradient background with subtle botanical shadows, [brand_color] tones, editorial feel"
- "Abstract geometric shapes with smooth gradient, modern minimal, [brand_colors]"
- "Lifestyle flat lay with [product_category] items, overhead shot, clean styling"

### Section Backgrounds
- "Subtle watercolor wash, [brand_color] tint, very light opacity"
- "Clean linen texture, off-white, natural fiber detail"
- "Soft bokeh light circles on dark background"

### Product Composites
- "Product on [surface], natural window light, soft shadows"
- "Hands holding product, [skin_tone], clean background"
- "Product arranged with [complementary items], editorial styling"

### Decorative Elements
- "Minimal line art [motif], single stroke, [brand_color]"
- "Abstract blob shape, organic form, [brand_color], transparent background"
- "Small icon illustration of [concept], flat design, [brand_color]"

---

## Anti-Patterns

1. **Don't generate when library has it** — waste of cost and time
2. **Don't use `url()` in section CSS** — blocked by validator. Use `<img>` or inline `style` attribute
3. **Don't generate product shots** — always use real product images from `list_products`
4. **Don't over-generate** — 2-4 assets per page max. Use CSS gradients/colors for the rest
5. **Don't use `quality: "high"` for everything** — reserve for hero/primary images only
6. **Don't forget alt text** — decorative images get `alt="" aria-hidden="true"`, meaningful ones get descriptive alt


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

# WORKFLOWS

## page-generation

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

### Capture Inspiration
```
capture_design_source({ url: "https://competitor.com" })
```
Screenshots + extracts design DNA (colors, fonts, layout style).

### List Captured References
```
list_design_sources()
```

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
- If no store exists, call `provision_store` first
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


