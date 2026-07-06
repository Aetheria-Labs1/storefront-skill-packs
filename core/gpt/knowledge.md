# Lexsis AI — Core Skills — Knowledge Base

> This document contains expert knowledge for building Shopify landing pages.
> Upload this as a knowledge file in your Custom GPT configuration.

---

---

## GENERATION-PROTOCOL

# Generation Protocol — How Pages Are Built

> This is the canonical reference for how AI agents generate storefront pages using the Lexsis AI MCP. All operational skills reference this protocol.

---

## MCP Workflow (Correct Order)

```
1. get_workspace_details      → workspace ID, plan tier
2. get_connected_stores       → store domain, Shopify data
3. get_brand_kit              → logo, fonts, colors, voice, border radius
4. get_design_md              → brand brief, design philosophy, don'ts
5. [page-type specific tools] → products, navigation, ad creatives, etc.
6. Generate page (two-phase)
7. validate_vibe_page         → structural/safety check
8. publish_vibe_page          → returns preview_url
9. Visual verification        → screenshot and verify
```

Steps 1-4 are ALWAYS run first. They establish context. Steps 5+ vary by skill.

---

## Two-Phase Generation (Fast Iteration Pattern)

### Phase A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind CSS first:
- Focus on layout, visual hierarchy, spacing, typography
- Use placeholder `<div>` elements where islands will go (mark with `data-placeholder="BuyBox"`)
- Write all copy, set all colors via `--lx-*` CSS variables
- Ensure mobile-first responsive design
- Apply shared keyframes for animations (fadeUp, fadeIn, scaleIn, etc.)

This phase is fast to iterate on — pure HTML renders instantly.

### Phase B — Island Mapping

Replace placeholder divs with actual island markers:
```html
<!-- Phase A placeholder -->
<div data-placeholder="BuyBox" class="...">Buy button goes here</div>

<!-- Phase B final -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

Use `get_island_schema({island_name})` resource (`vibe://schema/island/{name}`) to get exact prop shapes.

### Why Two-Phase?
- HTML renders in any browser preview — fast visual feedback
- Island hydration requires the renderer — slower feedback loop
- Separates design decisions from data-wiring decisions
- Easier to iterate on layout without breaking island props

---

## VibePage JSON Structure

```json
{
  "head": {
    "title": "Page Title — Brand Name",
    "fonts": ["https://fonts.googleapis.com/css2?family=..."],
    "use_cart_v2": true
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-font-heading: 'Playfair Display', serif; }",
  "sections": [
    { "id": "hero", "html": "<section>...</section>", "css": "...", "js": "..." }
  ]
}
```

### Rules
- **Tailwind CSS** in HTML class attributes (renderer includes Tailwind CDN)
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css`
- **Islands** via `data-island="Name"` + `data-props='JSON'` attributes
- **Section IDs** must be unique, kebab-case: "hero", "social-proof", "faq"
- **Section JS** is sandboxed — no fetch/XHR/eval/localStorage. Only DOM manipulation + IntersectionObserver
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft, slideInRight, marquee, float, shimmer, wordFade, pulseRing
- **No @import, no external URLs in CSS**, no inline `<style>` or `<script>` tags in HTML

### Available CSS Variables (override in theme_css)
| Variable | Default | Purpose |
|----------|---------|---------|
| `--lx-accent-color` | #5055aa | Primary CTA color |
| `--lx-accent-color-hover` | #4045aa | Hover state |
| `--lx-text-color` | #1a1a2e | Primary text |
| `--lx-text-muted` | #6b7280 | Secondary text |
| `--lx-bg-color` | #ffffff | Page background |
| `--lx-bg-surface` | #ffffff | Card backgrounds |
| `--lx-border-color` | #e5e7eb | Borders/dividers |
| `--lx-font-heading` | system-ui | Heading font |
| `--lx-font-body` | system-ui | Body font |
| `--lx-surface-alt` | #f9fafb | Alternating section bg |
| `--lx-lavender` | #c9b8e8 | Secondary accent |
| `--lx-teal` | #5bc8c0 | Tertiary accent |

---

## Visual Verification (Critical Step)

After `publish_vibe_page` returns a `preview_url`, ALWAYS verify visually.

### For Claude Code (Playwright MCP)

Install: https://playwright.dev/docs/getting-started-mcp

Add to Claude Code MCP config:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Then:
```
1. browser_navigate → preview_url
2. browser_take_screenshot({fullPage: true}) → full page capture
3. Review: layout, spacing, mobile responsiveness, broken images
4. If issues found → update_page_section to fix → re-verify
```

### For Codex (Built-in Browser)

Use the built-in browser tool to open the preview URL and visually inspect.

### For Cursor / Other IDEs

If no browser tool available, instruct user:
- "Preview URL: {url} — open in browser to verify"
- Suggest mobile viewport check (375px width)

### Installation Reference

Playwright MCP docs: https://playwright.dev/docs/getting-started-mcp

### What to Check
- [ ] Hero section visible above fold (no scroll needed for headline + CTA)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loading (not system fallback)
- [ ] Images rendering (not broken placeholders)
- [ ] Mobile layout not broken (stack columns, readable text)
- [ ] Islands hydrated (BuyBox shows product, not empty div)
- [ ] CTA buttons have proper contrast (WCAG AA: 4.5:1 min)
- [ ] No horizontal scroll on mobile
- [ ] Section spacing consistent (not cramped or overly spaced)

---

## Island Integration Reference

Islands are React components that hydrate client-side. They handle interactive commerce functionality.

### How to Embed
```html
<div data-island="IslandName" data-props='{"key": "value"}'></div>
```

### Key Islands by Use Case

| Need | Island | Key Props |
|------|--------|-----------|
| Add to cart | BuyBox | product.title, product.price, product.variants |
| Product images | ProductGallery | images[], layout |
| Cart drawer | DrawerShell | Contains CartLines + CartCheckoutButton |
| Reviews | ReviewCarousel | provider, productId |
| FAQ accordion | FAQ | items[{question, answer}] |
| Email capture | EmailCapture | provider, listId |
| Announcement | AnnouncementBar | message, link, dismissible |
| Navigation | Navbar / SiteHeader | links[], logo |
| Footer | Footer | links[], social[], newsletter |
| Product grid | EditorialProductGrid | products[], columns |
| Trust badges | TrustBadgeBar | badges[{icon, text}] |
| Social proof popup | SocialProofPopup | provider, delay |

### Prop Data Sources
- Product data → `get_product(product_id)` or `list_products`
- Navigation → `get_navigation`
- Reviews → configured in store (no manual data needed)
- Brand tokens → `get_brand_kit`

---

## Deprecated Tools (DO NOT USE)

These tools appeared in older skill versions but are no longer available:

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via onboarding flow, not page generation |
| `get_island_catalog` (tool) | Use resource `vibe://catalog/islands` instead |

---

## Quality Gates (Before Publishing)

1. **validate_vibe_page** — structural validation (required)
2. **check_page_integrity** — archetype-specific rules (recommended)
3. **Visual verification** — browser screenshot (required for final delivery)

If `validate_vibe_page` fails → fix errors → re-validate.
If `check_page_integrity` warns → assess if acceptable → proceed or fix.
If visual check fails → `update_page_section` → re-screenshot.


---

## CRO-RESEARCH

# CRO Research — 2026 Landing Page Best Practices

> Compiled from Baymard Institute, Unbounce, Shopify, CXL, Conversion Rate Experts, Nielsen Norman Group, Littledata, HubSpot, Optimizely, Wordstream, and Awwwards analysis. Data points sourced 2024-2026.

---

## Key Statistics

### Conversion Rate Benchmarks (Shopify, 2023-2026)

| Metric | Average | Top 20% | Top 10% |
|--------|---------|---------|---------|
| All Shopify traffic | 1.4% | >3.2% | >4.7% |
| Mobile | 1.2% | — | >3.9% |
| Desktop | 1.9% | — | >6.5% |
| Food & Beverage | 1.5% | >4.1% | >6.2% |
| Fashion | 1.9% | >4.3% | >6.1% |
| All industries (Wordstream) | 2.35% median | 5.31% | 11.45% |
| Landing page avg (CorePPC 2026) | 3.5%-5.2% | — | — |

**Source: Littledata (2,800 Shopify stores), Wordstream ($3B ad spend analysis)**

### Critical Conversion Multipliers

| Factor | Impact | Source |
|--------|--------|--------|
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Testimonials with real names | +22% CVR | Digital Applied 2026 |
| Autoplay video | -7% CVR | Digital Applied 2026 |
| Personalized CTAs | +202% vs default | HubSpot |
| 1-second page speed improvement | +2% CVR | Walmart |
| Minimizing page distractions | +10% CVR | EmailVendorSelection |
| Email traffic vs paid search | +60% CVR | Unbounce |
| Email traffic vs display ads | +370% CVR | Unbounce |
| Shop Pay at checkout | +5% lower-funnel CVR | Shopify |

### Page Speed Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5-4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200-500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1-0.25 | >0.25 |

- 70% of consumers say page speed influences purchase decisions (Unbounce)
- 50% expect full load in under 2 seconds
- Sites taking >3 seconds lose significant traffic
- 83% of landing page visits are on mobile (Unbounce 2024)
- Mobile = 52% of all website traffic (Statista Q1 2026)

### Cart Abandonment Drivers

| Cause | Percentage |
|-------|-----------|
| Unexpected costs (shipping, tax) | 39% |
| Insufficient payment methods | 10% |
| Shoppers checking return policy first | 93% |
| Easy returns influence purchase | 82% |
| Delivery estimate influences purchase | ~75% |

---

## Hero Section Patterns That Convert

### Pattern 1: Product-in-Action Hero (Highest CVR for DTC)
- Full-bleed product photography showing usage context
- Single benefit-driven headline matching traffic source
- One primary CTA above fold + sticky CTA on scroll
- 12% lift when combining above-fold + sticky CTA

**Optimal hero height**: 420-550px on desktop (Seton.de cut from 850px to 420px: -11% bounce, +19% form fills in 30 days)

### Pattern 2: Split-Hero (Product + Copy)
- 50/50 or 60/40 split: product image left, copy + CTA right
- Works best for supplement, beauty, and food brands
- Allows benefit bullets alongside product visual
- Price anchoring visible without scroll

### Pattern 3: Video Hero (Use With Caution)
- 85% of people convinced to buy after watching video (Wyzowl 2026)
- 38.6% of marketers say video is #1 landing page element
- CRITICAL: Disable autoplay — autoplay loses 7% of conversions
- Use click-to-play with compelling thumbnail
- Keep hero video under 60 seconds

### Pattern 4: Editorial Full-Bleed (Luxury/Fashion)
- Photography dominates 85%+ of viewport
- Minimal text overlay: 2-5 words maximum
- Single understated CTA ("Discover", "Explore")
- Works for brands where aspiration > information
- Awwwards winners (Lemaire, Delvaux, Balmoral) all use this

### Pattern 5: Cinematic Scroll-Snap (High-Ticket Products)
- Full-viewport sections with pagination indicators (01/09)
- Progressive product disclosure through chapters
- Build desire before showing price
- Radian (Awwwards SOTD): hero → video → 7 features → lifestyle → price reveal last

### What to Always Include Above the Fold
1. Clear headline matching the ad/email that drove the click
2. Product visual (static preferred over autoplay video)
3. Primary CTA button in contrasting color
4. One trust signal (star rating, "Free shipping", guarantee)
5. No more than 5 total elements (Dropbox benchmark)

### What Kills Hero Conversion
- Autoplay video (-7%)
- Rotating carousels (banner blindness, decision paralysis)
- Generic stock photography
- Headline that doesn't match traffic source
- CTA below the fold on mobile
- More than one competing CTA in hero zone

---

## Optimal Section Ordering

### High-Converting DTC Product Landing Page (Cold Traffic)

```
1. Hero: Product visual + benefit headline + CTA (above fold)
2. Social proof bar: Star rating + review count + press logos (3-5 logos)
3. Problem/Solution: Pain point → product as solution (2-3 bullet benefits)
4. Product demonstration: Video or image carousel showing usage
5. Features/Benefits grid: 3-6 key differentiators with icons
6. Detailed social proof: 2-3 full testimonials with photos + names
7. Ingredients/Materials: What's in it (transparency builds trust)
8. Comparison: vs competitors or vs doing nothing (subtle)
9. FAQ: 4-6 objection-handling questions near CTA
10. Final CTA: Repeated offer + urgency element + guarantee
```

### High-Converting DTC Product Page (Warm/Retargeting Traffic)

```
1. Hero: Product + price + variant selector + Add to Cart
2. Trust bar: Shipping info + returns + payment badges
3. Reviews section: Star breakdown + filterable reviews
4. Cross-sell: "Customers also bought" (Magnolia Bakery: banana pudding → cupcakes)
5. Final CTA: Sticky add-to-cart on mobile
```

### Supplement/Wellness Landing Page Sequence

```
1. Hero: Before/after or transformation promise + CTA
2. Problem amplification: "If you're experiencing X, Y, Z..."
3. Science/mechanism: How it works (simple diagram)
4. Ingredient spotlight: Key actives with dosages + research citations
5. Clinical proof: Study results, third-party testing badges
6. Testimonials: Transformation stories with timeline
7. Comparison table: vs alternatives (dosage, purity, price per serving)
8. Subscribe & Save offer: Price anchoring with subscription discount
9. Doctor/expert endorsement
10. Guarantee + FAQ + final CTA
```

### Beauty/Skincare Landing Page Sequence

```
1. Hero: Model using product + "As seen in" press logos
2. Before/After gallery: Real results with timeframe
3. Ingredient story: Hero ingredients with source/science
4. Texture/sensory: Close-up product texture shots
5. Routine builder: How it fits in your routine (morning/night)
6. UGC gallery: Real customer photos and reviews
7. Awards/certifications: Clean beauty badges, cruelty-free, etc.
8. Bundle/Kit offer: Value stacking
9. FAQ + CTA
```

### Fashion/Apparel Landing Page Sequence

```
1. Hero: Lifestyle editorial image + collection name
2. Product grid: 2-4 hero products with quick-add
3. Size/fit guide: Model measurements + fabric details
4. Styling inspiration: Editorial lookbook grid
5. Social proof: UGC gallery from real customers
6. Brand story: Sustainability/craftsmanship narrative
7. Related collections: Cross-selling categories
```

### Evidence-Based Ordering Rules

- Place benefits before features for cold traffic (Shopify 2026)
- Social proof most effective when placed after claims that raise skepticism
- FAQ performs best immediately before the final CTA (objection handling)
- Price reveal after value establishment converts better for high-ticket items
- First two paragraphs/sections receive the most eye fixations (NNGroup F-pattern)
- First and last items in any sequence are best remembered (Serial Position Effect)

---

## Niche-Specific Insights

### Beauty/Skincare

