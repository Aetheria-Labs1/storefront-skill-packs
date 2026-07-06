---
name: meta-traffic-part1
description: Storefront Design Intelligence (Part 1 of 3)
---

# Meta Ads → Landing Page — Storefront Design Intelligence

> **When to load**: Page generated from Meta (Facebook/Instagram) ad creative.  
> **Auto-loads as**: `vibe://skills/traffic-source-meta`

---

## The #1 Rule: Message Match

Meta traffic arrives **interrupted** — they were scrolling feed, not searching. The #1 conversion killer is message discontinuity between ad and landing page.

### Exact Match (Best for Direct Response)
Ad headline: "Finally, a yoga mat that doesn't slip during downward dog"  
Page headline: "Finally, a yoga mat that doesn't slip during downward dog"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
  Finally, a yoga mat that doesn't slip during downward dog
</h1>
<p class="text-lg mt-3" style="color:var(--lx-text-muted)">
  Join 47,000+ yogis who switched to the GripFlow™ non-slip surface
</p>
```

### Evolved Match (Best for Product Pages)
Ad headline: "The yoga mat your feet won't slide on"  
Page headline: "Meet the GripFlow™ Yoga Mat"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
  Meet the GripFlow™ Yoga Mat
</h1>
<p class="text-xl mt-4" style="color:var(--lx-text-muted)">
  The non-slip surface that keeps you locked in—even in hot yoga
</p>
```

### Visual Continuity
If the ad shows **product on pink background** → hero must match:

```html
<section class="relative min-h-[85vh] flex items-center" 
  style="background:linear-gradient(to bottom, #FFE5F0 0%, #FFFFFF 100%)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- Product hero content -->
  </div>
</section>
```

If the ad shows **bold sans-serif headline** → page font must match:

```css
:root {
  --lx-font-heading: 'Inter', system-ui, sans-serif;
}
```

**Ad CTA color = page CTA color:**

```css
:root {
  --lx-accent-color: #FF6B6B;  /* Extracted from ad creative */
}
```

---

## Mobile-First Reality

**85%+ of Meta ad traffic is mobile.** Every design decision must pass the "thumb-zone test."

### Typography for Mobile
All text uses fluid sizing:

```html
<!-- Hero headline -->
<h1 style="font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;letter-spacing:-0.02em;font-weight:700">
  Your yoga mat won't slip anymore
</h1>

<!-- Subline -->
<p style="font-size:clamp(1.125rem,3vw,1.375rem);line-height:1.4;margin-top:1rem">
  The GripFlow™ surface stays locked—even in hot yoga
</p>

<!-- Body copy -->
<p style="font-size:clamp(1rem,2.5vw,1.125rem);line-height:1.6">
  No more adjusting your hands mid-flow. No more slipping in downward dog.
</p>
```

### Spacing for Mobile
Use `clamp()` for all vertical spacing:

```html
<section style="padding-top:clamp(2rem,8vw,5rem);padding-bottom:clamp(2rem,8vw,5rem)">
  <!-- Section content -->
</section>
```

### Tap Targets & Thumb Zone
**All CTAs: min 44px height, large tap area**

```html
<!-- Primary CTA -->
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold transition-colors"
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white">
  Get yours now
</button>

<!-- Sticky CTA (thumb zone) -->
<div data-island="StickyBar" data-props='{
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "60-day guarantee"
}'></div>
```

---

## Section Sequence (The Meta Formula)

This is the **proven sequence for cold Meta traffic** (no brand familiarity, interrupted state):

### 1. Hero (Message Match + Immediate Trust)
**Why first**: 3-second decision window.

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-2xl mx-auto text-center space-y-5">
    <!-- Trust bar (immediate) -->
    <div class="flex justify-center items-center gap-2 text-sm">
      <div class="flex">
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="font-semibold" style="color:var(--lx-text-color)">4.9/5 from 12,847 reviews</span>
    </div>

    <!-- Headline (message match) -->
    <h1 class="font-bold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
      Your yoga mat won't slip anymore
    </h1>

    <!-- Subline -->
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTA -->
    <button class="px-8 py-4 rounded-lg font-semibold" 
      style="background:var(--lx-accent-color);color:white">
      Get yours now
    </button>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Yoga Mat" 
      class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

### 2. Trust Strip (Immediately After Hero)
**Why second**: Meta traffic has ZERO brand equity.

```html
<section class="py-8 border-b" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- shield icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">60-Day Guarantee</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Love it or return it</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- truck icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Free Shipping</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">On all US orders</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- star icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">12,847 5-Star Reviews</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Rated Excellent</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- award icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Featured in Yoga Journal</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Best Mat 2025</p>
      </div>
    </div>
  </div>
</section>
```

