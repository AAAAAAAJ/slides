# Style Prompt Studio

> Generate multi-style PPT slides with AI - Direct prompts for nanobanana2

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Core Capabilities

* **Expert at transforming complex professional knowledge into digestible content**
* **Deep search platform upvoted notes** - Quickly extract viral content logic
* **Skilled in summarization and analogies** - Make complex topics accessible
* **Visual-first approach** - Leverage graphics for better comprehension
* **Data-driven strategy** - Include specific numbers in each module when needed
* **Golden quotes summary** - Highlight key takeaways when necessary

---

## Quick Start (No Code Required)

### Step 1: Copy a Prompt
Copy any style prompt from [PROMPTS.md](PROMPTS.md)

### Step 2: Customize
Replace placeholders with your content:
- `{title}` → Your title
- `{subtitle}` → Your subtitle
- `{stats}` → Your data points

### Step 3: Generate
Paste into **nanobanana2** (gemini-3.1-flash-image-preview) and generate!

---

## Recommended Settings

| Setting | Value |
|---------|-------|
| **Model** | `gemini-3.1-flash-image-preview` (nanobanana2) |
| **Resolution** | `2048*1152` (2K 16:9) |
| **Aspect Ratio** | `16:9` |

---

## 11 Available Styles

| # | Style | Best For |
|---|-------|----------|
| 1 | Retro Pop Art | Creative showcases, brand decks |
| 2 | Minimalist Clean | Business presentations, corporate |
| 3 | Cyberpunk Neon | Tech topics, futuristic themes |
| 4 | Neo-Brutalism | Artistic expression, bold statements |
| 5 | Acid Graphics Y2K | Trendy content, youth audience |
| 6 | Modern Minimal Pop | Social media, lightweight content |
| 7 | Swiss International | Professional decks, high-end |
| 8 | Dark Editorial | Deep analysis, commentary |
| 9 | Design Blueprint | Technical docs, product specs |
| 10 | Neo-Brutalist UI | SaaS products, dashboard demos |
| 11 | Y2K Pixel Retro | Nostalgic themes, creative projects |

---

## Content Guidelines

### Title
- Max 8 words
- Bold and clear

### Subtitle
- Max 12 words
- One line explanation

### Key Stats
- 3-5 data points max
- Use specific numbers

### Visual Balance
- Leave 30% whitespace
- Font hierarchy: Title > Subtitle > Stats > Decorations

---

## Example Usage

### Input Prompt (Retro Pop Style)
```
Retro pop art style PPT slide, 1970s magazine aesthetic, flat design with thick black outlines, cream beige background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Stats: 2005, 4000+ companies, $600B valuation, Salmon pink, sky blue, mustard yellow, mint green accents, Geometric decorations, Bold typography, Professional presentation, 16:9
```

### Just paste this into nanobanana2!

---

## Project Structure

```
slides/
├── README.md           # This file
├── PROMPTS.md          # All 11 style prompts (copy from here)
├── styles/             # Style configurations (JSON)
└── demos/yc-intro/     # Example outputs
    ├── SHOWCASE.md
    └── images/         # 22 generated samples
```

---

## Full Prompts Reference

See **[PROMPTS.md](PROMPTS.md)** for all 11 style prompts ready to copy-paste.

---

## Tips for Best Results

1. **Be specific** - "thick black outlines" works better than "bold lines"
2. **Always specify 16:9** - For PPT format
3. **Limit text** - AI handles short text better
4. **Use color names + hex** - "salmon pink #FF6B6B"
5. **Iterate** - Small prompt tweaks = different results

---

## Links

- **GitHub**: https://github.com/AAAAAAAJ/slides
- **302.ai**: https://302.ai/
- **API Docs**: https://doc.302.ai/

---

## License

MIT License - See [LICENSE](LICENSE) for details
