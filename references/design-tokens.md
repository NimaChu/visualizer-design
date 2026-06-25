# Design Tokens

## Philosophy
- **Seamless**: Visuals blend into the host UI
- **Flat**: No gradients, mesh backgrounds, noise textures, or decorative effects
- **Compact**: Show the essential inline. Explain the rest in text

## Typography
- h1 = 15px, h2 = 14px, h3 = 13px — all `font-weight: 500`
- Body text = 13px, weight 400, `line-height: 1.6`
- **Two weights only: 400 regular, 500 bold.** Never use 600 or 700
- No font-size below 11px
- Sentence case always. Never Title Case, never ALL CAPS

## Font size calibration (SVG)

| Text | Chars | Weight | Size | Rendered width |
|------|-------|--------|------|----------------|
| Title | 12 | 500 | 14px | ~88px |
| Subtitle | 16 | 400 | 13px | ~104px |
| Body | 24 | 400 | 13px | ~156px |
| Caption | 20 | 400 | 12px | ~120px |

Box width formula: `rect_width = max(title_chars * 7, subtitle_chars * 6) + 24`

## CSS Variables

| Category | Variables |
|----------|-----------|
| Backgrounds | `--color-background-primary` (white), `-secondary` (surfaces), `-tertiary` (page bg), `-info`, `-danger`, `-success`, `-warning` |
| Text | `--color-text-primary` (black), `-secondary` (muted), `-tertiary` (hints), `-info`, `-danger`, `-success`, `-warning` |
| Borders | `--color-border-tertiary` (0.15 alpha, default), `-secondary` (0.3 alpha, hover), `-primary` (0.4 alpha), semantic variants |
| Typography | `--font-sans`, `--font-serif`, `--font-mono` |
| Layout | `--border-radius-md` (8px), `--border-radius-lg` (12px, preferred), `--border-radius-xl` (16px) |

## Color Palette (9 ramps x 7 levels)

Level meaning: 50=lightest fill, 100-200=light fills, 400=midtone, 600=accent/stroke, 800-900=text on light bg.

| Class | 50 | 100 | 200 | 400 | 600 | 800 | 900 |
|-------|----|-----|-----|-----|-----|-----|-----|
| c-purple | #EEEDFE | #CECBF6 | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |
| c-teal | #E1F5EE | #9FE1CB | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |
| c-coral | #FAECE7 | #F5C4B3 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |
| c-pink | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| c-gray | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| c-blue | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| c-green | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| c-amber | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| c-red | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

### Light/dark mode quick pick
- **Light mode**: 50 fill + 600 stroke + 800 title / 600 subtitle
- **Dark mode**: 800 fill + 200 stroke + 100 title / 200 subtitle

## Complexity Budget (hard limits)
- Box subtitles: <=5 words
- Colors: <=2 ramps per diagram
- Horizontal tier: <=4 boxes at full width (~140px each)

## UI Component Tokens
- Borders: always `0.5px solid var(--color-border-tertiary)` (or `-secondary` for emphasis)
- Corner radius: `var(--border-radius-md)` for most, `var(--border-radius-lg)` for cards
- Cards: white bg, 0.5px border, radius-lg, padding 1rem 1.25rem
- Form elements: pre-styled, write bare tags
- Round every displayed number (`Math.round()`, `.toFixed(n)`, `Intl.NumberFormat`)
- Spacing: rem for vertical rhythm, px for component-internal gaps

## Render Order
Structure code so static content remains useful before JavaScript runs:
- **HTML**: `<style>` (short) -> content HTML -> `<script>` last
- **SVG**: `<defs>` (markers) -> visual elements immediately
- Prefer inline `style="..."` over `<style>` blocks
- Keep `<style>` under ~15 lines
- No `<!-- comments -->` or `/* comments */`