### 3. Problem Agitation
**Why third**: Twist the knife before showing solution.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Sick of yoga mats that work against you?
    </h2>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Slipping during downward dog</h3>
        <p style="color:var(--lx-text-muted)">You adjust your hands 5 times per flow</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Sweaty palms = zero grip</h3>
        <p style="color:var(--lx-text-muted)">Hot yoga becomes a safety hazard</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Cheap mats fall apart</h3>
        <p style="color:var(--lx-text-muted)">You've replaced yours 3 times already</p>
      </div>
    </div>
  </div>
</section>
```

### 4. Solution (The Reveal)
**Why fourth**: Now they're primed.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto px-4">
    <div class="text-center mb-12">
      <h2 class="font-bold mb-4" 
        style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
        Meet the GripFlow™ Yoga Mat
      </h2>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        Engineered to solve every problem you just nodded at
      </p>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <!-- Feature 1 -->
      <div class="text-center space-y-4">
        <img src="texture-closeup.jpg" alt="GripFlow surface" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">GripFlow™ Non-Slip Surface</h3>
        <p style="color:var(--lx-text-muted)">
          Proprietary texture that gets grippier as you sweat
        </p>
      </div>

      <!-- Feature 2 -->
      <div class="text-center space-y-4">
        <img src="thickness-demo.jpg" alt="6mm cushion" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">6mm Cushion Core</h3>
        <p style="color:var(--lx-text-muted)">
          Knee-saving thickness without sacrificing stability
        </p>
      </div>

      <!-- Feature 3 -->
      <div class="text-center space-y-4">
        <img src="durability.jpg" alt="Lifetime warranty" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">Lifetime Durability</h3>
        <p style="color:var(--lx-text-muted)">
          Won't peel, crack, or fade—backed by lifetime warranty
        </p>
      </div>
    </div>
  </div>
</section>
```

### 5. Social Proof (Overcome Skepticism)
**Why fifth**: Flood them with proof.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      47,000+ yogis upgraded their practice
    </h2>

    <div class="grid md:grid-cols-3 gap-6">
      <!-- Review 1 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "I've tried 8 different mats. This is the only one that doesn't slip during hot yoga. The grip actually gets better when I sweat. Insane."
        </p>
        <div class="flex items-center gap-3">
          <img src="sarah-avatar.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Sarah M.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "Replaced my Manduka after 5 years. Should've done it sooner. The cushion is perfect—my knees don't hurt anymore."
        </p>
        <div class="flex items-center gap-3">
          <img src="mike-avatar.jpg" class="w-10 h-10 rounded-full" alt="Mike T." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Mike T.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny"
        </p>
        <div class="flex items-center gap-3">
          <img src="emma-avatar.jpg" class="w-10 h-10 rounded-full" alt="Emma L." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Emma L.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 6. Stats & Authority
**Why sixth**: Quantify the transformation.

```html
<section class="py-16 border-y" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-5xl mx-auto px-4">
    <div class="grid md:grid-cols-3 gap-8 text-center">
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">47K+</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Happy Customers</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">4.9/5</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Average Rating</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">99%</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Recommend to Friends</p>
      </div>
    </div>
  </div>
</section>
```

### 7. FAQ (Objection Handling)
**Why seventh**: Address the 5 questions stopping them.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-3xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Questions?
    </h2>

    <div data-island="FAQ" data-props='{
      "items": [
        {
          "question": "What's your return policy?",
          "answer": "60-day money-back guarantee. If you don't love it, return it for a full refund—no questions asked."
        },
        {
          "question": "How long does shipping take?",
          "answer": "All orders ship within 24 hours. Free 2-3 day shipping in the US."
        },
        {
          "question": "Is this really better than Manduka/Liforme?",
          "answer": "The GripFlow™ surface is proprietary. It's physics-tested to grip better as you sweat—other mats get slippery."
        },
        {
          "question": "What if I don't like it?",
          "answer": "Full refund within 60 days. We'll even cover return shipping."
        },
        {
          "question": "Do you have different colors/sizes?",
          "answer": "Yes! Available in 5 colors and 2 sizes (standard + XL). All colors have the same GripFlow™ surface."
        }
      ],
      "style": "minimal"
    }'></div>
  </div>
</section>
```

### 8. Final CTA (Last Chance)
**Why eighth**: They scrolled this far—remove all friction.

```html
<section style="padding:clamp(3rem,8vw,5rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto px-4 text-center space-y-6">
    <h2 class="font-bold" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Your last slippery yoga mat
    </h2>
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who upgraded to GripFlow™
    </p>
    <button class="w-full sm:w-auto px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Get my mat now
    </button>
    <div class="flex justify-center items-center gap-4 text-sm" style="color:var(--lx-text-muted)">
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- shield --></svg>
        60-day guarantee
      </span>
      <span>•</span>
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- truck --></svg>
        Free shipping
      </span>
    </div>
  </div>
</section>
```

---
