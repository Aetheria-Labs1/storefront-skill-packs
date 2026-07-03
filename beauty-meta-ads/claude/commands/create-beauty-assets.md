---
description: Generate brand-matched visual assets for a beauty storefront
allowed-tools: mcp__lexsis-ai__*
---

# /create-beauty-assets

Generate brand-matched visual assets for a beauty storefront

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

### beauty-expertise

# Beauty & Skincare — Storefront Design Intelligence
> When to load: Product vertical is beauty, skincare, haircare, body care, fragrance, or cosmetics.
## Philosophy
Beauty pages sell transformation, not product. Every section answers "what will I become?" not "what is this thing?"
## Section Sequences (by page type)
### PDP (Single Product)
## Island Combinations
### IngredientExplorer + BeforeAfter = The Beauty Conversion Stack
## Typography & Color
### Headline Styles
## Hero Patterns
### Editorial Split Hero (Beauty)
## Ingredient Section Pattern
```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-xs uppercase tracking-widest mb-3" style="color:var(--lx-accent-color)">
        Active Ingredients
      </p>
      <h2 class="mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
        4 Powerful Actives, One Gentle Formula
      </h2>
      <p class="max-w-2xl mx-auto" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
        Clinically proven concentrations for visible results
      </p>
    </div>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Vitamin C (L-Ascorbic Acid)","percentage":"20%","benefit":"Brightens skin tone, fades hyperpigmentation, boosts collagen production","source":"Derived from citrus fruits, stabilized in anhydrous base"},{"name":"Ferulic Acid","percentage":"0.5%","benefit":"Stabilizes vitamin C, enhances antioxidant protection","source":"Plant-derived from rice bran"},{"name":"Vitamin E (Tocopherol)","percentage":"1%","benefit":"Antioxidant protection, soothes and moisturizes","source":"Natural source tocopherol"},{"name":"Hyaluronic Acid","benefit":"Plumps skin, delivers 72-hour hydration","source":"Low + high molecular weight blend"}]}'></div>
  </div>
</section>
```
## Social Proof for Beauty
### Review Grid with Skin Type Metadata
## Photography & Assets
### What to Search/Generate
## Anti-Patterns (Beauty Killers)
| Anti-Pattern | Why It Kills | Fix |
|---|---|---|
| Generic product-on-white photography | Commodity positioning, no differentiation | Add context (marble, botanicals), show texture, show application |
| "Clean beauty" without specifics | Vague, virtue-signaling, no trust | Specify exclusions (parabens, sulfates) AND why |
| Too many products on one page | Decision paralysis | One hero product per page, cross-sell via carousel at end |
| Scientific jargon without explanation | Alienates non-expert buyers | Translate: "Niacinamide 10%" → "Minimizes pores and evens skin tone" |
| Stock model faces (full face) | Looks like an ad, can't see skin detail | Macro skin shots, hands applying, before/after close-ups |
| Masculine/aggressive typography | Feels urgent = cheap | Light weights (300-400), generous spacing, serif optional |
| Urgency timers on luxury beauty | Scarcity tactics destroy premium positioning | Use social proof numbers instead ("Join 10,000+ others") |
| Ignoring skin type targeting | "Will this work for MY skin?" is question #1 | Tag products with skin types, show filtered reviews |
| No ingredient transparency | Opacity = hiding something | Full ingredient list accessible, hero ingredients called out |
| Before/after in different lighting | Looks manipulated, kills trust instantly | Same lighting, angle, distance; unfiltered; timeline overlay |
| Generic benefits copy | "Hydrates skin" = every product ever | Specific, quantified: "72-hour hydration" "Reduces lines 23% in 4 weeks" |
| No usage instructions | Beauty buyers need to know HOW | Include "How to use": AM/PM? Before/after moisturizer? How much? |
## Complete Page Blueprint
### Premium Vitamin C Serum PDP (VibePage Format)

### visual-craft

# Visual Craft — Typography, Spacing, Color & Polish
Techniques for making vibe-code pages look premium. Load when polishing visual quality.
## Typography Hierarchy
### Fluid Sizing (clamp)
## Spacing Rhythm
### Section Padding
## Color Usage
### Accent Application
## Image Treatment
### Rounded + Shadow (product cards)
## Micro-Interactions
### Button States
## Glass Morphism
```html
<div class="backdrop-blur-md rounded-2xl p-6 border border-white/20" style="background:rgba(255,255,255,0.1)">
  Frosted glass card
</div>
```
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
## Responsive Patterns
### Grid Collapse

## Workflow

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