**Conversion drivers:**
- Before/After UGC increases purchase intent by 54% (Nosto)
- Ingredient transparency is table stakes — 63% research ingredients before buying
- "Clean beauty" certifications (EWG verified, cruelty-free, vegan) function as trust badges
- Texture close-ups reduce returns by setting sensory expectations
- Shade finders/quizzes reduce choice paralysis (Hick's Law application)

**Visual patterns:**
- Soft, warm color palettes (blush, cream, sage)
- Generous whitespace signaling "clean" positioning
- Model diversity in hero imagery
- Ingredient photography (raw botanicals, lab imagery)
- Dewy/luminous product photography with natural lighting

**Section-specific tactics:**
- Routine builder sections ("Your AM/PM ritual") increase AOV through bundling
- "Dermatologist recommended" badge near CTA
- Real customer review photos outperform studio UGC
- Subscription offers ("Never run out") with 10-15% savings

**Anti-patterns:**
- Over-retouched model photos (erodes trust)
- Cluttered ingredient lists without hierarchy
- Missing shade/skin-type guidance

---

### Supplements/Wellness

**Conversion drivers:**
- Third-party testing badges (NSF, USP, ConsumerLab) lift trust significantly
- Clinical study citations with specific numbers ("23% improvement in 8 weeks")
- Dosage transparency per serving
- "Made in USA" / GMP certified badges
- Subscription pricing prominently displayed (supplements are replenishment purchases)

**Visual patterns:**
- Clean, clinical aesthetic with natural accents
- White/green/earth tone palettes
- Ingredient spotlight photography (capsule cross-sections, powder textures)
- Data visualization for study results
- Doctor/practitioner endorsements with credentials

**Section-specific tactics:**
- "How it works" mechanism diagrams (simple 3-step)
- Comparison tables vs competitors (dosage, purity, price-per-day)
- Transformation timelines ("Week 1: ..., Week 4: ..., Week 12: ...")
- Subscribe & save with 15-25% discount anchoring
- Stack/bundle builders increase AOV 30-50%

**Anti-patterns:**
- Unsubstantiated health claims
- Missing supplement facts panel
- No third-party testing mention
- Aggressive countdown timers on health products (erodes trust)

---

### Fashion/Apparel

**Conversion drivers:**
- Size/fit guides reduce returns 20-30%
- On-model photography with diverse body types
- Quick-add-to-cart from grid (Marine Layer pattern: hover → size selector)
- "Complete the look" cross-sells
- Free returns prominently displayed (82% say returns influence purchase)

**Visual patterns (from Awwwards analysis):**
- Editorial lifestyle photography > flat-lay for hero
- Neutral, muted palettes for interface; garments provide color
- Generous whitespace between product cards
- Horizontal scroll carousels for collections
- Two-image product cards (front + hover alternate view)

**Section-specific tactics:**
- Gender segmentation immediately (Marine Layer: "New for Him" / "New for Her")
- Curated "edits" and themed collections create discovery paths
- Best sellers / trending sections leverage social proof
- Aspirational lifestyle section between product grids
- 365-day return policy prominently in header

**Anti-patterns:**
- Single product image per card
- Missing size guide
- No fabric/material information
- Over-saturated product photography that doesn't match reality

---

### Food/Beverage DTC

**Conversion benchmarks:** 1.5% average, top 10% achieve 6.2% (Littledata)

**Conversion drivers:**
- Appetite-appealing photography (warm lighting, steam, texture close-ups)
- Subscription-first pricing for consumables
- Sampling/trial offers lower barrier to entry
- Recipe integration showing usage contexts
- "Shipped fresh" / cold-chain messaging
- Bundle builders with mix-and-match flavors

**Visual patterns (from Awwwards - Bucks Sauce, Crav Burgers):**
- Bold, high-energy color palettes matching product (reds, yellows, warm tones)
- Playful typography with personality (chunky display fonts)
- Animated/interactive product reveals
- Developer Award winners suggest technical innovation sells food online
- Product personality > minimalism in food

**Section-specific tactics:**
- Flavor/variant selector with taste descriptions
- "How to use" recipe gallery
- Freshness/sourcing story (farm, roast date, batch number)
- Subscription discount (15-20% off) with skip/pause messaging
- Gift bundles for AOV boost

**Anti-patterns:**
- Cold/clinical photography for food
- Missing nutritional/ingredient info
- No portion/serving context
- Overly minimal design that doesn't convey flavor

---

### Home Goods

**Conversion drivers:**
- Room scene photography showing products in context
- Dimension/measurement details prominently placed
- Material/care information reduces returns
- "Free shipping over $X" threshold (incentivizes cart building)
- AR/3D product viewers for furniture

**Visual patterns:**
- Warm, lifestyle photography in aspirational interiors
- Neutral, earthy color palettes (the products ARE the visual interest)
- Large product images with zoom capability
- Grid layouts with consistent aspect ratios

**Section-specific tactics:**
- "Shop the room" shoppable lifestyle images
- Collections by room (Kitchen, Bedroom, Living Room)
- Gift registry / wishlist prominent
- Care instructions reduce post-purchase anxiety
- "Pairs well with" cross-sells

**Anti-patterns:**
- Products on plain white background without context
- Missing dimensions or scale reference
- No material/texture close-ups
- Stock-feeling lifestyle photography

---

### Luxury

**Conversion patterns (from Awwwards - Lemaire, Delvaux, Vero Studio):**

Luxury e-commerce operates by DIFFERENT rules — many standard CRO tactics actively harm luxury conversion:

**What works:**
- Radical restraint: 85%+ viewport is photography or whitespace
- No urgency tactics (countdown timers destroy luxury positioning)
- No discount codes visible on landing pages
- Price revealed late, after desire is built
- Invitation language ("Discover", "Explore") over command language ("Buy Now", "Shop")
- Editorial/lookbook architecture over product grid
- Heritage/craftsmanship storytelling
- 1-2 products per viewport (exclusivity through curation)
- Full-bleed, art-directed photography (separate crops for mobile/desktop)
- Monochrome interface (black, white, cream only)
- Lower-case navigation as anti-corporate signal

**What luxury sites deliberately omit:**
- Star ratings and review counts
- "Bestseller" badges
- "Only X left" scarcity
- Promotional banners
- Trust badges (the brand IS the trust)
- Aggressive CTAs with filled buttons
- Product grids with 4+ columns
- Price comparison or strikethrough pricing
- Newsletter popups

**Section-specific tactics:**
- Boutique appointment booking (Delvaux)
- Made-to-order / commission flows (Vero Studio)
- Heritage dates ("Since 1829") as credibility signals
- Geographic coordinates as mystique builders (Radian)
- Store locator as architectural storytelling
- Low-barrier reserve ("Reserve for $99" on $14,450 item)

**Anti-patterns for luxury:**
- Using discount codes or sale language
- Cluttered product grids
- Generic CTAs ("Add to Cart" vs "Reserve" or "Inquire")
- Stock photography
- Too much text/information density
- Standard e-commerce templates (Shopify default themes)

---

## Trust & Social Proof Placement

### Placement Hierarchy (By Impact)

1. **Immediately below hero** (star rating + review count + "X customers served")
   - Captures attention at highest-engagement moment
   - 91% of shoppers read at least one review before purchasing

2. **Next to price/CTA** (trust badges, guarantees, shipping info)
   - Reduces friction at the decision point
   - 93% review return policy before buying

3. **After key claims** (testimonials supporting specific benefits)
   - Place social proof directly after any claim that raises skepticism
   - "Think of it like seasoning: enough to convince without overpowering" (HubSpot)

4. **Near final CTA** (money-back guarantee, easy cancellation)
   - Reduces commitment anxiety
   - "Cancel anytime, no strings attached" as click-trigger

### Types by Effectiveness

| Type | Conversion Impact | Best Placement |
|------|-------------------|----------------|
| Testimonials with real names + photos | +22% CVR | After hero, before final CTA |
| Star ratings near product info | High trust signal | Hero zone or product card |
| Press logos (3-5 maximum) | Credibility lift | Below hero or in trust bar |
| UGC photos/videos | 54% purchase after seeing | Mid-page gallery |
| Influencer content vs brand content | 63% higher trust | Social proof section |
| Number-based proof ("10,000+ served") | Wisdom of crowd | Hero subtitle or trust bar |
| Verified buyer labels | Combats fake review skepticism | Within review cards |
| Expert endorsements | Category authority | After ingredient/feature sections |
| Case studies/results | B2B and supplements | Mid-page dedicated section |

### Social Proof Anti-Patterns

- Anonymous testimonials ("Jane D., Satisfied Customer") — unconvincing
- Too many logos cluttering the page
- Fake or inflated review counts
- Social proof with no verifiable details
- Reviews without dates (seem stale)
- Testimonials that don't address specific objections

### The 1% Paradox (Optimizely Data)

Optimizely found only a 1% CVR difference between pages with and without social proof. This means:
- Social proof placement matters MORE than presence
- Generic social proof adds minimal value
- Specific, relevant, objection-addressing proof converts
- Quality > quantity

---

## Mobile-First Conversion Patterns

### Critical Mobile Stats
- 83% of landing page visits are mobile (Unbounce 2024)
- Mobile converts at 1.2% vs desktop 1.9% (Shopify average)
- Top 10% mobile achieves 3.9% (still below desktop top 10% at 6.5%)
- The mobile conversion gap represents massive upside opportunity

### Mobile-Specific Layout Rules

**Above the fold (mobile = ~600px viewport):**
- Headline: max 8 words, 28-36px
- Subhead: max 15 words, 16-18px
- CTA button: full-width or near-full-width, min 48px tap target
- One trust signal (star rating or guarantee)
- NO navigation stealing vertical space

**Thumb-zone optimization:**
- Primary CTA in bottom-third of screen (natural thumb reach)
- Sticky bottom CTA bar for long pages
- Swipeable product carousels (not paginated grids)
- Tap targets minimum 44x44px (Apple HIG), ideally 48x48px

**Content hierarchy (mobile scroll):**
- Users scroll 3-4x on mobile vs desktop to see same content
- Front-load value proposition in first 600px
- Collapse long content into expandable accordions
- Use single-column layout exclusively
- Reduce hero image height to ensure CTA visibility

### Mobile Conversion Boosters
- Sticky add-to-cart bar: appears after scrolling past product section
- Apple Pay / Google Pay / Shop Pay buttons (reduces checkout friction)
- One-tap size/variant selection
- Expandable sections for details (keeps page scannable)
- Bottom-sheet modals instead of full-page navigation
- Pull-to-refresh familiar patterns

### Mobile Anti-Patterns
- Pop-ups covering >30% of screen (Google penalty + user frustration)
- Hamburger menus for primary CTAs
- Horizontal scroll for critical content (not discoverable)
- Text smaller than 16px (triggers zoom on iOS)
- Fixed headers taller than 60px (steals viewport)
- Image carousels without swipe indicators

---

## Psychology-Backed Layout Patterns

### Hick's Law (Decision Time vs Options)
**"The time to make a decision increases with the number and complexity of choices."**

Application:
- Limit variant options visible at once (max 5-7 per Miller's Law)
- Use "recommended" badges to guide choice
- Progressive disclosure: show 3 options, expandable to full list
- Single CTA per section (one clear action)
- Reduce navigation options on landing pages (remove main nav)

### Fitts' Law (Target Size & Distance)
**"Time to acquire a target = f(distance, size)"**

Application:
- CTA buttons: minimum 48px height, ideally 56-64px on mobile
- Reduce distance between decision point and action (CTA near price)
- Make primary CTA the largest interactive element on screen
- Group related actions close together
- Infinite-width targets: sticky bottom bars extend to screen edge

### Von Restorff Effect (Isolation Effect)
**"The item that differs from the rest is most likely remembered."**

Application:
- CTA color must contrast sharply with page palette
- Use single accent color ONLY for interactive elements
- "Best Value" or "Most Popular" badge on recommended option
- Break visual rhythm at key decision points
- One hero product among standard grid items

### Serial Position Effect
**"First and last items in a sequence are best remembered."**

Application:
- Place strongest benefit first in feature lists
- Place guarantee/trust signal last before CTA
- In section ordering: strongest social proof at start, guarantee at end
- Navigation: most important links at start and end of menu
- Reviews: show best review first, most recent last

### Goal-Gradient Effect
**"Motivation increases with proximity to goal."**

Application:
- Progress bars in checkout (80% of abandonment is form-related)
- "Almost there!" messaging during sign-up
- Free shipping threshold indicators in cart ("$15 away from free shipping")
- Step indicators in multi-part forms
- Pre-stamp loyalty cards (start at 2/10 not 0/8)

### Zeigarnik Effect
**"People remember interrupted tasks better than completed ones."**

Application:
- Cart abandonment reminders leverage this naturally
- "Your cart is waiting" messaging
- Saved/incomplete wishlists that pull users back
- Profile completion progress bars
- "Pick up where you left off" sections

### Peak-End Rule
**"Experiences judged by peak moment + ending, not average."**

Application:
- Invest in confirmation/thank-you page experience
- Add delight moment after add-to-cart (animation, confetti)
- Order confirmation should feel celebratory
- Unboxing anticipation content post-purchase
- Final page section should feel rewarding

### Aesthetic-Usability Effect
**"Attractive interfaces are perceived as more usable."**

Application:
- Visual polish actually increases tolerance for friction
- Beautiful product photography > functional documentation
- Consistent visual system signals competence
- Users forgive more from aesthetically pleasing pages
- Invest in typography and spacing even on "functional" pages

### Cognitive Load Management

**Miller's Law**: Working memory holds 7 ± 2 items
- Max 5-7 navigation items
- Max 5-7 product options visible at once
- Group features into 3-4 categories max
- Chunk pricing into simple tiers

**Doherty Threshold**: <400ms for interaction response
- Button feedback within 100ms
- Page transitions under 300ms
- Search results within 400ms
- If >400ms, show loading indicator

---

## Micro-Interactions That Convert

### Animation Timing Guidelines (Material Design 3)

| Type | Duration | Easing | Use Case |
|------|----------|--------|----------|
| Micro-feedback (button press) | 50-100ms | ease-out | Tap/click confirmation |
| Simple state change | 100-200ms | ease-in-out | Toggle, checkbox, switch |
| Element enter | 200-300ms | ease-out (decelerate) | Modal appear, dropdown open |
| Element exit | 150-250ms | ease-in (accelerate) | Modal dismiss, close |
| Page transition | 300-500ms | emphasized ease | Route changes, section swaps |
| Complex animation | 500-700ms | spring/bounce | Celebration, reward moments |
| Scroll reveal | 400-600ms | ease-out | Section fade-in on scroll |

### High-Impact Micro-Interactions

**Add-to-Cart Animation:**
- Product image flies to cart icon (300-400ms)
- Cart icon bounces/scales (200ms)
- Cart count increments with number flip
- Builds satisfaction at key conversion moment
- Alternative: slide-in cart drawer with product preview

**Button Hover/Press States:**
- Hover: subtle scale (1.02-1.05) + shadow lift (150ms ease-out)
- Press: scale down (0.97-0.98) + shadow reduce (50ms)
- Loading: spinner or progress indicator within button
- Success: checkmark morph + color shift to green (300ms)

**Scroll-Triggered Reveals:**
- Fade-up: translateY(20-40px) → 0, opacity 0→1, 400-600ms, staggered 100ms per element
- Threshold: trigger when element is 20% in viewport
- Only animate once (don't re-trigger on scroll up)
- Reduce motion for prefers-reduced-motion users

**Product Image Interactions:**
- Hover zoom: scale(1.05) on container, 200ms ease
- Gallery swipe: momentum-based with snap points
- Pinch-to-zoom on mobile
- Parallax depth on scroll (subtle, 5-15px shift)

**Typing/Chat Indicators:**
- Three-dot pulse animation (Your Doctors Online: +3x chat opens, +42% first messages)
- 300ms per dot cycle
- Creates human-like presence

**Price/Discount Reveals:**
- Crossed-out original price animates in first (200ms)
- New price scales in with slight bounce (300ms delay, 250ms duration)
- Savings badge pulses gently on initial reveal

**Progress/Loading States:**
- Skeleton screens > spinners (reduce perceived wait time)
- Shimmer animation: linear gradient sweep at 1.5-2s cycle
- Progress bars with percentage for longer operations
- Optimistic UI: show success state before server confirms

### Micro-Interactions That Hurt Conversion

- Parallax that causes motion sickness (more than 50px displacement)
- Scroll-jacking that hijacks natural scroll behavior
- Auto-playing carousels (users can't control timing)
- Animations that block interaction (>500ms without user input)
- Excessive particle effects or canvas animations (performance hit)
- Loading animations longer than 3 seconds without content hint
- Hover effects that hide content (desktop-only, invisible on mobile)

---

## Award-Winning E-Commerce Design Patterns

### Analysis from Awwwards SOTD Winners (June-July 2026)

#### Radian (SOTD + Developer Award)
**Category:** High-ticket mobility / Electric motorcycle
**Standout pattern:** Cinematic scroll-snap with section pagination (01/09)

- 10-12 sections in linear narrative structure
- Dark-mode-first (near-black background, yellow product accent)
- Parallax depth composition with separated z-axis layers
- Progressive product disclosure: form → function → feeling → price
- Price anchoring placed LAST ("From €14,450 - Reserve for €99")
- No traditional e-commerce elements on homepage
- Video bookends (opening release film + closing pre-order push)
- Geographic coordinates as design elements (mystique)
- Typography: industrial-modern, 60-100px+ headlines
- Macro spacing: 100-200px between sections

**Lesson:** For high-ticket items, build desire through cinematic pacing before revealing price. Reduce commitment with low-barrier reserve.

---

#### Balmoral Running (SOTD + Developer Award)
**Category:** Athletic apparel (premium positioning)
**Standout pattern:** Anti-athletic luxury for sportswear

- 10 sections: Hero → Editorial intro → Category features → Product carousels → About → Utility grid
- Full-bleed lifestyle hero with ultra-minimal text (just "SPRING-SUMMER 26")
- Monochrome interface (black/white); products provide ALL color
- 2-column product layouts (not 4-column grids) signaling exclusivity
- Geographic identity (Montreal) embedded in brand narrative
- Fashion-house seasonal cadence ("SS26") vs continuous drop model
- No urgency, no badges, no countdown timers
- Price display without decimals ($65 CAD, not $65.00)
- Typography: all-caps geometric sans, wide-tracked section headers

**Lesson:** Position athletic brands as quiet luxury through restraint. Fewer products per viewport = higher perceived value. Editorial architecture over catalog architecture.

---

#### Serotoninn (Fashion)
**Category:** Avant-garde fashion (Berlin aesthetic)
**Standout pattern:** Scientific notation as brand design language

- Numbered editorial sections (02., 03., 07.) with intentional gaps
- [Bracket] syntax for CTAs: `[ SEE COLLECTION ]` (terminal/code aesthetic)
- Loading screen with percentage counter builds anticipation
- mix-blend-mode:difference icons adapt to any background
- Paper textures + torn edges (analog meets digital)
- Dual-image product cards (front + hover alternate)
- European price formatting: `538,99_€` (underscore thousands)
- Category mega-menu with item counts: `[ DRESSES ] [ 26 ]`
- "DRAG CLICK" interaction prompts with branded lip icon

**Lesson:** Distinctive typographic/notation systems create memorable brand identity. Mixing clinical precision with emotional fashion storytelling creates tension that engages.

---

#### Lemaire (Fashion Luxury)
**Category:** Quiet luxury fashion
**Standout pattern:** Radical omission as luxury signal

- 7 sections: triptych hero → product spotlight → carousel → store locator → footer
- Three full-width category banners instead of rotating carousel
- Lowercase navigation throughout (anti-hierarchical)
- ZERO persuasion mechanics: no badges, no urgency, no "bestseller" tags
- Single product spotlight on homepage (not grid)
- Store locator as architectural storytelling (full-bleed interior photos per location)
- Mega-menu with inline product thumbnails (browse without leaving nav)
- Image-to-chrome ratio: 85%+ is photography or whitespace
- Price simple: "Regular price 1.090€" (no strikethrough)

**Lesson:** The confidence to NOT sell is itself a luxury signal. Omitting standard e-commerce elements signals exclusivity. The brand trusts the visitor's intentionality.

---

#### Delvaux (Luxury Goods)
**Category:** Heritage luxury leather goods
**Standout pattern:** Digital white-glove boutique experience

- 8-10 sections: Hero campaign → editorial cards → emblematics → craftsmanship → appointment → footer
- Responsive art direction: completely different image crops for mobile vs desktop (not just resizing)
- Zero product cards, prices, or "add to bag" on homepage
- Heritage anchoring: "Since 1829" + "The Oldest Fine Leather Goods House"
- Institutional framing: "Chronicles", "Craft Beyond Borders" (cultural institution, not retailer)
- Gallery-scale imagery at maximum quality (q=100)
- Boutique appointment booking as conversion action (not "add to cart")
- Each section is one-viewport-height (slow, deliberate scroll)

**Lesson:** Heritage luxury translates through institutional tone, art-directed photography, and replacing "shop" language with "discover/explore" invitations.

---

#### Vero Studio (Bespoke / Art)
**Category:** Commission-based art (wedding dress → sculpture)
**Standout pattern:** Gallery > Commerce

- 8 sections: typographic hero → value prop → process triptych → narrative → quote → gallery → poetry → CTA
- No hero image — typography IS the visual (italic word emphasis technique)
- Near-monochrome palette (white/cream/black only)
- Single-product confidence (entire site sells one offering)
- Italic words as consistent "whispered emphasis" voice throughout
- Poetry (Carl Sandburg quote) used as transitional section
- Commission-based CTA, not "Add to Cart"
- Coffee-table-book spacing between sections
- Loading animation (0% counter) as cinematic entrance

**Lesson:** For bespoke/high-value services, narrative structure (problem → solution → process → proof → invitation) outperforms catalog structure. The site itself must embody the craft it sells.

---

#### Marine Layer (Fashion Lifestyle)
**Category:** Established DTC casual fashion
**Standout pattern:** Editorial + transactional hybrid (best of both)

- 8-10 sections with editorial features alternating with shoppable carousels
- Dual-path hero segmentation ("New for Him" / "New for Her")
- Quick-add from grid: hover reveals size selector (reduces clicks to purchase)
- Curated "shops within the shop" (Espresso Edit, Hemp Shop)
- Free shipping threshold in cart drawer ("Spend $75 more...")
- Promotional stacking on product cards ("20% Off Any 3 Tees")
- Horizontal scroll carousels (not paginated grids)
- Announcement bar with free shipping/returns messaging
- 365-day return policy prominently in header
- Video content embedded within editorial sections
- Color swatch visibility on grid cards

**Lesson:** The highest-converting lifestyle fashion sites balance editorial storytelling (building desire) with transactional efficiency (quick-add, threshold messaging, size selectors on hover). Let users shop without leaving the browse experience.

---

#### Matcha Cartel (Food/Beverage)
**Category:** Premium matcha DTC
**Standout pattern:** Access-restricted vault as brand experience

- Passcode-gated entry ("PASSCODE: MC26")
- Multi-timezone display (New York, Tokyo, Rio) = global presence
- Surveillance/terminal typography (all-caps, monospaced)
- Minimal content on landing — treats entry as the experience
- "Cartel" underground narrative reframes wellness as illicit participation
- Dark, high-contrast palette

**Lesson:** For commodity products (matcha, coffee, water), brand world-building and experiential entry create perceived value impossible to achieve through product photography alone.

---

### Common Patterns Across Award Winners

| Pattern | Frequency | Impact |
|---------|-----------|--------|
| Dark/neutral background | 8/10 sites | Lets product be the color |
| Full-bleed photography | 10/10 | Cinematic quality |
| Minimal CTA styling (text links, not buttons) | 7/10 | Confidence over urgency |
| Loading/transition animations | 8/10 | Premium feel |
| Generous whitespace (100-200px sections) | 10/10 | Luxury signal |
| No promotional banners/popups | 9/10 | Anti-noise |
| Editorial copywriting over sales copy | 8/10 | Aspiration over persuasion |
| Video integration | 6/10 | Storytelling depth |
| Progressive disclosure | 7/10 | Reward scroll behavior |
| Geographic/place identity | 5/10 | Brand authenticity |

---

## Anti-Patterns to Avoid

### Conversion Killers (Data-Backed)

| Anti-Pattern | Impact | Source |
|--------------|--------|--------|
| Autoplay video | -7% CVR | Digital Applied |
| Page load >3 seconds | Significant bounce increase | Unbounce |
| Mismatched ad ↔ landing page | Bounce rate skyrockets | Nik Sharma |
| Rotating hero carousels | Banner blindness, reduced engagement | NNGroup |
| Multiple competing CTAs | Decision paralysis (Hick's Law) | General CRO |
| Pop-ups covering >30% mobile screen | Google penalty + user frustration | Google |
| Autoplay audio | Immediate exit | Universal |
| Fake urgency (resetting countdown timers) | Erodes trust permanently | CRO consensus |
| Generic stock photography | Lower trust perception | Unbounce |
| Separate first/last name fields | Extra friction for zero value | Form optimization data |

### UX Anti-Patterns

- **Navigation on landing pages**: Every link is an exit opportunity. Remove main nav.
- **Competing CTAs**: Wishlists, comparison tools, social shares alongside primary CTA dilute conversion.
- **Form validation errors on submit**: Validate inline as user types.
- **Desktop-only hover effects**: Invisible on mobile (52%+ of traffic).
- **Walls of text**: Triggers F-pattern scanning where 80% is skipped.
- **Infinite scroll without context**: Users lose spatial awareness.
- **Exit-intent popups on first visit**: Interrupts before value is established.

### Trust-Destroying Patterns

- **Fake "live" viewer counts** — users can tell
- **Countdown timers that reset on refresh** — destroys all trust
- **"Only 2 left!" on always-available products** — generates long-term distrust
- **Testimonials without verifiable details** — perceived as fabricated
- **Hiding shipping costs until checkout** — #1 abandonment reason (39%)
- **Required account creation** — add guest checkout always
- **CAPTCHA on checkout** — additional friction at worst moment

### Design Anti-Patterns

- **Low contrast CTAs** — button blends into page
- **CTA below the fold on mobile** — 83% of visits are mobile
- **Tiny tap targets** (<44px) — fat-finger frustration
- **Text over busy images without overlay** — illegible
- **Inconsistent button styles** — confuses interaction model
- **Hidden navigation labels** (icon-only) — increases cognitive load
- **Auto-advancing carousels faster than reading speed** — frustrating

---

## Sources

### Research & Data
- Littledata: https://www.littledata.io/average/ecommerce-conversion-rate (2,800 Shopify stores benchmarked)
- Unbounce: https://unbounce.com/landing-page-articles/landing-page-best-practices/
- Shopify Blog: https://www.shopify.com/blog/ecommerce-landing-page
- Wordstream: https://www.wordstream.com/blog/ws/2014/03/17/what-is-a-good-conversion-rate ($3B ad spend analysis)
- Baymard Institute: https://baymard.com/blog (456 UX articles, 200,000+ hours of research)
- Nielsen Norman Group: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
- HubSpot: https://blog.hubspot.com/marketing/landing-page-best-practices
- Optimizely: https://www.optimizely.com/optimization-glossary/landing-page-optimization/
- Conversion Rate Experts: https://conversion-rate-experts.com/cro-agency/ (19 years, 363% lift case studies)
- Crazy Egg: https://www.crazyegg.com/blog/landing-page-optimization/
- Laws of UX: https://lawsofux.com/ (30 UX laws with practical applications)
- web.dev Core Web Vitals: https://web.dev/articles/vitals
- Shopify Social Proof: https://www.shopify.com/blog/social-proof
- Shopify E-commerce Design: https://www.shopify.com/blog/ecommerce-website-design
- InvespCRO: https://www.invespcro.com/blog/landing-page-optimization/

### Case Studies & Statistics Cited
- Digital Applied 2026: +12% sticky CTA, +22% real testimonials, -7% autoplay
- CorePPC 2026: 3.5-5.2% average landing page CVR
- Wyzowl 2026: 85% convinced to buy after video
- Dynamic Yield: 2.69% sitewide average CVR
- Walmart: +2% CVR per 1s speed improvement
- Namuk: +45% CVR after Shopify migration
- Seton.de: -11% bounce, +19% form fills (hero 850→420px)
- Your Doctors Online: +3x chat opens (typing animation)
- BigChange: -2s load time → lower bounce + higher organic CVR
- Thrive Local: +38% engagement, +45% CTR (visual snapshot layout)
- Statista Q1 2026: 52% mobile traffic share
- Nielsen 2016: 80% seek recommendations
- Bizrate Insights: 91% read reviews before buying
- Nosto: 54% purchased after seeing visual UGC
- Route 2026: 93% check return policy, 82% influenced by easy returns
- Narvar 2025: ~75% influenced by delivery date estimate
- HypeAuditor: 30% higher engagement for verified accounts
- Traackr: +111% live shopping, +521% tap-to-shop with influencer codes

### Awwwards Analysis
- https://www.awwwards.com/websites/e-commerce/
- Radian: https://www.rideradian.com (SOTD + Developer Award, Jul 2026)
- Balmoral Running: https://www.balmoralrunning.com (SOTD + Developer Award, Jun 2026)
- Bucks Sauce: https://buckssauce.com (SOTD + Developer Award, Jul 2026)
- Serotoninn: https://serotoninn.com (Nominee)
- Lemaire: https://www.lemaire.fr (AKQA Paris)
- Delvaux: https://delvaux.com (51North)
- Vero Studio: https://verostudio.com (Rodeo studio)
- Marine Layer: https://www.marinelayer.com (Pattern)
- Matcha Cartel: https://matcha-cartel.com (Surd Studio)
- Crav Burgers: https://www.cravburgers.shop (SOTD + Developer Award, Jun 2026)

### Material Design Motion (MD3)
- Duration tokens: Short (50-200ms), Medium (250-400ms), Long (450-700ms)
- Easing: Emphasized (asymmetric), Standard, enter=decelerate, exit=accelerate
- Doherty Threshold: <400ms interaction response

---

## Quick Reference: The Golden Rules

1. **Match message to traffic source** — headline must echo the ad/email that brought them
2. **One page, one goal, one CTA** — repeated at intervals
3. **First 600px (mobile fold) must contain**: headline + product visual + CTA + one trust signal
4. **Page speed: LCP ≤2.5s** — every second costs 2% conversion
5. **Sticky CTA + above-fold CTA** = +12% lift
6. **Real testimonials with names + photos** = +22% lift
7. **Never autoplay video** = saves 7% loss
8. **Social proof after claims** — not randomly placed
9. **FAQ before final CTA** — handle objections at decision point
10. **Mobile-first always** — 83% of visits, design for 375px viewport first
11. **7 ± 2 rule** — max options visible at any decision point
12. **Progressive disclosure** — build desire before revealing price for high-ticket
13. **Personalize CTAs** — +202% over generic
14. **Animation: enter 200-300ms, exit 150-250ms, feedback <100ms**
15. **Luxury is different** — restraint and omission signal premium positioning


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

## QA-RECIPE

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Validate structure** — call `validate_vibe_page` on the generated JSON
2. **Save as draft** — call `publish_vibe_page` with `publish: false`
3. **Check integrity** — call `check_page_integrity` with the page's archetype

## Browser QA (if available)

### Viewports to test:
- Mobile: 390×844 (iPhone 14)
- Desktop: 1440×900

### Check for:
- [ ] No horizontal overflow at any viewport
- [ ] All images load (no broken/gray placeholders)
- [ ] Hero section visible above fold on both viewports
- [ ] Text readable without zooming on mobile
- [ ] Interactive islands respond to clicks (FAQ accordion, BuyBox variant selection)
- [ ] No console errors blocking render

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| FAQ items don't toggle | Missing island hydration script | Ensure page includes island runtime |
| 401 on publish | Using API key auth | Endpoint supports X-API-Key — ensure key is valid |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `publish: true` → live page, edge-cached, visible to shoppers
- Always draft first, QA, then publish


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


## generate-pdp

# Product Detail Page (PDP) Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate high-converting product detail pages. BuyBox island is REQUIRED. Sticky CTA adds +12% CVR. Reviews placement adds +22% CVR. Variant swatches reduce bounce 15%.

## Triggers

"product page", "PDP", "product detail", "product landing", "product showcase"

## CRO-Backed Section Ordering

```
1. Hero (Split)         — product visual + benefit headline + CTA above fold
2. Product Gallery      — swipeable images, zoom on desktop
3. BuyBox + Variants    — price visible without scrolling (CRITICAL)
4. Benefits Grid        — 3-5 benefit cards with icons
5. Ingredients/Specs    — transparency builds trust (63% research ingredients before buying)
6. Reviews              — +22% CVR with real names/photos (place after claims)
7. Related Products     — cross-sell grid (Magnolia Bakery pattern)
8. FAQ                  — objection handling immediately before final CTA
9. Sticky CTA (mobile)  — +12% CVR, appears after scrolling past BuyBox
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details   → workspace ID, plan tier
get_connected_stores    → store domain, Shopify data
get_brand_kit           → logo, fonts, colors, voice, border radius
get_design_md           → brand brief, design philosophy, don'ts
```

Then page-specific:
```
get_product(product_id) → title, variants, images, price, metafields
get_navigation          → navbar/footer links
list_products           → related products for cross-sell
```

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind CSS. Use `data-placeholder` where islands go:

```html
<div data-placeholder="BuyBox" class="min-h-[200px] border border-dashed border-gray-300 rounded-lg p-4">
  Buy panel renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Mobile-first responsive design (375px base)
- Hero height: 420-550px (Seton.de data: -11% bounce, +19% engagement)
- CTA buttons: min 48px height, use `--lx-accent-color`
- Price MUST be visible without scrolling
- Single h1 (product title), h2 per section

## Phase 2B — Island Mapping

Replace placeholders with actual islands. Use `vibe://schema/island/{name}` for prop shapes.

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **BuyBox** (REQUIRED) | Section 3 | `get_product` → variants, price, images |
| ProductGallery | Section 2 | `get_product` → images array |
| VariantSwatches | Section 3 | `get_product` → variant options |
| StickyCart | Section 9 | product title + price |
| ReviewCarousel | Section 6 | provider + productId |
| FAQ | Section 8 | items[{question, answer}] |

```html
<!-- BuyBox (REQUIRED) -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"v1","title":"30ml","price":"$29.99"},{"id":"v2","title":"60ml","price":"$49.99"}],"images":["url1","url2"]}}'></div>

<!-- StickyCart -->
<div data-island="StickyCart" data-props='{"product":{"title":"...","price":"$29.99"},"threshold":600}'></div>
```

## Niche Variants

### Beauty PDP
- Hero: dewy product shot with soft lighting, split-layout
- Ingredients section: hero actives with source/science, EWG/cruelty-free badges
- Before/after UGC gallery (+54% purchase intent — Nosto)
- Routine builder: "Your AM/PM ritual" (increases AOV via bundling)
- Texture close-ups reduce returns by setting sensory expectations

### Supplement PDP
- Clinical data section: study results with specific numbers ("23% improvement in 8 weeks")
- Dosage/serving info prominently displayed
- Third-party testing badges (NSF, USP, ConsumerLab) — significant trust lift
- Transformation timeline: "Week 1... Week 4... Week 12..."
- Subscribe & save with 15-25% discount anchoring
- NO aggressive countdown timers on health products (erodes trust)

### Fashion PDP
- Size guide section with model measurements + fabric details (reduces returns 20-30%)
- Two-image product cards (front + hover alternate view)
- "Complete the look" cross-sell section
- Color variant swatches visible on first viewport
- Free returns messaging prominent (82% say returns influence purchase)

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: BuyBox renders, price visible, variants selectable, mobile layout intact
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL and inspect.
**Other IDEs:** Provide URL: "Preview: {url} — verify at 375px mobile width"

### Verification Checklist
- [ ] BuyBox island hydrates (shows product, not empty div)
- [ ] Price visible without scrolling on mobile
- [ ] Variant selector works (swatches clickable)
- [ ] Sticky CTA appears after scrolling past BuyBox
- [ ] Product images render (not broken placeholders)
- [ ] Brand colors applied via `--lx-accent-color` (not default purple)
- [ ] Mobile: no horizontal scroll, single column stack
- [ ] CTA contrast ratio >= 4.5:1 (WCAG AA)

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Section CSS Pattern

```html
<section id="pdp-hero" class="py-16 md:py-24 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Content with --lx-* variables -->
  </div>
</section>
```

## Conversion Data Reference

| Tactic | Impact | Source |
|--------|--------|--------|
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Real testimonials with names/photos | +22% CVR | Digital Applied 2026 |
| Variant swatches (vs dropdown) | -15% bounce | CXL |
| Size guide presence | -20-30% returns | Baymard |
| Before/after UGC | +54% purchase intent | Nosto |
| Subscribe & save option | +30-50% AOV | Supplement industry avg |
| FAQ before final CTA | Objection handling at decision point | NNGroup |
| Price visible without scroll | Table stakes (abandonment if hidden) | Baymard |


## generate-landing-page

# Campaign / Ad Landing Page Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate high-converting post-click landing pages. ZERO navigation (+30% CVR from reduced distraction). Single CTA repeated 3x minimum. Message-match from ad creative is non-negotiable.

## Triggers

"landing page", "campaign page", "ad landing", "post-click", "LP", "convert ad to page"

## Core Principles (CRO-Backed)

- **ZERO navigation** — every link is an exit. Remove header nav entirely. +30% CVR (EmailVendorSelection)
- **Single CTA repeated 3x** — hero, mid-page offer, bottom (minimum)
- **Message-match** — headline must echo ad within 2 words (mismatch = bounce spike)
- **One page, one goal** — no wishlists, comparisons, social shares alongside primary CTA
- **Hero height: 420-550px** — Seton.de cut 850→420px: -11% bounce, +19% form fills

## CRO Section Ordering (Cold Traffic DTC)

```
1. Hero               — message-match headline + product visual + CTA (above fold)
2. Social Proof Bar   — star rating + review count + press logos (3-5 max)
3. Problem/Solution   — pain points → product as answer (2-3 bullets)
4. Product Demo       — video (click-to-play ONLY, never autoplay: -7% CVR) or carousel
5. Benefits Grid      — 3-6 differentiators with icons, mapped from ad claims
6. Detailed Proof     — 2-3 full testimonials with photos + real names (+22% CVR)
7. Ingredients/How    — transparency section or 3-step "How It Works"
8. Comparison         — vs competitors or vs doing nothing (subtle)
9. FAQ                — 4-6 objection-handling Qs immediately before CTA
10. Final CTA         — restate offer + guarantee + urgency
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details       → workspace ID, plan tier
get_connected_stores        → store domain, Shopify data
get_brand_kit               → logo, fonts, colors, voice, border radius
get_design_md               → brand brief, design philosophy, don'ts
```

Then page-specific:
```
analyze_ad_creative(url)    → extract headline, claims, colors, CTA, tone, product
match_persona_to_ad(...)    → target persona (demographics, pain points, motivations)
get_product(product_id)     → product data for BuyBox island
list_products               → catalog context
```

## Traffic Source Calibration

### Meta (Facebook/Instagram) — Warm, Social Proof Heavy
- Hero matches ad visual exactly (same product angle, lighting, model)
- Shorter copy, more visual storytelling
- Social proof dominant: reviews, UGC, influencer mentions (+63% trust vs brand content)
- Urgency elements: limited stock, time-bound offer
- Before/after transformations (54% purchase after visual UGC — Nosto)

### Google (Search/Shopping) — Intent-Driven, Feature-First
- Hero directly answers search query intent
- Detailed specs, comparison tables, feature lists
- Credibility: certifications, expert endorsements, clinical data
- Structured information layout (scannable, F-pattern aware)
- FAQ section more prominent (searchers have specific questions)

### TikTok — Scroll-Stopping, Video-Native
- Bold visual hero with energy/movement
- Short punchy copy (1-2 lines per section max)
- Creator-style social proof (not corporate testimonials)
- Before/after transformations front and center
- Price reveal after desire built (younger demo more price-sensitive)

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate full page as plain HTML + Tailwind. Mark island positions:

```html
<!-- NO navigation header — logo only, non-clickable -->
<header class="py-4 px-6">
  <img src="..." alt="Brand" class="h-8 mx-auto" />
</header>

<!-- BuyBox placeholder -->
<div data-placeholder="BuyBox" class="min-h-[180px] p-4 border border-dashed rounded-lg">
  Commerce panel renders here
</div>
```

Rules:
- All colors via `--lx-*` variables
- NO `<nav>` elements, NO anchor links in header/footer
- CTA buttons: min 48px height, full-width on mobile, `--lx-accent-color`
- Max-width: 5xl (narrower than PDP — focused reading lane)
- Mobile sticky CTA bar at bottom

## Phase 2B — Island Mapping

Only ONE commerce island needed (BuyBox). Minimal islands = fast page load.

```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$39.99","compareAtPrice":"$59.99","variants":[...],"images":["..."]},"offer":{"discount":"33%","badge":"Limited Time"}}'></div>
```

Use `vibe://schema/island/BuyBox` for exact prop shape.

## Hero Patterns by Niche

### Supplements — Product-in-Action Hero
- Full-bleed product on nightstand/kitchen counter (usage context)
- Benefit headline matching ad: "Finally Sleep Through the Night"
- Single CTA + one trust signal (star rating or "Free shipping")

### Beauty — Split-Hero (Product + Copy)
- 50/50 split: product left (dewy macro shot), copy + CTA right
- "As seen in" press logos beneath hero
- Price anchoring visible without scroll

### Fashion — Video Hero (Click-to-Play)
- Compelling thumbnail (NOT autoplay — saves 7% CVR loss)
- Creator-style try-on video
- Bold 2-5 word headline overlay

## Urgency Tactics: What Works vs. What Backfires

**Works (data-backed):**
- Limited-time offer with real end date (not resetting timer)
- Low stock indicator on genuinely scarce items
- "Free shipping ends tonight" with actual deadline
- Seasonal/launch window messaging

**Backfires (trust-destroying):**
- Countdown timers that reset on refresh — destroys ALL trust permanently
- "Only 2 left!" on always-available products
- Fake "live viewer" counts
- Urgency on health/wellness products (erodes trust in category)

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: no nav links, CTA 3x visible, headline matches ad, mobile layout
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL.
**Other IDEs:** "Preview: {url} — verify no navigation exists, CTA appears 3x"

### Verification Checklist
- [ ] ZERO navigation links (no header nav, no footer nav, logo not clickable)
- [ ] Headline matches ad creative within 2-word difference
- [ ] CTA button appears minimum 3 times (hero, offer, final)
- [ ] All CTA buttons perform same action (single goal)
- [ ] No competing actions (no wishlist, share, compare buttons)
- [ ] Hero above fold with product visual + CTA visible (no scroll needed)
- [ ] Mobile: sticky bottom CTA bar present
- [ ] Brand colors applied via `--lx-accent-color`
- [ ] No autoplay video (click-to-play only)

## Quality Gates

1. `validate_vibe_page` — structural check (REQUIRED)
2. `check_page_integrity` — archetype rules
3. Visual verification — screenshot (REQUIRED)

## Conversion Data Reference

| Tactic | Impact | Source |
|--------|--------|--------|
| Remove navigation | +30% CVR | EmailVendorSelection |
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Real testimonials (names + photos) | +22% CVR | Digital Applied 2026 |
| Personalized CTAs | +202% vs default | HubSpot |
| Autoplay video | -7% CVR (AVOID) | Digital Applied 2026 |
| Message mismatch (ad vs page) | Bounce spikes | Nik Sharma |
| Single CTA focus | +10% CVR | EmailVendorSelection |
| Hero 420-550px height | -11% bounce, +19% fills | Seton.de case study |
| FAQ before final CTA | Objection handling | NNGroup serial position |


## generate-homepage

# Brand Homepage Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate brand-first homepages. Navigation-driven, multi-CTA, storytelling-focused. Category grid adds +18% engagement. Featured products carousel drives discovery. Navbar + Footer islands REQUIRED.

## Triggers

"homepage", "home page", "main page", "front page", "store home"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation (REQUIRED island)
2. Hero                — brand lifestyle visual + value prop CTA
3. Categories Grid     — +18% engagement vs flat product list
4. Bestsellers         — featured products carousel (social proof via "popular")
5. Brand Story         — editorial mid-page (founder, mission, craft)
6. Testimonials        — 3 reviews with real names/photos (+22% CVR)
7. Trust Bar           — press logos + certifications (3-5 max)
8. Newsletter          — email capture with incentive ("10% off first order")
9. Footer              — full nav columns + legal + social (REQUIRED island)
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details   → workspace ID, plan tier
get_connected_stores    → store domain, Shopify data
get_brand_kit           → logo, fonts, colors, voice, brand story
get_design_md           → brand brief, design philosophy, positioning
```

Then page-specific:
```
get_navigation          → header nav links, footer columns, collection hierarchy
list_products           → identify bestsellers, new arrivals, featured items
```

`get_navigation` is CRITICAL for homepages — it provides the full site structure.

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate full page as plain HTML + Tailwind. Mark island positions:

```html
<!-- Navbar placeholder -->
<div data-placeholder="SiteHeader" class="h-16 border-b border-gray-200">
  Navigation renders here
</div>

<!-- Product grid placeholder -->
<div data-placeholder="EditorialProductGrid" class="min-h-[400px] grid grid-cols-2 md:grid-cols-4 gap-4">
  Product cards render here
</div>

<!-- Footer placeholder -->
<div data-placeholder="Footer" class="bg-gray-900 text-white py-12">
  Footer renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Multiple CTAs to DIFFERENT destinations (explore, shop, learn — not all same link)
- Full-width hero (lifestyle imagery, not product-only)
- Max-width 7xl for content sections
- Mobile: hamburger nav, single column, touch-friendly targets (48px min)

## Phase 2B — Island Mapping

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **Navbar / SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **Footer** (REQUIRED) | Section 9 | `get_navigation` → footer links, social |
| EditorialProductGrid | Section 4 | `list_products` → bestsellers array |
| EmailCapture | Section 8 | provider, listId, incentive |

```html
<!-- SiteHeader -->
<div data-island="SiteHeader" data-props='{"logo":{"src":"...","alt":"Brand"},"links":[{"label":"Shop","href":"/collections/all"},{"label":"About","href":"/pages/about"}],"cartEnabled":true}'></div>

<!-- Footer -->
<div data-island="Footer" data-props='{"logo":{"src":"..."},"columns":[{"title":"Shop","links":[...]},{"title":"About","links":[...]}],"social":[{"platform":"instagram","url":"..."}],"newsletter":true}'></div>
```

Use `vibe://schema/island/SiteHeader` and `vibe://schema/island/Footer` for exact props.

## Award-Winning Homepage Patterns

### Marine Layer Style (Editorial + Transactional Hybrid)
- Dual-path hero segmentation: "New for Him" / "New for Her"
- "This Just In" horizontal scroll carousel between editorial sections
- Quick-add from grid: hover reveals size selector (reduces clicks to purchase)
- Curated "shops within the shop" (Espresso Edit, Hemp Shop)
- 365-day return policy in announcement bar
- Color swatch visibility on grid cards
- Free shipping threshold in cart drawer

### Orbea Style (Full-Bleed Cinematic)
- Full-viewport video hero with brand manifesto overlay
- Category grid with dramatic overlay text
- Progressive product disclosure through scroll
- Minimal text: 2-5 words per section headline
- Dark background, product provides color
- Geographic identity embedded in narrative

### DTC Wellness (Clean + Trustworthy)
- Soft, warm hero with lifestyle imagery
- Category pills for quick filtering
- Ingredient/process transparency section
- Doctor/expert endorsement mid-page
- Subscription CTA prominent
- Clean whitespace signaling premium positioning

## Homepage-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Category grid (vs flat list) | +18% engagement | Shopify 2026 |
| Featured products carousel | Discovery path creation | Marine Layer pattern |
| Social proof below fold | Acceptable (not critical above fold on homepages) | NNGroup |
| Multiple CTAs (different goals) | Expected on homepages (unlike LPs) | Conversion Rate Experts |
| Announcement bar (shipping/returns) | Reduces cart abandonment anxiety | Route 2026 |
| Newsletter with incentive | 10-15% signup rates | Industry avg |
| Editorial mid-page (brand story) | Increases time-on-site, reduces bounce | Awwwards analysis |

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: nav renders, hero visible, categories grid, footer complete
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL.
**Other IDEs:** "Preview: {url} — verify navigation works, collections display"

### Verification Checklist
- [ ] SiteHeader island renders with navigation links from `get_navigation`
- [ ] Hero communicates brand value prop in 3 seconds (not product-specific)
- [ ] Multiple CTAs go to DIFFERENT destinations (shop, about, collections)
- [ ] Category/collection grid links are functional
- [ ] Featured products show real data (real prices, real titles)
- [ ] Footer renders with all nav columns + social + payment icons
- [ ] Mobile: hamburger nav works, single column, touch-friendly
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Fonts loading (not system fallback)
- [ ] Heading hierarchy: single h1 in hero, h2 per section

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Page Feels Editorial, Not Catalog

The homepage is a BRAND experience. It should feel like a magazine cover, not a product spreadsheet:
- Generous whitespace between sections (py-16 md:py-24 minimum)
- Lifestyle photography > product-on-white
- Copy speaks to identity/values, not just features
- Collections named creatively (not just "Shirts" — "The Weekend Edit")
- Visual rhythm: alternate full-bleed and contained sections
- First and last impressions matter most (Serial Position Effect)


## generate-collection

# Collection / Category Page Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`

Generate browsable product listing pages. Grid-focused with EditorialProductGrid island. Quick-add buttons add +15% add-to-cart from grid. Consistent card aspect ratios prevent layout shift. Mid-grid promotional cards every 6-8 products drive AOV.

## Triggers

"collection page", "category page", "product grid", "shop all", "PLP", "product listing"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation + breadcrumb (REQUIRED island)
2. Hero Banner         — collection title + description (max 300px desktop, 200px mobile)
3. Filter/Sort Bar     — collapsible sidebar desktop, bottom sheet mobile
4. Product Grid        — EditorialProductGrid island (the star of the page)
5. Mid-Grid Promo      — promotional card every 6-8 products
6. Social Proof        — compact trust bar below grid
7. Newsletter          — compact single-line signup
8. Footer              — full nav + payment icons (REQUIRED island)
```

## Phase 0 — Context (ALWAYS first, in order)

```
get_workspace_details   → workspace ID, plan tier
get_connected_stores    → store domain, Shopify data
get_brand_kit           → logo, fonts, colors, voice, border radius
get_design_md           → brand brief, design philosophy, don'ts
```

Then page-specific:
```
get_navigation          → navbar/footer links, collection hierarchy, breadcrumb
list_products           → all products in target collection (titles, prices, images, variants, tags)
```

Critical extractions from `list_products`:
- Product count (determines pagination: "Load More" at 12+ products)
- Available filter dimensions: price range, product type, color, size, tags
- Variant data per product (for color swatches on cards)
- Sale/compare-at prices (for badge display)

## Phase 2A — Raw HTML + Tailwind (No Islands)

Generate full page as plain HTML + Tailwind. Mark island positions:

```html
<!-- SiteHeader placeholder -->
<div data-placeholder="SiteHeader" class="h-16 border-b">
  Navigation + breadcrumb renders here
</div>

<!-- Product Grid placeholder -->
<div data-placeholder="EditorialProductGrid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 min-h-[600px]">
  Product cards render here
</div>

<!-- Footer placeholder -->
<div data-placeholder="Footer" class="bg-gray-900 text-white py-12">
  Footer renders here
</div>
```

Rules:
- All colors via `--lx-*` variables (set in `theme_css`)
- Grid is the STAR — hero banner stays short (max 300px desktop, 200px mobile)
- Tighter section padding than other page types: `py-8 md:py-12`
- Consistent card aspect ratios (1:1 or 3:4) with `object-fit: cover`
- Product titles truncated to 2 lines max (prevent layout break)
- Price always visible on card (never hidden behind interaction)

## Phase 2B — Island Mapping

### Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **EditorialProductGrid** (REQUIRED) | Section 4 | `list_products` → products array |
| **Footer** (REQUIRED) | Section 8 | `get_navigation` → footer links |

```html
<!-- EditorialProductGrid -->
<div data-island="EditorialProductGrid" data-props='{"products":[{"id":"p1","title":"...","price":"$29.99","compareAtPrice":"$39.99","image":"...","secondImage":"...","variants":[{"color":"Black","swatch":"#000"},{"color":"White","swatch":"#fff"}],"badge":"Sale","quickAdd":true}],"columns":{"mobile":2,"tablet":3,"desktop":4},"quickAddEnabled":true,"promoCard":{"position":7,"title":"Buy 2, Get 1 Free","image":"...","href":"/collections/bundles"}}'></div>
```

Use `vibe://schema/island/EditorialProductGrid` for exact prop shape.

## Responsive Grid Columns

| Viewport | Columns | Card Min Width | Gap |
|----------|---------|----------------|-----|
| Mobile (< 640px) | 2 | ~160px | 12px |
| Tablet (640-1024px) | 3 | ~200px | 16px |
| Desktop (> 1024px) | 4 | ~280px | 20px |

## Product Card Anatomy

Every card MUST include:
1. **Image** — consistent aspect ratio (3:4 recommended), `object-fit: cover`
2. **Hover image** — second product image on hover (desktop only)
3. **Title** — truncated to 2 lines, `--lx-font-heading`
4. **Price** — always visible; if on sale: `<s>$39.99</s> $29.99` in accent color
5. **Color swatches** — small dots if product has color variants (max 5 visible + "+3")
6. **Quick-add button** — appears on hover (desktop) or always visible (mobile)
7. **Badge** — "New", "Sale", "Bestseller" positioned top-left

### Quick-Add Behavior (+15% add-to-cart from grid)
- Single-variant products: "Add to Cart" button adds directly
- Multi-variant products: "Choose Options" links to PDP
- On success: "Added!" micro-feedback animation (checkmark morph, 300ms)
- Never interrupt browsing with full-page redirects

## Mid-Grid Promotional Card

Insert after every 6-8 products (spans full grid width):
- Brand accent color background (`--lx-accent-color`)
- Promotional message: bundle deal, free shipping threshold, seasonal sale
- Single CTA button with contrasting color
- Different visual weight from product cards (clearly promotional, not confusable)

Example placements:
- Position 7: "Buy 2, Get 1 Free" bundle promo
- Position 14: "Free shipping on orders over $75" threshold nudge
- Position 21: "Subscribe & Save 20%" for consumables

## Filtering UX

### Desktop — Collapsible Sidebar
- Left sidebar (240px width) with filter groups
- Each group expandable/collapsible (accordion pattern)
- Active filters shown as removable chips above grid
- "Clear All" link when filters active
- Product count updates: "Showing 12 of 48 products"

### Mobile — Bottom Sheet
- "Filter" button in sticky bar triggers bottom sheet modal
- Full-screen overlay with filter groups
- "Apply Filters (12)" button shows result count
- "Clear" link in sheet header
- Sort dropdown: separate from filters, always accessible

## Visual Verification (REQUIRED)

After `publish_vibe_page` returns `preview_url`:

**Claude Code (Playwright MCP):**
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
Check: grid renders, cards aligned, images consistent, quick-add visible
If broken → update_page_section → re-verify
```

**Codex:** Use built-in browser to open preview URL.
**Other IDEs:** "Preview: {url} — verify grid layout at 375px, 768px, 1280px"

### Verification Checklist
- [ ] Grid renders with correct column count per breakpoint
- [ ] All product images same aspect ratio (no layout jank)
- [ ] Prices visible on every card (including sale strikethrough)
- [ ] Quick-add buttons functional (hover on desktop, visible on mobile)
- [ ] Color swatches display correctly (not overflowing card)
- [ ] Mid-grid promo card visually distinct from product cards
- [ ] Filter bar sticky on scroll (desktop)
- [ ] Breadcrumb: Home > Collections > [Name] correct
- [ ] Mobile: 2-col grid, no horizontal overflow
- [ ] Brand colors via `--lx-*` variables applied

## Quality Gates

1. `validate_vibe_page` — structural validation (REQUIRED)
2. `check_page_integrity` — archetype-specific rules
3. Visual verification — browser screenshot (REQUIRED)

## Collection-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Quick-add buttons on grid | +15% add-to-cart | Shopify 2026 |
| Consistent card aspect ratios | Prevents CLS (must be <= 0.1) | Web.dev |
| Price visible on card | Table stakes (hidden price = lost sale) | Baymard |
| "Added!" micro-feedback | Peak-end rule — reward moment | Material Design 3 |
| Mid-grid promo card | AOV lift via threshold/bundle nudge | Marine Layer pattern |
| Hover second image | +engagement, reduces PDP bounce rate | Fashion industry std |
| 2-col mobile grid | Optimal for thumb browsing | Apple HIG (48px targets) |
| Short hero (< 300px) | Grid is the star — don't bury it | Baymard |
| Breadcrumb navigation | Reduces bounce, aids discovery | NNGroup |
| Load More (vs pagination) | Lower friction continuation | Infinite scroll without losing context |

## Section CSS Pattern

```html
<!-- Tighter padding for collection pages — grid density matters -->
<section id="collection-grid" class="py-8 md:py-12 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Grid content -->
  </div>
</section>
```


## generate-listicle

# SEO Listicle / Comparison Page Generation

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`

Generate SEO-optimized long-form listicle and comparison pages (>2000 words) with proper heading hierarchy, anchor navigation, and embedded commerce islands.

## When to Use

- "Top 10 best [products] for [use case]"
- "[Brand A] vs [Brand B]" comparison pages
- "Best alternatives to [product]"
- "Product roundup" or "buyer's guide"
- Any search-intent page designed to rank and convert

## CRO Evidence (from CRO-RESEARCH-2026)

- Anchor nav (sticky TOC on desktop) increases time-on-page **+40%** — users jump between entries, reducing bounce
- Comparison table placed at page bottom captures "ready to buy" readers — they scroll past entries → land on table → decide
- Winner badge on recommended product drives **+25% CTR** over unbadged entries
- FAQ before final CTA handles objections at decision point (Serial Position Effect: last items best remembered)
- Real testimonials with names increase trust **+22% CVR** (Digital Applied 2026)
- E-E-A-T signals (author byline, last-updated date, methodology) correlate with higher search placement and user trust

## Generation Flow (5 Phases)

### Phase 0 — Context & SEO Research

```
get_workspace_details    → workspace ID, plan tier
get_connected_stores     → store domain, Shopify data
get_brand_kit            → logo, fonts, colors, voice
get_design_md            → brand brief, design philosophy
list_products            → full product catalog (select featured items)
get_navigation           → navbar/footer links for internal linking
```

Determine from user input:
- Primary keyword (h1 target)
- Product list (3-10 products to feature)
- Comparison criteria (price, features, use case, rating)
- Author name for E-E-A-T byline

### Phase 1 — Asset Discovery

For each product in the listicle:
1. `search_design_library` — find existing product/lifestyle imagery
2. `get_product(product_id)` — pull product images, price, description
3. `generate_asset` — only if no suitable imagery exists (style: `photography`, purpose: `product_lifestyle`)
4. `view_asset` — verify before embedding

Generate one hero asset for the page header (style: `editorial`, purpose: `hero_bg`, aspect: `landscape`).

### Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind first. Use `data-placeholder` where islands will go. Focus on layout, hierarchy, spacing, and typography. All colors via `--lx-*` CSS variables.

Write 8-12 sections:

**Section 1: Hero + E-E-A-T Signals**
- h1 matching primary keyword exactly
- Subtitle with freshness signal: "Updated [Month] [Year] — [N] products tested"
- Author byline with name, role, and avatar
- Last-updated date + methodology disclosure link
- Full-bleed background or gradient

```html
<section id="hero" class="relative py-20 md:py-28 px-6 bg-[--lx-bg-color]">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="font-[--lx-font-heading] text-4xl md:text-5xl font-bold text-[--lx-text-color] leading-tight">{Keyword-Matched Title}</h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4">Updated July 2026 — {N} products tested over {X} weeks</p>
    <div class="flex items-center justify-center gap-3 mt-6">
      <img src="{author_avatar}" alt="{Author Name}" class="w-10 h-10 rounded-full" />
      <div class="text-left">
        <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">{Author Name}</p>
        <p class="font-[--lx-font-body] text-xs text-[--lx-text-muted]">{Role} · {X} years in {category}</p>
      </div>
    </div>
  </div>
</section>
```

**Section 2: Sticky Table of Contents (Anchor Nav)**
- Desktop: sticky sidebar or horizontal sticky bar below header
- Ordered list linking to each `#product-N` section ID
- "Jump to verdict" shortcut at end
- CRO: anchor nav increases time-on-page +40%

```html
<nav id="toc" class="sticky top-0 z-40 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-3 px-6 overflow-x-auto">
  <ol class="flex gap-6 max-w-5xl mx-auto text-sm font-[--lx-font-body] whitespace-nowrap">
    <li><a href="#product-1" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">1. {Name}</a></li>
    <li><a href="#product-2" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">2. {Name}</a></li>
    <!-- ... -->
    <li><a href="#verdict" class="font-semibold text-[--lx-accent-color]">Verdict</a></li>
  </ol>
</nav>
```

**Section 3: Introduction + Methodology**
- h2: "How We Chose the Best [Category]"
- 150-200 words: selection criteria, testing methodology
- Internal links to related pages via `get_navigation`
- Methodology disclosure builds E-E-A-T trust

**Sections 4-N: Product Entries (one per product)**
- h2: "[Product Name] — Best for [Use Case]"
- Product image (alternating left/right layout per entry)
- 150-250 word mini-review
- h3 sub-sections for features where needed
- Pros/Cons as structured lists
- Key specs mini-table
- Star rating visual (CSS-only using `--lx-accent-color`)
- `data-placeholder="BuyBox"` where commerce island goes
- Winner badge (CRO: +25% CTR on recommended product):

```html
<section id="product-1" class="py-16 px-6 border-b border-[--lx-border-color]">
  <div class="max-w-4xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-start">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-[--lx-accent-color]/10 text-[--lx-accent-color] rounded-full text-xs font-semibold mb-3">
          <span>★</span> Editor's Choice
        </div>
        <span class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">#1 Pick</span>
        <h2 class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">{Product Name}</h2>
        <p class="text-sm text-[--lx-text-muted] mt-1">Best for: {use case}</p>
        <p class="mt-4 font-[--lx-font-body] text-[--lx-text-color]/80 leading-relaxed">{Review paragraph}</p>
        <div class="mt-4 grid grid-cols-2 gap-4">
          <div>
            <h3 class="font-semibold text-green-600 text-sm">Pros</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>+ {pro}</li></ul>
          </div>
          <div>
            <h3 class="font-semibold text-red-500 text-sm">Cons</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>- {con}</li></ul>
          </div>
        </div>
        <div data-placeholder="BuyBox" class="mt-6 p-4 border border-dashed border-[--lx-border-color] rounded">Add to cart island</div>
      </div>
      <div>
        <img src="{asset_url}" alt="{product name}" class="rounded-lg shadow-md w-full" />
      </div>
    </div>
  </div>
</section>
```

**Section N+1: Comparison Table**
- Full-width responsive table with feature matrix
- Highlight "Best Overall" / "Best Value" / "Best Premium" rows
- Mobile: horizontal scroll with sticky first column
- CRO: captures ready-to-buy readers who scrolled through all entries

**Section N+2: Verdict (Winner)**
- h2: "Our Top Pick"
- `data-placeholder="BuyBox"` for winning product
- Runner-up mention linking back to its anchor

**Section N+3: FAQ with Schema.org JSON-LD**
- h2: "Frequently Asked Questions"
- 5-8 questions targeting "People Also Ask" queries
- Embedded FAQPage structured data:

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}]}
</script>
```

**Section N+4: Related Content (Internal Linking)**
- 3-4 card grid linking to related listicles/collections
- Anchor text optimized for adjacent keywords

### Phase 2B — Island Mapping

Replace all `data-placeholder` divs with hydrated islands:

```html
<!-- Replace each placeholder -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"...","title":"Default"}]}}'></div>
```

Use `get_island_schema("BuyBox")` to confirm exact prop shape. Each product entry gets its own BuyBox island.

### Phase 3 — Validation

```
validate_vibe_page(page_data)
check_page_integrity(page_id)
```

SEO quality checks:
- Exactly one h1 tag (hero)
- h2 for each product entry, h3 for sub-features
- All anchor nav links resolve to section IDs
- FAQ schema JSON-LD is valid
- Total word count > 2000
- No duplicate section IDs

### Phase 4 — Publish & Verify

```
publish_vibe_page(page_data) → returns preview_url
```

**Visual Verification (REQUIRED):**

For Claude Code (Playwright MCP):
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
```

