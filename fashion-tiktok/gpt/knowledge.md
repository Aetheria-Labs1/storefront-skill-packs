# Fashion — TikTok Ads Landing Pages — Knowledge Base

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

## FASHION-EXPERTISE

# Fashion & Apparel — Storefront Blueprint Design Intelligence

> **When to load**: Product vertical is fashion, clothing, apparel, shoes, accessories, streetwear, athleisure, or basics. Auto-loads via `vibe://skills/vertical-fashion`.

## The Fashion Page Philosophy

Fashion pages sell **aspiration and identity**, not fabric specs. The page IS the lookbook. Every section should answer **"who will I become wearing this?"**

**Design must feel:**
- **Curated** — every element intentional, nothing generic
- **Editorial** — magazine spread quality, not catalog listing
- **Image-forward** — photography carries the narrative, design stays minimal to let imagery breathe

The photography does 80% of the work. Your job is to frame it perfectly and get out of the way.

---

## VibePage Architecture

Fashion pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. NOT JSON schema.

**VibePage structure:**
```json
{
  "head": {
    "title": "...",
    "meta": [...]
  },
  "theme_css": ":root { --lx-accent-color: #000; ... }",
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

**CSS Variables:**
- `var(--lx-accent-color)` — Brand accent
- `var(--lx-text-color)` — Primary text
- `var(--lx-text-muted)` — Secondary text
- `var(--lx-bg-color)` — Page background
- `var(--lx-bg-surface)` — Card/surface background
- `var(--lx-border-color)` — Borders
- `var(--lx-font-heading)` — Heading font family
- `var(--lx-font-body)` — Body font family

**Available Islands:**
- `BuyBox` — Add to cart, variant selection
- `ProductGallery` — Multi-image viewer with zoom
- `VariantSwatches` — Color/size/style selector
- `SizeGuide` — Drawer with measurements
- `ReviewCarousel` — Customer reviews with photos
- `ProductCarousel` — Horizontal product scroller
- `VideoPlayer` — Video embed with controls
- `ImageZoom` — Detail inspection overlay
- `FAQ` — Collapsible Q&A
- `EmailCapture` — Newsletter signup
- `StickyBar` — Floating CTA bar
- `TrustBadgeBar` — Payment/shipping badges

**Tailwind Conventions:**
- All utility classes available
- Responsive: `sm:`, `md:`, `lg:`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`

---

## Section Sequences (by page type)

### Single Product PDP (8-10 sections)

**Editorial approach**: Tell the product story through imagery first, utility second.

```
1. Editorial hero (full-bleed on-model shot)
   WHY: First impression = aspiration. Show product styled on body.

2. ProductGallery island (4-6 angles)
   WHY: Fashion buyers need fit, drape, texture visible. Build confidence.

3. BuyBox + VariantSwatches
   WHY: Conversion moment. Clean, uncluttered.

4. Product details (materials, care, sizing)
   WHY: Utility specs. Keep minimal.

5. Styling grid (outfit compositions)
   WHY: Show versatility. "3 ways to wear it." Drives AOV.

6. ProductCarousel ("Complete the Look")
   WHY: Cross-sell through styling, not generic "related."

7. SizeGuide island (drawer trigger)
   WHY: Reduce returns. Include model measurements.

8. ReviewCarousel (UGC-heavy, customer photos)
   WHY: Social proof. Real people wearing > star ratings.

9. Final CTA (minimal, single action)
   WHY: Final conversion nudge. Keep understated.

10. Newsletter (optional: "Get styling tips")
    WHY: Build community. Fashion wins on relationship.
```

**WHY this order**: Emotion first (hero, gallery, styling), then rational (details, reviews), then convert.

---

### Collection / Drop Page (10-12 sections)

**Lookbook-first storytelling**: This is a campaign, not a product list.

```
1. Campaign hero (full-bleed model shot + drop name)
2. Split editorial (campaign image + manifesto text)
3. Lookbook grid (8-12 tiles, mixed sizes)
4. Featured pieces (asymmetric bento layout)
5. Value props ("Sustainably Made" / "Limited Edition")
6. VideoPlayer (campaign film)
7. Stats (if relevant: "200 pieces only")
8. Social proof (UGC grid)
9. ProductCarousel ("Shop Collection")
10. Newsletter ("Be first for Drop 05")
```

---

### Lookbook / Editorial (6-8 sections)

**Image-heavy, minimal text**: Magazine pacing.

```
1. Full-bleed hero (1-2 word headline)
2. Lookbook grid (12-16 tiles, uniform aspect ratio)
3. Typographic break (pull quote)
4. Editorial split (model + detail)
5. Video (campaign film)
6. Social proof (press mentions)
7. Understated CTA ("View Collection")
```

---

### Sale / Seasonal Campaign (8-10 sections)

**Urgency + editorial quality.**

```
1. Sale hero ("End of Season / Up to 50% Off")
2. Countdown timer (if time-bound)
3. Sale grid (8-12 items, price badges)
4. Featured picks (hero items at deep discounts)
5. Value props ("Free Shipping" / "Easy Returns")
6. Stats ("1,200+ sold this weekend")
7. ProductCarousel ("Selling Fast")
8. Reviews (customer photos)
9. Bold CTA ("Shop Sale")
10. Newsletter ("Be first for next sale")
```

---

## Island HTML Patterns

### ProductGallery + VariantSwatches + SizeGuide Stack

**Full PDP product section:**

```html
<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
      
      <!-- Left: Gallery -->
      <div>
        <div data-island="ProductGallery" data-props='{
          "images": [
            {"url": "/hero-editorial.jpg", "alt": "Model wearing product"},
            {"url": "/front-flat.jpg", "alt": "Front view"},
            {"url": "/back-flat.jpg", "alt": "Back view"},
            {"url": "/detail-texture.jpg", "alt": "Fabric detail"},
            {"url": "/styled-context.jpg", "alt": "Styled with accessories"}
          ],
          "layout": "editorial",
          "zoom": true,
          "aspectRatio": "3:4"
        }'></div>
      </div>

      <!-- Right: BuyBox -->
      <div class="flex flex-col gap-8">
        <div>
          <p class="text-xs uppercase tracking-widest text-gray-500 mb-3">Organic Cotton</p>
          <h1 class="text-4xl sm:text-5xl font-light mb-4" style="font-family: var(--lx-font-heading);">
            The Relaxed Tee
          </h1>
          <p class="text-base text-gray-600 mb-6">Soft, pre-washed, made to last.</p>
          <p class="text-2xl font-semibold mb-8">$48</p>
        </div>

        <!-- Color Swatches -->
        <div>
          <p class="text-sm font-medium mb-3">Color</p>
          <div data-island="VariantSwatches" data-props='{
            "type": "color",
            "display": "swatch",
            "size": "lg",
            "showLabel": true
          }'></div>
        </div>

        <!-- Size Selection -->
        <div>
          <div class="flex items-center justify-between mb-3">
            <p class="text-sm font-medium">Size</p>
            <button class="text-sm underline" onclick="openSizeGuide()">Size Guide</button>
          </div>
          <div data-island="VariantSwatches" data-props='{
            "type": "size",
            "display": "button",
            "size": "md"
          }'></div>
        </div>

        <!-- Add to Cart -->
        <div data-island="BuyBox" data-props='{
          "showPrice": false,
          "showQuantity": true,
          "ctaText": "Add to Bag"
        }'></div>

        <!-- Product Details -->
        <div class="border-t pt-6">
          <details class="group">
            <summary class="flex items-center justify-between cursor-pointer text-sm font-medium mb-2">
              Material
              <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="text-sm text-gray-600 mt-2">100% organic cotton. GOTS certified.</p>
          </details>
        </div>

        <div class="border-t pt-6">
          <details class="group">
            <summary class="flex items-center justify-between cursor-pointer text-sm font-medium mb-2">
              Fit & Care
              <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="text-sm text-gray-600 mt-2">Relaxed fit. True to size. Model is 5'10", wearing M.</p>
            <p class="text-sm text-gray-600 mt-2">Machine wash cold. Hang dry.</p>
          </details>
        </div>
      </div>

    </div>
  </div>

  <!-- Size Guide Drawer Island -->
  <div data-island="SizeGuide" data-props='{
    "measurements": [
      {"size": "XS", "chest": "32-34\"", "waist": "24-26\"", "hip": "34-36\""},
      {"size": "S", "chest": "34-36\"", "waist": "26-28\"", "hip": "36-38\""},
      {"size": "M", "chest": "38-40\"", "waist": "30-32\"", "hip": "40-42\""},
      {"size": "L", "chest": "42-44\"", "waist": "34-36\"", "hip": "44-46\""}
    ],
    "fitDescription": "Relaxed fit. Size down for fitted look.",
    "modelStats": "Model is 5'\''10\" (178cm), wearing size M."
  }'></div>
</section>
```

