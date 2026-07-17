# Organic Blob Shapes

SVG clip-path shapes for creating organic, non-rectangular hero sections. Uses `clipPathUnits="objectBoundingBox"` for responsive scaling.

## When to Use

- Hero sections that need to feel organic/natural (not boxy)
- Lifestyle brands, beach/outdoor, wellness, DTC
- Section dividers with wavy edges
- Testimonial/quote callout shapes
- Any section where hard edges feel too corporate

## Quick Reference

See `reference/blob-shapes.md` for the full shape catalog (6 blob presets + 3 wave divider variants).

## Implementation Pattern

```html
<!-- Hidden SVG defines the shape -->
<svg width="0" height="0" aria-hidden="true">
  <defs>
    <clipPath id="unique-id" clipPathUnits="objectBoundingBox">
      <path d="M0.875,1 H0.124 ..."></path>
    </clipPath>
  </defs>
</svg>

<!-- Container gets clipped -->
<div style="clip-path: url(#unique-id); -webkit-clip-path: url(#unique-id); min-height: 95vh;">
  <!-- Background image + content overlay -->
</div>
```

## Shape Selection by Mood

| Mood | Shape | ID |
|------|-------|-----|
| Premium/minimal | Soft rounded blob | `blob-soft-rounded` |
| Editorial/fashion | Asymmetric organic | `blob-asymmetric` |
| Playful/DTC | Bubble top | `blob-bubble-top` |
| Natural/wellness | Wavy edges | `blob-wavy-subtle` |
| Tech/modern | Tight pill | `blob-tight-pill` |
| Testimonial | Speech bubble | `blob-speech` |

## Wavy Section Dividers

For transitions between sections (instead of hard lines):

```html
<svg viewBox="0 0 1200 40" preserveAspectRatio="none" style="width:100%;height:40px;display:block">
  <path d="M0,40 C150,0 350,0 600,20 C850,40 1050,0 1200,10 L1200,0 L0,0 Z" fill="#ffffff"></path>
</svg>
```

## Rules

- Always include `-webkit-clip-path` for Safari
- Use unique IDs per section (avoid conflicts if multiple blobs on same page)
- Keep container `min-height` set — clip-path on 0-height elements breaks
- No dark overlay needed if image contrast is already good
- Pair with generous margins (20px+ on sides) so the blob shape is visible against the page bg
