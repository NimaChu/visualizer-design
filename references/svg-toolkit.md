# SVG Toolkit

## Setup Rules
- viewBox fixed to `"0 0 680 H"`. **680 must not change** — it is the basis for all coordinate calculations
- `width="100%"` on root `<svg>`
- H = bottommost element + 20px. Do not guess — calculate from actual coordinates
- Safe area: x=40 to x=640, y=40 to y=(H-40)
- Background: transparent (host provides the bg)
- One SVG per output unless the user explicitly asks for a multi-visual artifact
- No rotated text
- Use 0.5px strokes for diagram borders and edges
- Every `<path>` or `<polyline>` used as a connector MUST have `fill="none"`

## Pre-built Classes

| Class | Description |
|-------|-------------|
| `t` | sans 14px primary |
| `ts` | sans 12px secondary |
| `th` | sans 14px medium (500) |
| `box` | neutral rect (bg-secondary fill, border stroke) |
| `node` | clickable group with hover effect |
| `arr` | arrow line (1.5px, open chevron head) |
| `leader` | dashed leader line (tertiary stroke, 0.5px) |
| `c-{ramp}` | colored node — apply to `<g>` or rect/circle/ellipse (not paths) |

## Arrow Marker (must include in every SVG `<defs>` if using arrows)

```svg
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
```

## Node Examples

### Single-line node (44px height)
```svg
<g class="node c-blue">
  <rect x="100" y="20" width="180" height="44" rx="8" stroke-width="0.5"/>
  <text class="th" x="190" y="42" text-anchor="middle" dominant-baseline="central">T-cells</text>
</g>
```

### Two-line node (56px height)
```svg
<g class="node c-blue">
  <rect x="100" y="20" width="200" height="56" rx="8" stroke-width="0.5"/>
  <text class="th" x="200" y="38" text-anchor="middle" dominant-baseline="central">Dendritic cells</text>
  <text class="ts" x="200" y="56" text-anchor="middle" dominant-baseline="central">Detect foreign antigens</text>
</g>
```

## Accessibility
- SVG widgets use `role="img"` with `<title>` and `<desc>` as first children

## Hard Rules
- No `<!-- comments -->` in code
- No font-size below 11px
- No emoji — use CSS shapes or SVG paths
- No gradients/shadows/blur (exception: one gradient for illustrative diagrams)
- No dark/colored backgrounds on outer containers (transparent only)
- No `position: fixed`
- No DOCTYPE, `<html>`, `<head>`, `<body>` tags
- External CDN only from: cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net, unpkg.com
