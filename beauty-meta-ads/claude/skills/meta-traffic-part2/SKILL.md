---
name: meta-traffic-part2
description: Storefront Design Intelligence (Part 2 of 3)
---

## Hero Patterns for Meta Traffic

### Pattern 1: Social Proof Hero
**Best for**: High-review-count products

```html
<section class="relative min-h-[85vh] flex items-center px-4" style="background:white">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-semibold uppercase tracking-wide" style="color:var(--lx-accent-color)">
      Rated #1 Yoga Mat of 2025
    </p>

    <!-- Trust stars (prominent) -->
    <div class="flex justify-center items-center gap-2">
      <div class="flex">
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="text-lg font-bold" style="color:var(--lx-text-color)">4.9/5 stars (12,847 reviews)</span>
    </div>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em">
      The mat that finally grips
    </h1>

    <!-- Subline -->
    <p style="font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get yours now
      </button>
      <button class="px-8 py-4 rounded-lg font-semibold border" 
        style="border-color:var(--lx-border-color);color:var(--lx-text-color)">
        Watch 60-sec review
      </button>
    </div>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Mat" class="w-full max-w-lg mx-auto rounded-lg" />

    <!-- Trust badges -->
    <div class="flex flex-wrap justify-center gap-6 text-sm pt-4">
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- users --></svg>
        <span>47,000+ customers</span>
      </span>
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- shield --></svg>
        <span>60-day money-back guarantee</span>
      </span>
    </div>
  </div>
</section>
```

### Pattern 2: Video Hero
**Best for**: Demo-heavy products

```html
<section class="relative min-h-[90vh] flex items-center" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4 space-y-6">
    <!-- Video -->
    <div data-island="VideoPlayer" data-props='{
      "video_url": "grip-test-demo.mp4",
      "autoplay": true,
      "loop": true,
      "muted": true,
      "controls": true,
      "aspect_ratio": "16:9"
    }'></div>

    <!-- Content below video -->
    <div class="text-center space-y-4">
      <h1 class="font-bold leading-[1.1]" 
        style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
        Watch it grip in real-time
      </h1>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        The surface that gets better as you sweat
      </p>
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get my GripFlow mat
      </button>
      <div class="flex justify-center gap-4 text-sm pt-2">
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <span>4.9/5 stars</span>
        </span>
        <span>•</span>
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4"><!-- truck --></svg>
          <span>Free 2-day shipping</span>
        </span>
      </div>
    </div>
  </div>
</section>
```

### Pattern 3: UGC-Style Hero
**Best for**: Facebook, high authenticity

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:#FAFAFA">
  <div class="max-w-5xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-center">
      <!-- Real customer photo -->
      <img src="customer-selfie-with-mat.jpg" alt="Customer photo" 
        class="w-full rounded-lg shadow-lg" />

      <!-- Content -->
      <div class="space-y-5">
        <h1 class="font-semibold leading-[1.15]" 
          style="font-family:var(--lx-font-body);font-size:clamp(1.75rem,5vw,3rem)">
          "This mat changed my practice"
        </h1>
        <p class="text-lg" style="color:var(--lx-text-muted)">
          — Sarah M., verified customer (+ 46,999 others)
        </p>
        <button class="w-full md:w-auto px-8 py-4 rounded-lg font-semibold" 
          style="background:var(--lx-accent-color);color:white">
          Try it risk-free
        </button>
        <div class="flex flex-wrap gap-4 text-sm pt-2">
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
            <span>60-day guarantee</span>
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
            <span>4.9/5 from 12,847 reviews</span>
          </span>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Pattern 4: Countdown Urgency Hero
**Best for**: Sales/launches

```html
<section class="relative min-h-[85vh] flex items-center px-4" 
  style="background:linear-gradient(to bottom, #FEF3C7 0%, #FFFFFF 100%)">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-bold uppercase tracking-wide" style="color:#B45309">
      Limited Time: Launch Sale
    </p>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
      40% off ends tonight
    </h1>

    <!-- Subline -->
    <p class="text-xl" style="color:var(--lx-text-muted)">
      The GripFlow mat at its lowest price ever
    </p>

    <!-- Countdown -->
    <div data-island="CountdownTimer" data-props='{
      "end_time": "2026-12-31T23:59:59Z",
      "headline": "Sale ends in:",
      "style": "minimal",
      "size": "large"
    }'></div>

    <!-- CTA -->
    <button class="px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Claim my 40% off
    </button>

    <!-- Product image -->
    <img src="product-hero.jpg" alt="GripFlow Mat" class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

---

## Trust Stacking (Critical for Cold Traffic)

Meta traffic has **ZERO brand familiarity**. Trust must be immediate, overwhelming, and specific.

### The Trust Stack (All 3 Layers)

#### Layer 1: Hero Trust Bar
```html
<div class="flex flex-wrap justify-center gap-4 text-sm">
  <span class="flex items-center gap-2 font-semibold">
    <div class="flex">
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    </div>
    <span>4.9/5 (12,847 reviews)</span>
  </span>
  <span class="flex items-center gap-2 font-semibold">
    <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
    <span>60-Day Guarantee</span>
  </span>
