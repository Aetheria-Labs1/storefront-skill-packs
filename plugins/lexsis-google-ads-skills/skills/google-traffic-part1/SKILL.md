---
name: google-traffic-part1
description: Google traffic arrives with **INTENT**. They searched. They typed keywords. They're already interested — your job is to **answer immediately**. (Part 1 of 2)
---

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