For Codex: use built-in browser to open preview_url and inspect.
For other IDEs: provide preview URL and instruct user to verify at 375px and 1280px.

**Checklist:**
- [ ] Sticky TOC visible and functional on desktop
- [ ] All anchor links scroll to correct sections
- [ ] Product images rendering (not broken placeholders)
- [ ] Winner badge visible on recommended product
- [ ] Comparison table scrollable on mobile (no overflow)
- [ ] BuyBox islands hydrated with real product data
- [ ] Brand colors applied via `--lx-*` variables
- [ ] FAQ accordion functional
- [ ] No horizontal scroll on mobile

## Quality Bar

- Total word count > 2000 across all sections
- Proper heading hierarchy: h1 (hero) → h2 (entries) → h3 (features)
- Sticky anchor nav with valid section ID targets
- Comparison table responsive (horizontal scroll on mobile, sticky first column)
- Each product entry has a working BuyBox island
- FAQ includes valid Schema.org FAQPage JSON-LD
- Winner badge on recommended product (+25% CTR)
- Author byline + last-updated date (E-E-A-T)
- Internal linking structure via `get_navigation`
- All `--lx-*` CSS variables (NOT `--color-*`)
- Mobile-first: readable at 375px width
- No fetch/XHR, eval, localStorage, @import, duplicate IDs


