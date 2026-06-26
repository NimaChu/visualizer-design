---
name: visualizer-design
description: Create polished inline SVG and lightweight HTML visuals for explaining complex information in agent chat. Use when the user asks to visualize, draw, show a diagram, chart, flow, architecture, process, comparison, timeline, concept map, state machine, or asks to explain a concept, principle, workflow, lifecycle, mechanism, system design, or "how X works" where structure would be clearer visually. Also trigger for Chinese requests like 可视化, 画图, 图解, 流程, 原理, 工作机制, 工作流程, 架构, 对比, 解释一下. Choose the output format by need; use direct fenced SVG as a strong default for static custom visual explanations in OpenCode/Codex, Mermaid for simple canonical diagrams, markdown tables for simple comparisons, and local HTML for interactive artifacts.
---

# Visualizer Design System

Produce professional visuals that agents can return directly in chat or as local artifacts: inline SVG, Mermaid, lightweight HTML, local SVG files, local HTML files, charts, maps, and compact markdown tables.

## When to Use

- User says "show me", "visualize", "diagram", "chart", "draw", "illustrate", "画图", "可视化", "流程图", or "图表"
- User asks to explain a concept, principle, workflow, lifecycle, mechanism, architecture, comparison, or "how X works"
- User says "解释一下", "工作原理", "工作机制", "工作流程", "图解", "架构", "流程", "对比", or similar Chinese phrasing
- Educational/teaching requests — diagrams make learning far more effective
- Comparing concepts where a visual is clearer than prose
- Architecture & systems design discussions
- Any spec that names a visual artifact ("comparison table of X vs Y", "state machine for Z")

## Core Principles

1. **Seamless**: visuals should feel native to the Codex response or generated artifact
2. **Flat**: no gradients, shadows, blur, or decorative effects. Clean flat surfaces only
3. **Compact**: show the essential visual, explain the rest in normal response text
4. **Separated**: prose belongs in the reply; the visual contains only visual content and necessary labels

## Delivery Modes

Choose the smallest delivery mode that satisfies the request. Do not force one format when another is clearer or more reliable.

- **Inline fenced SVG**: strong default for static custom visuals in chat. Use for polished diagrams, architecture maps, timelines, concept maps, state machines, comparison visuals, and explanatory illustrations.
- **Mermaid**: use for simple canonical flowcharts, ERDs, state machines, and sequence diagrams when the host supports Mermaid and the standard syntax is enough. Do not use Mermaid merely because a diagram has arrows; if the request is a visual explanation of a concept or mechanism, prefer inline SVG.
- **Markdown table**: use for simple comparisons when a table is clearer and lighter than a diagram.
- **Inline HTML fragment**: use only when the user needs source they can inspect or reuse. Keep it as a fragment, not a full document.
- **Local SVG file**: write a `.svg` file for polished static diagrams that need reuse, screenshotting, or iteration.
- **Local HTML file**: write a `.html` file for interactive controls, Chart.js, D3 maps, steppers, or multi-part widgets. If the artifact needs a server, start one and provide the local URL.

Do not use host-specific widget APIs unless the current environment explicitly provides them and the user wants that output. For OpenCode/Codex chat, favor portable direct-rendering formats: markdown tables, Mermaid when supported, and fenced SVG.

## SVG Preference Heuristics

Prefer inline fenced SVG when any of these are true:

- The user asks for a visual explanation of a concept, principle, system, workflow, or mechanism
- The answer would otherwise need multiple paragraphs to describe relationships, feedback loops, layers, or actors
- The visual benefits from spatial grouping, emphasis, annotations, or a polished teaching style
- The user says "可视化解释", "图解", "解释工作原理", "工作机制", or similar phrasing

If you say you will output SVG, output SVG in the final answer. Do not announce SVG and then switch to Mermaid or plain markdown.

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

## Validation

For local `.svg` files, run `scripts/check-svg.py <file.svg>` before final delivery. For inline SVG, mentally apply the same checks before answering.

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
