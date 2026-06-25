# Interactive HTML Widget Guide

## When to use HTML vs SVG
- **HTML**: interactive controls (sliders, buttons, live state displays, charts, steppers)
- **SVG**: static diagrams, flowcharts, illustrations

## Patterns

### Pattern 1: Interactive Explainer
- Use HTML for controls — sliders, buttons, live state displays, charts
- No card wrapper — whitespace is the container
- Use standard event handlers for local interactivity. Do not depend on host-specific chat callbacks.
- Keep prose explanations in normal response text, not embedded in HTML

### Pattern 2: Compare Options
- Use `repeat(auto-fit, minmax(160px, 1fr))` for grid
- Featured card: `border: 2px solid var(--color-border-info)` (the only scenario where 2px border is allowed)
- Badge: `background: var(--color-background-info); color: var(--color-text-info); font-size: 12px`

### Pattern 3: Data Record
- Wrap in a single raised card
- Avatar/initials circle: 44px, `background: var(--color-background-info)`, `color: var(--color-text-info)`, `font-weight: 500`

```html
<div style="background: var(--color-background-primary); border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 1rem 1.25rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
    <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--color-background-info); display: flex; align-items: center; justify-content: center; font-weight: 500; font-size: 14px; color: var(--color-text-info);">MR</div>
    <div>
      <p style="font-weight: 500; font-size: 15px; margin: 0;">Maya Rodriguez</p>
      <p style="font-size: 13px; color: var(--color-text-secondary); margin: 0;">VP of Engineering</p>
    </div>
  </div>
</div>
```

## Steppers (for cycles and sequential processes)
- Keep the initial static content useful before JavaScript runs
- JS-driven steppers are fine for local HTML artifacts
- For cycles: HTML stepper with position indicator (`* o o`). Next wraps from last stage back to first
- Never draw cycles as rings in SVG

## Layout Patterns
- **Editorial** (explanatory content): no card wrapper, prose flows naturally
- **Card** (bounded objects like contact records): single raised card wraps the whole thing
- **Grid**: use `minmax(0, 1fr)` to clamp overflow
- **Table overflow**: use `table-layout: fixed` in constrained layouts (<=700px)
- Don't put tables in HTML widgets — output them as markdown in response text

## Metric Cards
- `background: var(--color-background-secondary)`, no border, `border-radius: var(--border-radius-md)`, padding 1rem
- Muted 13px label above, 24px/500 number below
- Use in grids of 2-4 with `gap: 12px`

## Accessibility
- Begin HTML widgets with a visually-hidden `<h2 class="sr-only">` containing a one-sentence summary

## Render Order
- `<style>` (short, under ~15 lines) -> content HTML -> `<script>` last
- Prefer inline `style="..."` over large `<style>` blocks when that keeps the fragment easier to inspect

## Hard Rules
- No DOCTYPE, `<html>`, `<head>`, `<body>` tags — just content fragments
- No `position: fixed`
- No comments in code
- No font-size below 11px
- No emoji
- No gradients/shadows/blur
- External CDN only from: cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net, unpkg.com
