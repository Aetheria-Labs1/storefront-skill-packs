---
description: Set up an A/B test with a variant page and monitor results
allowed-tools: mcp__lexsis-ai__*
---

# /run-experiment

Set up an A/B test with a variant page and monitor results

## Context

- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.

## Workflow

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


