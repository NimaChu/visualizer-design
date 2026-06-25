---
name: visualizer-design
version: 1.0.0
summary: "Codex-compatible SVG/HTML visual design system for professional diagrams, charts, interactive widgets, and illustrations."
triggers:
  - visualize
  - diagram
  - chart
  - draw
  - illustrate
  - "show me"
  - "画图"
  - "可视化"
  - "流程图"
  - "图表"
---

# Visualizer Design System

Produce professional SVG/HTML visuals: diagrams, charts, interactive widgets, and illustrations that Codex can return as Markdown, Mermaid, local files, or browser-previewable artifacts.

## When to Use

- User says "show me", "visualize", "diagram", "chart", "draw", "illustrate"
- Educational/teaching requests — diagrams make learning far more effective
- Comparing concepts where a visual is clearer than prose
- Architecture & systems design discussions
- Any spec that names a visual artifact ("comparison table of X vs Y", "state machine for Z")

## Core Principles

1. **Seamless**: visuals should feel native to the Codex response or generated artifact
2. **Flat**: no gradients, shadows, blur, or decorative effects. Clean flat surfaces only
3. **Compact**: show the essential visual, explain the rest in normal response text
4. **Separated**: prose belongs in the reply; the visual contains only visual content and necessary labels

## Codex Delivery Modes

Choose the smallest delivery mode that satisfies the request.

- **Markdown/Mermaid**: use Mermaid for standard flowcharts, ERDs, state machines, sequence diagrams, and architecture diagrams when custom polish is not required.
- **Inline code block**: return a fenced `svg` or `html` block when the user wants source they can inspect or reuse.
- **Local SVG file**: write a `.svg` file in the workspace for polished static diagrams, then provide a clickable absolute file link. When useful in the Codex desktop app, show the file with Markdown image syntax using the absolute path.
- **Local HTML file**: write a `.html` file for interactive controls, Chart.js, D3 maps, steppers, or multi-part widgets. If the artifact needs a server, start one and provide the local URL.
- **Data Analytics widget**: for quantitative charts backed by reviewed table data, prefer Codex's Data Analytics chart/report widgets when available and appropriate.

Do not use host-specific widget APIs. This skill is designed for Codex surfaces.

## Quick Reference

| Need | Read this file |
|------|---------------|
| Colors, typography, spacing, CSS variables | `references/design-tokens.md` |
| SVG structure, viewBox, classes, arrows | `references/svg-toolkit.md` |
| Flowcharts, structural diagrams, illustrations | `references/diagram-guide.md` |
| Interactive HTML widgets, steppers | `references/interactive-guide.md` |
| Chart.js bar/line/doughnut charts | `references/chart-guide.md` |
| D3 geographic choropleth maps | `references/map-guide.md` |
| Art and illustration style | `references/art-guide.md` |

## Execution Checklist

Before outputting any visual, verify:

- [ ] No comments in generated visual code unless required for maintainability
- [ ] No font-size below 11px
- [ ] No emoji — use CSS shapes or SVG paths
- [ ] No gradients/shadows/blur (exception: one gradient allowed for illustrative diagrams)
- [ ] SVG viewBox is `"0 0 680 H"` (680 is fixed width)
- [ ] Every `<path>`/`<polyline>` connector has `fill="none"`
- [ ] Arrow marker included in `<defs>` if using arrows
- [ ] Text has `dominant-baseline` and `text-anchor`
- [ ] HTML has `<h2 class="sr-only">` or SVG has `<title>`/`<desc>` for accessibility
- [ ] No DOCTYPE, `<html>`, `<head>`, or `<body>` tags
- [ ] External CDN only from: cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net, unpkg.com