## generate-bundle-page

# Bundle Builder Page Generation

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`

Generate interactive bundle-builder pages with step-based UX, discount tier visualization, live price calculation, and progress indicators via the BundleBuilder island.

## When to Use

- "Create a build-your-own bundle page"
- "Box builder where customers pick 3-5 products"
- "Mix and match page with volume discounts"
- "Bundle deal landing page"
- Any page where customers assemble a multi-product bundle with tiered pricing

## CRO Evidence (from CRO-RESEARCH-2026)

- Progress bar toward next discount tier increases AOV **+18%** (Goal-Gradient Effect: motivation increases with proximity to goal)
- Showing savings as dollar amount (not just %) improves completion **+12%** ("You're saving $14.70" > "Save 15%")
- Pre-selected starter bundle for decision-fatigued users reduces choice paralysis (Hick's Law: decision time increases with options)
- "X bundles sold today" urgency counter leverages social proof without fake scarcity
- Sticky CTA + above-fold CTA combined = **+12% CVR** (Digital Applied 2026)
- Stack/bundle builders increase AOV **30-50%** (CRO-RESEARCH supplements data)
- Mobile sticky summary at bottom leverages Fitts' Law (infinite-width targets at screen edge)
- Free shipping threshold indicators in cart: "Add $15 more for free shipping" activates Goal-Gradient Effect

## Generation Flow (5 Phases)

### Phase 0 — Context Gathering

```
get_workspace_details    → workspace ID, plan tier
get_connected_stores     → store domain, Shopify data
get_brand_kit            → logo, fonts, colors, voice
get_design_md            → brand brief + guidelines
list_products            → bundleable products catalog
get_navigation           → navbar/footer links
```

Then fetch island schema:
```
get_island_schema("BundleBuilder") → props shape, config, slots
```

Determine from user input:
- Product pool (which products can be bundled)
- Minimum/maximum items per bundle (default: min 2, max 6)
- Discount tiers (default: 2 items = 10%, 3 = 15%, 4+ = 20%)
- Bundle theme/name (e.g., "Build Your Skincare Routine")

### Phase 1 — Asset Discovery

1. `search_design_library` — hero imagery, lifestyle shots showing bundles/boxes
2. `generate_asset` — hero background if none found (style: `photography`, purpose: `hero_bg`, aspect: `landscape`)
3. Product images come from `get_product(id)` for each bundleable item
4. `view_asset` — verify hero asset quality

### Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind first. Mark interactive zones with `data-placeholder`. All colors via `--lx-*` CSS variables.

Write 7 sections:

**Section 1: Hero (Savings Hook)**
- h1: "Build Your [Category] Bundle & Save Up to [max]%"
- Subtitle emphasizing mix-and-match + escalating savings
- Visual showing example bundle (3-4 product thumbnails fanned)
- Primary CTA: "Start Building" (anchor to product grid)
- CRO: savings amount in hero headline not just percentage (+12% completion)

```html
<section id="hero" class="relative min-h-[60vh] flex items-center justify-center px-6 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-br from-[--lx-accent-color]/10 via-[--lx-bg-color] to-[--lx-lavender]/10"></div>
  <div class="relative z-10 text-center max-w-3xl mx-auto">
    <p class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide font-[--lx-font-body] mb-4">Build Your Box</p>
    <h1 class="font-[--lx-font-heading] text-4xl md:text-6xl font-bold text-[--lx-text-color] leading-tight">
      Build Your Bundle<br/>
      <span class="text-[--lx-accent-color]">Save Up to 20%</span>
    </h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4 max-w-xl mx-auto">
      Mix and match your favorites. The more you add, the more you save.
    </p>
    <a href="#products" class="inline-block mt-8 px-8 py-4 bg-[--lx-accent-color] text-white font-semibold rounded-lg hover:bg-[--lx-accent-color-hover] transition-colors text-lg">
      Start Building
    </a>
  </div>