---

### ProductCarousel for Cross-Sell

**"Complete the Look" carousel:**

```html
<section class="py-16 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-light mb-8" style="font-family: var(--lx-font-heading);">
      Complete the Look
    </h2>
    
    <div data-island="ProductCarousel" data-props='{
      "products": [
        {"id": "prod_123", "title": "Wide Leg Cargo", "price": "$98", "image": "/cargo.jpg"},
        {"id": "prod_124", "title": "Canvas Sneaker", "price": "$68", "image": "/sneaker.jpg"},
        {"id": "prod_125", "title": "Canvas Tote", "price": "$38", "image": "/tote.jpg"}
      ],
      "layout": "scroll",
      "ctaStyle": "quickAdd",
      "showBadges": true
    }'></div>
  </div>
</section>
```

---

### VideoPlayer for Campaign Films

```html
<section class="py-24 bg-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light text-white mb-12 text-center">
      Drop 04 Campaign Film
    </h2>
    
    <div data-island="VideoPlayer" data-props='{
      "url": "/campaign-film-drop-04.mp4",
      "poster": "/campaign-hero.jpg",
      "autoplay": false,
      "muted": true,
      "controls": true,
      "aspectRatio": "16:9"
    }'></div>
  </div>
</section>
```

---

## Typography

**DRAMATIC size contrast = editorial feel.**

### Hero Headlines (Full-Bleed Sections)

```html
<section class="relative h-screen flex items-center justify-center">
  <img src="/hero-editorial.jpg" alt="New Season" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/20"></div>
  
  <div class="relative z-10 text-center text-white px-4">
    <p class="text-xs uppercase tracking-widest mb-4 opacity-80">Spring 2026</p>
    <h1 class="font-light leading-none" 
        style="font-size: clamp(3rem, 8vw, 7.5rem); 
               letter-spacing: -0.02em;
               max-width: 16ch;
               margin: 0 auto;">
      New Season
    </h1>
  </div>
</section>
```

**Key values:**
- Hero: `clamp(3rem, 8vw, 7.5rem)` = 48px–120px
- Font weight: `300` (ultra-light)
- Letter-spacing: `-0.02em` (tight)
- Line height: `1.0` (compact)
- Max-width: `16ch` (forces dramatic line breaks)

---

### Eyebrows (Collection Names, Seasons)

```html
<p class="text-xs uppercase font-medium tracking-widest text-gray-500 mb-3" 
   style="letter-spacing: 0.15em;">
  Spring 2026
</p>
```

**Examples:**
- "SPRING 2026"
- "COLLAB / ARTIST NAME"
- "LIMITED EDITION"

---

### Section Headings

```html
<h2 class="font-normal mb-8" 
    style="font-size: clamp(1.75rem, 4vw, 3rem); 
           letter-spacing: -0.01em;
           font-family: var(--lx-font-heading);">
  Complete the Look
</h2>
```

Keep 2-4 words max. Let products speak.

---

### Body Text (Rare Usage)

```html
<p class="text-base leading-relaxed text-gray-600" 
   style="max-width: 60ch;">
  100% organic cotton. Pre-washed. Made in Portugal.
</p>
```

**Use only for:**
- Materials
- Care instructions
- Fit descriptions

---

## Color & Backgrounds

**Monochrome is king. Black + white + ONE accent.**

### Streetwear (Dark Mode)

```html
<section class="py-24 bg-[#0a0a0a] text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-5xl font-extrabold uppercase mb-8">Drop 04</h2>
    <p class="text-base text-white/70">Limited edition. 200 pieces only.</p>
  </div>
</section>
```

CSS vars:
```css
:root {
  --lx-bg-color: #0a0a0a;
  --lx-text-color: #ffffff;
  --lx-accent-color: #ff6b00;
}
```

---

### Premium Basics (Clean White)

```html
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light text-black mb-8">Essential Tee</h2>
    <p class="text-base text-gray-600">Soft, timeless, made to last.</p>
  </div>
</section>
```

CSS vars:
```css
:root {
  --lx-bg-color: #ffffff;
  --lx-text-color: #0a0a0a;
  --lx-text-muted: rgba(0,0,0,0.6);
}
```

---

### Editorial (High Contrast B&W Photography)

```html
<section class="relative h-screen">
  <img src="/hero-bw.jpg" alt="Editorial" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-b from-black/30 to-black/60"></div>
  
  <div class="relative z-10 h-full flex items-center justify-center text-white">
    <h1 class="text-6xl sm:text-8xl font-light">New Season</h1>
  </div>
</section>
```

---

## Hero Patterns

### Full-Bleed Editorial Hero

```html
<section class="relative h-screen flex items-center">
  <img src="/hero-on-model.jpg" alt="Editorial hero" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/30"></div>
  
  <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
    <div class="max-w-2xl">
      <p class="text-xs uppercase tracking-widest text-white/80 mb-4">Organic Cotton</p>
      <h1 class="text-white font-light leading-none mb-6" 
          style="font-size: clamp(3rem, 8vw, 7rem);">
        The Relaxed Tee
      </h1>
      <p class="text-lg text-white/90 mb-8">Soft, pre-washed, made to last.</p>
      <button class="bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition">
        Shop Now
      </button>
    </div>
  </div>
</section>
```

---

### Split Lookbook Hero

```html
<section class="min-h-screen bg-white">
  <div class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
    
    <!-- Left: Image -->
    <div class="relative h-[60vh] lg:h-screen">
      <img src="/lookbook-split.jpg" alt="Lookbook" class="absolute inset-0 w-full h-full object-cover" />
    </div>

    <!-- Right: Text -->
    <div class="flex items-center justify-center p-8 lg:p-16">
      <div class="max-w-md">
        <p class="text-xs uppercase tracking-widest text-gray-500 mb-4">Spring 2026</p>
        <h1 class="text-5xl sm:text-6xl font-light mb-6">Made for Movement</h1>
        <p class="text-base text-gray-600 mb-8 leading-relaxed">
          Relaxed silhouettes. Premium materials. Designed in Los Angeles for the way you live.
        </p>
        <a href="/collection" class="inline-block border-b-2 border-black text-sm uppercase tracking-wide pb-1 hover:opacity-70 transition">
          Explore Collection
        </a>
      </div>
    </div>

  </div>
</section>
```

