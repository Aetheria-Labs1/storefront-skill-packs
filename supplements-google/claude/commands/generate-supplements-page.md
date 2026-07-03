---
description: Generate a supplements/wellness landing page with clinical proof and comparison patterns
allowed-tools: mcp__lexsis-ai__*
---

# /generate-supplements-page

Generate a supplements/wellness landing page with clinical proof and comparison patterns

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

### supplements-expertise

# Supplements & Performance DTC — Storefront Design Intelligence
> **When to load:** Product vertical is supplements, vitamins, protein, nootropics, fitness nutrition, biohacking, wellness, performance enhancers, adaptogens, pre-workout, recovery formulas.
## Philosophy
Supplements occupy a unique trust chasm: buyers are both skeptical (burned by false claims) AND impulsive (desperate for results). The page must be simultaneously **clinical authority** and **modern performance brand**.
## Section Sequences
### Single Product (12-14 sections)
1. **Hero** — bold benefit + trust anchor (rating, sold count)
2. **Trust Bar** — certifications, 3rd-party tested, made-in badges
3. **Problem/Solution** — visceral problem state → product as solution
4. **Key Benefits** — 3-4 benefits with icons, clinical language
5. **Ingredient Spotlight** — Tabs island for each active ingredient
6. **Clinical Proof** — stats grid + research references
7. **How It Works** — timeline or process flow
8. **Pricing/Offer** — QuantityBreaks island + SubscriptionToggle
9. **Comparison Table** — CompareTable island vs. competitors
10. **Social Proof** — ReviewCarousel island + SocialProofPopup
11. **FAQ** — FAQ island (dosing, safety, interactions)
12. **Stack Recommendation** — ProductCarousel island for bundles
13. **Guarantee** — risk reversal (60-day refund, money-back)
14. **Final CTA** — StickyBar island with countdown
## Island Combinations
### CompareTable + QuantityBreaks + CountdownTimer
## Typography & Color
### Dark Mode Default
```css
:root {
  --lx-bg-color: #0a0a0a;
  --lx-bg-surface: #0f0f0f;
  --lx-text-color: #ffffff;
  --lx-text-muted: #9ca3af;
  --lx-accent-color: #84cc16; /* electric lime */
  --lx-accent-secondary: #3b82f6; /* blue */
  --lx-border-color: rgba(255,255,255,0.1);
  --lx-font-heading: 'Inter', -apple-system, sans-serif;
  --lx-font-body: 'Inter', -apple-system, sans-serif;
}
```
## Hero Patterns
### Bold Centered Dark Hero
## Clinical Proof Section
```html
<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold text-white mb-12" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Backed by Science</h2>
    <div class="grid md:grid-cols-3 gap-8 mb-12">
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">23%</div>
        <p class="text-white font-semibold mb-2">Increase in Strength</p>
        <p class="text-sm text-gray-400">After 8 weeks (Journal of Strength Research, 2024)</p>
      </div>
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">18%</div>
        <p class="text-white font-semibold mb-2">Longer Endurance</p>
        <p class="text-sm text-gray-400">Before fatigue onset (Sports Medicine Study, 2025)</p>
      </div>
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">94%</div>
        <p class="text-white font-semibold mb-2">Users Report Better Focus</p>
        <p class="text-sm text-gray-400">In our customer survey (n=1,847)</p>
      </div>
    </div>
    <div data-island="Tabs" data-props='{"tabs":[{"label":"Study 1: Strength Gains","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Effects of L-Citrulline Supplementation on Resistance Training Adaptations</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Journal of Strength Research, 2024</p><p class=\"text-gray-300\"><strong>Findings:</strong> Participants supplementing with 5000mg L-Citrulline daily showed a 23% greater increase in 1RM bench press compared to placebo after 8 weeks.</p>"},{"label":"Study 2: Endurance Extension","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Beta-Alanine and Exercise Performance: A Meta-Analysis</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Sports Medicine, 2025</p><p class=\"text-gray-300\"><strong>Findings:</strong> Meta-analysis of 27 studies showed beta-alanine supplementation (2.4-6.4g daily) increased time to exhaustion by 18% in high-intensity exercise.</p>"},{"label":"Study 3: Cognitive Enhancement","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Caffeine and Cognitive Performance During Exercise</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Nutrition Reviews, 2024</p><p class=\"text-gray-300\"><strong>Findings:</strong> 200mg caffeine improved reaction time, focus, and decision-making during prolonged exercise by 12-15% compared to placebo.</p>"}],"variant":"dark"}'></div>
  </div>
</section>
```
## Pricing Section
```html
<section class="py-12 px-4" style="background:#0a0a0a">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold text-white mb-2" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Choose Your Supply</h2>
    <p class="text-center text-gray-400 mb-8">Best value when you stock up</p>
    <div data-island="QuantityBreaks" data-props='{"options":[{"quantity":1,"label":"1 Month Supply (30 servings)","price":59.99,"unit_price":"$1.99/serving","badge":""},{"quantity":3,"label":"3 Month Supply (90 servings)","price":149.97,"unit_price":"$1.66/serving","badge":"Save 16%","recommended":true},{"quantity":6,"label":"6 Month Supply (180 servings)","price":269.94,"unit_price":"$1.49/serving","badge":"Save 25% — Best Deal"}]}'></div>
    <div class="mt-8">
      <div data-island="SubscriptionToggle" data-props='{"one_time_price":59.99,"subscription_price":47.99,"subscription_discount":"20%","subscription_benefits":["Cancel anytime","Free shipping","Priority support","Early access to new products"]}'></div>
    </div>
  </div>
</section>
## Comparison Section
```html
<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-5xl mx-auto">

### google-traffic

# Google Ads & SEO → Landing Page — Storefront Design Intelligence
> **When to load:** Page designed for Google Ads (Search/Shopping/Display) or organic SEO traffic.
## Philosophy
Google traffic arrives with **INTENT**. They searched. They typed keywords. They're already interested — your job is to **answer immediately**.
## Intent-Based Architecture
Google traffic falls into **4 intent categories**. Each requires a different page structure:
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
## Above-the-Fold Rules
**Transactional intent MUST show:**
- Product image (high quality, zoomable)
- Price (actual number, not "learn more")
- Star rating + review count
- Primary CTA ("Add to Cart", not "Learn More")
- Key trust signal (free shipping, guarantee)
## Hero Patterns
### Product+Price Hero (Transactional)
## CompareTable Strategy
**The power island for Google comparison traffic.** When someone searches "X vs Y", they want a table. Give it to them.
## Information Density
Google searchers **want substance**. Unlike social traffic (skim, scroll, bounce), they came to read.
## FAQ as Conversion Tool
FAQ is not an afterthought — it's a **conversion section** for Google traffic.
## Trust Signals
Google searchers are **validation-driven**. They want proof.
## Pricing Display
**NEVER hide the price.** Google searchers came to evaluate — they will bounce if they can't see the price above fold.
## SEO-Ready Structure
Google searchers often came via **organic search** — your page should be SEO-optimized by default.
## Anti-Patterns
**12 Google landing page killers:**
## Complete Blueprints
### Blueprint 1: Transactional Product Page (Omega-3 Example)
## Summary
**Google traffic = intent-driven.** Answer their query immediately, then earn the conversion with evidence.

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