</section>
```

**Section 2: Step Progress Indicator**
- 3-step visual: Choose (active) → Review → Checkout
- Sticky on scroll (`position: sticky; top: 0; z-index: 30`)
- Current step uses `--lx-accent-color`, inactive uses `--lx-text-muted`
- Connecting lines between steps

```html
<nav id="progress" class="sticky top-0 z-30 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-4">
  <div class="max-w-4xl mx-auto flex items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-accent-color] text-white flex items-center justify-center text-sm font-bold">1</span>
      <span class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">Choose</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">2</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Review</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">3</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Checkout</span>
    </div>
  </div>
</nav>
```

**Section 3: Discount Tier Visualization**
- Visual tier ladder: 3 cards showing escalating savings
- Current tier highlighted with accent border + background tint
- "Add X more for next tier" nudge text
- Show dollar savings (not just %): CRO +12% completion
- CRO: progress bar toward next tier +18% AOV

```html
<section id="tiers" class="py-12 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-3xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl font-bold text-center text-[--lx-text-color] mb-8">The More You Add, The More You Save</h2>
    <div class="grid grid-cols-3 gap-4">
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-accent-color] bg-[--lx-accent-color]/5">
        <p class="text-3xl font-bold text-[--lx-accent-color]">10%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">2 items</p>
        <p class="text-xs text-[--lx-accent-color] mt-2 font-medium">Save ~$7</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">15%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">3 items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$14</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">20%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">4+ items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$24+</p>
      </div>
    </div>
  </div>
