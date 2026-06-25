# Art and Illustration Guide

Use SVG. Same technical rules (viewBox 680, safe area, transparent bg) but the aesthetic is different:

## Principles
- **Fill the canvas** — art should feel rich, not sparse
- **Bold colors**: mix text-color categories for variety (info blue, success green, warning amber)
- Art is the one place custom `<style>` color blocks are fine — freestyle colors, `prefers-color-scheme` for dark mode variants
- **Layer overlapping opaque shapes** for depth
- **Organic forms** with `<path>` curves, `<ellipse>`, `<circle>`
- **Texture via repetition** (parallel lines, dots, hatching) not raster effects
- **Geometric patterns** with `<g transform="rotate()">` for radial symmetry

## Difference from Diagrams
| Aspect | Diagrams | Art |
|--------|----------|-----|
| Fill | Sparse, structured | Dense, layered |
| Color | <=2 ramps, semantic | Freestyle, bold mixing |
| Custom styles | Minimize | Encouraged |
| Gradients | Forbidden (mostly) | Acceptable for artistic effect |
| Shapes | Rectilinear, precise | Organic, curved |

## Technical Rules (still apply)
- viewBox `"0 0 680 H"`
- Safe area: x=40 to x=640, y=40 to y=(H-40)
- No font-size below 11px
- No emoji
- No comments in code
- `role="img"` with `<title>` and `<desc>` for accessibility