---

## Lookbook Grid (Asymmetric)

**Editorial-style asymmetric grid with CSS Grid:**

```html
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-12">3 Ways to Wear It</h2>
    
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Large hero tile (2x2) -->
      <div class="col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-1.jpg" alt="Casual look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
      </div>

      <!-- Medium tile (1x2) -->
      <div class="col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-2.jpg" alt="Layered look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-3.jpg" alt="Dressed up" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-4.jpg" alt="Detail shot" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>
    </div>
  </div>
</section>
```

**Grid size mapping:**
- Large: `col-span-2 row-span-2` (2x2)
- Medium: `col-span-1 row-span-2` (1x2)
- Small: `col-span-1 row-span-1` (1x1)

**Hover effects** (via CSS):
- `group-hover:scale-105` — Zoom
- `group-hover:brightness-110` — Shimmer
- Ken Burns: `transition-transform duration-700`

---

## Social Proof / Reviews

**UGC-first, with customer measurements:**

```html
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-4">What Customers Are Wearing</h2>
    <p class="text-base text-gray-600 mb-12">Real people, real fit feedback.</p>

    <div data-island="ReviewCarousel" data-props='{
      "displayMode": "ugc_gallery",
      "items": [
        {
          "customerName": "Alex M.",
          "customerStats": "5'\''8\", 145lbs, size M",
          "rating": 5,
          "reviewText": "Perfect fit. True to size. Fabric is so soft—ordering more colors.",
          "customerPhoto": "/ugc-customer-1.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size",
          "styleTags": ["casual", "everyday"]
        },
        {
          "customerName": "Sarah J.",
          "customerStats": "5'\''6\", 130lbs, size S",
          "rating": 5,
          "reviewText": "Love the relaxed fit. Great for layering.",
          "customerPhoto": "/ugc-customer-2.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size"
        }
      ],
      "filters": ["sizeRating", "styleTags"],
      "sortBy": "photosFirst"
    }'></div>

    <!-- Size Rating Summary -->
    <div class="mt-12 max-w-md mx-auto">
      <p class="text-sm font-medium mb-4">Fit Rating</p>
      <div class="space-y-2">
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Small</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 10%;"></div>
          </div>
          <span class="text-xs text-gray-600">10%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">True to Size</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 85%;"></div>
          </div>
          <span class="text-xs text-gray-600">85%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Large</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 5%;"></div>
          </div>
          <span class="text-xs text-gray-600">5%</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

**WHY**: Customer body stats + photos = trust. Aggregate fit data reduces returns.

---

## Anti-Patterns (Fashion Page Killers)

### 1. Product-on-white-only (No Lifestyle)
**Bad**: Only flat-lay white-background shots.  
**Fix**: Lead with on-model editorial. Flat-lays secondary.

### 2. Stock Photos
**Bad**: Generic stock models.  
**Fix**: Custom or AI-generated brand-consistent imagery.

### 3. Centered Symmetric Layouts
**Bad**: Every section centered, equal columns.  
**Fix**: Asymmetric grids, off-center text, varied sizes.

### 4. Too Much Text
**Bad**: Long paragraphs explaining product story.  
**Fix**: 1-3 word headlines. Let imagery carry narrative.

### 5. Corporate Typography
**Bad**: Arial, same size everywhere.  
**Fix**: Dramatic size contrast. Ultra-light heroes (300 weight).

### 6. Equal-Column Product Grids
**Bad**: 4-column grid, all same size.  
**Fix**: Asymmetric lookbook grids. Mixed sizes.

### 7. Generic "Shop Now" CTAs
**Bad**: Every CTA says "Shop Now."  
**Fix**: "Shop [Collection]", "Add to Bag", "View Lookbook."

### 8. Ignoring Mobile Aspect Ratios
**Bad**: 16:9 landscape heroes that crop poorly.  
**Fix**: Portrait aspect ratios (3:4, 4:5). Test mobile.

### 9. Size Chart as Afterthought
**Bad**: Size chart buried in footer.  
**Fix**: SizeGuide island link prominent near BuyBox.

### 10. No Model Measurements
**Bad**: Product photos with no fit context.  
**Fix**: Always include: "Model is 5'10", wearing M."

### 11. Overuse of Urgency (Non-Sale)
**Bad**: Countdown timers on regular PDPs.  
**Fix**: Use urgency only for real sales/drops.

### 12. No UGC / Customer Photos
**Bad**: Only professional brand photos in reviews.  
**Fix**: ReviewCarousel with UGC. Prioritize customer photos.

---

## Complete Fashion PDP Blueprint

**Full VibePage JSON for a premium fashion PDP:**

```json
{
  "head": {
    "title": "The Relaxed Tee — Organic Cotton",
    "meta": [
      {"name": "description", "content": "Soft, pre-washed, made to last."}
    ]
  },
  "theme_css": ":root { --lx-accent-color: #0a0a0a; --lx-text-color: #0a0a0a; --lx-text-muted: rgba(0,0,0,0.6); --lx-bg-color: #ffffff; --lx-font-heading: 'Inter', sans-serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative h-screen flex items-center\"><img src=\"/hero-editorial.jpg\" alt=\"The Relaxed Tee\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/20\"></div><div class=\"relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full\"><div class=\"max-w-2xl\"><p class=\"text-xs uppercase tracking-widest text-white/80 mb-4\">Organic Cotton</p><h1 class=\"text-white font-light leading-none mb-6\" style=\"font-size: clamp(3rem, 8vw, 7rem);\">The Relaxed Tee</h1><p class=\"text-lg text-white/90 mb-8\">Soft, pre-washed, made to last.</p><a href=\"#product\" class=\"inline-block bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition\">Shop Now</a></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product",
      "html": "<section class=\"py-16 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><div class=\"grid grid-cols-1 lg:grid-cols-2 gap-12\"><div><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"url\":\"/hero-editorial.jpg\",\"alt\":\"Model wearing product\"},{\"url\":\"/front-flat.jpg\",\"alt\":\"Front view\"},{\"url\":\"/back-flat.jpg\",\"alt\":\"Back view\"},{\"url\":\"/detail-texture.jpg\",\"alt\":\"Fabric detail\"}],\"layout\":\"editorial\",\"zoom\":true,\"aspectRatio\":\"3:4\"}'></div></div><div class=\"flex flex-col gap-8\"><div><p class=\"text-xs uppercase tracking-widest text-gray-500 mb-3\">Organic Cotton</p><h2 class=\"text-4xl sm:text-5xl font-light mb-4\">The Relaxed Tee</h2><p class=\"text-base text-gray-600 mb-6\">Soft, pre-washed, made to last.</p><p class=\"text-2xl font-semibold mb-8\">$48</p></div><div><p class=\"text-sm font-medium mb-3\">Color</p><div data-island=\"VariantSwatches\" data-props='{\"type\":\"color\",\"display\":\"swatch\",\"size\":\"lg\",\"showLabel\":true}'></div></div><div><div class=\"flex items-center justify-between mb-3\"><p class=\"text-sm font-medium\">Size</p><button class=\"text-sm underline\">Size Guide</button></div><div data-island=\"VariantSwatches\" data-props='{\"type\":\"size\",\"display\":\"button\",\"size\":\"md\"}'></div></div><div data-island=\"BuyBox\" data-props='{\"showPrice\":false,\"showQuantity\":true,\"ctaText\":\"Add to Bag\"}'></div><div class=\"border-t pt-6\"><details class=\"group\"><summary class=\"flex items-center justify-between cursor-pointer text-sm font-medium mb-2\">Material<svg class=\"w-5 h-5 transition-transform group-open:rotate-180\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M19 9l-7 7-7-7\"/></svg></summary><p class=\"text-sm text-gray-600 mt-2\">100% organic cotton. GOTS certified.</p></details></div></div></div></div><div data-island=\"SizeGuide\" data-props='{\"measurements\":[{\"size\":\"XS\",\"chest\":\"32-34\\\"\",\"waist\":\"24-26\\\"\",\"hip\":\"34-36\\\"\"},{\"size\":\"S\",\"chest\":\"34-36\\\"\",\"waist\":\"26-28\\\"\",\"hip\":\"36-38\\\"\"}],\"fitDescription\":\"Relaxed fit. Size down for fitted.\",\"modelStats\":\"Model is 5'10\\\" (178cm), wearing M.\"}'></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "styling",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">3 Ways to Wear It</h2><div class=\"grid grid-cols-2 lg:grid-cols-4 gap-4\"><div class=\"col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-1.jpg\" alt=\"Casual\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-2.jpg\" alt=\"Layered\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-1 relative aspect-square overflow-hidden group\"><img src=\"/styled-3.jpg\" alt=\"Dressed up\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-3xl font-light mb-8\">Complete the Look</h2><div data-island=\"ProductCarousel\" data-props='{\"products\":[{\"id\":\"prod_123\",\"title\":\"Wide Leg Cargo\",\"price\":\"$98\",\"image\":\"/cargo.jpg\"},{\"id\":\"prod_124\",\"title\":\"Canvas Sneaker\",\"price\":\"$68\",\"image\":\"/sneaker.jpg\"}],\"layout\":\"scroll\",\"ctaStyle\":\"quickAdd\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">What Customers Are Wearing</h2><div data-island=\"ReviewCarousel\" data-props='{\"displayMode\":\"ugc_gallery\",\"items\":[{\"customerName\":\"Alex M.\",\"customerStats\":\"5'8\\\", 145lbs, size M\",\"rating\":5,\"reviewText\":\"Perfect fit. True to size.\",\"customerPhoto\":\"/ugc-1.jpg\",\"sizeRating\":\"true_to_size\"}],\"sortBy\":\"photosFirst\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center\"><a href=\"#product\" class=\"inline-block bg-black text-white px-12 py-5 text-sm font-medium uppercase tracking-wide hover:bg-gray-800 transition\">Add to Bag</a></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Fashion pages are **editorial, image-forward, minimal**. Photography does 80% of the work.

**Core principles:**
1. **Aspiration first** — hero imagery before specs
2. **Whitespace = luxury** — generous spacing (py-16, py-24)
3. **Dramatic typography** — huge heroes, tiny eyebrows
4. **Monochrome + one accent** — let product color pop
5. **Asymmetric layouts** — editorial ≠ symmetry
6. **Minimal copy** — 1-3 word headlines
7. **UGC > professional reviews** — real customers, real fit
8. **Size guide prominent** — reduce returns, model stats
9. **Lookbook grids** — asymmetric CSS Grid, mixed sizes
10. **Sub-vertical tailoring** — streetwear ≠ basics ≠ athleisure

Use HTML+Tailwind. Inject islands via `data-island`. Use CSS vars for theming. Test on mobile. Let imagery lead.


---

## TIKTOK-TRAFFIC

# TikTok & Short-Form Video → Landing Page — Storefront Design Intelligence

> When to load: Page is being generated for TikTok ad traffic, Instagram Reels traffic, YouTube Shorts traffic, or any short-form video platform.

## Philosophy

**3-second hook or death.** Visitors from TikTok were interrupted mid-scroll. They weren't searching — they were swiping entertainment. Your page has 3 seconds before the back button.

**Speed > explanation. Proof > promises. Action > education.**

**Raw authenticity wins.** UGC screenshots beat professional photography. Short punchy fragments beat polished copy. Casual lowercase beats corporate tone. The page should feel creator-made, not brand-designed.

**Mobile-ONLY reality.** 95%+ mobile traffic. Design for 375px width. Desktop is an afterthought.

## Mobile-Only Reality

**Every decision flows from mobile-first constraints:**

- **Single column everything** — no side-by-side layouts
- **48px+ tap targets** — thumb-zone CTAs within 120px of bottom edge
- **Short viewport sections** — each section = one mobile screen max (~600px vertical)
- **No hover states** — all interactions tap/swipe only
- **Swipeable carousels** — not click-through galleries

**Viewport target:** iPhone SE (375×667px) to iPhone 14 Pro Max (430×932px). Design for the smaller end.

**Tailwind patterns:**
```html
<!-- Full-width mobile tap target -->
<button class="w-full min-h-[56px] px-6 py-4 text-lg font-bold">
  Get Mine — 40% Off
</button>

<!-- Single column layout -->
<div class="flex flex-col gap-6 px-4">
  <!-- All content stacks vertically -->
</div>

<!-- Mobile-first spacing -->
<section class="py-12 px-4 md:py-16 md:px-6">
  <!-- 48px mobile, 64px desktop -->
</section>
```

## Section Sequence (TikTok Formula)

**6-8 sections MAX. Each section = one decision closer to purchase.**

1. **Hero** (3-second hook) — Video, bold claim, or before/after visual
2. **Social proof strip** — Stars + "as seen on TikTok" (immediate validation)
3. **Problem/Solution** — Visual agitation (before/after, lifestyle contrast)
4. **Product showcase** — BuyBox island, simple and fast
5. **Reviews** — UGC-style screenshots, casual testimonials
6. **CTA** — Final push with urgency/scarcity
7. *Optional:* **FAQ** (max 4 questions, expandable)
8. *Optional:* **Newsletter** (only if email-first funnel)

**Why short:** Average TikTok landing page session = 23 seconds. Highest bounce rate of any platform. If they're still scrolling after 6 sections, they're already convinced. More sections = more chances to lose them.

**What to cut:** Feature grids, company story, mission statements, detailed specs, multiple testimonial sections. Every section must directly drive purchase intent.

## Hero Patterns

### Pattern 1: Video-First Hero

**When to use:** Product demo video exists, or ad itself was a video demonstration.

```html
<section class="relative min-h-[70vh] bg-black flex items-center justify-center overflow-hidden">
  <!-- VideoPlayer island (autoplay, muted, loop) -->
  <div data-island="VideoPlayer" 
       data-props='{"src":"VIDEO_URL","autoplay":true,"muted":true,"loop":true,"poster":"POSTER_URL","aspectRatio":"9:16"}'
       class="absolute inset-0 w-full h-full">
  </div>
  
  <!-- Content overlay -->
  <div class="relative z-10 text-center px-4 max-w-md mx-auto">
    <h1 class="text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-white mb-4">
      Watch It Work
    </h1>
    <p class="text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-300 mb-8">
      Real results in 60 seconds
    </p>
    <button class="w-full min-h-[56px] px-8 py-4 bg-[var(--lx-accent-color)] text-white font-bold text-lg rounded-lg">
      Get Mine — 40% Off
    </button>
  </div>
</section>
```

**Video spec:** 15-30s max. Show product in use, not talking heads. Vertical (9:16) or square (1:1). Autoplay, muted, loop.

### Pattern 2: Bold Text Punch

**When to use:** Strong claim, high-contrast offer, no video asset.

```html
<section class="relative min-h-[65vh] bg-gradient-to-br from-purple-600 to-purple-800 flex items-center justify-center px-4 py-16">
  <div class="text-center max-w-md mx-auto">
    <h1 class="text-[clamp(2.5rem,10vw,3.5rem)] font-black tracking-tighter leading-[0.95] text-white mb-6">
      Clearer Skin<br/>In 7 Days
    </h1>
    <p class="text-[clamp(1.125rem,4.5vw,1.25rem)] font-semibold leading-tight text-purple-200 mb-8">
      Or your money back. No questions.
    </p>
    <button class="w-full min-h-[56px] px-8 py-4 bg-white text-purple-700 font-bold text-lg rounded-lg">
      Try It Risk-Free
    </button>
  </div>
</section>
```

**Text rules:** Max 4 words per line. Line breaks (`<br/>`) for emphasis. No sentences — fragments only. Dark background always.

### Pattern 3: Before/After Hero

**When to use:** Transformation product (skincare, fitness, home, fashion).

```html
<section class="relative min-h-[75vh] bg-white flex items-center justify-center px-4 py-12">
  <div class="max-w-lg mx-auto text-center">
    <!-- Eyebrow -->
    <div class="text-sm font-bold tracking-wider uppercase text-purple-600 mb-3">
      Real Customer • 14 Days
    </div>
    
    <!-- Headline -->
    <h1 class="text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold tracking-tight leading-[1.15] text-black mb-8">
      Same Routine.<br/>Different Results.
    </h1>
    
    <!-- BeforeAfter island -->
    <div data-island="BeforeAfter" 
         data-props='{"before":"BEFORE_URL","after":"AFTER_URL","beforeLabel":"BEFORE","afterLabel":"14 DAYS"}'
         class="mb-8 rounded-2xl overflow-hidden">
    </div>
    
    <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg">
      Get Started
    </button>
  </div>
</section>
```

**Image spec:** Same angle, same lighting, clear difference. Labels: "BEFORE" and specific timeframe ("14 DAYS"), not generic "AFTER".

### Pattern 4: UGC Screenshot Hero

**When to use:** Viral review/comment exists, or mimicking TikTok native feel.

```html
<section class="relative min-h-[60vh] bg-neutral-50 flex items-center justify-center px-4 py-12">
  <div class="max-w-md mx-auto text-center">
    <!-- Screenshot mockup -->
    <div class="mb-8 relative">
      <img src="SCREENSHOT_URL" alt="TikTok comment screenshot" class="rounded-2xl shadow-2xl mx-auto max-w-[320px]"/>
    </div>
    
    <!-- Headline (quoted comment) -->
    <h1 class="text-[clamp(1.5rem,6vw,2rem)] font-bold tracking-tight leading-snug text-black italic mb-4">
      "I was skeptical but this actually works? 😭"
    </h1>
    
    <!-- Attribution -->
    <p class="text-[clamp(0.875rem,3.5vw,1rem)] font-medium text-neutral-600 mb-8">
      — @sarah.wellness, 847K views
    </p>
    
    <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg">
      Shop the Viral Product
    </button>
  </div>
</section>
```

**Screenshot aesthetic:** Phone UI chrome visible, Instagram/TikTok comment format, engagement numbers, casual language with emojis.

## Video Integration

**VideoPlayer island placement hierarchy:**

1. **Hero VideoPlayer** — Product in action, autoplay muted
2. **Before/After video** — Time-lapse transformation (15s max)
3. **Review video** — Customer testimonial (vertical selfie format)

**Autoplay rules:** Hero = autoplay. Anywhere else = click-to-play (mobile bandwidth).

**HTML pattern for VideoPlayer island:**

```html
<div class="relative aspect-[9/16] max-w-[375px] mx-auto rounded-2xl overflow-hidden">
  <div data-island="VideoPlayer" 
       data-props='{
         "src": "VIDEO_URL",
         "autoplay": true,
         "muted": true,
         "loop": true,
         "controls": false,
         "poster": "THUMBNAIL_URL",
         "aspectRatio": "9:16"
       }'>
  </div>
</div>
```

**Video types that convert:**

- **Product demo** (15s) — Show use case, result, benefit. No talking.
- **Unboxing reaction** — Authentic excitement. "First impressions" format.
- **Before/After transformation** — Time-lapse or side-by-side.
- **Creator testimonial** — Casual to camera, <30s, specific claim.

**What to avoid:** Corporate explainer videos, founder stories, brand films, anything >45s.

## The TikTok Native Aesthetic

**Raw beats polished.** UGC-style content outperforms studio photography 2-3x for TikTok traffic. Make it feel creator-made.

### Visual Principles

**Colors:**
- Pure white (`#ffffff`) or pure black (`#000000`) backgrounds — no off-whites, no gradients (except in CTAs)
- Bold accent colors — purple-600, pink-500, amber-500, emerald-500
- High contrast always — mobile readability in bright sunlight

**Typography:**
- Bold sans-serif only — Inter, DM Sans, Poppins (weight 700-900)
- No decorative fonts, no serifs, no script
- Large sizes — `clamp(1.75rem, 7vw, 2.5rem)` minimum for headlines
- Tight letter-spacing — `-0.02em` to `-0.04em`

**Content format:**
- Short punchy fragments, not sentences
- Line breaks for emphasis
- Emojis OK in eyebrows and trust indicators
- ALL CAPS for urgency elements (sparingly)

**Imagery:**
- Phone-screenshot quality > professional photography
- Casual lifestyle shots > studio product shots
- Selfie-style reviews > corporate headshots
- UGC videos > brand videos

### Concrete Tailwind Classes (TikTok Aesthetic)

**Headlines (punchy, bold, high-contrast):**
```html
<h2 class="text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-black">
  Transform Your Skin
</h2>
```

**Sublines (supporting, readable, medium weight):**
```html
<p class="text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-600">
  Real results in 7 days
</p>
```

**Eyebrows (category/proof, uppercase, accent color):**
```html
<div class="text-sm font-bold tracking-wider uppercase text-purple-600">
  ✨ As Seen On TikTok
</div>
```

**Review text (casual, quoted, italic):**
```html
<blockquote class="text-[clamp(1rem,4vw,1.125rem)] font-semibold leading-relaxed text-black italic">
  "okay this is actually insane 😭"
</blockquote>
```

## Social Proof (TikTok-Style)

**Format principle:** Make it look screenshotted from TikTok/Instagram comments, not designed by marketing.

### Pattern 1: Screenshot Aesthetic Reviews

```html
<section class="py-12 px-4 bg-white">
  <div class="max-w-md mx-auto">
    <!-- ReviewCarousel island -->
    <div data-island="ReviewCarousel" 
         data-props='{
           "reviews": [
             {"text": "okay i was NOT expecting this to work but here we are 😭", "name": "Sarah M.", "handle": "@sarah.wellness", "rating": 5, "platform": "tiktok"},
             {"text": "why did nobody tell me about this sooner??", "name": "Mike Chen", "handle": "@mikesfitness", "rating": 5, "platform": "instagram"},
             {"text": "literally changed my skin", "name": "Emma", "rating": 5, "platform": "tiktok"}
           ],
           "autoplay": true,
           "interval": 4000
         }'>
    </div>
  </div>
</section>
```

**Copy rules:** Lowercase, casual punctuation, emojis, no formal language. "this actually works" > "I'm very satisfied with this product."

### Pattern 2: Star Rating with Huge Count

```html
<section class="py-8 px-4 bg-neutral-50">
  <div class="max-w-md mx-auto flex flex-col gap-6">
    <!-- Large star rating -->
    <div class="text-center">
      <div class="text-6xl font-black text-black mb-2">4.9</div>
      <div class="text-3xl text-amber-400 mb-2">★★★★★</div>
      <div class="text-sm font-medium text-neutral-600">14,847 reviews</div>
    </div>
    
    <!-- Orders stat -->
    <div class="text-center border-t border-neutral-200 pt-6">
      <div class="text-4xl font-black text-black mb-1">127K+</div>
      <div class="text-base font-semibold text-neutral-800">Orders This Month</div>
      <div class="text-sm text-neutral-500">As seen on TikTok</div>
    </div>
  </div>
</section>
```

**Display format:** Giant numbers, specific counts (not rounded), "As seen on TikTok" badge language.

### Pattern 3: SocialProofPopup Island

```html
<!-- Placed at page level, triggers immediately -->
<div data-island="SocialProofPopup" 
     data-props='{
       "trigger": "immediate",
       "frequency": 8000,
       "messages": [
         "Sarah from Los Angeles just ordered",
         "Mike from Austin just ordered",
         "Jessica from Miami just ordered"
       ],
       "position": "bottom-left"
     }'>
</div>
```

**Timing:** Appears immediately (no scroll delay), every 8-12 seconds. First name + city format. Max 5 words.

## CTA Strategy

**Single CTA, repeated everywhere.** Do not confuse with multiple competing actions. One primary CTA on entire page.

**Button label hierarchy:**
1. **Benefit + urgency:** "Get Mine — 40% Off" (best)
2. **Direct benefit:** "Try It Risk-Free"
3. **Action + scarcity:** "Shop Now — Limited Stock"
4. **Never:** "Learn More", "Explore Collection", "Read Reviews"

**StickyBar appears immediately:**

```html
<!-- Page-level StickyBar island -->
<div data-island="StickyBar" 
     data-props='{
       "trigger": "immediate",
       "position": "bottom",
       "ctaText": "Get 40% Off Today",
       "showPrice": true,
       "showCountdown": false
     }'>
</div>
```

**All CTAs use consistent styling:**

```html
<button class="w-full min-h-[56px] px-8 py-4 bg-[var(--lx-accent-color)] text-white font-bold text-lg rounded-lg shadow-lg active:scale-95 transition-transform">
  Get Mine — 40% Off
</button>
```

**Never use:** Ghost or outline variants for primary CTA. Link variant only for secondary actions ("No thanks").

**Large tap targets:** 56px height minimum, full-width on mobile.

## Urgency (When to Use It)

**TikTok traffic = impulse audience.** They arrived mid-scroll, not mid-search. Urgency triggers work exceptionally well.

### When to Apply Urgency

- **Flash sale traffic:** CountdownTimer + InventoryIndicator
- **Product launch:** InventoryIndicator + SocialProofPopup
- **Viral product:** SocialProofPopup + "trending" language
- **Always-on:** SocialProofPopup only (least aggressive)

### Pattern 1: CountdownTimer (Real Deadline)

```html
<section class="py-12 px-4 bg-white text-center">
  <h2 class="text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-black mb-6">
    40% Off Ends Tonight
  </h2>
  
  <!-- CountdownTimer island -->
  <div data-island="CountdownTimer" 
       data-props='{
         "endTime": "2026-06-28T04:59:59Z",
         "label": "Sale ends in:",
         "style": "compact"
       }'
       class="mb-8">
  </div>
  
  <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg max-w-md mx-auto">
    Shop Now
  </button>
</section>
```

**Placement:** Hero section or immediately after. Must be visible without scrolling.

**Copy tone:** Casual, not corporate. "ends tonight" > "LIMITED TIME OFFER". Lowercase feels authentic.

### Pattern 2: InventoryIndicator

```html
<div data-island="InventoryIndicator" 
     data-props='{
       "currentStock": 12,
       "threshold": 20,
       "message": "Only {{count}} left in stock"
     }'
     class="text-center py-4">
</div>
```

**When it works:** Specific low numbers (8-15). "only 12 left" feels real. "only 197 left" feels fake.

**Placement:** Near BuyBox, before final CTA section.

### Pattern 3: SocialProofPopup (Purchase Notifications)

```html
<div data-island="SocialProofPopup" 
     data-props='{
       "trigger": "immediate",
       "frequency": 10000,
       "messages": [
         "3 people viewing this right now",
         "Sarah just ordered from Miami",
         "12 sold in the last hour"
       ]
     }'>
</div>
```

**Tone:** Casual, specific, believable. First names, cities, recent timeframes (<1 hour).

**Authenticity rule:** If you wouldn't text it to a friend, don't show it as social proof.

## Content Rules

**Maximum lengths:**
- Headline: 5 words (4 ideal)
- Subline: 12 words (8-10 ideal)
- Review quote: 80 characters
- FAQ answer: 40 words
- CTA button: 4 words

**Fragment sentences OK:** "Clearer skin. Faster results." > "Get clearer skin with faster results."

**Line breaks for emphasis:**
```html
<h1>Transform Your Skin<br/>In Just 7 Days</h1>
```
Not: `<h1>Transform Your Skin In Just 7 Days</h1>`

**Emojis:** OK in eyebrows ("✨ As Seen On TikTok"), trust indicators ("⚡ Free Shipping"), casual reviews. NOT in headlines or CTAs.

**Casual > formal:**
- "this actually works" > "clinically proven results"
- "ordered 3 more" > "highly recommend"
- "didn't believe it but wow" > "exceeded expectations"

**Active voice, present tense:** "Get results in 7 days" > "Results can be seen within a week"

### Good vs Bad Examples

**Hero headline (GOOD):**
- "Clearer Skin\nIn 7 Days"
- "The Viral TikTok Blender"
- "10,000 Sold Yesterday"

**Hero headline (BAD):**
- "Discover Our Revolutionary Skincare Solution"
- "Premium Quality You Can Trust"
- "Join Thousands of Happy Customers"

**Subline (GOOD):**
- "Or your money back. No questions."
- "Same routine. Different results."
- "Ships today if you order now."

**Subline (BAD):**
- "We use only the finest ingredients sourced from around the world."
- "Our commitment to quality is unmatched in the industry."

**Review (GOOD):**
- "okay this is actually insane 😭"
- "why did nobody tell me about this??"
- "already ordered 3 more for friends"

**Review (BAD):**
- "I am very satisfied with this purchase and would recommend it to others."
- "Great product, fast shipping, excellent customer service."

**CTA (GOOD):**
- "Get Mine — 40% Off"
- "Try It Risk-Free"
- "Shop Now — Only 12 Left"

**CTA (BAD):**
- "Learn More About Our Products"
- "Explore Our Collection"
- "Add To Cart"

## Anti-Patterns (TikTok Landing Page Killers)

### 1. Long Pages (>8 Sections)

**Why it kills:** TikTok traffic bounces fast. Every section is a chance to lose them. The "tell them everything" approach destroys conversion.

**Fix:** Cut ruthlessly. 6-8 sections max. If a section doesn't directly drive purchase intent, delete it.

### 2. Corporate/Polished Tone

**Why it kills:** Cognitive dissonance. They came from casual UGC, landed on corporate marketing. Feels like bait-and-switch.

**Fix:** Write like a creator, not a brand. Casual language, fragments, lowercase, emojis, authenticity over polish.

### 3. Desktop-First Design

**Why it kills:** 95% mobile traffic. Desktop-optimized layouts look broken, feel slow, require too much scrolling on mobile.

**Fix:** Design for 375px width. Single column. Large touch targets. Test on actual device, not Chrome DevTools.

### 4. Long Copy Anywhere

**Why it kills:** TikTok trained them for 15-second chunks. Paragraphs feel like homework.

**Fix:** Max 12 words per text block. Use line breaks. Replace paragraphs with bullet fragments.

### 5. Multiple Competing CTAs

**Why it kills:** Decision paralysis. "Shop All", "Learn More", "Watch Video", "Read Reviews" — they'll click none.

**Fix:** One CTA, repeated. Same button text throughout entire page.

### 6. No Video

**Why it kills:** They came from video, expect video. Static images feel outdated, less trustworthy.

**Fix:** Video in hero or immediately after. Product demo, before/after, or UGC testimonial. 15-30s max.

### 7. Polished Studio Photography

**Why it kills:** UGC aesthetic wins on TikTok. Professional photos feel like "ads", trigger skepticism.

**Fix:** Casual lifestyle shots. Phone-photo quality. Customer photos over brand photos. Screenshot aesthetic for reviews.

### 8. Formal Testimonials

**Why it kills:** "I am very satisfied" doesn't match how people actually talk. Feels scripted, fake.

**Fix:** Short punchy quotes. Casual language. "this actually works 😭" > "highly recommend this product."

### 9. Gradients/Decorative Elements

**Why it kills:** Visual noise on mobile. Slow-loading. Distracts from content. Feels 2015.

**Fix:** Solid backgrounds. Pure white or pure black. Bold accent colors for CTAs only. Clean, fast, focused.

### 10. Slow-Loading Assets

**Why it kills:** 3-second attention span. If page takes >2s to load, they're gone.

**Fix:** Optimize images (<200KB each). Lazy-load below-fold content. Inline critical CSS. Test on 3G.

### 11. Hiding Price

**Why it kills:** TikTok traffic is comparison-shopping mentally. Hidden price = "click to reveal" friction = bounce.

**Fix:** Show price in hero or immediately after. BuyBox island placement in sections 3-4, not 6-7.

### 12. No Social Proof Above Fold

**Why it kills:** Trust is the barrier. They don't know your brand. Without immediate social proof, they assume it's a scam.

**Fix:** Star rating + count in hero section. "4.9★ from 14,847 reviews" or "127K orders this month" above fold.

## Complete Blueprint

### Full 6-Section TikTok Landing Page (VibePage JSON)

```json
{
  "head": {
    "title": "The Viral TikTok Blender — 40% Off Today",
    "description": "10,000 sold this week. Smooth, quiet, 30 seconds. As seen on TikTok.",
    "og_image": "PRODUCT_IMAGE_URL"
  },
  "theme_css": ":root { --lx-accent-color: #7c3aed; --lx-text-color: #000000; --lx-text-muted: #6b7280; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; --lx-border-color: #e5e7eb; --lx-font-heading: 'Inter', system-ui, sans-serif; --lx-font-body: 'Inter', system-ui, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[70vh] bg-black flex items-center justify-center overflow-hidden\"><div data-island=\"VideoPlayer\" data-props='{\"src\":\"VIDEO_URL\",\"autoplay\":true,\"muted\":true,\"loop\":true,\"poster\":\"POSTER_URL\",\"aspectRatio\":\"9:16\"}' class=\"absolute inset-0 w-full h-full\"></div><div class=\"relative z-10 text-center px-4 max-w-md mx-auto\"><h1 class=\"text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-white mb-4\">The Viral Blender<br/>Everyone's Talking About</h1><p class=\"text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-300 mb-8\">Smooth. Quiet. 30 Seconds.</p><button class=\"w-full min-h-[56px] px-8 py-4 bg-purple-600 text-white font-bold text-lg rounded-lg shadow-lg\">Get 40% Off Today</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "social-proof",
      "html": "<section class=\"py-8 px-4 bg-neutral-50\"><div class=\"max-w-md mx-auto flex flex-col gap-6\"><div class=\"text-center\"><div class=\"text-6xl font-black text-black mb-2\">4.9</div><div class=\"text-3xl text-amber-400 mb-2\">★★★★★</div><div class=\"text-sm font-medium text-neutral-600\">14,847 reviews</div></div><div class=\"text-center border-t border-neutral-200 pt-6\"><div class=\"text-4xl font-black text-black mb-1\">2.4M</div><div class=\"text-base font-semibold text-neutral-800\">TikTok Views</div><div class=\"text-sm text-neutral-500\">This Week</div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "problem-solution",
      "html": "<section class=\"py-12 px-4 bg-white\"><div class=\"max-w-lg mx-auto\"><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-center text-black mb-8\">Smoothies That Actually Taste Good</h2><div class=\"grid grid-cols-2 gap-4\"><div class=\"bg-neutral-100 rounded-2xl p-6 text-center\"><div class=\"text-4xl mb-3\">😵</div><div class=\"font-bold text-neutral-800 mb-2\">Other Blenders</div><div class=\"text-sm text-neutral-600\">Chunky. Loud. Takes Forever.</div></div><div class=\"bg-purple-50 rounded-2xl p-6 text-center border-2 border-purple-600\"><div class=\"text-4xl mb-3\">✨</div><div class=\"font-bold text-black mb-2\">With This</div><div class=\"text-sm text-neutral-800\">Smooth. Quiet. 30 Seconds.</div></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "buybox",
      "html": "<section class=\"py-12 px-4 bg-white\"><div class=\"max-w-md mx-auto\"><div class=\"rounded-2xl overflow-hidden shadow-2xl mb-6\"><img src=\"PRODUCT_IMAGE_URL\" alt=\"Product\" class=\"w-full aspect-square object-cover\"/></div><div data-island=\"BuyBox\" data-props='{\"productId\":\"PRODUCT_ID\",\"price\":79,\"salePrice\":47,\"ctaText\":\"Add To Cart — $47 (Was $79)\"}' class=\"mb-6\"></div><div data-island=\"InventoryIndicator\" data-props='{\"currentStock\":12,\"threshold\":20,\"message\":\"Only {{count}} left in stock\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-12 px-4 bg-neutral-50\"><div class=\"max-w-md mx-auto\"><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-center text-black mb-8\">What People Are Saying</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"text\":\"this changed my mornings honestly\",\"name\":\"Emma\",\"handle\":\"@emmawellness\",\"rating\":5},{\"text\":\"quieter than my old one?? how\",\"name\":\"Tyler\",\"handle\":\"@tylerscooks\",\"rating\":5},{\"text\":\"bought 2 more as gifts\",\"name\":\"Sarah\",\"handle\":\"@sarahfitness\",\"rating\":5}],\"autoplay\":true,\"interval\":4000}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "final-cta",
      "html": "<section class=\"py-12 px-4 bg-purple-600\"><div class=\"max-w-md mx-auto text-center\"><div data-island=\"CountdownTimer\" data-props='{\"endTime\":\"2026-06-28T04:59:59Z\",\"label\":\"Sale ends in:\",\"style\":\"compact\"}' class=\"mb-6\"></div><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-white mb-6\">40% Off Ends Tonight</h2><button class=\"w-full min-h-[56px] px-8 py-4 bg-white text-purple-700 font-bold text-lg rounded-lg shadow-lg\">Get Mine Now</button></div></section>",
      "css": "",
      "js": ""
    }
  ],
  "islands": [
    {
      "type": "StickyBar",
      "props": {
        "trigger": "immediate",
        "position": "bottom",
        "ctaText": "Get 40% Off Today",
        "showPrice": true,
        "showCountdown": false
      }
    },
    {
      "type": "SocialProofPopup",
      "props": {
        "trigger": "immediate",
        "frequency": 8000,
        "messages": [
          "Sarah from Los Angeles just ordered",
          "Mike from Austin just ordered",
          "Jessica from Miami just ordered"
        ],
        "position": "bottom-left"
      }
    }
  ]
}
```

**Why this blueprint works:**

1. **Video hook** matches ad creative (continuity, no jarring transition)
2. **Social proof immediate** (4.9★ + 14K reviews + 2.4M TikTok views above fold)
3. **Problem/solution visual** (before/after in 2-column grid, mobile-friendly)
4. **BuyBox at section 4** (mid-page, after trust established, not buried)
5. **UGC reviews** (casual language, screenshot aesthetic, carousel format)
6. **Urgency at end** (countdown + scarcity for final push, not aggressive until they're convinced)
7. **StickyBar + SocialProofPopup** (page-level islands = CTA always accessible, social proof continuous)

**Total page height:** ~4 mobile screens. Fast scroll. Every section drives purchase intent. No friction.

---

**Final principle:** When in doubt, make it shorter, bolder, more casual. TikTok traffic punishes traditional marketing. The page should feel like it was made by a creator who sold out, not a brand trying to go viral.


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

## ANIMATION-SYSTEM

# Animation System — Vibe-Code Reference

CSS-only and vanilla JS animations for storefront pages. No framer-motion, no React — pure CSS keyframes + IntersectionObserver for scroll triggers.

---

## When to Animate vs Not

**Animate:**
- Hero headline on premium/editorial/bold brands
- Section entrances on scroll (fade-up, slide-in)
- Background gradients on dark/vibrant brands
- Stats/numbers counting up
- Floating decorative elements

**Don't animate:**
- Clinical/minimal brands (medical, simple skincare) → zero or subtle only
- Product images → never animate product shots
- More than 3 animated sections per page → overwhelming
- Text that needs to be read immediately (pricing, CTA copy)

---

## Section CSS: Keyframe Animations

Place in section `css` field. Scoped per section.

### Fade In Up (most common entrance)

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}
```

### Slide In Left/Right

```css
@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-40px); }
  to { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}