</section>
```

**Section 4: Product Selection Grid (BundleBuilder zone)**
- h2: "Choose Your Products"
- Responsive grid: 2 cols mobile, 3-4 cols desktop
- Each product card: image, name, individual price, "Add to Bundle" button
- Optional category filter tabs above grid
- `data-placeholder="BundleBuilder"` wrapping the grid
- CRO: pre-select a "starter bundle" for decision-fatigued users (Hick's Law)

```html
<section id="products" class="py-16 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl md:text-3xl font-bold text-[--lx-text-color] text-center mb-8">Choose Your Products</h2>
    <p class="text-center text-[--lx-text-muted] font-[--lx-font-body] mb-8">Select 2 or more items to unlock bundle savings</p>
    <div data-placeholder="BundleBuilder" class="border-2 border-dashed border-[--lx-border-color] rounded-xl p-8 min-h-[400px] flex items-center justify-center">
      <p class="text-[--lx-text-muted]">BundleBuilder island: product grid + live cart + tier progress</p>
    </div>
  </div>
</section>
```

**Section 5: Social Proof**
- "X bundles sold today" urgency counter (real data, not fake)
- 2-3 customer testimonials specific to bundles/value
- Star ratings with review excerpts
- UGC images of received bundles
- CRO: social proof after claims that raise skepticism (+22% with real names)

```html
<section id="social-proof" class="py-16 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-4xl mx-auto text-center">
    <p class="font-[--lx-font-body] text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">Trusted by Bundlers</p>
    <p class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">1,247 bundles built this week</p>
    <div class="grid md:grid-cols-3 gap-6 mt-12">
      <!-- Testimonial cards with real names, photos, star ratings -->
    </div>
  </div>
</section>
```

**Section 6: FAQ**
- h2: "Bundle FAQs"
- 4-6 questions: pricing, changes, minimums, shipping
- Schema.org FAQPage JSON-LD embedded
- CRO: FAQ before final CTA handles objections (Serial Position Effect)

**Section 7: Mobile Sticky Summary**
- Fixed bottom bar on mobile (hidden on desktop)
- Shows: item count, current savings, "View Bundle" button
- Leverages Fitts' Law: infinite-width target at screen edge

```html
<div class="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-[--lx-bg-color] border-t border-[--lx-border-color] p-4 shadow-lg">
  <div class="flex items-center justify-between">
    <div>
      <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">0 items selected</p>
      <p class="font-[--lx-font-body] text-xs text-[--lx-accent-color]">Add 2+ to save</p>
    </div>
    <button class="px-6 py-3 bg-[--lx-accent-color] text-white rounded-lg font-semibold text-sm">View Bundle</button>
  </div>
</div>
```

### Phase 2B — Island Mapping

Replace `data-placeholder="BundleBuilder"` with the hydrated island:

```html
<div data-island="BundleBuilder" data-props='{
  "products": [{"id":"gid://shopify/Product/1","title":"...","price":"$34.00","image":"..."}],
  "minItems": 2,
  "maxItems": 6,
  "discountTiers": [
    {"minQuantity": 2, "discountPercent": 10, "label": "Save 10%"},
    {"minQuantity": 3, "discountPercent": 15, "label": "Save 15%"},
    {"minQuantity": 4, "discountPercent": 20, "label": "Save 20%"}
  ],
  "layout": "grid",
  "columns": {"mobile": 2, "tablet": 3, "desktop": 4},
  "showProgress": true,
  "preselected": []
}'></div>
```

Use `get_island_schema("BundleBuilder")` to confirm exact prop shape before mapping.

### Phase 3 — Validation

```
validate_vibe_page(page_data)
check_page_integrity(page_id)
```

Additional checks:
- BundleBuilder island has valid product IDs from the store
- Discount tiers are logically sequential (higher qty = higher discount)
- Sticky elements (progress bar, mobile summary) don't overlap
- Price displays use consistent currency formatting
- Island props match schema from `get_island_schema`

### Phase 4 — Publish & Verify

```
publish_vibe_page(page_data) → returns preview_url
```

**Visual Verification (REQUIRED):**

For Claude Code (Playwright MCP):
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
```

For Codex: use built-in browser to open preview_url and inspect.
For other IDEs: provide preview URL and instruct user to verify at 375px and 1280px.

**Checklist:**
- [ ] Hero CTA scrolls to product grid
- [ ] Step progress indicator sticky and visible
- [ ] Discount tier cards rendering with correct percentages
- [ ] BundleBuilder island hydrated (products visible, add buttons work)
- [ ] Mobile sticky summary bar visible on small viewports
- [ ] Brand colors applied via `--lx-*` variables
- [ ] No horizontal scroll on mobile
- [ ] Progress bar updates as items added (island handles this)
- [ ] Dollar savings shown alongside percentage

## Quality Bar

- BundleBuilder island correctly configured with valid product IDs and discount tiers
- Discount tier visualization shows both percentage AND dollar savings (+12% completion)
- Progress bar toward next tier visible (+18% AOV)
- Pre-selected starter bundle option for choice-paralyzed users
- Step progress indicator sticky and functional
- Mobile: sticky bottom summary bar, swipeable product grid (2-col)
- "X bundles sold today" social proof (real, not fabricated)
- All `--lx-*` CSS variables (NOT `--color-*`)
- Proper heading hierarchy (h1 hero, h2 per section)
- FAQ includes Schema.org FAQPage JSON-LD
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Minimum 2 items required before checkout CTA enables
- Currency formatting consistent throughout


## generate-editorial

# Editorial / Magazine-Style Page Generation

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`

Generate long-form editorial pages with cinematic visuals, magazine layout patterns, and restrained shoppable product moments (max 2-3 commerce touchpoints per 1000 words).

## When to Use

- "Create a brand story page"
- "Build a lookbook for our new collection"
- "Magazine-style editorial with shoppable products"
- "Content page that tells our brand story"
- "Journal/blog landing with embedded commerce"
- Any page where narrative and visual storytelling take priority, with commerce woven in after emotional peaks

## CRO Evidence (from CRO-RESEARCH-2026)

- Commerce touchpoints placed **after emotional peaks** (story resolution, reveal moment) convert higher than those interrupting narrative flow
- Aesthetic-Usability Effect: beautiful interfaces perceived as more usable — users forgive more from aesthetically pleasing pages
- Editorial architecture (like Lemaire, Delvaux) signals premium positioning — fewer products per viewport = higher perceived value
- 85% of Awwwards luxury winners use 85%+ viewport as photography or whitespace
- Generous section spacing (80-120px vertical) signals luxury/quality brand (all award winners: 100-200px between sections)
- Full-bleed photography dominates award-winning e-commerce (10/10 Awwwards SOTD winners)
- Drop cap + large body text (text-xl+) with generous line-height creates comfortable magazine reading
- Peak-End Rule: experiences judged by peak moment + ending — invest in final section delight
- Invitation language ("Discover", "Explore") outperforms command language ("Buy Now", "Shop") for editorial/luxury
- UGC photos/videos drive **54% purchase intent** after seeing (Nosto) — embed in gallery sections

## Design Patterns (Award-Winning References)

**Serotoninn style:** High-contrast B&W + single color accent, vertical typography, numbered editorial sections, massive editorial photos, bracket-notation CTAs `[ DISCOVER ]`

**Lemaire style:** Ultra-minimal, lowercase navigation, zero persuasion mechanics, 85%+ viewport is photography/whitespace, radical omission as luxury signal, single product spotlight

**Vero Studio style:** Typography IS the visual (no hero image), italic word emphasis, near-monochrome palette, poetry as transitions, coffee-table-book spacing

**Radian style:** Cinematic scroll-snap, pagination indicators (01/09), progressive disclosure through chapters, geographic coordinates as design elements

## Generation Flow (5 Phases)

### Phase 0 — Context & Creative Direction

```
get_workspace_details    → workspace ID, plan tier
get_connected_stores     → store domain, Shopify data
get_brand_kit            → logo, fonts, colors, voice
get_design_md            → brand brief + tone of voice + design philosophy
list_products            → products to weave into narrative (select 2-5)
get_navigation           → navbar/footer links
```

Heavy use of design library (editorial = existing brand photography, not AI-generated):
```
search_design_library({ query: "editorial lifestyle brand" })
search_design_library({ query: "behind the scenes studio process" })
search_design_library({ query: "texture detail closeup material" })
search_design_library({ query: "portrait founder team" })
```

Determine from user input:
- Narrative angle (brand origin, collection story, seasonal mood, day-in-the-life)
- Products to feature (2-5 max shoppable moments)
- Visual mood (minimal/luxe/raw/warm/cool)
- Tone of voice (aspirational, intimate, bold, poetic)

### Phase 1 — Asset Discovery (Heavy — Editorial Is Image-Driven)

Editorial pages require 6-10 high-quality images. ALWAYS prioritize existing brand photography over generation:

1. `search_design_library` — run 4-6 queries covering hero, lifestyle, texture, behind-scenes, portraits
2. `generate_asset` — ONLY for gaps after exhausting library:
   - Hero: style `editorial`, purpose `hero_bg`, aspect `landscape`, quality `high`
   - Look images: style `photography`, purpose `product_lifestyle`, aspect `portrait`, quality `high`
   - Interlude textures: style `photography`, purpose `section_bg`, aspect `landscape`
3. `view_asset` — verify EVERY image (editorial quality demands visual review)

Budget: up to 6-8 assets for editorial. Always prefer library over generation.

### Phase 2A — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind first. Use `data-placeholder` where islands will go. All colors via `--lx-*` CSS variables. Total narrative content MUST exceed 800 words.

Write 8-10 sections with generous whitespace (section padding 80-120px vertical):

**Section 1: Full-Bleed Cinematic Hero**
- Full-viewport image (min-height: 80vh or 100vh)
- Minimal text: editorial title + category/date label (2-5 words max overlay)
- Text positioned bottom-left with dark gradient overlay
- No navigation clutter — image breathes
- CRO: Radian/Lemaire pattern — photography dominates 85%+ viewport

```html
<section id="hero" class="relative min-h-screen flex items-end overflow-hidden">
  <div class="absolute inset-0">
    <img src="{hero_asset_url}" alt="{contextual alt}" class="w-full h-full object-cover" />
    <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
  </div>
  <div class="relative z-10 max-w-4xl mx-auto px-8 pb-20 md:pb-28">
    <p class="font-[--lx-font-body] text-sm uppercase tracking-[0.2em] text-white/60 mb-4">{Category} · {Season Year}</p>
    <h1 class="font-[--lx-font-heading] text-4xl md:text-6xl lg:text-7xl font-bold text-white leading-[1.1]">
      {Editorial Title}
    </h1>
    <p class="font-[--lx-font-body] text-lg text-white/75 mt-6 max-w-2xl">{Opening hook — one evocative sentence}</p>
  </div>
</section>
```

**Section 2: Opening Narrative (Drop Cap)**
- 200-300 words of storytelling prose
- Wide reading column (max-w-3xl centered)
- Large body text (text-xl) with generous line-height (leading-relaxed)
- Drop cap on first letter (CSS `first-letter:` pseudo-element)
- Set the scene — NO products yet, pure narrative
- Vertical padding: py-20 md:py-32 (80-128px)

```html
<section id="opening" class="py-20 md:py-32 px-6">
  <div class="max-w-3xl mx-auto">
    <p class="font-[--lx-font-body] text-xl md:text-2xl leading-relaxed text-[--lx-text-color]/85 first-letter:text-6xl first-letter:font-[--lx-font-heading] first-letter:font-bold first-letter:float-left first-letter:mr-4 first-letter:mt-1 first-letter:text-[--lx-accent-color]">
      {Opening narrative — 200-300 words setting the scene, introducing the story...}
    </p>
    <p class="font-[--lx-font-body] text-lg leading-relaxed text-[--lx-text-color]/70 mt-8">
      {Second paragraph deepening the story...}
    </p>
    <p class="font-[--lx-font-body] text-lg leading-relaxed text-[--lx-text-color]/70 mt-6">
      {Third paragraph...}
    </p>
  </div>
</section>
```

**Section 3: Shoppable Look #1 (After Emotional Peak)**
- Asymmetric grid: image 60% + product details 40%
- Image: hero-quality lifestyle shot with product in context
- Product details: name, one-line narrative description, price
- `data-placeholder="EditorialProductGrid"` for commerce
- CRO: place commerce AFTER emotional peak (story resolution), not interrupting flow
- Invitation language: "Discover" or "Explore" (not "Buy Now")

```html
<section id="look-1" class="py-20 md:py-28">
  <div class="grid md:grid-cols-5 gap-0 items-stretch">
    <div class="md:col-span-3">
      <img src="{look_1_asset}" alt="{contextual alt}" class="w-full h-full object-cover min-h-[500px]" />
    </div>
    <div class="md:col-span-2 flex flex-col justify-center px-8 md:px-14 py-12 bg-[--lx-bg-color]">
      <p class="font-[--lx-font-body] text-xs uppercase tracking-[0.15em] text-[--lx-accent-color] mb-4">The Look</p>
      <h2 class="font-[--lx-font-heading] text-2xl md:text-3xl font-bold text-[--lx-text-color]">{Look Title}</h2>
      <p class="font-[--lx-font-body] text-[--lx-text-color]/70 mt-4 leading-relaxed">{Narrative description — why this piece matters in the story}</p>
      <div data-placeholder="EditorialProductGrid" class="mt-8 p-4 border border-dashed border-[--lx-border-color] rounded">Product island</div>
    </div>
  </div>
</section>
```

**Section 4: Pull Quote / Interlude**
- Full-width with texture or tinted background
- Large pull quote (text-3xl to text-5xl) centered, italic
- Attribution (founder, designer, brand voice)
- Visual break between shoppable moments
- Generous padding: py-24 md:py-32 (96-128px)
- Optional: Vero Studio style — poetry as transitional section

```html
<section id="interlude" class="py-24 md:py-32 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-4xl mx-auto text-center">
    <blockquote class="font-[--lx-font-heading] text-3xl md:text-4xl lg:text-5xl font-light text-[--lx-text-color] leading-snug italic">
      "{Evocative brand statement or founder quote}"
    </blockquote>
    <cite class="font-[--lx-font-body] text-sm text-[--lx-text-muted] mt-8 block not-italic uppercase tracking-[0.15em]">
      — {Name}, {Title}
    </cite>
  </div>
