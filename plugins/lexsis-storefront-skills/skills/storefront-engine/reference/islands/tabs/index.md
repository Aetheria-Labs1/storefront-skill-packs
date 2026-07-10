# Tabs — Island Directory

Tabbed content organizer for product details, specs, ingredients, and multi-section content.

## Files

| File | Purpose |
|------|---------|
| `layouts/bordered.json` | Full bordered tab panel, bottom-border active indicator |
| `layouts/underline.json` | Minimal underline tabs, clean content area below |
| `layouts/pills.json` | Pill-shaped tab buttons (rounded-full), modern compact |

## Quick Reference

- **Variants**: bordered, underline, pills
- **Schema**: `vibe://schema/island/Tabs`
- **Layouts**: `vibe://islands/tabs/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place mid-page for organizing dense content (specs, ingredients, reviews, shipping)
- Pair with: BuyBox (tabs below for product details), FAQ (alternative to tabs)
- Bordered variant best for content-heavy panels (long descriptions)
- Pills variant best for short, scannable content (3-4 tabs max)
- Underline variant is the safest default for most pages
- Never nest tabs inside tabs; use accordion for sub-grouping
- defaultTab prop sets which tab opens first (0-indexed)
