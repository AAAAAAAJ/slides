#!/usr/bin/env python3
"""
YC Introduction Demo - Generate all 11 styles
Uses 302.ai Seedream 4.0 API
"""

import os
import requests
import base64
from pathlib import Path
import time

API_KEY = os.getenv("API_KEY", "sk-G6kKNWh3MNrKzCfLIjJzt8MzFTIt8acHbPtPqcaNNFMtGVeW")
API_BASE = "https://api.302.ai"

OUTPUT_DIR = Path(__file__).parent / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

STYLES = [
    {"name": "01-retro-pop", "display": "Retro Pop Art",
     "prompt_en": "Retro pop art style PPT presentation slide, 1970s magazine aesthetic, flat design with thick black outlines, cream beige background, Large title text: What is Y Combinator, Subtitle: Startup Accelerator, Statistics: 2005, 4000+ companies, 600B valuation, Salmon pink, sky blue, mustard yellow, mint green accents, Geometric decorations, Bold sans-serif typography, Professional slide design",
     "prompt_cn": "复古波普艺术风格 PPT 幻灯片，70 年代杂志美学，平涂设计配粗黑边框，米色背景，大标题文字：什么是 Y Combinator，副标题：创业加速器，统计数据：2005 年成立，4000+ 公司，$600B 估值，鲑鱼粉、天空蓝、芥末黄、薄荷绿配色，几何装饰，粗体无衬线字体，专业幻灯片设计"},

    {"name": "02-minimal", "display": "Minimalist Clean",
     "prompt_en": "Minimalist clean design PPT slide, White background, generous whitespace, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Stats: 2005, 4000+, $600B, Subtle gray and blue accents, Thin elegant lines, Professional corporate presentation, Simple elegant layout",
     "prompt_cn": "极简主义设计 PPT 幻灯片，白色背景，大量留白，标题文字：什么是 Y Combinator，副标题：创业加速器，数据：2005、4000+、$600B，微妙灰色和蓝色点缀，细雅线条，专业企业幻灯片，简洁优雅布局"},

    {"name": "03-cyberpunk", "display": "Cyberpunk Neon",
     "prompt_en": "Cyberpunk neon style PPT slide, Dark charcoal background, Title text: What is Y Combinator with neon glow, Subtitle: Startup Accelerator, Neon colors: magenta cyan yellow, Tech grid patterns, circuit decorations, Holographic data panels, glow effects, Futuristic UI elements, Digital presentation aesthetic",
     "prompt_cn": "赛博朋克霓虹风格 PPT 幻灯片，深色木炭背景，标题文字：什么是 Y Combinator 配霓虹发光效果，副标题：创业加速器，霓虹配色：品红、青色、黄色，科技网格图案，电路装饰，全息数据面板，发光效果，未来主义 UI 元素，数字化演示美学"},

    {"name": "04-neo-brutalism", "display": "Neo-Brutalism",
     "prompt_en": "Neo-brutalism style PPT slide, raw design, Cream background, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Bold primary colors: red blue yellow, Thick 4px black outlines, hard shadows, Brutalist frames, bold typography, Stark contrast",
     "prompt_cn": "新粗野主义风格 PPT 幻灯片，原始设计，奶油色背景，标题文字：什么是 Y Combinator，副标题：创业加速器，大胆原色：红色蓝色黄色，4px 粗黑边框，硬阴影，粗野主义框架，粗体排版，强烈对比"},

    {"name": "05-acid-graphics", "display": "Acid Graphics Y2K",
     "prompt_en": "Acid graphics Y2K style PPT slide, Light gray background, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Metallic chrome elements, holographic accents, Colors: purple pink mint gold, Liquid shapes, star sparkles, mesh gradients, Y2K aesthetic, futuristic design",
     "prompt_cn": "酸性图形 Y2K 风格 PPT 幻灯片，浅灰背景，标题文字：什么是 Y Combinator，副标题：创业加速器，金属铬元素，全息点缀，配色：紫色粉色薄荷绿金色，液态形状，星形闪光，网格渐变，Y2K 美学，未来主义设计"},

    {"name": "06-modern-minimal-pop", "display": "Modern Minimal Pop",
     "prompt_en": "Modern minimal pop art PPT slide, Instagram aesthetic, Pastel background, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Pastel colors: mint cream coral purple, Star burst graphics, thin line circles, Tilted color blocks, small arrows, Clean sans-serif typography, Swiss design influence",
     "prompt_cn": "现代极简波普艺术 PPT 幻灯片，Instagram 美学，柔和粉彩背景，标题文字：什么是 Y Combinator，副标题：创业加速器，粉彩色：薄荷绿奶油黄珊瑚橙紫色，星爆图形，细线圆圈，倾斜色块，小型箭头，干净无衬线字体，瑞士设计影响"},

    {"name": "07-swiss-international", "display": "Swiss International",
     "prompt_en": "Swiss international style PPT slide, brutalist graphic design, Light gray background, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Bold geometric color blocks, diagonal typography, High saturation colors: blue green yellow purple pink orange, Helvetica font, Asymmetric composition",
     "prompt_cn": "瑞士国际主义风格 PPT 幻灯片，粗野主义平面设计，浅灰背景，标题文字：什么是 Y Combinator，副标题：创业加速器，大胆几何色块，斜向排版，高饱和度配色：蓝绿黄紫粉橙，Helvetica 字体，非对称构图"},

    {"name": "08-dark-editorial", "display": "Dark Editorial",
     "prompt_en": "Dark editorial PPT slide, New York Times style, Black background with white dot grid, Title text: What is Y Combinator, Subtitle: Startup Accelerator, White text, orange accent, Minimalist wireframe illustrations, Serif typography, Dramatic negative space, Newspaper aesthetic",
     "prompt_cn": "暗黑编辑出版风格 PPT 幻灯片，纽约时报风格，黑色背景配白色点阵网格，标题文字：什么是 Y Combinator，副标题：创业加速器，白色文字，橙色点缀，极简线框插画，衬线字体，戏剧性留白，报纸美学"},

    {"name": "09-design-blueprint", "display": "Design Blueprint",
     "prompt_en": "Design blueprint PPT slide, Figma documentation style, White background with cyan grid lines, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Figma selection boxes, Annotation lines, numbered labels, Technical UI mockup, Clean sans-serif font",
     "prompt_cn": "设计蓝图风格 PPT 幻灯片，Figma 文档风格，白色背景配青色网格线，标题文字：什么是 Y Combinator，副标题：创业加速器，Figma 选择框，标注线，编号标签，技术 UI 模型，干净无衬线字体"},

    {"name": "10-neo-brutalist-ui", "display": "Neo-Brutalist UI",
     "prompt_en": "Neo-brutalist UI PPT slide, dashboard interface, Cream background, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Pastel panels: mint yellow lavender, Thick 3px black outlines, Card-based layout, flat colors, Bold typography, stat cards, SaaS dashboard",
     "prompt_cn": "新粗野主义 UI PPT 幻灯片，仪表板界面，奶油色背景，标题文字：什么是 Y Combinator，副标题：创业加速器，柔和色板：薄荷绿黄色淡紫色，3px 粗黑边框，卡片布局，平涂色彩，粗体排版，数据卡片，SaaS 仪表板"},

    {"name": "11-y2k-pixel-retro", "display": "Y2K Pixel Retro",
     "prompt_en": "Y2K pixel retro PPT slide, 1990s aesthetic, Dark background with noise texture, Title text: What is Y Combinator, Subtitle: Startup Accelerator, Bright colors: yellow orange green, Pixel art computer icons, CRT monitor graphics, Isometric tech, Pixel font, Vintage 1990s design",
     "prompt_cn": "Y2K 像素复古风格 PPT 幻灯片，1990 年代美学，深色背景配噪点纹理，标题文字：什么是 Y Combinator，副标题：创业加速器，明亮配色：黄色橙色绿色，像素艺术电脑图标，CRT 显示器图形，等距技术，像素字体，复古 1990 年代设计"},
]