.slide-left { animation: slideInLeft 0.7s ease-out forwards; opacity: 0; }
.slide-right { animation: slideInRight 0.7s ease-out forwards; opacity: 0; }
```

### Scale In (cards, badges)

```css
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
.scale-in { animation: scaleIn 0.5s ease-out forwards; opacity: 0; }
```

### Stagger Children

```css
.stagger > * { opacity: 0; animation: fadeInUp 0.5s ease-out forwards; }
.stagger > *:nth-child(1) { animation-delay: 0s; }
.stagger > *:nth-child(2) { animation-delay: 0.1s; }
.stagger > *:nth-child(3) { animation-delay: 0.2s; }
.stagger > *:nth-child(4) { animation-delay: 0.3s; }
.stagger > *:nth-child(5) { animation-delay: 0.4s; }
.stagger > *:nth-child(6) { animation-delay: 0.5s; }
```

---

## Scroll-Triggered Reveal (Section JS)

Use section `js` field. IntersectionObserver fires animation on scroll.

```javascript
(function() {
  var els = document.querySelectorAll('[data-section-id="SECTION_ID"] [data-reveal]');
  if (!els.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  els.forEach(function(el) { observer.observe(el); });
})();
```

Pair with CSS:
```css
[data-reveal] { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-reveal].revealed { opacity: 1; transform: translateY(0); }
[data-reveal]:nth-child(2) { transition-delay: 0.1s; }
[data-reveal]:nth-child(3) { transition-delay: 0.2s; }
```

HTML: `<div data-reveal>Content appears on scroll</div>`

**Important:** Replace `SECTION_ID` with the actual section id in the JS.

---

## Headline Effects (CSS-only)

### Word-by-Word Fade

```css
@keyframes wordFade {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
.headline-word { display: inline-block; opacity: 0; animation: wordFade 0.4s ease-out forwards; }
.headline-word:nth-child(1) { animation-delay: 0.0s; }
.headline-word:nth-child(2) { animation-delay: 0.12s; }
.headline-word:nth-child(3) { animation-delay: 0.24s; }
.headline-word:nth-child(4) { animation-delay: 0.36s; }
.headline-word:nth-child(5) { animation-delay: 0.48s; }
```

HTML: Wrap each word in `<span class="headline-word">Word</span>`

### Text Reveal (clip-path)

```css
@keyframes textReveal {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0% 0 0); }
}
.text-reveal { animation: textReveal 0.8s ease-out forwards; }
```

### Gradient Text Shift

```css
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.gradient-text {
  background: linear-gradient(90deg, var(--lx-accent-color), #8b5cf6, var(--lx-accent-color));
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientShift 4s ease infinite;
}
```

### Underline Draw

```css
@keyframes drawUnderline {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
.highlight-word { position: relative; display: inline-block; }
.highlight-word::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--lx-accent-color);
  transform-origin: left;
  animation: drawUnderline 0.6s ease-out 0.3s forwards;
  transform: scaleX(0);
}
```

---

## Background Animations

### Gradient Shift (hero/CTA backgrounds)

```css
@keyframes bgShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.animated-bg {
  background: linear-gradient(135deg, var(--lx-accent-color), var(--lx-bg-surface), var(--lx-accent-color));
  background-size: 400% 400%;
  animation: bgShift 8s ease infinite;
}
```

### Floating Elements (decorative)

```css
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  33% { transform: translateY(-15px) rotate(3deg); }
  66% { transform: translateY(-8px) rotate(-2deg); }
}
.float-1 { animation: float 6s ease-in-out infinite; }
.float-2 { animation: float 8s ease-in-out infinite; animation-delay: -2s; }
.float-3 { animation: float 7s ease-in-out infinite; animation-delay: -4s; }
```

### Parallax (scroll-based offset)

Section JS:
```javascript
(function() {
  var section = document.querySelector('[data-section-id="SECTION_ID"]');
  var bg = section && section.querySelector('.parallax-bg');
  if (!bg) return;
  function onScroll() {
    var rect = section.getBoundingClientRect();
    var speed = 0.3;
    bg.style.transform = 'translateY(' + (rect.top * speed) + 'px)';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
```

---

## Micro-Interactions (Tailwind transitions)

### Button Hover
```html
<button class="transition-all duration-200 hover:scale-[1.02] hover:shadow-lg active:scale-[0.98]" style="background:var(--lx-accent-color)">
  Shop Now
</button>
```

### Card Hover Lift
```html
<div class="transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">Card</div>
```

### Image Hover Zoom
```html
<div class="overflow-hidden rounded-xl">
  <img class="transition-transform duration-500 hover:scale-110" src="..." />
</div>
```

---

## Brand Tone → Animation Mapping

| Tone | Level | Recommended |
|---|---|---|
| Luxury/Premium | Subtle, slow | Fade-in-up (0.8s), text-reveal, gradient-text |
| Playful/Bold | Energetic | Stagger, scale-in, floating elements, gradient-shift |
| Clinical/Minimal | Near-zero | Simple fade (0.4s) only |
| Editorial | Refined | Word-by-word, slide-left/right, underline-draw |
| Earthy/Organic | Gentle | Slow fade (1s), parallax, float |
| Tech/DTC | Snappy | Fast stagger (0.08s delay), scale-in |

---

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