</section>
```

**Section 5: Mid-Narrative (Continue Story)**
- 150-200 words continuing the narrative arc
- Same reading column (max-w-3xl)
- Text-lg with relaxed line-height
- Build toward the next emotional peak before Look #2
- Internal cross-reference or anecdote

**Section 6: Shoppable Look #2 (Reversed Layout)**
- Mirror layout of Look #1 (image right, text left on desktop)
- Different product(s) featured in new context
- CRO: commerce placed after second emotional peak (reveal moment)
- Same `data-placeholder="EditorialProductGrid"` pattern

**Section 7: Asymmetric Image Grid (Behind the Scenes)**
- 2-3 images in CSS grid with varying spans (not uniform)
- 100-150 words about craft/process/people
- Humanizes the brand — studio shots, raw materials, hands at work
- NO commerce in this section — pure storytelling
- CRO: Aesthetic-Usability Effect — visual polish increases trust

```html
<section id="behind-scenes" class="py-20 md:py-28 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl font-bold text-[--lx-text-color] mb-12 text-center">Behind the Scenes</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
      <div class="col-span-2 row-span-2">
        <img src="{bts_1}" alt="{alt}" class="w-full h-full object-cover rounded-lg" />
      </div>
      <div class="col-span-1">
        <img src="{bts_2}" alt="{alt}" class="w-full h-full object-cover rounded-lg aspect-square" />
      </div>
      <div class="col-span-1">
        <img src="{bts_3}" alt="{alt}" class="w-full h-full object-cover rounded-lg aspect-square" />
      </div>
    </div>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-color]/70 mt-10 max-w-2xl mx-auto text-center leading-relaxed">
      {Behind the scenes narrative — craft, process, people, materials}
    </p>
  </div>
</section>
```

**Section 8: Shoppable Collection Grid (Optional, Max 2-3 items)**
- h2: "Explore the Collection" (invitation language, not "Shop Now")
- `data-placeholder="EditorialProductGrid"` with editorial variant
- Clean, minimal cards preserving editorial feel
- 3-4 column grid maximum
- CRO: Peak-End Rule — this is near the end, make it rewarding

**Section 9: Closing Narrative**
- 100-150 words wrapping the story
- Callback to the opening (narrative closure)
- Subtle CTA: "Discover more" linking to collection

**Section 10: Footer**
- Standard brand footer via `get_navigation`

### Phase 2B — Island Mapping

Replace `data-placeholder="EditorialProductGrid"` with hydrated islands. Maximum 2-3 commerce islands total (editorial restraint):

```html
<div data-island="EditorialProductGrid" data-props='{
  "products": [{"id":"gid://shopify/Product/1","title":"...","price":"$89.00","image":"..."}],
  "columns": {"mobile": 1, "desktop": 2},
  "variant": "editorial",
  "showPrice": true,
  "showQuickAdd": true,
  "ctaText": "Discover"
}'></div>
```

Use `get_island_schema("EditorialProductGrid")` to confirm exact prop shape.

### Phase 3 — Validation

```
validate_vibe_page(page_data)
check_page_integrity(page_id)
```

Editorial-specific checks:
- Hero image is high quality and full-bleed
- Text legible over all image backgrounds (contrast via gradient overlay)
- Commerce islands do NOT interrupt narrative flow (placed after peaks only)
- Maximum 2-3 commerce touchpoints total
- Total narrative word count > 800
- Pull quote section has adequate padding (py-24+)
- Image aspect ratios consistent within asymmetric grids
- Reading column max-w-3xl for prose (comfortable reading)
- Section padding 80-120px vertical throughout

### Phase 4 — Publish & Verify

```
publish_vibe_page(page_data) → returns preview_url
```

**Visual Verification (REQUIRED):**

For Claude Code (Playwright MCP):
```
browser_navigate → preview_url
browser_take_screenshot → full page capture
```

For Codex: use built-in browser to open preview_url and inspect.
For other IDEs: provide preview URL and instruct user to verify at 375px and 1280px.

**Checklist:**
- [ ] Cinematic hero: full-bleed, high-quality image, text legible via gradient
- [ ] Drop cap rendering on opening paragraph
- [ ] Generous whitespace between sections (80-120px)
- [ ] Pull quote visually distinct (large italic font, centered, padded)
- [ ] Asymmetric image grid not broken on mobile (single column)
- [ ] Commerce islands only appear after narrative peaks (not interrupting)
- [ ] Maximum 2-3 shoppable moments total
- [ ] Brand colors applied via `--lx-*` variables
- [ ] Fonts loading (heading + body distinct)
- [ ] Total narrative > 800 words (read through for quality)
- [ ] No horizontal scroll on mobile
- [ ] Editorial feel preserved — not a product catalog

## Quality Bar

- Cinematic full-bleed hero (min-height: 80vh, gradient overlay for text contrast)
- Magazine layout patterns: drop cap, pull quotes, asymmetric grids, full-bleed images
- Maximum 2-3 commerce touchpoints per 1000 words (editorial restraint over conversion pressure)
- Commerce placed AFTER emotional peaks (story resolution, reveal moment)
- Invitation language ("Discover", "Explore") not command language ("Buy Now")
- >800 words total narrative content
- Generous whitespace: section padding 80-120px vertical
- Large body text (text-xl+) with relaxed line-height for comfortable reading
- All images via `search_design_library` first (editorial = real photography, not AI)
- Asymmetric/editorial grid layouts (not uniform boxes)
- Pull quotes: large italic font, generous padding, visual separation
- All `--lx-*` CSS variables (NOT `--color-*`)
- Mobile-first: single column, images stack, readable without pinching
- Contextual alt text on all images (narrative, not just product names)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs


## ad-to-page

# Ad Creative to Landing Page

Generate a high-converting landing page from an ad creative with full scent continuity (headline, palette, CTA, tone match from click to page).

## Prerequisites

- At least one ad creative synced (Meta/Google/TikTok)
- Store connected and brand kit configured

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Identify and Analyze the Ad

```
get_ad_creatives({ store_id, status: "active" })
```

Present available creatives (thumbnail + headline + spend). User picks one, or use highest-spend active creative.

```
analyze_ad_creative({ creative_id })
```

Extracts: headline, subheadline, claims, color_palette, tone, cta_text, target_audience, urgency_signals, imagery_style.

### Step 3 — Match Persona and Source Assets

```
match_persona_to_ad({ creative_id })
```

Maps to persona: demographics, pain points, motivations, objections, buying stage. Determines page tone.

```
search_design_library({ query: "<product/topic from ad>" })
```

Find product shots and lifestyle images matching the ad aesthetic. Use `generate_asset` if library insufficient.

### Step 4 — Two-Phase Page Generation

**Phase A — Raw HTML + Tailwind (no islands)**

Generate full page as HTML + Tailwind. Scent continuity rules:
- Hero headline = ad headline (semantic match, max 2-word variation)
- `--lx-accent-color` set to ad's dominant color
- CTA text matches or escalates the ad CTA
- First fold answers the same promise the ad made
- Zero navigation links (single CTA focus)

Structure: Hero > Problem/Agitation > Solution > Social Proof > Features > CTA repeat > FAQ

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

Use `--lx-*` CSS variables in `theme_css` for all brand colors and fonts.

**Phase B — Island Mapping**

Replace placeholders with hydrated islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

Use `get_island_schema` for exact prop shapes.

### Step 5 — Validate and Publish Draft

```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { publish: false })
```

Always publish as draft first. Returns `preview_url`.

### Step 6 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify."

Checklist:
- [ ] Hero headline matches ad headline (scent continuity)
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Single CTA focus (no nav leakage)
- [ ] Mobile layout not broken (stack, readable text)
- [ ] Islands hydrated (BuyBox shows product data)
- [ ] Social proof section present

If issues found: `update_page_section` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Which ad? | Ask user, or highest-spend active creative |
| Which product? | Extract from ad analysis (primary product) |
| Draft or live? | Always draft first -- user confirms |
| Long or short? | Video ad = longer storytelling; static = concise |
| Include pricing? | Only if ad mentions price/discount explicitly |

## Quality Gates

- Hero headline >=80% semantic similarity to ad headline
- Color palette matches ad dominant colors (set via `--lx-accent-color`)
- Single primary CTA throughout (no competing actions)
- Mobile-first layout (most ad traffic is mobile)
- No navigation links that leak traffic from conversion
- Ad urgency signals carried through (countdown, limited stock, etc.)
- Page passes `validate_vibe_page` with zero errors


## page-redesign

# Page Redesign (Modernize/Refresh Existing Page)

Visually refresh an existing page using performance data to preserve what works and redesign what does not.

## Prerequisites

- Target page exists (published or draft)
- Brand kit up to date (may have changed since page creation)
- Page analytics available for performance-informed decisions

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
get_design_md()                  → brand brief, design philosophy, constraints
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
find_page({ query: "page name or slug" })
```
Or:
```
list_pages({ status: "published" })
```

Then load full page data:
```
get_page(page_id)
inspect_page_sections(page_id)
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
get_page_analytics(page_id)
```

Categorize each section:
- **KEEP** — high CVR, proven copy, minor visual polish only
- **REDESIGN** — same content, new layout/styling
- **REPLACE** — low-performing, rebuild approach
- **REMOVE** — adds friction, no conversion value

Key rule: NEVER redesign sections that are converting well. Analytics data overrides aesthetic preferences.

### Step 4 — Apply Section-by-Section Updates

For each section to change:
```
update_page_section(page_id, section_id, { html, css, settings })
```

For reordering (if scroll-depth data suggests better flow):
```
move_page_section(page_id, section_id, new_position)
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
validate_vibe_page(page_id)
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
diff_page_versions(page_id, { from: previous_version, to: current_version })
```

Present structural diff to user for approval before publishing.

### Step 7 — Publish Draft and Visual Verification

```
publish_page(page_id, { draft: true })
```

