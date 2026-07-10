---
name: storefront-engine
description: Core orchestrator for Lexsis AI storefront page generation. Routes requests to the correct workflow, manages tool sequencing, and loads reference knowledge on demand. Auto-invoked by commands and agents.
allowed-tools: mcp__lexsis-ai__*
---

# Storefront Engine — Core Orchestrator

This is the routing and orchestration layer for all Lexsis AI storefront operations. It determines the correct workflow based on user input and coordinates tool calls in the optimal sequence.

## How This Works

1. **Commands** (generate, optimize, remix, experiment, cart, publish, analyze-page, extract-island, search-docs) invoke this skill automatically
2. **Agents** (cro-analyzer, page-builder) have their own orchestration logic
3. **Reference files** in `reference/` contain deep knowledge — load ONLY what you need
4. **Island schemas** in `reference/islands/{name}/schema.json` — full prop types, parts, examples, anti-patterns

---

# Workflow Orchestration — Execution Engine

Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.

---

## Phase -1: Page Planning (MANDATORY)

> Do NOT skip this phase. Do NOT proceed to Flow Selection until a plan is approved.
> Skip ONLY if: user is editing an existing page, a CRO_BLUEPRINT is already provided, or user explicitly says "skip planning" / "just build it".

### Step 1 — Assess What's Known

Score the user's input:

| Signal | Check |
|--------|-------|
| Page type (landing, PDP, homepage, collection, editorial, listicle, bundle) | stated? |
| Target audience / persona | described? |
| Products or collection to feature | named? |
| Traffic source (Meta, Google, TikTok, email, organic) | mentioned? |
| Conversion goal (purchase, signup, browse) | clear? |
| Reference URL or ad creative | provided? |
| Tone/style preference | specified? |

- **4+ signals present** → proceed to Step 3 (auto-plan)
- **< 4 signals** → proceed to Step 2 (ask questions)

### Step 2 — Adaptive Discovery

Ask ONLY questions whose answers are missing. Never ask more than 4 at once.

**Tier 1 (always ask if missing):**
1. "What type of page?" (landing / PDP / homepage / collection / editorial)
2. "Who is this for?" (audience: demographics + pain point)
3. "What should visitors do?" (single conversion goal)

**Tier 2 (ask if Tier 1 reveals complexity):**
4. "Where does traffic come from?" (impacts visual density + social proof weight)
5. "Any sections you specifically want?" (hero style, FAQ, comparison table, etc.)
6. "Should this feel bold/energetic or minimal/premium?" (visual approach)
7. "Any animations or scroll effects?" (parallax, reveal-on-scroll, sticky elements)

**Follow-up triggers:**
- Multiple products mentioned → "Which is the hero product? Are others cross-sells or equals?"
- Health/beauty vertical → "Do you have clinical data or certifications to feature?"
- Ad creative provided → "Should the page match the ad's exact style, or just the message?"

### Step 3 — Generate Page Plan

Produce a structured plan covering:

**A. Section Sequence** (ordered list)
For each section:
- Section ID + type (e.g. `hero-split`, `social-proof-bar`, `features-grid`)
- Purpose (what it communicates / why it's here in this position)
- Key content (headline direction, imagery type, specific products)
- Island requirement (if interactive: BuyBox, FAQ, ReviewCarousel, etc.)
- Animation (fade-up, parallax, sticky, reveal, none)

**B. Visual Rhythm**
- Spacing pattern (tight-loose-tight, progressive relaxation, etc.)
- Color temperature flow (hero warm → middle neutral → CTA warm)
- Typography hierarchy (display → heading → body sizes)

**C. Inter-Section Communication**
- Narrative thread (how sections connect logically)
- CTA placement strategy (where and how many)
- Social proof distribution (where trust signals appear and why)
- Scroll incentives (what makes user keep scrolling)

**D. Technical Requirements**
- Islands needed (exact list)
- Custom animations (scroll-triggered reveals, parallax, sticky)
- Asset requirements (hero image, lifestyle shots, textures, icons)

### Step 4 — Present Plan for Approval

Show the plan to the user in this format:

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
3. [problem-solution] — Pain → product as answer (emotional)
   Animation: reveal on scroll
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

Wait for user confirmation. If user suggests changes, update plan and re-present.

### Step 5 — Hand Off to Generation

Once approved, the plan becomes the binding blueprint for all subsequent phases:
- Phase 0 context gathering targets the plan's requirements
- Phase 1 asset generation follows the plan's imagery needs
- Phase 2 HTML generation follows the plan's section sequence EXACTLY
- Section purposes from the plan guide the copywriting
- Animation choices from the plan guide the JS/CSS

---

## Flow Selection (AFTER Phase -1 planning is approved)

> NOTE: The plan from Phase -1 overrides default section sequences below.
> Use the plan's section_sequence, not the generic templates.

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
- **generation-protocol.md** — Page generation rules, constraints, and quality gates
- **cro-research.md** — Conversion rate optimization research and data (2026)
- **storefront-craft.md** — Load FIRST on any page generation task. Core craft principles.
- **workflow-orchestration.md** — Tool sequences, parallelization, flow selection
- **conversion-psychology.md** — AIDA framework → section order mapping
- **visual-craft.md** — Premium visual techniques. Load when polishing quality.
- **island-patterns.md** — How to embed, wrap, and combine React islands in vibe-code HTML
- **premium-patterns.md** — Copy-and-adapt HTML+Tailwind patterns for high-converting sections
- **animation-system.md** — CSS-only + IntersectionObserver animations. No framer-motion.
- **design-enrichment.md** — Using generate_asset, edit_asset, view_asset for custom imagery
- **qa-recipe.md** — Validation, integrity checks, screenshot QA workflow
- **reference-pdp-remix.md** — PDP reference site patterns and adaptation techniques

### Verticals (industry-specific knowledge)
- **vertical-beauty.md** — Beauty/skincare patterns, ingredient displays, routine builders
- **vertical-supplements.md** — Supplements: clinical data, dosage, subscription-first
- **vertical-fashion.md** — Fashion: size guides, lookbooks, "Add to Bag" conventions
- **vertical-food.md** — Food/beverage DTC: flavor profiles, subscription boxes
- **vertical-home.md** — Home goods: room scenes, measurement guides, material specs
- **vertical-luxury.md** — Luxury: editorial restraint, heritage storytelling, exclusivity

### Traffic Sources
- **traffic-source-meta.md** — Meta/Facebook/Instagram ad optimization patterns
- **traffic-source-google.md** — Google Search/Shopping ad optimization
- **traffic-source-tiktok.md** — TikTok ad creative adaptation

### Island Reference
- **islands/_contract.md** — Rules ALL island wrappers must follow (spacing, colors, responsive, data-parts)
- **islands/{name}/schema.json** — Full props, types, variants, examples, parts, anti-patterns (47 islands)
- **islands/{name}/index.md** — Composition rules, file index, quick reference
- **islands/{name}/layouts/*.json** — Pre-built section templates (renderer-compatible)

### Operational (workflow procedures)
- **page-generation.md** — Generate pages using MCP tools
- **design-assets.md** — Manage visual assets and brand identity
- **publishing.md** — Page publishing, previews, lifecycle
- **page-editing.md** — Edit existing pages via section-level operations
- **analytics.md** — Page performance data and A/B experiments
- **generate-pdp.md** — Product detail pages (BuyBox required, sticky CTA +12% CVR)
- **generate-landing-page.md** — Post-click landing pages (zero nav, +30% CVR)
- **generate-homepage.md** — Brand homepages (nav, collections, story)
- **generate-collection.md** — Product grids with EditorialProductGrid + QuickAdd
- **generate-listicle.md** — SEO long-form comparison pages (>2000 words)
- **generate-bundle-page.md** — Bundle builders with BundleBuilder island
- **generate-editorial.md** — Magazine-style shoppable editorial content
- **ad-to-page.md** — Ad creative → message-matched landing page
- **page-redesign.md** — Refresh existing pages preserving what works
- **competitor-remix.md** — Rebuild competitor page with your brand
- **personalization-variant.md** — Per-persona page variants
- **ab-test-variant.md** — Hypothesis-driven A/B test setup
- **section-library.md** — Insert section patterns into existing pages
- **cart-composition.md** — Cart V2 drawer composition (DrawerShell + atomic islands)
- **cart-v2-management.md** — Read/modify/validate cart configuration via MCP