</div>
```

#### Layer 2: Persistent Trust Badge Bar
```html
<div data-island="TrustBadgeBar" data-props='{
  "position": "top_sticky",
  "badges": [
    {"icon": "star", "text": "4.9/5 (12,847)", "color": "gold"},
    {"icon": "shield_check", "text": "60-Day Guarantee", "color": "blue"},
    {"icon": "truck", "text": "Free Shipping", "color": "green"},
    {"icon": "award", "text": "Yoga Journal Pick", "color": "purple"}
  ],
  "layout": "scroll",
  "background": "white"
}'></div>
```

#### Layer 3: Social Proof Popup
```html
<div data-island="SocialProofPopup" data-props='{
  "position": "bottom_left",
  "events": [
    {"type": "purchase", "name": "Sarah from NYC", "product": "GripFlow Mat", "time": "2 min ago"},
    {"type": "review", "name": "Mike from LA", "rating": 5, "time": "5 min ago"},
    {"type": "purchase", "name": "Emma from Austin", "product": "GripFlow Mat", "time": "8 min ago"}
  ],
  "interval": 8000,
  "show_delay": 3000,
  "style": "minimal"
}'></div>
```

### Trust Signal Hierarchy

**Tier 1 (Hero)**: Star rating + review count, customer count, guarantee  
**Tier 2 (Trust Strip)**: Free shipping, press mentions, security badges  
**Tier 3 (Section 5)**: Detailed testimonials with photos, before/after, expert endorsements

---

## Social Proof (UGC > Polished)

Meta traffic trusts **authentic > polished**.

### UGC-Style Reviews (Facebook)
```html
<div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid #E5E7EB">
  <!-- Stars -->
  <div class="flex">
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
  </div>

  <!-- Review text (casual tone) -->
  <p style="color:#1F2937;font-size:0.9375rem;line-height:1.5">
    okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny
  </p>

  <!-- Author -->
  <div class="flex items-center gap-3">
    <img src="customer-selfie.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
    <div>
      <p class="font-semibold text-sm">Sarah M.</p>
      <p class="text-xs" style="color:#6B7280">Verified Buyer • New York, NY</p>
    </div>
  </div>

  <!-- Optional: customer photo with product -->
  <img src="review-photo-in-use.jpg" class="w-full rounded-lg mt-3" alt="Customer photo" />
</div>
```

### Specific Numbers > Vague Claims

❌ "Thousands of happy customers"  
✅ "47,482 customers (and counting)"

❌ "Highly rated"  
✅ "4.9/5 stars from 12,847 verified reviews"

❌ "Fast shipping"  
✅ "Ships in 24 hours • Arrives in 2-3 days"

---

## CTA Strategy (Single Goal, Repeat 3x)

### The Rule: One Conversion Goal
All CTAs point to the same action.

**Single product**: "Get my GripFlow mat"  
**Multi-product**: "Shop yoga mats"  
**Lead gen**: "Get my free guide"

### Benefit-Driven CTA Copy

❌ Generic: "Shop now" / "Buy now"  
✅ Benefit-driven:
- "Get my GripFlow mat"
- "Solve my slipping problem"
- "Try it risk-free"
- "Claim my 40% off"

### CTA Placement (3x Rule)

**CTA #1: Hero**
```html
<button class="px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get my GripFlow mat
</button>
```

**CTA #2: After Social Proof**
```html
<div class="text-center space-y-4">
  <h3 class="font-bold text-2xl">Ready to upgrade?</h3>
  <button class="px-8 py-4 rounded-lg font-semibold" 
    style="background:var(--lx-accent-color);color:white">
    Get yours now
  </button>
  <p class="text-sm" style="color:var(--lx-text-muted)">60-day guarantee • Free shipping</p>
</div>
```

**CTA #3: Sticky Bar**
```html
<div data-island="StickyBar" data-props='{
  "position": "bottom",
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "Free shipping • 60-day guarantee"
}'></div>
```

### Mobile CTA Sizing
```html
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold" 
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white;font-size:1rem">
  Get yours now
</button>
```

---

## Urgency for Meta Traffic (Use Sparingly)

### When to Use Urgency
✅ Real sale with deadline  
✅ Limited inventory (< 50 units)  
✅ Launch window  
✅ Seasonal cutoff

❌ Fake scarcity  
❌ Persistent urgency

### CountdownTimer
```html
<div data-island="CountdownTimer" data-props='{
  "end_time": "2026-12-31T23:59:59Z",
  "headline": "Sale ends in:",
  "style": "minimal",
  "show_labels": true,
  "size": "large"
}'></div>
```

### Inventory Indicator
```html
<div data-island="InventoryIndicator" data-props='{
  "threshold": 50,
  "text": "Only {count} left in stock",
  "style": "warning"
}'></div>
```

---

## Mobile Patterns

### Container Padding
```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Content -->
</div>
```

### Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Grid items -->
</div>
```

### Full-Width CTA on Mobile
```html
<button class="w-full sm:w-auto px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get yours now
</button>
```

### Stack on Mobile
```html
<div class="flex flex-col sm:flex-row gap-4">
  <button>Primary CTA</button>
  <button>Secondary CTA</button>
</div>
```

---