def generate_image(prompt, output_path):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "prompt": prompt,
        "size": "1920*1080",
        "enable_base64_output": True,
        "enable_sync_mode": True
    }

    try:
        response = requests.post(f"{API_BASE}/ws/api/v3/bytedance/seedream-v4", headers=headers, json=payload, timeout=120)
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 200 and "data" in result:
                data = result["data"]
                if "outputs" in data and len(data["outputs"]) > 0:
                    img_data_uri = data["outputs"][0]
                    if img_data_uri.startswith("data:image"):
                        b64_data = img_data_uri.split(",", 1)[1]
                        with open(output_path, "wb") as f:
                            f.write(base64.b64decode(b64_data))
                        return True
        return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False


def main():
    print("=" * 60)
    print("YC Introduction Demo - 11 Styles × 2 Languages = 22 Images")
    print("=" * 60)

    generated = 0
    failed = 0

    for style in STYLES:
        for lang, prompt in [("en", style["prompt_en"]), ("cn", style["prompt_cn"])]:
            output_path = OUTPUT_DIR / f"{style['name']}-{lang}.png"
            print(f"\n🎨 Generating: {style['display']} ({lang})...")
            if generate_image(prompt, output_path):
                print(f"   ✅ Saved: {output_path}")
                generated += 1
            else:
                print(f"   ❌ Failed")
                failed += 1
            time.sleep(2)

    print(f"\n{'='*60}")
    print(f"Complete! Success: {generated}, Failed: {failed}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
