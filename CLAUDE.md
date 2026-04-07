# CLAUDE.md - Style Prompt Studio

## Project Overview

Generate multi-style PPT slides using nanobanana2 (gemini-3.1-flash-image-preview).

## Core Capabilities

> 你擅长将复杂专业知识转化为干货内容

- 🔍 **深度搜索平台高赞笔记** - 快速提炼爆款逻辑
- 📝 **擅长总结和比喻** - 让复杂主题通俗易懂
- 🎨 **多用图形化表现** - 视觉优先，提升理解
- 📊 **数据说话策略** - 每个模块包含具体数字
- 💬 **金句总结** - 必要时展示关键洞察

## Quick Usage

```bash
# No code required - copy prompts directly from PROMPTS.md
# 1. Copy prompt from PROMPTS.md
# 2. Replace {title}, {subtitle}, {stats}
# 3. Paste into nanobanana2
```

## API Settings

- **Model**: `gemini-3.1-flash-image-preview` (nanobanana2)
- **Resolution**: `2048*1152` (2K 16:9)
- **Endpoint**: `/google/v1/models/gemini-3.1-flash-image-preview:predict`

## 19 Styles

1. `retro-pop` - 70s magazine aesthetic
2. `minimal` - Clean corporate look
3. `cyberpunk` - Dark futuristic
4. `neo-brutalism` - Bold raw design
5. `acid-graphics` - Y2K metallic
6. `modern-minimal-pop` - Instagram pastel
7. `swiss-international` - Swiss design
8. `dark-editorial` - NYT review style
9. `design-blueprint` - Figma doc style
10. `neo-brutalist-ui` - Dashboard UI
11. `y2k-pixel-retro` - 90s pixel art
12. `bento-grid` - Modular card matrix
13. `scrapbook-diy` - Handmade collage vibe
14. `aurora-ui` - Premium AI mesh-gradient interface
15. `glassmorphism-light` - Airy frosted-glass cards
16. `dark-glassmorphism` - Smoked glass control-plane aesthetic
17. `frutiger-aero` - Glossy optimistic 2000s tech-utopia
18. `claymorphism` - Chunky playful 3D cards
19. `classic-deep-skeuomorphism` - Leather, metal, glass, tactile retro UI

## Content Guidelines

| Element | Rule | Example |
|---------|------|---------|
| Title | ≤8 words | "What is Y Combinator" |
| Subtitle | ≤12 words | "Startup Accelerator" |
| Stats | 3-5 data points | "2005, 4000+, $600B" |
| Whitespace | 30% | - |
| Hierarchy | Title > Subtitle > Stats | - |

## File Structure

```
slides/
├── README.md           # Main documentation
├── PROMPTS.md          # All 19 style prompts
├── skill.json          # OpenClaw skill config
├── styles/             # JSON style configs
└── demos/yc-intro/images/  # 22 sample outputs
```

## Commands

```bash
# View all prompts
cat PROMPTS.md

# View generated samples
ls demos/yc-intro/images/

# Push updates
git add -A && git commit -m "message" && git push
```
