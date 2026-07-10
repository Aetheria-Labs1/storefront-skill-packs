---
name: storefront-engine
description: Core orchestrator for Lexsis AI storefront page generation. Routes requests to the correct workflow, manages tool sequencing, and loads reference knowledge on demand. Auto-invoked by commands and agents.
allowed-tools: mcp__lexsis-ai__*
---

# Storefront Engine — Core Orchestrator

This is the routing and orchestration layer for all Lexsis AI storefront operations. It determines the correct workflow based on user input and coordinates tool calls in the optimal sequence.

## How This Works

1. **Commands** (generate, optimize, remix, experiment, cart, publish) invoke this skill automatically
2. **Agents** (cro-analyzer, page-builder) have their own orchestration logic
3. **Reference files** in `reference/` contain deep knowledge — load ONLY what you need

---

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
│  → DESIGN-FIRST FLOW (agent screenshots URL → extracts tokens → uses as theme → generate)
│  → If user says "analyze", "use as reference", "like this" → run /analyze-page first
│  → If user points at a specific component → run /extract-island first
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
├─ Agent screenshots URL               → extracted palette, fonts, spacing, tone
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

## Reference Files

Load these with `Read reference/{name}.md` when you need specific knowledge. Do NOT load all at once.

### Knowledge (domain expertise)
- **generation-protocol.md** — ---
- **cro-research.md** — ---
- **storefront-craft.md** — Load this skill first on any storefront page generation task.
- **workflow-orchestration.md** — Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.
- **conversion-psychology.md** — Map the AIDA framework to section order. Each stage requires specific psychology and placement.
- **visual-craft.md** — Techniques for making vibe-code pages look premium. Load when polishing visual quality.
- **island-patterns.md** — How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using c
- **qa-recipe.md** — 1. **Validate structure** — call `validate_vibe_page` on the generated JSON

### Operational (workflow procedures)
- **page-generation.md** — Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.
- **design-assets.md** — Manage visual assets (search, generate, edit) and brand identity (kit, themes).
- **publishing.md** — Manage page publishing, previews, and lifecycle.
- **page-editing.md** — Edit existing pages using section-level operations.
- **analytics.md** — Access page performance data and manage A/B experiments.
- **generate-pdp.md** — Generate high-converting product detail pages. BuyBox island is REQUIRED. Sticky CTA adds +12% CVR. 
- **generate-landing-page.md** — Generate high-converting post-click landing pages. ZERO navigation (+30% CVR from reduced distractio
- **generate-homepage.md** — Generate brand-first homepages. Navigation-driven, multi-CTA, storytelling-focused. Category grid ad
- **generate-collection.md** — Generate browsable product listing pages. Grid-focused with EditorialProductGrid island. Quick-add b
- **generate-listicle.md** — Generate SEO-optimized long-form listicle and comparison pages (>2000 words) with proper heading hie
- **generate-bundle-page.md** — Generate interactive bundle-builder pages with step-based UX, discount tier visualization, live pric
- **generate-editorial.md** — Generate long-form editorial pages with cinematic visuals, magazine layout patterns, and restrained 
- **ad-to-page.md** — Generate a high-converting landing page from an ad creative with full scent continuity (headline, pa
- **page-redesign.md** — Visually refresh an existing page using performance data to preserve what works and redesign what do
- **competitor-remix.md** — Capture a competitor page, decompose its structure, and rebuild it using the user's own brand identi
- **personalization-variant.md** — Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience s
- **ab-test-variant.md** — Clone an existing page, apply a single focused change based on a clear hypothesis, launch a controll
- **section-library.md** — Insert common section patterns into existing pages — one section at a time, matched to the page's ex
- **cart-composition.md** — Compose a Cart V2 drawer using atomic islands inside a DrawerShell container. Use when store has `ca
- **cart-v2-management.md** — How to read, modify, and validate store-level cart configuration using MCP tools.
