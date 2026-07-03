---
name: page-generation
description: Storefront Page Generation
---

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
