---
description: Optimize a food brand page for subscription conversion — trial offers, frequency selection
allowed-tools: mcp__lexsis-ai__*
---

# /optimize-food-subscription

Optimize a food brand page for subscription conversion — trial offers, frequency selection

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

### food-expertise

# Food & Beverage DTC — Storefront Design Intelligence
> When to load: Product vertical is food, beverages, snacks, meal kits, coffee, tea, specialty food.
## Philosophy
Food pages sell with the SENSES. The visitor should almost taste/smell the product through the screen. Photography is 80% of the conversion. Every section should trigger appetite or curiosity.
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
## Section Sequences
### Single Product (coffee, hot sauce, artisan snack)
## Island Combinations
**The Food DTC Conversion Stack:**
## Typography & Color
### Typography
## Hero Patterns
### Food Photography Hero
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

## Workflow

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


