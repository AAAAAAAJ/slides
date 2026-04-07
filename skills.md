# OpenClaw Skill - Style Prompt Studio

Generate multi-style PPT slides using nanobanana2 (gemini-3.1-flash-image-preview).

## Quick Start

```bash
# Install skill
npx skills add https://github.com/AAAAAAAJ/slides

# Or use the skill directly in Claude Code
@style-prompt-studio
```

## Usage

### Step 1: Copy Prompt
Copy any style prompt from [PROMPTS.md](PROMPTS.md)

### Step 2: Customize
Modify text content as needed

### Step 3: Generate
Paste into nanobanana2 (gemini-3.1-flash-image-preview)

## Available Styles

| Style | Description |
|-------|-------------|
| `retro-pop` | 70s magazine aesthetic, thick outlines, geometric decorations |
| `minimal` | Clean white background, generous whitespace, corporate look |
| `cyberpunk` | Dark background, neon glow, futuristic UI |
| `neo-brutalism` | Raw design, bold colors, 4px outlines |
| `acid-graphics` | Y2K aesthetic, metallic chrome, liquid shapes |
| `modern-minimal-pop` | Instagram pastel, star bursts, Swiss influence |
| `swiss-international` | Geometric blocks, diagonal typography, Helvetica |
| `dark-editorial` | Black background, white dots, NYT style |
| `design-blueprint` | Figma style, cyan grid, technical UI |
| `neo-brutalist-ui` | Dashboard UI, card layout, SaaS aesthetic |
| `y2k-pixel-retro` | 90s pixel art, CRT monitors, VT323 font |
| `bento-grid` | Rounded modular card matrix for product and KPI slides |
| `scrapbook-diy` | Handmade collage, tape, stickers, handwritten notes |
| `aurora-ui` | Premium dark mesh-gradient AI-native interface aesthetic |
| `glassmorphism-light` | Airy frosted-glass cards on blurred gradient background |
| `dark-glassmorphism` | Smoked glass control-plane aesthetic for AI and SaaS |
| `frutiger-aero` | Glossy 2000s eco-tech utopian glass-and-sky language |
| `claymorphism` | Chunky toy-like 3D cards with soft shadows and candy colors |
| `classic-deep-skeuomorphism` | Pre-iOS7 leather, metal, glass, and tactile dashboard feel |

## Recommended Settings

- **Model**: `gemini-3.1-flash-image-preview` (nanobanana2)
- **Resolution**: `2048*1152` (2K 16:9)
- **Aspect Ratio**: `16:9`

## Example Prompts

### Retro Pop Style
```
Retro pop art style PPT slide, 1970s magazine aesthetic, flat design with thick black outlines, cream beige background, bold title text, subtitle below, key statistics displayed as cards, Salmon pink #FF6B6B, sky blue #4ECDC4, mustard yellow #FFD93D, mint green #6BCB77 accents, Geometric decorations: quarter circles, concentric rings, star bursts, Bold sans-serif typography, Professional presentation design, 16:9
```

### Minimalist Clean Style
```
Minimalist clean design PPT slide, White background, generous whitespace, centered title text, subtitle below, key stats in simple cards, Subtle gray and blue accents, Thin elegant lines, Inter Helvetica font, Professional corporate presentation, Simple elegant layout, 16:9
```

## Core Capabilities

> 你擅长将复杂专业知识转化为干货内容

- 🔍 **深度搜索平台高赞笔记** - 快速提炼爆款逻辑
- 📝 **擅长总结和比喻** - 让复杂主题通俗易懂
- 🎨 **多用图形化表现** - 视觉优先，提升理解
- 📊 **数据说话策略** - 每个模块包含具体数字
- 💬 **金句总结** - 必要时展示关键洞察

## Content Guidelines

| Element | Rule | Example |
|---------|------|---------|
| Title | ≤8 words | "What is Y Combinator" |
| Subtitle | ≤12 words | "Startup Accelerator" |
| Stats | 3-5 data points | "2005, 4000+, $600B" |
| Whitespace | 30% | - |

## Files

- [README.md](README.md) - Main documentation with image gallery
- [PROMPTS.md](PROMPTS.md) - All 19 style prompts (copy from here)
- [skill.json](skill.json) - OpenClaw skill configuration
- [CLAUDE.md](CLAUDE.md) - Skill context for Claude

## License

MIT License
