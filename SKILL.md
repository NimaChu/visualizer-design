---
name: visualizer-design
description: Create polished local HTML, inline SVG, Mermaid, and markdown visuals for explaining complex information in agent chat or browser artifacts. Use when the user asks to visualize, draw, show a diagram, chart, flow, architecture, process, comparison, timeline, concept map, state machine, or asks to explain a concept, principle, workflow, lifecycle, mechanism, system design, or "how X works" where structure would be clearer visually. Also trigger for Chinese requests like 可视化, 画图, 图解, 流程, 原理, 工作机制, 工作流程, 架构, 对比, 解释一下. Choose the output format by host and need: Codex can use inline/local SVG or Mermaid when supported; OpenCode should default to a local HTML artifact and open it in the browser because its chat UI does not render SVG or Mermaid inline.
---

# Visualizer Design System

Produce professional visuals that agents can return directly in chat or as local artifacts: local HTML files, inline SVG, Mermaid, lightweight HTML fragments, local SVG files, charts, maps, and compact markdown tables.

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

Choose the smallest delivery mode that satisfies the request, host, and rendering surface. Do not force one format when another is clearer or more reliable.

### Host-aware defaults

- **OpenCode**: default to a local `.html` artifact for visual explanations. OpenCode chat does not reliably render fenced SVG or Mermaid inline. Write a complete HTML file containing inline SVG/CSS/JS as needed, open it in the user's default browser, and keep the final response concise.
- **Codex desktop**: use inline fenced SVG when the user wants source in chat; use a local `.svg` file plus a file link or Markdown image when a polished reusable visual is better; use local HTML for interaction, Chart.js, D3 maps, steppers, or multi-part widgets.
- **Other chat hosts**: prefer markdown tables for simple comparisons, Mermaid only when the host supports it, and fenced SVG only when the host can render or the user wants source.

### Format routing

- **Local HTML file**: default for visual explanations in OpenCode, and for any interactive artifact. Embed SVG directly in the HTML so it opens without a build step. If the artifact needs a server, start one and provide the local URL.
- **Inline fenced SVG**: use when the chat host can render SVG inline or when the user explicitly wants reusable SVG source. Use for polished diagrams, architecture maps, timelines, concept maps, state machines, comparison visuals, and explanatory illustrations.
- **Local SVG file**: use for polished static diagrams that need reuse, screenshotting, iteration, or Codex desktop image display.
- **Mermaid**: use for simple canonical flowcharts, ERDs, state machines, and sequence diagrams only when the host supports Mermaid or the user explicitly asks for Mermaid source. Do not use Mermaid merely because a diagram has arrows.
- **Markdown table**: use for simple comparisons when a table is clearer and lighter than a diagram.
- **Inline HTML fragment**: use only when the user needs source they can inspect or reuse. Keep it as a fragment, not a full document.

Do not use host-specific widget APIs unless the current environment explicitly provides them and the user wants that output. For OpenCode, favor local HTML artifacts plus browser opening. For chat-only fallback, use markdown tables or compact ASCII diagrams.

## SVG Preference Heuristics

Prefer SVG as the internal drawing format when any of these are true. In OpenCode, place the SVG inside a local HTML artifact; in Codex, choose inline SVG or a local SVG file based on the request.

- The user asks for a visual explanation of a concept, principle, system, workflow, or mechanism
- The answer would otherwise need multiple paragraphs to describe relationships, feedback loops, layers, or actors
- The visual benefits from spatial grouping, emphasis, annotations, or a polished teaching style
- The user says "可视化解释", "图解", "解释工作原理", "工作机制", or similar phrasing

If you say you will create a visual, create a rendered visual artifact appropriate to the host. Do not leave OpenCode users with only SVG or Mermaid source unless they explicitly requested source code.

## OpenCode Browser Workflow

When creating a visual artifact in OpenCode:

1. Write a local `.html` file in the current workspace or a clearly named output location.
2. Embed the visual directly in the file with inline SVG, CSS, and lightweight JavaScript when needed.
3. Open the file in the default browser after creation. On Windows, use `Start-Process -FilePath "<absolute-path-to-file.html>"`.
4. In the final answer, state the file path and mention that it was opened. If browser launch fails, give the path and the exact command the user can run.

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
- [ ] Inline HTML fragments do not include DOCTYPE, `<html>`, `<head>`, or `<body>` tags; local `.html` files may include a complete document when useful
- [ ] External CDN only from: cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net, unpkg.com
