# Style Prompt Studio

> 为 PPT/幻灯片生成多风格视觉内容

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介

这是一个**PPT 幻灯片风格生成系统**，支持 11 种视觉风格，可批量生成中英文版本的设计稿。

---

## 快速开始

### 1. 准备环境

```bash
# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install requests
```

### 2. 设置 API Key

获取 302.ai API Key：https://app.inference.sh/settings/keys

```bash
export API_KEY="sk-your-api-key-here"
```

### 3. 运行生成脚本

```bash
cd demos/yc-intro
python generate.py
```

---

## 支持的 11 种风格

| 风格 | 描述 | 适用场景 |
|------|------|----------|
| Retro Pop Art | 70 年代复古波普 | 创意展示、品牌宣传 |
| Minimalist Clean | 极简主义 | 企业汇报、产品介绍 |
| Cyberpunk Neon | 赛博朋克霓虹 | 科技主题、未来感展示 |
| Neo-Brutalism | 新粗野主义 | 个性化表达、艺术展示 |
| Acid Graphics Y2K | 酸性设计/Y2K | 潮流内容、年轻受众 |
| Modern Minimal Pop | 现代极简波普 | 社交媒体、轻量内容 |
| Swiss International | 瑞士国际主义 | 专业设计、高端展示 |
| Dark Editorial | 暗黑编辑出版 | 深度内容、评论分析 |
| Design Blueprint | 设计蓝图 | 产品文档、技术说明 |
| Neo-Brutalist UI | 粗野主义 UI | 界面展示、SaaS 产品 |
| Y2K Pixel Retro | Y2K 像素复古 | 怀旧主题、创意内容 |

---

## 项目结构

```
slides/
├── README.md                 # 项目说明
├── styles/                   # 风格配置文件
│   ├── retro-pop.json
│   ├── minimal.json
│   ├── cyberpunk.json
│   ├── neo-brutalism.json
│   ├── acid-graphics.json
│   ├── modern-minimal-pop.json
│   ├── swiss-international.json
│   ├── dark-editorial.json
│   ├── design-blueprint.json
│   ├── neo-brutalist-ui.json
│   └── y2k-pixel-retro.json
├── demos/
│   └── yc-intro/             # YC 主题 Demo
│       ├── generate.py       # 生成脚本
│       ├── content.md        # 内容模板
│       ├── SHOWCASE.md       # 效果展示
│       └── images/           # 生成的图片
└── scripts/
    └── generate-batch.py     # 批量生成脚本
```

---

## 自定义内容

### 步骤 1：编辑内容模板

修改 `demos/yc-intro/content.md` 中的内容：

```markdown
# 标题
title_en: "Your Topic Here"
title_cn: "你的主题在这里"

# 副标题
subtitle_en: "A Brief Description"
subtitle_cn: "简短描述"

# 关键数据
stats:
  - label_en: "Founded"
    label_cn: "成立时间"
    value: "2024"
```

### 步骤 2：运行生成

```bash
python demos/yc-intro/generate.py
```

---

## 批量生成脚本

使用批量生成脚本一次性生成所有风格：

```bash
python scripts/generate-batch.py \
  --prompt "Your presentation title" \
  --styles all \
  --output ./output
```

---

## API 使用说明

### Seedream 4.0 (推荐)

```python
import requests

API_KEY = "sk-your-api-key"
prompt = "Your design prompt here"

response = requests.post(
    "https://api.302.ai/ws/api/v3/bytedance/seedream-v4",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "prompt": prompt,
        "size": "1920*1080",
        "enable_base64_output": True,
        "enable_sync_mode": True
    }
)

result = response.json()
image_data = result["data"]["outputs"][0]  # data:image/jpeg;base64,...
```

---

## 示例输出

查看 [demos/yc-intro/SHOWCASE.md](demos/yc-intro/SHOWCASE.md) 查看所有 11 种风格的生成效果。

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)