Returns `preview_url`.

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify."

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues found: `update_page_section` to fix, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
publish_page(page_id)
```

If redesign later hurts metrics: `rollback_page_version(page_id, version_id)` is available.

## Decision Points

| Question | Decision |
|----------|----------|
| Full rebuild or section-by-section? | >70% sections changing = full rebuild is faster |
| Keep copy or rewrite? | Keep unless analytics show messaging problems |
| Preserve section order? | Yes, unless scroll-depth shows clear drop-off pattern |
| Same section types or new? | Prefer new layouts for freshness; same types if copy fits |
| A/B test old vs new? | Recommend if page has >500 daily visitors |

## Quality Gates

- URL/slug PRESERVED (never change -- breaks SEO and ad links)
- Page title and meta description preserved unless explicitly requested
- High-CVR sections retain their copy and core structure
- New design matches current brand kit (`--lx-*` variables)
- Mobile responsiveness maintained or improved
- All existing islands remain functional
- Version history intact (rollback available)
- Page passes `validate_vibe_page` with zero errors


## competitor-remix

# Competitor Remix (Rebuild from Reference URL)

Capture a competitor page, decompose its structure, and rebuild it using the user's own brand identity, copy, and products. NEVER copy content -- only structural inspiration.

## Prerequisites

- User provides a reference URL
- Store connected and brand kit configured
- User's own product/content available to replace competitor's

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Capture Reference Design

```
capture_design_source({ url })
```

Screenshots the page and extracts structural layout data.

```
extract_brand_design({ url })
```

Pulls competitor's design DNA: color palette, typography, spacing rhythm, border radius, shadow depth, image treatment style, overall aesthetic (minimal, bold, editorial, etc.).

### Step 3 — Decompose into Section Map

Analyze captured page into numbered section breakdown:
```
1. Full-bleed hero — product centered, headline overlay, gradient wash
2. Trust badge row — 4 icons with micro-labels, centered
3. Split feature section — image left, text right, 50/50
4. Testimonial carousel — 3 cards, star ratings, photos
5. Product grid — 3 columns, hover zoom
6. FAQ accordion — 6 items, expandable
7. Final CTA — full-width, contrasting background
```

For each: note layout pattern, content type, approximate proportions, interactive elements.

### Step 4 — Map to Lexsis Capabilities

For each competitor section:
- Island available? Use `get_island_schema(island_name)` for prop shapes
- Static HTML+Tailwind section? (most common)
- Requires custom interactivity? Flag for JS sandbox

### Step 5 — Source User's Own Assets

```
search_design_library({ query: "<relevant product/category>" })
list_products({ limit: 10 })
```

Replace ALL competitor imagery with user's own assets. Generate new if needed:
```
generate_asset({ prompt: "...", style_reference: "brand_kit" })
```

CRITICAL: NEVER reference, hotlink, or reuse competitor images/copy/logos.

### Step 6 — Two-Phase Generation

**Phase A — Raw HTML + Tailwind (no islands)**

For each section from the decomposition:
- **Structure**: Keep competitor's layout pattern (grid, split, stacked)
- **Brand**: Replace ALL colors/fonts/spacing with user's `--lx-*` variables
- **Content**: Write original copy serving user's value proposition
- **Images**: User's own assets exclusively
- **CTAs**: Aligned with user's conversion goals

Set all brand tokens in `theme_css`:
```css
:root { --lx-accent-color: #...; --lx-font-heading: '...', serif; }
```

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

**Phase B — Island Mapping**

Replace placeholders with hydrated islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"...","answer":"..."}]}'></div>
```

### Step 7 — Validate and Publish Draft

```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { publish: false })
```

Returns `preview_url`.

### Step 8 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify alongside reference."

Checklist:
- [ ] ZERO competitor content carried over (no copy, images, logos)
- [ ] All colors from user's `--lx-*` variables (not competitor palette)
- [ ] Structural similarity recognizable but not pixel-perfect
- [ ] User's brand fonts loading (not system fallback)
- [ ] Mobile layout works independently
- [ ] Islands hydrated with user's own product data
- [ ] Original copy serves user's value proposition

If issues found: `update_page_section` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Keep exact structure or adapt? | Adapt: remove irrelevant sections, add where user has more to say |
| Which sections to skip? | Competitor-specific (their awards, team), navigation that does not fit |
| How close to follow? | Structural only -- proportions, flow, section types |
| Interactive elements? | Map to available islands; static equivalent if no island exists |

## Quality Gates

- ZERO competitor content (copy, images, logos, brand marks)
- Page uses exclusively user's `--lx-*` CSS variables
- All images are user's own or freshly generated
- All product references from user's own catalog
- Copy is original, serving user's value proposition
- Mobile layout independent (do not assume competitor's responsive approach)
- Page passes `validate_vibe_page` with zero errors


## personalization-variant

# Personalization Variant (Persona-Specific Page Versions)

Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience segment's motivations and objections.

## Prerequisites

- Base page exists (the page to personalize from)
- Personas defined or user describes target audiences
- Brand kit available (shared across all variants)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Load Personas and Base Page

```
list_personas()
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
get_page(page_id)
get_page_content(page_id)
```

Understand current structure, copy, and section types. This is the default variant.

### Step 3 — Plan Persona Adaptations

For each selected persona, identify what changes (ordered by conversion impact):

| Priority | Element | Personalization Strategy |
|----------|---------|--------------------------|
| 1 | Hero headline + subheadline | Tone shift: urgent for deal-seekers, aspirational for status-seekers (+202% CVR) |
| 2 | Hero image | Demographic match: age, lifestyle, environment |
| 3 | Social proof selection | Relevant testimonials matching persona's concern |
| 4 | CTA text | Motivation match: savings-focused vs quality-focused vs speed-focused |
| 5 | Section ordering | Pain-first for problem-aware, solution-first for solution-aware |

Not everything changes. Keep brand identity (colors, fonts, logo) consistent across all variants.

### Step 4 — Source Persona-Matched Assets

For each persona:
```
search_design_library({ query: "<persona-relevant imagery>" })
```

Find images reflecting the persona's world. Generate if needed:
```
generate_asset({ prompt: "...", demographic: "<persona context>" })
```

### Step 5 — Create Each Variant

For each persona:
```
create_page_variation(page_id, {
  name: "<persona_name> variant",
  changes: {
    sections: [
      { section_id: "hero", html: "...", css: "..." },
      { section_id: "social-proof", html: "..." },
      { section_id: "cta-block", html: "..." }
    ]
  }
})
```

All variants use the same `--lx-*` CSS variables (brand stays consistent). Only content, imagery, and tone change.

Islands remain identical across variants -- only the surrounding copy/imagery adapts:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

### Step 6 — Validate All Variants

For each variant:
```
validate_vibe_page(variant_page_id)
```

Ensure all render correctly, islands work, mobile intact.

### Step 7 — Visual Verification (Each Variant)

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: variant_preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open each variant's preview_url.

**Other IDEs:** Provide URLs: "Variant A: {url_a}, Variant B: {url_b} -- open to verify."

Checklist (per variant):
- [ ] Headline tone matches persona (urgent vs aspirational vs analytical)
- [ ] Hero image reflects persona demographic
- [ ] CTA language aligns with persona motivation
- [ ] Social proof relevant to persona's concerns
- [ ] Brand identity consistent (`--lx-*` variables unchanged)
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly

### Step 8 — (Optional) Set Up Persona-Targeted Experiment

```
create_ab_test({
  page_id: base_page_id,
  variants: [
    { page_id: variant_a_id, weight: 33, targeting: { persona: "deal-seekers" } },
    { page_id: variant_b_id, weight: 33, targeting: { persona: "quality-seekers" } },
    { page_id: base_page_id, weight: 34, targeting: { default: true } }
  ]
})
```

Traffic routes to matching persona variant based on UTM/audience signals.

## Decision Points

| Question | Decision |
|----------|----------|
| Which personas? | Top 2-3 highest-value segments (by revenue or volume) |
| What to personalize? | Headlines + hero image + CTA = highest impact; start there |
| Full rewrite or selective? | Selective: 3-5 elements max per variant to isolate impact |
| Auto-assign or manual? | Auto if UTM/referrer identifies segment; manual for broad traffic |
| How many variants? | 2-4 max -- more variants need more traffic for significance |

## Quality Gates

- Each variant feels genuinely tailored (not just a headline swap)
- Imagery matches persona demographic and psychographic profile
- CTA language aligns with persona motivation
- Social proof relevant to persona (industry-matched, use-case-matched)
- All variants share same `--lx-*` brand identity
- Each variant passes `validate_vibe_page` independently
- Tone consistent within each variant (headline tone = body copy tone)
- Structural integrity maintained (no broken sections or islands)


## ab-test-variant

# A/B Test Variant (Hypothesis-Driven Experiment)

Clone an existing page, apply a single focused change based on a clear hypothesis, launch a controlled experiment, and monitor for statistical significance via mSPRT.

## Prerequisites

- Target page exists and is published (needs traffic)
- Sufficient traffic (minimum 200 daily visitors, recommend 500+)
- Clear metric to optimize (CVR, AOV, bounce rate, scroll depth)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
```

These two calls ALWAYS run first. No exceptions.

### Step 2 — Load Current Page and Baseline

```
get_page(page_id)
get_page_analytics(page_id)
```

Record baseline performance:
- Conversion rate (primary metric)
- Bounce rate, average time on page
- Scroll depth, CTA click-through
- Revenue per visitor

This is the control to beat.

### Step 3 — Formulate Hypothesis

Structure: "Changing **[element]** from **[current]** to **[proposed]** will improve **[metric]** by **[estimated %]** because **[reason based on user behavior]**."

Document the hypothesis BEFORE creating the variant. Not post-hoc.

Common high-impact tests (ordered by typical lift):
1. Hero headline copy (+5-15% CVR)
2. CTA button color/text (+3-10% CTR)
3. Social proof placement (+5-22% depending on type)
4. Hero image: lifestyle vs product-focused (+8-12%)
5. Section ordering: problem-first vs solution-first (+3-7%)
6. Price anchoring: was/now vs % off (+4-8%)

### Step 4 — Create the Variant

```
duplicate_page(page_id)
```

Creates exact copy. Then apply the SINGLE focused change:
```
update_page_section(variant_page_id, section_id, { html, css, settings })
```

RULE: ONE change per test. Multiple changes make attribution impossible.

All styling via `--lx-*` CSS variables. Islands unchanged unless the test specifically targets island props:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

### Step 5 — Validate Variant

```
validate_vibe_page(variant_page_id)
```

Ensure variant renders correctly, all islands work, mobile intact.

### Step 6 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: variant_preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open variant preview.

**Other IDEs:** Provide URL: "Variant preview: {url} -- verify change is visible."

Checklist:
- [ ] The ONE change is clearly visible
- [ ] Everything else identical to control
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly
- [ ] No unintended side effects (broken spacing, color bleed)

### Step 7 — Launch Experiment

```
create_ab_test({
  page_id: page_id,
  hypothesis: "Changing [X] will improve [metric] because [reason]",
  variants: [
    { page_id: page_id, weight: 50, name: "Control (A)" },
    { page_id: variant_page_id, weight: 50, name: "Variant (B)" }
  ],
  primary_metric: "conversion_rate",
  minimum_sample: 1000
})
```

50/50 split is standard. 80/20 only for high-traffic pages testing risky changes.

### Step 8 — Monitor Results

```
get_experiment_results(experiment_id)
```

Returns: CVR per variant with confidence intervals, statistical significance (mSPRT), sample size, winner recommendation, secondary metrics.

RULES:
- NEVER call a winner before mSPRT reports `significant: true`
- Minimum 1000 visitors per variant for evaluation
- Check device split (variant may win mobile, lose desktop)
- Monitor secondary metrics (winning CVR but tanking AOV is not a win)

### Step 9 — Scale Winner

Only when `significant: true`:
```
scale_winner(experiment_id, winning_variant_id)
```

Routes 100% traffic to winner. Marks experiment complete.

If no winner after 2000+ visitors per variant: the change has no meaningful impact. Stop test, formulate bolder hypothesis.

## Decision Points

| Question | Decision |
|----------|----------|
| What to test first? | Highest impact, lowest effort: headline > CTA > hero > layout |
| Traffic split? | 50/50 default; 80/20 for high-traffic + risky changes |
| When to check? | After 500+ visitors per variant; avoid daily peeking |
| When to stop? | Significant result OR >3000 visitors/variant with no signal |
| Variant loses? | Document learning, revert to control, new hypothesis |
| Multiple tests? | Only on DIFFERENT pages; never two tests on same page |

## Quality Gates

- ONE change per test (scientific rigor -- isolate the variable)
- Hypothesis documented BEFORE variant creation
- Minimum 1000 visitors per variant before evaluating
- Statistical significance required (mSPRT p<0.05) before declaring winner
- Both variants pass `validate_vibe_page`
- Control remains untouched for test duration
- Secondary metrics monitored alongside primary
- Learning documented regardless of outcome (losses teach as much as wins)
- Wait for mSPRT -- never call early based on gut feeling


## brand-setup

# First-Time Brand Setup

Bootstrap a new workspace — verify connectivity, extract brand identity, configure the kit and theme, and verify everything renders correctly with `--lx-*` CSS variables.

## When to Use

- New merchant onboarding (no brand kit exists yet)
- Reconnecting or reconfiguring an existing store
- Extracting brand identity from an existing website URL
- Resetting brand kit after a rebrand

## Prerequisites

- Shopify store credentials (domain + access token) OR an existing connected store
- A reference URL to extract brand design from (merchant's live site, competitor, or mood board)
- Workspace must be provisioned (the MCP session implies this)

## Flow

### 1. Check workspace exists

```
get_workspace_details
```

- Confirms workspace ID, plan tier, and session validity
- If workspace missing or invalid: abort with clear error

### 2. Check store connection

```
get_connected_stores
```

- If store already connected: proceed to step 3
- If no store: store provisioning happens via Shopify OAuth (outside MCP) — instruct user to connect store first

### 3. Collect reference URL

Ask user for their store URL or an existing site URL for design extraction:
- "What URL should I extract your brand design from? (Your Shopify store, existing website, or a reference site you like)"

### 4. Extract brand design from URL

```
extract_brand_design({ url })
```

- Pulls: primary/secondary/accent colors, font families, spacing scale, logo URL, imagery style, tone of voice
- Works on any public URL (Shopify store, competitor, portfolio site)
- If extraction fails: fall back to manual input (ask for colors, fonts, logo URL)

### 5. Check existing brand kit

```
get_brand_kit
```

- If kit exists and user wants to override: proceed with update
- If kit exists and user wants to keep: skip to step 7
- If no kit: create new from extracted values

### 6. Present extracted values for confirmation

Show user the extracted brand values and ask for confirmation/adjustment:

```
Extracted brand identity:
- Primary color: #4F46E5
- Secondary color: #10B981
- Accent color: #F59E0B
- Heading font: Playfair Display
- Body font: Inter
- Logo URL: https://...
- Border radius: 8px
- Voice/tone: Premium, confident

Does this look right? Any adjustments?
```

Wait for user confirmation before proceeding.

### 7. Update brand kit

Update brand kit with confirmed values via the Golem API (brand kit is managed there, not via MCP tool directly). The MCP session carries the auth context.

### 8. Apply to default theme

```
list_themes
```

Then:

```
update_theme({
  colors: { primary, secondary, accent, background, surface, text },
  typography: { heading_font, body_font, scale_ratio },
  spacing: { base_unit, section_padding },
  borders: { radius, style },
  logo_url,
  favicon_url
})
```

- All `--lx-*` CSS variables must be populated
- Fonts must be valid Google Fonts families or system font stacks

### 9. Verify design library access

```
search_design_library({ query: "brand" })
```

- Confirm assets (logo, favicon, OG image) are accessible
- If missing: prompt user to upload or use `import_asset`

### 10. Verify product catalog synced

```
list_products({ limit: 5 })
```

- Confirm products synced from Shopify
- If empty: warn user that product-based sections won't render

### 11. Generate test section to verify brand rendering

Create a simple hero section using the brand colors, fonts, and logo:

```html
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto text-center">
    <img src="{logo_url}" alt="{brand_name}" class="h-12 mx-auto mb-8" />
    <h1 class="text-4xl md:text-5xl font-bold mb-4" style="font-family: var(--lx-font-heading); color: var(--lx-text-color)">
      Your Brand, Beautifully Rendered
    </h1>
    <p class="text-lg mb-8" style="font-family: var(--lx-font-body); color: var(--lx-text-muted)">
      This is a test section to verify your brand kit renders correctly.
    </p>
    <a href="#" class="inline-block px-8 py-3 rounded-lg text-white font-semibold" style="background-color: var(--lx-accent-color)">
      Test CTA Button
    </a>
  </div>
</section>
```

Publish as draft:

```
publish_vibe_page({ ... draft: true })
```

Visually verify:
- Fonts loading correctly (not system fallback)?
- Brand colors applied (not default purple)?
- Logo rendering (not 404/broken)?
- CTA button has proper contrast?

### 12. Confirm to user

"Brand configured. Ready to generate pages."

## Decision Points

| Scenario | Action |
|---|---|
| Store not connected | Instruct user to complete Shopify OAuth first |
| Brand kit already exists | Ask: override, merge, or keep existing? |
| URL extraction fails | Fall back to manual input (ask for colors, fonts, logo) |
| No products synced yet | Warn user; product sections will show placeholders |
| Multiple themes needed | Create default first, additional via separate `update_theme` calls |
| Colors fail contrast check | Suggest adjusted shade that passes WCAG AA |

## Quality Checks

- All `--lx-*` CSS variables populated (no fallback `unset` values):
  - `--lx-accent-color`, `--lx-accent-color-hover`
  - `--lx-text-color`, `--lx-text-muted`
  - `--lx-bg-color`, `--lx-bg-surface`, `--lx-surface-alt`
  - `--lx-border-color`
  - `--lx-font-heading`, `--lx-font-body`
- Logo URL accessible (not 404, correct MIME type)
- Fonts from Google Fonts or brand CDN (valid URL)
- Color contrast WCAG AA: 4.5:1 for normal text, 3:1 for large text
- If extracted colors fail contrast: suggest adjustment with passing alternative
- At least one product visible in catalog
- Test section renders without validation errors

## Deprecated Tools (DO NOT USE)

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via Shopify OAuth onboarding, not MCP |


## section-library

# Quick Section Insert

Insert common section patterns into existing pages — one section at a time, matched to the page's existing brand style. NOT full page generation.

## When to Use

- Adding a single section to an existing page (NOT building a full page from scratch)
- User requests a specific section type by name (hero, FAQ, testimonials, etc.)
- Filling a gap in page structure (e.g., "add social proof between hero and product")
- Quick iteration on page layout without regenerating the whole page

## Prerequisites

- Target page must already exist (use `page-generation` skill for new pages)
- Brand kit should be configured (read it to match styles)
- Know the desired position (before/after which section, or index)

## Flow

### 1. Identify target page

```
find_page({ query: "page name or slug" })
```

Or user specifies page by name/ID directly.

### 2. Read current page structure + brand context

```
get_page({ page_id })
```

```
inspect_page_sections({ page_id })
```

- Note existing section IDs, order, and style patterns
- Identify where new section fits in the narrative flow

### 3. Read brand kit for style matching

```
get_brand_kit
```

- Extract colors, fonts, spacing to match new section to existing page
- All generated CSS must use `--lx-*` variables, never hardcoded hex values

### 4. Select section type from reference table (below)

If the section uses an island component, read its schema:

```
vibe://schema/island/{IslandName}
```

- Get required props, variants, and configuration options
- Ensure props match the island's expected shape exactly

### 5. Generate section HTML (single section, not full page)

- Match existing page's color usage, font sizes, spacing
- Use `--lx-*` CSS custom properties from brand kit (not hardcoded values)
- Include responsive breakpoints (mobile-first: 320px, 768px, 1024px, 1440px)
- For islands: use `data-island="Name" data-props='JSON'` pattern
- For plain HTML: use Tailwind classes + inline style with CSS variables

### 6. Preview the section update (dry-run)

```
preview_section_update({ page_id, section_id: null, html, css, position })
```

- Dry-run to verify it won't break page layout
- Check for conflicts with existing sections

### 7. Insert section into page

```
update_page_section({ page_id, section_id: null, html, css, position })
```

- `null` section_id = "add new" (not update existing)
- Position formats: `"before:{section_id}"`, `"after:{section_id}"`, or numeric index

### 8. Visual verify updated page

Navigate to the page preview URL and verify:
- New section renders correctly
- No layout breakage in surrounding sections
- Mobile responsive (no horizontal scroll)
- Islands hydrated (interactive elements working)
- Colors and fonts match the rest of the page

## Section Reference Table

| Section Type | Island | Position Hint | Key Pattern |
|---|---|---|---|
| Hero (full-bleed) | none (HTML) | first | bg-image + overlay text + CTA button |
| Hero (split) | none (HTML) | first | 2-col: image + text/CTA |
| Product Showcase | ProductGallery + BuyBox | after hero | split layout, gallery left, buy right |
| Testimonials/Reviews | ReviewCarousel | mid-page | card carousel, star ratings |
| FAQ Accordion | FAQ | before footer | collapsible Q&A, schema.org markup |
| Trust Badge Row | TrustBadgeBar | after hero or before CTA | 3-5 icons with short labels |
| Newsletter Signup | EmailCapture | before footer | centered, single input + button |
| Feature Grid | none (HTML) | mid-page | 3-col, icon + heading + description |
| Comparison Table | none (HTML) | mid-page | responsive table, checkmarks |
| CTA Banner | none (HTML) | near bottom | full-width colored band, button |
| Product Carousel | EditorialProductGrid | mid-page | horizontal scroll, 3-4 visible |
| Video Embed | none (HTML) | mid-page | 16:9 aspect ratio container |
| Stats/Counter Row | none (HTML) | after hero | 3-4 big numbers + labels |
| Logo/Press Bar | none (HTML) | after hero | "As seen in" horizontal logos |
| Announcement Bar | AnnouncementBar | very first (position 0) | dismissible top banner |

## Position Guidelines

| Position Rule | Rationale |
|---|---|
| Trust/social proof: within 1 scroll of primary CTA | Reduces friction at decision point |
| FAQ: always before footer | Captures "almost convinced" visitors with objection handling |
| Newsletter: before footer, after main content | Low-commitment conversion for non-buyers |
| Announcement: always position 0 (top of page) | Urgency/promo visibility before scroll |
| Product grid: mid-page for discovery, below fold for cross-sell | Context-dependent placement |

## HTML Template Pattern (for non-island sections)

```html
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="font-family: var(--lx-font-heading); color: var(--lx-text-color)">
      Section Title
    </h2>
    <!-- Content here -->
  </div>
</section>
```

## Island Section Pattern

```html
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div data-island="ReviewCarousel" data-props='{"provider":"shopify","productId":"gid://shopify/Product/123","layout":"cards","columns":3}'></div>
  </div>
</section>
```

Key rules for islands:
- Always use `data-island="Name"` attribute (exact casing from catalog)
- Always use `data-props='JSON'` with single quotes wrapping valid JSON
- Read `vibe://schema/island/{name}` before generating to get correct prop shape
- Never nest islands inside each other

## Quality Bar

- Section matches existing page typography (same heading sizes, body font)
- Colors use `--lx-*` CSS custom properties from brand kit (not hardcoded hex)
- Responsive: works at 320px, 768px, 1024px, 1440px breakpoints
- Proper spacing: consistent with adjacent sections (no jarring gaps)
- Islands have valid props matching their schema exactly
- Page still valid after insertion (no layout breaks)
- Section has a unique, kebab-case ID
- No horizontal scroll introduced on mobile
- Images use proper aspect ratios and lazy loading
- CTA buttons meet WCAG AA contrast (4.5:1 min)

## Deprecated Tools (DO NOT USE)

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via Shopify OAuth onboarding, not MCP |


