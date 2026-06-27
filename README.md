# visualizer-design

Host-aware visual design skill for agents. It helps Codex, OpenCode, and similar coding agents turn explanation requests into polished SVG, HTML, Mermaid, chart, map, and markdown visual artifacts.

The skill is intentionally lightweight: it is not a rendering service or a framework. It is a set of routing rules, design tokens, SVG conventions, and validation checks that tell an agent when to use each visual format and how to make the result feel clean, compact, accessible, and reusable.

## Why use it

Agents are good at explaining in prose, but many topics become clearer as a diagram: workflows, system architecture, lifecycle states, tradeoffs, mechanisms, charts, maps, and "how this works" explanations. `visualizer-design` gives the agent a repeatable visual language instead of improvising a new diagram style every time.

Use it when a user asks to:

- visualize, draw, diagram, chart, or illustrate something
- explain a principle, workflow, system, architecture, mechanism, or lifecycle
- compare options where spatial grouping is clearer than paragraphs
- create a local visual artifact that can be opened, reused, or iterated on
- handle Chinese prompts such as `可视化`, `画图`, `图解`, `流程`, `原理`, `工作机制`, `架构`, or `对比`

## What it produces

The skill chooses the smallest reliable output format for the current host and request:

| Need | Preferred output |
| --- | --- |
| Polished explanation in Codex chat | Inline fenced SVG or local SVG |
| OpenCode visual explanation | Local HTML artifact opened in the browser |
| Interactive controls, steppers, Chart.js, or D3 maps | Local HTML |
| Standard flowchart, ERD, state machine, or sequence diagram | Mermaid, when the host supports it |
| Simple comparison | Markdown table |
| Reusable static visual | Local SVG file plus validation |

## Host-aware behavior

- **Codex desktop**: use inline SVG when chat-readable source is useful, local SVG when the visual should be reusable, and local HTML for interactive artifacts.
- **OpenCode**: default to a local `.html` file because its chat UI may not render fenced SVG or Mermaid reliably.
- **Other hosts**: prefer markdown tables, Mermaid, SVG source, or local files based on what the host can render.

The skill deliberately avoids relying on host-specific widget APIs unless the current environment explicitly provides one and the user wants that output.

## Design principles

- **Seamless**: visual output should feel native to the response or artifact.
- **Flat**: clean surfaces, simple strokes, no decorative blur or shadows.
- **Compact**: show the structure visually and keep explanation in normal prose.
- **Accessible**: include SVG titles/descriptions and useful fallbacks.
- **Validated**: local SVG files can be checked with the included validator.

## Repository layout

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- art-guide.md
|   |-- chart-guide.md
|   |-- design-tokens.md
|   |-- diagram-guide.md
|   |-- interactive-guide.md
|   |-- map-guide.md
|   `-- svg-toolkit.md
`-- scripts/
    `-- check-svg.py
```

## Install

Clone or copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/NimaChu/visualizer-design.git ~/.codex/skills/visualizer-design
```

If you already copied it manually, update with:

```bash
cd ~/.codex/skills/visualizer-design
git pull --ff-only origin main
```

Restart Codex after installing or updating so the skill registry is refreshed.

## Quick start

Ask your agent for a visual explanation:

```text
Use visualizer-design to explain how this skill routes a diagram request.
```

For Codex, a good response may include inline SVG directly in chat. For OpenCode, a good response should usually create and open a local HTML artifact.

## Validation

For local SVG files, run:

```bash
python3 scripts/check-svg.py path/to/visual.svg
```

The validator checks the key SVG rules used by this skill, including the fixed `680` viewBox width, accessibility metadata, readable font sizes, connector fills, and arrow marker requirements.

## Authoring workflow

1. Read `SKILL.md`.
2. Select the output mode from the delivery routing rules.
3. Read only the relevant reference guide.
4. Generate the visual artifact.
5. Validate local SVG files with `scripts/check-svg.py`.
6. Keep the final answer concise and link to any generated local files.

## License

No license has been declared yet. Treat the repository as all rights reserved until a license file is added.
