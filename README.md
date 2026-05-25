# Thomas Shang's Tufte-Style Book Template

A bilingual Tufte-style XeLaTeX book template — *English first, 中文版在后*.
This repository ships one English entry file, one Chinese entry file, one shared
style file, a palette-introduction generator script, and 24 swappable color
palettes. The template supports:

- English / Chinese bilingual mode switching
- XeLaTeX + xeCJK font mapping
- biblatex + biber bibliography workflow
- Tufte-style table of contents, title page, chapter titles, and sidenotes
- A palette mechanism aligned with the companion beamer template: `\OUCSetPalette{N}`
- 24 complete palettes — the 10 original base palettes plus 14 thematic palettes added by this project
- Pre-built English and Chinese sample PDFs ready to open without compiling

> Entry files: `Thomas-Tufte-book.tex` (English) and `Thomas-Tufte-book-zh.tex` (Chinese)
> Shared style: `Thomas-Tufte-bilingual-book.sty`
> Preview PDFs: `Thomas-Tufte-book.pdf` / `Thomas-Tufte-book-zh.pdf`

---

## Contents (English)

1. [File Structure](#file-structure)
2. [Prerequisites](#prerequisites)
3. [Quick Start](#quick-start)
4. [How to Compile](#how-to-compile)
5. [Core Interfaces](#core-interfaces)
6. [Palette Overview](#palette-overview)
7. [Contributing — Add Your Own Palette](#contributing--add-your-own-palette)
8. [Acknowledgements](#acknowledgements)

For the full bilingual palette quick-reference table and the detailed
philosophy-driven palette catalogue, scroll down to the Chinese section
[完整色版速查](#完整色版速查) and [附录：全部配色方案详述](#附录全部配色方案详述);
each entry already carries bilingual color names.

---

## File Structure

```text
Thomas Shang's Tufte-Style Book Template/
├── Thomas-Tufte-bilingual-book.sty    ← Shared style file; all template logic lives here
├── Thomas-Tufte-book.tex              ← English entry file
├── Thomas-Tufte-book-zh.tex           ← Chinese entry file
├── Thomas-Tufte-book.pdf              ← Pre-built English sample PDF (open directly)
├── Thomas-Tufte-book-zh.pdf           ← Pre-built Chinese sample PDF
├── palette-intro-en.tex               ← English palette-intro chapter (auto-generated; do not edit by hand)
├── palette-intro-zh.tex               ← Chinese palette-intro chapter (auto-generated; do not edit by hand)
├── gen_palette_intro.py               ← Generator script + source-of-truth data for the two files above
├── sample-handout.bib                 ← Local bibliography database
├── figure/                            ← Local figure assets
│   └── *.pdf                          ← Figures actually referenced by the templates
└── fonts/                             ← Bundled fallback fonts (system fonts take priority)
```

You normally only need to edit:

- `Thomas-Tufte-book.tex` — English content
- `Thomas-Tufte-book-zh.tex` — Chinese content

`Thomas-Tufte-bilingual-book.sty` should rarely be touched unless you want to
extend layout or font strategy. To add a new palette, follow the
[contributing](#contributing--add-your-own-palette) section and touch only
three well-marked interfaces.

---

## Prerequisites

This template **requires XeLaTeX**. The style file simultaneously uses
`fontspec`, `xeCJK`, and `biblatex[backend=biber]`, so the build environment
must provide:

- `xelatex`
- `biber`
- A complete TeX distribution (TeX Live full scheme or MiKTeX recommended)

### macOS

- MacTeX is recommended
- Most system fonts already satisfy the English and CJK fallback chains

### Windows

- TeX Live or MiKTeX recommended
- If you use MiKTeX, enable automatic installation of missing packages
- Make sure at least some of the following fonts are available:
  - English serif: Palatino Linotype / TeX Gyre Pagella / Times New Roman
  - Sans-serif: Helvetica Neue / TeX Gyre Heros / Arial
  - CJK: Source Han Serif SC / Noto Serif CJK SC / Songti SC / SimSun / Microsoft YaHei / SimHei / KaiTi / FangSong

### Linux

- Install `texlive-full` and `latexmk`
- Install `fonts-noto-cjk`

---

## Quick Start

1. Pick an entry file:
   - English: `Thomas-Tufte-book.tex`
   - Chinese: `Thomas-Tufte-book-zh.tex`
2. Update metadata:
   - `\title{...}`
   - `\date{...}`
   - `\author{...}`
   - `\publisher{...}`
3. Pick a palette:

```latex
\OUCSetPalette{7}  % 0..23
```

4. Use the semantic color names in the body:

```latex
{\color{primary}Primary emphasis}
{\color{accent}Deepest emphasis}
{\color{spotcolor}Theme spot color (e.g. Kyoto's vermilion)}
```

5. Compile to PDF.

---

## How to Compile

### Recommended: latexmk

English:

```bash
latexmk -xelatex Thomas-Tufte-book.tex
```

Chinese:

```bash
latexmk -xelatex Thomas-Tufte-book-zh.tex
```

### Manual multi-pass

English:

```bash
xelatex Thomas-Tufte-book.tex
biber   Thomas-Tufte-book
xelatex Thomas-Tufte-book.tex
xelatex Thomas-Tufte-book.tex
```

Chinese:

```bash
xelatex Thomas-Tufte-book-zh.tex
biber   Thomas-Tufte-book-zh
xelatex Thomas-Tufte-book-zh.tex
xelatex Thomas-Tufte-book-zh.tex
```

> Do **not** use `pdflatex`.
> If `xelatex` is not on your PATH, install a TeX distribution first.

---

## Core Interfaces

### Language

```latex
\newcommand{\BookLanguage}{english}
\SetBookLanguage{\BookLanguage}
```

Allowed values: `english`, `chinese`.

### Palette

```latex
\OUCSetPalette{N}
```

Where `N` is in the range `0..23`. The style file exposes:

- `oucpal1` … `oucpal6` — palette swatches, light to dark
- `primary` — defaults to `pal5`
- `accent` — defaults to `pal6`
- `paleblue` — defaults to `pal1`
- `spotcolor` — theme spot color; defaults to `accent`, becomes Kyoto's vermilion under the Kyoto theme

### Structured table headers

```latex
\booktableheadrow
\booktableheadcell{Header Text}
```

### Chapters and table of contents

Chapter titles, part/chapter labels, and page numbers in the ToC are already
wired into the palette system; no extra configuration needed.

---

## Palette Overview

There are 24 palettes (indices `0..23`). Each palette exposes six swatches
ordered light → dark; `primary = pal5`, `accent = pal6`. A quick-reference
table (with both English and Chinese palette names) is provided in the
[完整色版速查](#完整色版速查) section of the Chinese half — the palette names
and RGB triples are language-neutral and read identically to English readers.

The 14 thematic palettes (indices 10–23) each ship with a short
"color philosophy" paragraph in Chinese; these are intentionally cultural and
left in their original language. The pre-built PDFs include English
equivalents inside the *Palette Catalogue* chapter, which is auto-generated
from `gen_palette_intro.py`.

---

## Contributing — Add Your Own Palette

**This template is open. If you have tuned a six-color set for a book, a
painting, a city, or a memory, please send it back so the palette family can
keep growing.**

All edit points are marked with `===== ADD-A-PALETTE INTERFACE =====`
comment blocks; a single workspace search will locate them.

1. **`Thomas-Tufte-bilingual-book.sty`** — runtime palette logic
   - **Interface ①** — append one `\or` branch to `\OUCSetPalette`:
     ```latex
     \or
       \book@setpalettecolors{Your Palette Name}{R1,G1,B1}{R2,G2,B2}{R3,G3,B3}{R4,G4,B4}{R5,G5,B5}{R6,G6,B6}%
     ```
     Colors are listed light → dark and map to `pal1`…`pal6`.
   - **Interface ②** — append one line to `\bookpaletteguideentries`:
     ```latex
     \bookpaletteguideentry{N}{Your Palette Name}{R1,G1,B1}{R2,G2,B2}{R3,G3,B3}{R4,G4,B4}{R5,G5,B5}{R6,G6,B6}%
     ```
     `N` is the new index; this row appears in the palette quick-reference chapter.

2. **`gen_palette_intro.py`** — source data for the palette-intro chapter
   - **Interface ③** — append one `P.append(dict(...))` entry following the
     existing format (bilingual philosophy text + six-color table + per-color
     gloss).
   - Then run `python3 gen_palette_intro.py` to regenerate
     `palette-intro-zh.tex` and `palette-intro-en.tex`.

### Conventions

- **Color order:** light → dark. `pal1` is the lightest (backgrounds /
  sidebars), `pal6` the darkest (titles / strongest emphasis). The
  text-contrast rules and "lightest three / darkest three" display assume
  this order.
- **Color philosophy:** every palette should carry at least one short
  philosophy paragraph stating what it is trying to express. This is the
  tradition this project tries to preserve — more important than just a row
  of RGB triples.
- **Naming:** anchor English palette names to a concrete cultural reference
  (a painting, an album, a city, a literary reference). Chinese names should
  match the intended imagery rather than be a literal translation.
- **How to contribute:** fork → edit the three interfaces → run
  `python3 gen_palette_intro.py` → rebuild both demos → open a pull request.
  Or post the RGB values plus design notes in an issue and the maintainer
  will fold them in.

To **use** an existing palette, just write `\OUCSetPalette{N}` (N from 0 to 23)
in your entry file.

---

## Notes

- This repository is the public release of the `OUC-Haide-Book-Template`
  project, rebranded under the full name *Thomas Shang's Tufte-Style Book
  Template*.
- Both pre-built demo PDFs are included so the template's look-and-feel can
  be inspected without installing a TeX distribution.
- `palette-intro-{zh,en}.tex` are auto-generated from `gen_palette_intro.py`;
  edit the script and rerun it to amend palette commentary.
- The upstream beamer template and the original Tufte sample files are not
  redistributed here; see the links in *Acknowledgements* below.

---

## Acknowledgements

This template builds on several open-source projects:

- **Tufte-LaTeX** — origin of the `tufte-book` document class on which this
  template is based; the typographic foundation of the whole layout.
  <https://github.com/Tufte-LaTeX/tufte-latex>
- **OUC-Haide-Beamer-Template** — direct source of the palette mechanism and
  visual language; `\OUCSetPalette` and the palette family are inherited and
  extended from that beamer template.
  <https://github.com/Hatsuyuki017/OUC-Haide-Beamer-Template>
- **Mattia Puddu** — the VDQI-inspired title and contents page in his
  Tufte-style book layout directly inspired this template's front matter.
  <https://mattiapuddu25.github.io/index.html>

---

# 中文版 / Chinese Version

一套基于 Tufte 风格书籍版式重构的 XeLaTeX 双语图书模板。
本仓库提供英文与中文两个入口文件、一个共享样式文件、一个配色介绍生成脚本，以及 24 套可切换的配色方案。模板支持：

- 英文 / 中文双模式切换
- XeLaTeX + xeCJK 字体映射
- biblatex + biber 参考文献流程
- Tufte 风格目录、标题页、章节标题与边注体系
- 与 beamer 模板一致的 palette 机制：`\OUCSetPalette{N}`
- 24 套完整配色，包括原始 10 套基础 palette 和本项目扩展的 14 套主题 palette
- 预生成的英文 / 中文示例 PDF，可直接打开阅读模板的全部外观

> 入口文件：`Thomas-Tufte-book.tex`（英文）与 `Thomas-Tufte-book-zh.tex`（中文）
> 共享样式：`Thomas-Tufte-bilingual-book.sty`
> 预览 PDF：`Thomas-Tufte-book.pdf` / `Thomas-Tufte-book-zh.pdf`

---

## 目录

1. [文件结构](#文件结构)
2. [使用前提](#使用前提)
3. [快速开始](#快速开始)
4. [编译方式](#编译方式)
5. [核心接口](#核心接口)
6. [配色总览](#配色总览)
7. [完整色版速查](#完整色版速查)
8. [附录：全部配色方案详述](#附录全部配色方案详述)
9. [参与贡献：添加你自己的配色](#参与贡献添加你自己的配色)

---

## 文件结构

```text
Thomas Shang's Tufte-Style Book Template/
├── Thomas-Tufte-bilingual-book.sty       ← 共享样式文件，所有模板逻辑在此
├── Thomas-Tufte-book.tex                 ← 英文入口文件
├── Thomas-Tufte-book-zh.tex              ← 中文入口文件
├── Thomas-Tufte-book.pdf                 ← 预生成的英文示例 PDF（可直接打开预览）
├── Thomas-Tufte-book-zh.pdf              ← 预生成的中文示例 PDF
├── palette-intro-en.tex               ← 《配色介绍》章节的英文生成结果（自动生成，勿手改）
├── palette-intro-zh.tex               ← 《配色介绍》章节的中文生成结果（自动生成，勿手改）
├── gen_palette_intro.py               ← 上述两个文件的生成脚本 / 配色文案数据源
├── sample-handout.bib                 ← 本地参考文献数据库
├── figure/                            ← 本地图形资源目录
│   └── *.pdf                          ← 模板实际调用的示例图片
└── fonts/                             ← 随仓库随行的备选字体（备份用，系统字体优先）
```

你通常只需要编辑：

- `Thomas-Tufte-book.tex`：英文模式内容
- `Thomas-Tufte-book-zh.tex`：中文模式内容

一般不需要直接改动 `Thomas-Tufte-bilingual-book.sty`，除非你要继续扩展版式或字体策略；如果你只是要添加一组新配色，只需按本文末尾「参与贡献」一节的指引修改三处接口即可。

---

## 使用前提

本模板必须使用 XeLaTeX。样式文件中同时使用了 `fontspec`、`xeCJK` 与 `biblatex[backend=biber]`，因此编译环境必须同时具备：

- `xelatex`
- `biber`
- 一套完整的 TeX 发行版（推荐 TeX Live Full Scheme 或 MiKTeX）

### macOS

- 推荐安装 `MacTeX`
- 系统自带多数字体可直接命中模板的英文字体与 CJK fallback 链

### Windows

- 推荐安装 `TeX Live` 或 `MiKTeX`
- 若使用 MiKTeX，请开启缺失宏包自动安装
- 建议确保系统中至少存在下列字体中的一部分：
  - 英文字体：Palatino Linotype / TeX Gyre Pagella / Times New Roman
  - 无衬线：Helvetica Neue / TeX Gyre Heros / Arial
  - 中文字体：Source Han Serif SC / Noto Serif CJK SC / Songti SC / SimSun / Microsoft YaHei / SimHei / KaiTi / FangSong

### Linux

- 推荐安装 `texlive-full` 与 `latexmk`
- 建议安装 `fonts-noto-cjk`

---

## 快速开始

1. 选择入口文件：
	- 英文：`Thomas-Tufte-book.tex`
	- 中文：`Thomas-Tufte-book-zh.tex`
2. 修改元数据：
	- `\title{...}`
	- `\date{...}`
	- `\author{...}`
	- `\publisher{...}`
3. 选择配色：

```latex
\OUCSetPalette{7}  % 0..23
```

4. 在正文中使用语义色名：

```latex
{\color{primary}主强调色}
{\color{accent}最深强调色}
{\color{spotcolor}主题点睛色（如 Kyoto 的朱红）}
```

5. 编译生成 PDF

---

## 编译方式

### 推荐：latexmk

英文版：

```bash
latexmk -xelatex Thomas-Tufte-book.tex
```

中文版：

```bash
latexmk -xelatex Thomas-Tufte-book-zh.tex
```

### 手动多遍编译

英文版：

```bash
xelatex Thomas-Tufte-book.tex
biber Thomas-Tufte-book
xelatex Thomas-Tufte-book.tex
xelatex Thomas-Tufte-book.tex
```

中文版：

```bash
xelatex Thomas-Tufte-book-zh.tex
biber Thomas-Tufte-book-zh
xelatex Thomas-Tufte-book-zh.tex
xelatex Thomas-Tufte-book-zh.tex
```

> 不要使用 `pdflatex`。  
> 若当前环境中 `xelatex` 不在 PATH 中，请先安装 TeX 发行版并配置 PATH。

---

## 核心接口

### 语言接口

```latex
\newcommand{\BookLanguage}{english}
\SetBookLanguage{\BookLanguage}
```

可选值：

- `english`
- `chinese`

### 配色接口

```latex
\OUCSetPalette{N}
```

其中 `N` 取值范围：`0..23`

当前样式暴露以下颜色名：

- `oucpal1` 到 `oucpal6`：按浅到深排列
- `primary`：默认映射到 `pal5`
- `accent`：默认映射到 `pal6`
- `paleblue`：默认映射到 `pal1`
- `spotcolor`：主题点睛色；默认等于 `accent`，Kyoto 主题时切换为朱红

### 结构化表格表头

```latex
\booktableheadrow
\booktableheadcell{Header Text}
```

### 章节与目录

章节标题、目录中的 `part/chapter` 标签和页码，已经自动接入 palette 系统，不需要额外配置。

---

## 配色总览

下表列出全部 24 套配色的编号、名称、主色与气质概要。表中主色对应 `primary=pal5`，深强调色对应 `accent=pal6`。

| N | 名称 | Primary | Accent | 风格关键词 |
|---|---|---|---|---|
| 0 | OUC Default | `rgb(30,58,138)` | `rgb(30,41,59)` | 经典学术蓝 |
| 1 | Brunneophobia | `rgb(86,67,53)` | `rgb(42,23,14)` | 暖土、烧褐、厚重 |
| 2 | Van Dyke | `rgb(68,60,94)` | `rgb(61,43,39)` | 灰紫、内敛、旧画布 |
| 3 | Back in Black | `rgb(74,63,75)` | `rgb(22,19,21)` | 近单色、烟粉、炭黑 |
| 4 | Belle of the Ball | `rgb(118,118,44)` | `rgb(53,77,4)` | 橄榄、珊瑚、复古舞会 |
| 5 | Pine Tree | `rgb(167,88,26)` | `rgb(43,47,34)` | 秋金、松影、赭褐 |
| 6 | Provence Blue | `rgb(82,92,121)` | `rgb(53,66,94)` | 普罗旺斯雾蓝 |
| 7 | Fresco Blue | `rgb(4,75,102)` | `rgb(2,31,46)` | 壁画蓝、清冷海青 |
| 8 | Monet | `rgb(16,86,102)` | `rgb(10,51,35)` | 印象派粉彩与深青 |
| 9 | Narcissus | `rgb(190,108,26)` | `rgb(110,60,31)` | 沙土、暖金、铁锈橘 |
| 10 | Roman Empire | `rgb(120,20,40)` | `rgb(88,28,90)` | 罗马、军团红、骨螺紫 |
| 11 | Greece | `rgb(48,105,175)` | `rgb(90,42,92)` | 希腊、民主蓝、陶器赤 |
| 12 | Kanagawa | `rgb(13,38,76)` | `rgb(29,25,35)` | 江户、浪蓝、墨线 |
| 13 | Starry Night | `rgb(22,50,30)` | `rgb(20,36,88)` | 夜空、月黄、柏影 |
| 14 | A Thousand Li | `rgb(48,105,76)` | `rgb(35,78,112)` | 千里江山、青绿、古绢 |
| 15 | And Quiet Flows the Don | `rgb(52,70,90)` | `rgb(88,26,24)` | 顿河、浊蓝、暗血 |
| 16 | Cyberpunk Edgerunners | `rgb(15,32,98)` | `rgb(14,8,28)` | 夜都、荧光、赛博过载 |
| 17 | The Grand Budapest Hotel | `rgb(128,88,148)` | `rgb(143,52,65)` | 旧贵族、粉紫、奶油底 |
| 18 | Renaissance Florence | `rgb(46,70,118)` | `rgb(85,54,34)` | 文艺复兴、青金、陶红 |
| 19 | Soviet Avant-Garde | `rgb(196,28,28)` | `rgb(24,20,18)` | 构成主义、红黑、工业 |
| 20 | Constantinople | `rgb(102,32,65)` | `rgb(30,52,88)` | 拜占庭、金辉、海都 |
| 21 | France | `rgb(180,32,40)` | `rgb(44,74,138)` | 法兰西、红白蓝再解读 |
| 22 | Kyoto | `rgb(80,94,68)` | `rgb(34,40,66)` | 京都、禅寂、幽玄 |
| 23 | Siamese Dream | `rgb(188,105,40)` | `rgb(42,68,48)` | 失真摇滚、青春期、连体梦境 |

---

## 完整色版速查

正文部分保留每套 palette 的“完整色版”，便于直接浏览与选择。六色均按 `pal1 -> pal6` 由浅到深排列。Kyoto 另有 `spotcolor = rgb(170,50,36)`。

### 0. OUC Default

```text
OUC Default A   rgb(239, 246, 255)
OUC Default B   rgb(219, 234, 254)
OUC Default C   rgb( 96, 165, 250)
OUC Default D   rgb( 37,  99, 235)
OUC Default E   rgb( 30,  58, 138)
OUC Default F   rgb( 30,  41,  59)
```

### 1. Brunneophobia

```text
Brunneophobia A rgb(238, 211, 180)
Brunneophobia B rgb(213, 148,  79)
Brunneophobia C rgb(213, 148,  79)
Brunneophobia D rgb(180,  69,  15)
Brunneophobia E rgb( 86,  67,  53)
Brunneophobia F rgb( 42,  23,  14)
```

### 2. Van Dyke

```text
Van Dyke A       rgb(236, 194, 188)
Van Dyke B       rgb(169, 159, 191)
Van Dyke C       rgb(169, 159, 191)
Van Dyke D       rgb(191, 113, 133)
Van Dyke E       rgb( 68,  60,  94)
Van Dyke F       rgb( 61,  43,  39)
```

### 3. Back in Black

```text
Back in Black A  rgb(240, 217, 228)
Back in Black B  rgb(193, 160, 172)
Back in Black C  rgb(193, 160, 172)
Back in Black D  rgb(128, 108, 121)
Back in Black E  rgb( 74,  63,  75)
Back in Black F  rgb( 22,  19,  21)
```

### 4. Belle of the Ball

```text
Belle A          rgb(226, 203, 192)
Belle B          rgb(206, 171, 150)
Belle C          rgb(210, 135, 106)
Belle D          rgb(229,  74,  57)
Belle E          rgb(118, 118,  44)
Belle F          rgb( 53,  77,   4)
```

### 5. Pine Tree

```text
Pine Tree A      rgb(238, 200, 111)
Pine Tree B      rgb(222, 166,  32)
Pine Tree C      rgb(222, 166,  32)
Pine Tree D      rgb(177, 120, 133)
Pine Tree E      rgb(167,  88,  26)
Pine Tree F      rgb( 43,  47,  34)
```

### 6. Provence Blue

```text
Provence A       rgb(170, 188, 175)
Provence B       rgb(137, 156, 154)
Provence C       rgb(137, 156, 154)
Provence D       rgb(110, 124, 139)
Provence E       rgb( 82,  92, 121)
Provence F       rgb( 53,  66,  94)
```

### 7. Fresco Blue

```text
Fresco A         rgb(166, 224, 244)
Fresco B         rgb( 71, 169, 207)
Fresco C         rgb( 71, 169, 207)
Fresco D         rgb(  9, 121, 158)
Fresco E         rgb(  4,  75, 102)
Fresco F         rgb(  2,  31,  46)
```

### 8. Monet

```text
Monet A          rgb(247, 244, 213)
Monet B          rgb(211, 150, 140)
Monet C          rgb(211, 150, 140)
Monet D          rgb(131, 153,  88)
Monet E          rgb( 16,  86, 102)
Monet F          rgb( 10,  51,  35)
```

### 9. Narcissus

```text
Narcissus A      rgb(221, 213, 200)
Narcissus B      rgb(185, 149, 144)
Narcissus C      rgb(185, 149, 144)
Narcissus D      rgb(199, 149,  72)
Narcissus E      rgb(190, 108,  26)
Narcissus F      rgb(110,  60,  31)
```

### 10. Roman Empire

```text
Carrara Marble   rgb(236, 232, 225)
Gloria Aurum     rgb(212, 175,  55)
Laurel Viridis   rgb( 74, 110,  65)
Legion Crimson   rgb(180,  30,  30)
Senate Bordeaux  rgb(120,  20,  40)
Tyrian Purple    rgb( 88,  28,  90)
```

### 11. Greece

```text
Parian Marble      rgb(245, 240, 228)
Gloria Aurum       rgb(212, 175,  55)
Athena's Olive     rgb( 98, 128,  48)
Attic Terracotta   rgb(188,  82,  38)
Agora Kyanos       rgb( 48, 105, 175)
Dionysian Grape    rgb( 90,  42,  92)
```

### 12. Kanagawa

```text
Nami-shiro       rgb(237, 233, 222)
Boten            rgb(208, 224, 238)
Fuji-gasumi      rgb(150, 186, 210)
Bero-ai          rgb( 26,  78, 132)
Shinkai          rgb( 13,  38,  76)
Sumi             rgb( 29,  25,  35)
```

### 13. Starry Night

```text
Lumière Lunaire    rgb(240, 208,  68)
Lueurs du Village  rgb(198, 140,  52)
Aube Glacée        rgb(105, 155, 200)
Tourbillon Outremer rgb( 48,  96, 165)
Cyprès Nocturne    rgb( 22,  50,  30)
Minuit Cobalt      rgb( 20,  36,  88)
```

### 14. A Thousand Li

```text
Song Silk        rgb(218, 203, 170)
Sky Azurite      rgb(110, 165, 195)
Ochre-Gold       rgb(183, 118,  45)
Pale Malachite   rgb( 96, 148, 110)
Malachite True   rgb( 48, 105,  76)
Azurite Deep     rgb( 35,  78, 112)
```

### 15. And Quiet Flows the Don

```text
Полынь            rgb(142, 120,  70)
Степной Пепел     rgb(110, 108, 104)
Донская Земля     rgb(118,  86,  52)
Ржавое Железо     rgb(122,  66,  36)
Мутный Дон        rgb( 52,  70,  90)
Запёкшаяся Кровь  rgb( 88,  26,  24)
```

### 16. Cyberpunk Edgerunners

```text
Psycho Yellow    rgb(225, 255,   8)
Flatline Green   rgb( 10, 238, 100)
Neon Magenta     rgb(238,  18, 120)
Edgerunner Red   rgb(205,  20,  35)
Luna Blue        rgb( 15,  32,  98)
Night City Void  rgb( 14,   8,  28)
```

### 17. The Grand Budapest Hotel

```text
Crème Vanille      rgb(247, 235, 215)
Brume Alpine       rgb(168, 178, 196)
Rose Méndl         rgb(237, 148, 158)
Doré Antique       rgb(176, 136,  60)
Violet Concierge   rgb(128,  88, 148)
Bordeaux Vintage   rgb(143,  52,  65)
```

### 18. Renaissance Florence

```text
Avorio Fiorentino            rgb(238, 228, 208)
Oro dell'Altare              rgb(190, 148,  52)
Cotto Brunellesco            rgb(172,  84,  50)
Verde Cipresso               rgb( 54,  80,  60)
Oltremare di Lapislazzuli    rgb( 46,  70, 118)
Noce Toscano                 rgb( 85,  54,  34)
```

### 19. Soviet Avant-Garde

```text
ГАЗЕТА   rgb(225, 218, 205)
ПЛАКАТ   rgb(200, 150,  32)
БЕТОН    rgb(118, 114, 108)
ЧЕРТЁЖ   rgb( 50,  80, 138)
КРАСНЫЙ  rgb(196,  28,  28)
ЧЁРНЫЙ   rgb( 24,  20,  18)
```

### 20. Constantinople

```text
Λευκός · Fildişi   rgb(236, 225, 207)
Χρυσός · Altın     rgb(195, 150,  42)
Ώχρα · Toprak      rgb(170, 112,  50)
Κυπαρίσσι · Selvi  rgb( 50,  76,  58)
Πορφύρα · Mor      rgb(102,  32,  65)
Βόσπορος · Boğaz   rgb( 30,  52,  88)
```

### 21. France

```text
Ivoire Champagne    rgb(232, 222, 205)
Olive Dorée         rgb(142, 133,  58)
Zinc Parisien       rgb(122, 126, 132)
Lavande Provençale  rgb(143, 108, 148)
Rouge Marianne      rgb(180,  32,  40)
Bleu République     rgb( 44,  74, 138)
```

### 22. Kyoto

```text
Kinushiro      rgb(234, 226, 212)
Sakura-nezumi  rgb(204, 184, 178)
Aotake-nezumi  rgb(116, 126, 120)
Karacha        rgb(110,  84,  64)
Koke-iro       rgb( 80,  94,  68)
Kon            rgb( 34,  40,  66)
Shu-hi         rgb(170,  50,  36)   % spotcolor
```

### 23. Siamese Dream

```text
Luna           rgb(238, 226, 208)
Disarm         rgb(182, 180, 193)
Today          rgb(198, 158,  65)
Hummer         rgb(150, 145, 135)
Mayonaise      rgb(188, 105,  40)
Soma           rgb( 42,  68,  48)
```

---

## 附录：全部配色方案详述

以下附录中，原有 10 套基础 palette 与扩展的 14 套主题 palette 采用统一体例：

- 色彩哲学
- 六色配色组表格
- 完整色板
- 结构性说明文本

### Palette 0 — OUC Default

#### 色彩哲学

这是一套以学院、海洋与结构秩序为核心的深蓝配色。它的逻辑不是“炫技”，而是为信息排布建立稳定骨架：浅蓝负责留白，亮蓝负责导视，海军蓝负责权威，近黑蓝负责收束。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Mist Blue | `rgb(239,246,255)` | 近白浅蓝，用于背景与呼吸空间 |
| Soft Sky | `rgb(219,234,254)` | 次浅层，适合轻量信息区 |
| Signal Blue | `rgb(96,165,250)` | 导视蓝，用于提示与弱强调 |
| Structural Blue | `rgb(37,99,235)` | 中层结构色，清晰且现代 |
| Academic Navy | `rgb(30,58,138)` | 主色，稳定、理性、带学院权威 |
| Deep Harbor | `rgb(30,41,59)` | 最深锚点，用于最强对比与收边 |

#### 完整色板

```text
Mist Blue        rgb(239, 246, 255)
Soft Sky         rgb(219, 234, 254)
Signal Blue      rgb( 96, 165, 250)
Structural Blue  rgb( 37,  99, 235)
Academic Navy    rgb( 30,  58, 138)
Deep Harbor      rgb( 30,  41,  59)
```

结构说明：这组色从几乎不可见的浅蓝一路收束到深港湾蓝，形成非常清晰的层级链。它适合学术正文、目录、章节标题与表格表头，也最接近模板的默认气质。

### Palette 1 — Brunneophobia

#### 色彩哲学

Brunneophobia 以烧土、木器、皮革和窑火残温为基调。它不是明亮的棕，而是被岁月熏过的褐；它给人的感受更像是陶器表面、旧木桌面和书脊革面，适合厚重但不压迫的书籍视觉。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Clay Mist | `rgb(238,211,180)` | 浅陶土底色 |
| Ochre Sand | `rgb(213,148,79)` | 暖黄褐中层 |
| Ochre Sand | `rgb(213,148,79)` | 重复槽位，用于 5 色 palette 映射 |
| Kiln Orange | `rgb(180,69,15)` | 窑火赭橙 |
| Walnut Brown | `rgb(86,67,53)` | 主色，稳重木褐 |
| Charred Earth | `rgb(42,23,14)` | 最深焦土色 |

#### 完整色板

```text
Clay Mist     rgb(238, 211, 180)
Ochre Sand    rgb(213, 148,  79)
Ochre Sand    rgb(213, 148,  79)
Kiln Orange   rgb(180,  69,  15)
Walnut Brown  rgb( 86,  67,  53)
Charred Earth rgb( 42,  23,  14)
```

结构说明：浅陶土与焦土黑拉开两端，中间用烧赭色压缩空间，因此整组色温暖、稳定、克制，适合文学、历史或旧物气质明显的内容。

### Palette 2 — Van Dyke

#### 色彩哲学

Van Dyke 像旧画布、玫瑰灰与褪色靛紫之间的低语。它不靠高对比夺目，而靠一种近乎粉尘感的暗雅来维持存在，适合需要柔和戏剧性的页面。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Dust Rose | `rgb(236,194,188)` | 浅灰粉底 |
| Faded Indigo | `rgb(169,159,191)` | 雾靛紫 |
| Faded Indigo | `rgb(169,159,191)` | 重复槽位 |
| Old Wine | `rgb(191,113,133)` | 旧酒红中层 |
| Muted Indigo | `rgb(68,60,94)` | 主色，低饱和靛紫 |
| Burnt Umber | `rgb(61,43,39)` | 深棕灰锚点 |

#### 完整色板

```text
Dust Rose      rgb(236, 194, 188)
Faded Indigo   rgb(169, 159, 191)
Faded Indigo   rgb(169, 159, 191)
Old Wine       rgb(191, 113, 133)
Muted Indigo   rgb( 68,  60,  94)
Burnt Umber    rgb( 61,  43,  39)
```

结构说明：粉、紫、酒红和棕灰共同形成一条旧油画式的综合色链，视觉情绪偏安静、偏文学，也比普通紫系更沉着。

### Palette 3 — Back in Black

#### 色彩哲学

这套 palette 不是纯黑白，而是带烟粉残温的近单色体系。它像舞台幕后、天鹅绒暗影与化妆镜边缘残留的暖灰粉，在单色控制中保留了一丝人味。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Powder Haze | `rgb(240,217,228)` | 浅烟粉 |
| Mauve Dust | `rgb(193,160,172)` | 雾粉紫 |
| Mauve Dust | `rgb(193,160,172)` | 重复槽位 |
| Velvet Gray | `rgb(128,108,121)` | 灰紫中层 |
| Charcoal Mauve | `rgb(74,63,75)` | 主色，炭灰紫 |
| Stage Black | `rgb(22,19,21)` | 最深近黑 |

#### 完整色板

```text
Powder Haze    rgb(240, 217, 228)
Mauve Dust     rgb(193, 160, 172)
Mauve Dust     rgb(193, 160, 172)
Velvet Gray    rgb(128, 108, 121)
Charcoal Mauve rgb( 74,  63,  75)
Stage Black    rgb( 22,  19,  21)
```

结构说明：近单色体系意味着它不会干扰排版结构，但烟粉底让它不至于冷硬到失去质感，适合沉静、精致、偏展览式的页面。

### Palette 4 — Belle of the Ball

#### 色彩哲学

这套 palette 像复古舞会：瓷粉底、珊瑚红光与末段橄榄深绿在同一舞厅里相遇。它有轻微戏剧性，但主色落在橄榄上，因此最终仍是受控制的复古感。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Porcelain Blush | `rgb(226,203,192)` | 浅粉米色 |
| Antique Peach | `rgb(206,171,150)` | 旧桃色 |
| Coral Clay | `rgb(210,135,106)` | 珊瑚土色 |
| Ballroom Coral | `rgb(229,74,57)` | 亮珊瑚强调 |
| Olive Court | `rgb(118,118,44)` | 主色，橄榄宫廷绿 |
| Moss Shadow | `rgb(53,77,4)` | 最深苔影绿 |

#### 完整色板

```text
Porcelain Blush rgb(226, 203, 192)
Antique Peach   rgb(206, 171, 150)
Coral Clay      rgb(210, 135, 106)
Ballroom Coral  rgb(229,  74,  57)
Olive Court     rgb(118, 118,  44)
Moss Shadow     rgb( 53,  77,   4)
```

结构说明：浅暖底负责旧贵族柔光，珊瑚负责舞会的瞬时亮度，橄榄和苔影把整体重新压回复古而非甜腻的方向。

### Palette 5 — Pine Tree

#### 色彩哲学

Pine Tree 是一套秋意极强的 palette。金黄、赭橙、松影绿和深炭灰共同构成暮秋林地的空间：暖色负责光，深色负责树影与风干之后的静默。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Autumn Gold | `rgb(238,200,111)` | 秋金底色 |
| Harvest Ochre | `rgb(222,166,32)` | 丰收黄赭 |
| Harvest Ochre | `rgb(222,166,32)` | 重复槽位 |
| Faded Berry | `rgb(177,120,133)` | 微灰莓色过渡 |
| Burnt Orange | `rgb(167,88,26)` | 主色，深赭橙 |
| Pine Shadow | `rgb(43,47,34)` | 最深松林影 |

#### 完整色板

```text
Autumn Gold   rgb(238, 200, 111)
Harvest Ochre rgb(222, 166,  32)
Harvest Ochre rgb(222, 166,  32)
Faded Berry   rgb(177, 120, 133)
Burnt Orange  rgb(167,  88,  26)
Pine Shadow   rgb( 43,  47,  34)
```

结构说明：这是一组典型“暖色推进、深绿收尾”的 palette，适合想要土地感、季节感和轻微叙事情绪的页面。

### Palette 6 — Provence Blue

#### 色彩哲学

Provence Blue 的美感在于其去鲜亮化的冷静。它不像海边明信片那样耀眼，而更像窗台陶盆、雾里石墙和暮色薰衣草田上方的压低天空。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Herb Mist | `rgb(170,188,175)` | 灰草本浅层 |
| Stone Green | `rgb(137,156,154)` | 石墙青灰 |
| Stone Green | `rgb(137,156,154)` | 重复槽位 |
| Slate Air | `rgb(110,124,139)` | 板岩空气蓝 |
| Provence Slate | `rgb(82,92,121)` | 主色，普罗旺斯板岩蓝 |
| Evening Indigo | `rgb(53,66,94)` | 最深夜幕蓝 |

#### 完整色板

```text
Herb Mist      rgb(170, 188, 175)
Stone Green    rgb(137, 156, 154)
Stone Green    rgb(137, 156, 154)
Slate Air      rgb(110, 124, 139)
Provence Slate rgb( 82,  92, 121)
Evening Indigo rgb( 53,  66,  94)
```

结构说明：整体色温冷而不硬，灰度充足，因此适合正文页面与目录等需要长期观看的内容，而不会造成刺眼疲劳。

### Palette 7 — Fresco Blue

#### 色彩哲学

Fresco Blue 参考湿壁画和海风吹蚀后的青蓝表面。它的亮部像被石灰稀释过，深部则像颜料渗入墙体深层，是一套非常干净而有历史肌理的蓝绿体系。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Wash Blue | `rgb(166,224,244)` | 壁画洗淡浅蓝 |
| Fresh Cyan | `rgb(71,169,207)` | 海青中层 |
| Fresh Cyan | `rgb(71,169,207)` | 重复槽位 |
| Mineral Teal | `rgb(9,121,158)` | 矿物青 |
| Fresco Teal | `rgb(4,75,102)` | 主色，壁画深青 |
| Abyss Ink | `rgb(2,31,46)` | 最深墨海色 |

#### 完整色板

```text
Wash Blue    rgb(166, 224, 244)
Fresh Cyan   rgb( 71, 169, 207)
Fresh Cyan   rgb( 71, 169, 207)
Mineral Teal rgb(  9, 121, 158)
Fresco Teal  rgb(  4,  75, 102)
Abyss Ink    rgb(  2,  31,  46)
```

结构说明：这是一套最适合现代、科技、理工与清爽视觉的基础 palette 之一，深浅分层非常清楚，且整体比 OUC Default 更具设计感。

### Palette 8 — Monet

#### 色彩哲学

Monet 将象牙、灰粉、苔绿和深青压进同一画面，它更像印象派的空气，而不是印象派的花。轻柔但不弱，浅层留白很多，深层却仍有足够的结构支撑。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Ivory Light | `rgb(247,244,213)` | 浅象牙底 |
| Dusty Coral | `rgb(211,150,140)` | 灰珊瑚 |
| Dusty Coral | `rgb(211,150,140)` | 重复槽位 |
| Field Green | `rgb(131,153,88)` | 野地绿 |
| Dark Teal | `rgb(16,86,102)` | 主色，深青 |
| Forest Teal | `rgb(10,51,35)` | 最深林影青 |

#### 完整色板

```text
Ivory Light  rgb(247, 244, 213)
Dusty Coral  rgb(211, 150, 140)
Dusty Coral  rgb(211, 150, 140)
Field Green  rgb(131, 153,  88)
Dark Teal    rgb( 16,  86, 102)
Forest Teal  rgb( 10,  51,  35)
```

结构说明：柔和象牙与灰珊瑚让它有很强的页面亲和力，而深青与森林绿则保证了阅读层级，尤其适合叙事型、艺术型文档。

### Palette 9 — Narcissus

#### 色彩哲学

Narcissus 是一组干燥、温暖且带泥土颗粒感的 palette。浅层是砂土与旧布，中段是枯黄赭橙，深段则压到铁锈与木炭棕上，整体非常适合历史、考古与地景主题。

#### 六色配色组

| 颜色 | RGB | 说明 |
|---|---|---|
| Sand Veil | `rgb(221,213,200)` | 浅砂底 |
| Dust Rose | `rgb(185,149,144)` | 尘土玫瑰 |
| Dust Rose | `rgb(185,149,144)` | 重复槽位 |
| Dry Ochre | `rgb(199,149,72)` | 干赭黄 |
| Rust Amber | `rgb(190,108,26)` | 主色，铁锈橘 |
| Burnt Cedar | `rgb(110,60,31)` | 最深焦木棕 |

#### 完整色板

```text
Sand Veil   rgb(221, 213, 200)
Dust Rose   rgb(185, 149, 144)
Dust Rose   rgb(185, 149, 144)
Dry Ochre   rgb(199, 149,  72)
Rust Amber  rgb(190, 108,  26)
Burnt Cedar rgb(110,  60,  31)
```

结构说明：这组色有很强的土气与锈感，适合需要温暖但不甜、古朴但不沉死的页面气氛。

### Palette 10 — Roman Empire

#### 色彩哲学

罗马帝国的颜色必须同时承载石、血、权力、荣誉与凯旋。卡拉拉大理石的冷白是建筑与神庙的基底；军团红与元老院酒红构成权力内部的双重红色结构；月桂绿与荣耀金提供战胜后的秩序与典仪；骨螺紫则作为皇权的终极象征压住全局。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 大理石 | Carrara Marble | `rgb(236,232,225)` | 卡拉拉大理石的冷白底色，略带暖灰，呈现神庙与雕像的质感 |
| 荣耀金 | Gloria Aurum | `rgb(212,175,55)` | 凯旋式黄金的中性金，介于铸币与神像镀金之间，不过暖也不过冷 |
| 桂冠 | Laurel Viridis | `rgb(74,110,65)` | 月桂冠叶片的哑光深绿，非翠绿，取干燥叶片的沉稳色调 |
| 罗马军团 | Legion Crimson | `rgb(180,30,30)` | 军团战袍的鲜烈战红，饱和而有力，象征铁与血 |
| 元老院 | Senate Bordeaux | `rgb(120,20,40)` | 元老院托加袍缘的深沉酒红，比军团红更内敛、更权贵 |
| 奥古斯都紫 | Tyrian Purple | `rgb(88,28,90)` | 骨螺紫染料的历史色，价比黄金，专属皇权，深邃而神秘 |

#### 完整色板

```text
Carrara Marble   rgb(236, 232, 225)
Legion Crimson   rgb(180,  30,  30)
Senate Bordeaux  rgb(120,  20,  40)
Laurel Viridis   rgb( 74, 110,  65)
Gloria Aurum     rgb(212, 175,  55)
Tyrian Purple    rgb( 88,  28,  90)
```

设计思路：石白提供文明底盘，双重红色负责军政权力的层次分工，绿色与金色构成凯旋秩序，而骨螺紫作为最高暗部锚点，使整组配色具备帝国神圣性而不流于舞台化。

### Palette 11 — Greece

#### 色彩哲学

希腊主题配色以神庙大理石为底，以民主蓝统领视觉，以荣耀金做高光点缀。陶器赤、橄榄银绿与葡萄紫从文化层面补足人间性、智慧与戏剧性，使其不止停留在“蓝白金”的旅游符号，而具有古典文明的复杂呼吸。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 帕罗斯大理石 | Parian Marble | `rgb(245,240,228)` | 暖白而偏象牙，是神庙与雕像的物质底色 |
| 荣耀金 | Gloria Aurum | `rgb(212,175,55)` | 沿用罗马组的中性荣耀金 |
| 橄榄银绿 | Athena's Olive | `rgb(98,128,48)` | 雅典娜所赠橄榄树的沉稳绿调 |
| 陶器赤 | Attic Terracotta | `rgb(188,82,38)` | 红绘陶器底色，是神话与英雄叙事的媒介色 |
| 民主蓝 | Agora Kyanos | `rgb(48,105,175)` | 爱琴海与 Agora 上空的中性蔚蓝 |
| 狄俄尼索斯葡萄紫 | Dionysian Grape | `rgb(90,42,92)` | 象征酒神、戏剧与狂欢节的深紫 |

#### 完整色板

```text
Parian Marble      rgb(245, 240, 228)  ░░  底色·神庙·纯粹
Agora Kyanos       rgb( 48, 105, 175)  ██  主色·民主·爱琴海
Gloria Aurum       rgb(212, 175,  55)  ██  点缀·荣耀·神明
Attic Terracotta   rgb(188,  82,  38)  ██  辅色·叙事·人间
Dionysian Grape    rgb( 90,  42,  92)  ██  暗调·神秘·戏剧
Athena's Olive     rgb( 98, 128,  48)  ██  中调·智慧·生命
```

配色逻辑：以大理石白为底，民主蓝统领视觉重心，金色做高光点缀；陶器赤与橄榄绿构成一对冷暖平衡的中间调，葡萄紫作为最深的暗部锚点，整体在地中海阳光下呈现出既庄重又充满生命力的古典张力。

### Palette 12 — Kanagawa

#### 色彩哲学

《神奈川冲浪里》的革命性在于葛饰北斎将普鲁士蓝引入浮世绘，以单一色系的深浅变奏构建戏剧张力，再以墨线和和纸留白完成空间收束。这是一组以蓝为骨、以白为气、以墨为锚的江户时代色板。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 波白·沫雪 | Nami-shiro | `rgb(237,233,222)` | 浪尖破碎的泡沫，非纯白，带有和纸的微暖底色 |
| 暮天·天际 | Boten | `rgb(208,224,238)` | 海平线处的天空渐变色，苍茫而留白 |
| 富士霞·远岚 | Fuji-gasumi | `rgb(150,186,210)` | 远景富士山的淡蓝轮廓，虚化而沉静 |
| ベロ藍·浪蓝 | Bero-ai | `rgb(26,78,132)` | 画面主体，普鲁士蓝浪身 |
| 深海·暗涌 | Shinkai | `rgb(13,38,76)` | 浪底最深处的墨蓝，近乎黑而仍保有蓝的冷意 |
| 墨·轮廓 | Sumi | `rgb(29,25,35)` | 木版印刷的墨线，统摄全图骨架 |

#### 完整色板

```text
ベロ藍  Bero-ai      rgb( 26,  78, 132)  ██  主色·浪·生命力
深海    Shinkai      rgb( 13,  38,  76)  ██  暗调·深渊·压迫感
富士霞  Fuji-gasumi  rgb(150, 186, 210)  ██  中调·远景·永恒
暮天    Boten        rgb(208, 224, 238)  ░░  浅调·天空·呼吸感
波白    Nami-shiro   rgb(237, 233, 222)  ░░  高光·泡沫·和纸质感
墨      Sumi         rgb( 29,  25,  35)  ██  锚点·轮廓·版画骨骼
```

配色逻辑：整组色彩以普鲁士蓝家族为核心，从墨黑→深海蓝→浪蓝→富士霞→暮天→波白构成一条完整的明度递进链，如同浪从深处涌起、在浪尖碎裂成雪沫的瞬间。这种“单色系深浅变奏”正是江户浮世绘木版印刷美学的精髓。

### Palette 13 — Starry Night

#### 色彩哲学

梵高的《星月夜》并非印象派而是后印象派的极点：夜空以钴蓝与群青为骨，铬黄月光在蓝色重压下迸裂，柏树如黑色火焰直刺苍穹，村庄的暖黄则是唯一的人间余温。整组色板以三层蓝构成情绪纵深，用冷暖对抗驱动画面生命力。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 月华铬黄 | Lumière Lunaire | `rgb(240,208,68)` | 月亮与星芒的爆裂光晕 |
| 村灯琥珀 | Lueurs du Village | `rgb(198,140,52)` | 村庄窗口透出的暖黄 |
| 晨曦苍蓝 | Aube Glacée | `rgb(105,155,200)` | 漩涡边缘的淡蓝过渡 |
| 星涡群青 | Tourbillon Outremer | `rgb(48,96,165)` | 漩涡主体的群青蓝 |
| 柏影墨绿 | Cyprès Nocturne | `rgb(22,50,30)` | 前景柏树的深邃暗绿 |
| 深夜钴蓝 | Minuit Cobalt | `rgb(20,36,88)` | 夜空最深处的底色 |

#### 完整色板

```text
Minuit Cobalt       rgb( 20,  36,  88)  ██  深锚·情绪底色·夜的重量
Tourbillon Outremer rgb( 48,  96, 165)  ██  主旋·漩涡·后印象笔触
Aube Glacée         rgb(105, 155, 200)  ██  过渡·呼吸·边界之光
Lumière Lunaire     rgb(240, 208,  68)  ██  爆点·月华·生命燃烧
Cyprès Nocturne     rgb( 22,  50,  30)  ██  沉默·柏树·拒绝被照亮
Lueurs du Village   rgb(198, 140,  52)  ██  余温·人间·唯一的暖
```

配色逻辑：三层蓝色构成由深至浅的情绪纵深轴。月华铬黄与村灯琥珀是画面仅有的两个暖色，一个属于宇宙、一个属于人间；柏影墨绿作为视觉锚点，以最暗的植物色把整组色的运动重新拉回大地。

### Palette 14 — A Thousand Li

#### 色彩哲学

《千里江山图》的颜色来自矿物颜料的层层积染：石青与石绿不一次着色，而是沉入绢底，形成“薄中见厚”的通透矿物感。整组色板围绕青绿主调、层次渐变、金赭点缀、空灵雅致与古绢质感展开。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 古绢底 | Song Silk | `rgb(218,203,170)` | 千年绢素氧化后的暖米底色 |
| 天青·浅 | Sky Azurite | `rgb(110,165,195)` | 远山与江面折光的浅石青 |
| 赭金 | Ochre-Gold | `rgb(183,118,45)` | 礁石、屋舍与金线的温度色 |
| 苍绿·浅 | Pale Malachite | `rgb(96,148,110)` | 中景与云雾之间的过渡绿 |
| 石绿·正 | Malachite True | `rgb(48,105,76)` | 山体受光面的正孔雀石绿 |
| 石青·深 | Azurite Deep | `rgb(35,78,112)` | 山体阴面与水深处的矿蓝骨架 |

#### 完整色板

```text
霁山青  Azurite Deep    rgb( 35,  78, 112)  ██  骨·深邃·山之阴面
苍岭绿  Malachite True  rgb( 48, 105,  76)  ██  肉·华贵·山之受光
烟渚色  Sky Azurite     rgb(110, 165, 195)  ██  气·空灵·远山与水
岚霭绿  Pale Malachite  rgb( 96, 148, 110)  ██  韵·渐变·云雾中景
砂岩赭  Ochre-Gold      rgb(183, 118,  45)  ██  点·温度·金赭人迹
宋绢暖  Song Silk       rgb(218, 203, 170)  ░░  底·时间·千年绢素
```

五大特征的色彩映射：青绿主调由霁山青与苍岭绿共同锚定；层次渐变通过深青到浅青、正绿到浅绿的双链条完成；金赭点缀由砂岩赭承担温度调节；空灵雅致来自烟渚色与岚霭绿打开的呼吸感；古绢质感则由宋绢暖托起整组颜色的时间厚度。

### Palette 15 — And Quiet Flows the Don

#### 色彩哲学

这组配色拒绝一切鲜亮，只保留时间磨损之后的残余：不是蓝，是浊蓝；不是红，是暗血；不是黄，是枯苇；不是灰，是冻土与铅尘。它试图用“冷灰 + 土褐 + 暗血 + 浊蓝”压住史诗的沉重与苦难。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 枯苇秋黄 | Полынь | `rgb(142,120,70)` | 被霜打过的苇草与苦艾的颜色 |
| 草原铅灰 | Степной Пепел | `rgb(110,108,104)` | 冬日荒原天地混为一色的灰 |
| 黄土大地 | Донская Земля | `rgb(118,86,52)` | 顿河流域栗钙土的褐色 |
| 铁锈赭红 | Ржавое Железо | `rgb(122,66,36)` | 军刀与枪托上的锈色 |
| 顿河浊蓝 | Мутный Дон | `rgb(52,70,90)` | 裹挟泥沙与血色的浊蓝河水 |
| 暗血战痕 | Запёкшаяся Кровь | `rgb(88,26,24)` | 凝固渗入军衣的深褐红 |

#### 完整色板

```text
Мутный Дон        顿河浊蓝  rgb( 52,  70,  90)  ██  冷·流动·命运底色
Степной Пепел     草原铅灰  rgb(110, 108, 104)  ██  重·静止·时间灰烬
Донская Земля     黄土大地  rgb(118,  86,  52)  ██  钝·厚重·苦难根基
Полынь            枯苇秋黄  rgb(142, 120,  70)  ██  涩·残存·短暂温柔
Ржавое Железо     铁锈赭红  rgb(122,  66,  36)  ██  锈·腐蚀·荣光衰败
Запёкшаяся Кровь  暗血战痕  rgb( 88,  26,  24)  ██  沉·凝固·史诗之重
```

色彩结构的悲剧逻辑：冷灰压顶，土褐承重，暗血锚底，铁锈贯穿时间感。整组色没有任何“希望色”，只有不同层级的磨损与沉郁。

### Palette 16 — Cyberpunk Edgerunners

#### 色彩哲学

《边缘行者》的视觉语言是一种过载美学：极暗底色与极亮荧光之间没有缓冲层。夜之城的霓虹不是繁荣而是麻醉，Lucy 的蓝是唯一的逃逸路径，黄色与绿色则是失控和运转的赛博症状。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 迷幻荧黄 | Psycho Yellow | `rgb(225,255,8)` | 过载与赛博精神病的临界黄 |
| 电路荧绿 | Flatline Green | `rgb(10,238,100)` | 骇入代码流与改造体的运转色 |
| 霓虹品红 | Neon Magenta | `rgb(238,18,120)` | 酒吧、广告牌与欢场的霓虹色 |
| 鲜血赤红 | Edgerunner Red | `rgb(205,20,35)` | 边缘行者的代价之红 |
| 露娜深蓝 | Luna Blue | `rgb(15,32,98)` | Lucy、月球与梦的颜色 |
| 夜都虚空 | Night City Void | `rgb(14,8,28)` | 承载全部霓虹的深紫黑底 |

#### 完整色板

```text
Night City Void   夜都虚空  rgb( 14,   8,  28)  ██  底·深渊·过载的容器
Luna Blue         露娜深蓝  rgb( 15,  32,  98)  ██  沉·梦境·唯一的出口
Edgerunner Red    鲜血赤红  rgb(205,  20,  35)  ██  烈·代价·无处回避
Neon Magenta      霓虹品红  rgb(238,  18, 120)  ██  燥·谎言·城市的麻醉
Flatline Green    电路荧绿  rgb( 10, 238, 100)  ██  冷·运转·改造的代码
Psycho Yellow     迷幻荧黄  rgb(225, 255,   8)  ██  爆·失控·过载的临界
```

色彩结构的叙事逻辑：虚空压底，冷暖裂变，荧光过载，红色终章。没有黑暗，霓虹只是颜料；没有月球梦，夜之城就只剩噪声。

### Palette 17 — The Grand Budapest Hotel

#### 色彩哲学

这组配色像裹着柔光滤镜的旧欧洲童话：粉不是少女粉，而是旧玫瑰；紫不是妖艳紫，而是礼仪与人格；奶油底、复古暗金与雾蓝共同保证其明亮却不甜腻、优雅却不失时间感。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 香草奶油 | Crème Vanille | `rgb(247,235,215)` | 饭店内壁与蛋糕胚的暖底色 |
| 阿尔卑斯雾蓝 | Brume Alpine | `rgb(168,178,196)` | 低饱和冷调，负责降温与透气 |
| 美酒蔷薇 | Rose Méndl | `rgb(237,148,158)` | 饭店外墙与甜品盒的标志旧玫瑰 |
| 古铜暗金 | Doré Antique | `rgb(176,136,60)` | 镜框、门把与制服肩章的旧贵族金 |
| 执行者紫 | Violet Concierge | `rgb(128,88,148)` | 古斯塔夫先生制服的权威紫 |
| 复古酒绛 | Bordeaux Vintage | `rgb(143,52,65)` | 图书馆、密谋与危险的暗影锚点 |

#### 完整色板

```text
Rose Méndl        美酒蔷薇     rgb(237, 148, 158)  ░░  主角·童话·旧玫瑰尘埃
Violet Concierge  执行者紫     rgb(128,  88, 148)  ██  人格·权威·荒诞尊严
Crème Vanille     香草奶油     rgb(247, 235, 215)  ░░  底气·呼吸·世界的空气
Doré Antique      古铜暗金     rgb(176, 136,  60)  ██  岁月·贵族·不肯褪去的光
Brume Alpine      阿尔卑斯雾蓝 rgb(168, 178, 196)  ░░  冷静·降温·现实的边缘
Bordeaux Vintage  复古酒绛     rgb(143,  52,  65)  ██  暗影·危险·令甜不腻的苦
```

五重美学法则的色彩映射：马卡龙柔色由蔷薇粉与执行者紫承担；奶油暖底由香草奶油统摄负空间；复古暗金负责贵族重量；雾蓝作为冷调调节器；酒绛则以一粒暗色防止整体沦为甜品陈列。

### Palette 18 — Renaissance Florence

#### 色彩哲学

佛罗伦萨的颜色不是被设计出来的，而是从矿石、金箔、陶土、木板和宗教空间中生长出来的。它们共同构成一种天然矿物色 + 暖金 + 陶土红 + 深褐墨绿 + 象牙白的古典秩序。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 翡冷翠象牙 | Avorio Fiorentino | `rgb(238,228,208)` | 大理石与坦培拉底板的暖象牙 |
| 祭坛暖金 | Oro dell'Altare | `rgb(190,148,52)` | 背光金箔与旧贵族金饰的旧金 |
| 穹顶陶红 | Cotto Brunellesco | `rgb(172,84,50)` | 穹顶砖瓦与佛罗伦萨屋檐的陶土红 |
| 柏影墨绿 | Verde Cipresso | `rgb(54,80,60)` | 托斯卡纳柏树与铜绿的深绿 |
| 青金矿蓝 | Oltremare di Lapislazzuli | `rgb(46,70,118)` | 圣母袍服式的青金石蓝 |
| 胡桃深褐 | Noce Toscano | `rgb(85,54,34)` | 核桃木画板与阴影底釉的深褐 |

#### 完整色板

```text
Avorio Fiorentino     翡冷翠象牙  rgb(238, 228, 208)  ░░  底·呼吸·大理石与铅白
Oro dell'Altare       祭坛暖金    rgb(190, 148,  52)  ██  光·神圣·五百年旧金
Cotto Brunellesco     穹顶陶红    rgb(172,  84,  50)  ██  暖·人间·窑火与砖瓦
Oltremare             青金矿蓝    rgb( 46,  70, 118)  ██  重·肃穆·圣母的袍色
Verde Cipresso        柏影墨绿    rgb( 54,  80,  60)  ██  沉·自然·托斯卡纳丘陵
Noce Toscano          胡桃深褐    rgb( 85,  54,  34)  ██  根·人文·木质与大地
```

四重气质的色彩映射：青金矿蓝与祭坛暖金构成神圣庄重；象牙与陶红实现温润华贵；六色统一去现代化，形成古典醇厚；深绿与胡桃褐则把神圣重新拉回人的手艺与土地。

### Palette 19 — Soviet Avant-Garde

#### 色彩哲学

苏联先锋主义拒绝调和、拒绝渐变、拒绝装饰。每一种颜色都是硬边宣言：红色是行动，黑色是绝对，灰色是承重，蓝色是机械理性，赭黄是宣传中的未来，粗纸白则是大众传播的廉价载体。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 粗纸白 | ГАЗЕТА | `rgb(225,218,205)` | 新闻纸白，粗粝、民主、反精英 |
| 宣传赭黄 | ПЛАКАТ | `rgb(200,150,32)` | 丰收海报里的赭黄承诺 |
| 混凝土灰 | БЕТОН | `rgb(118,114,108)` | 工业化进程的中性见证者 |
| 机械蓝 | ЧЕРТЁЖ | `rgb(50,80,138)` | 蓝图与纪律的冷蓝 |
| 列宁红 | КРАСНЫЙ | `rgb(196,28,28)` | 革命旗帜式的沉重红 |
| 铸铁黑 | ЧЁРНЫЙ | `rgb(24,20,18)` | 黑色方块般的绝对黑 |

#### 完整色板

```text
КРАСНЫЙ  列宁红    rgb(196,  28,  28)  ██  宣言·行动·革命的硬边
ЧЁРНЫЙ   铸铁黑    rgb( 24,  20,  18)  ██  绝对·虚无·零度的确定
БЕТОН    混凝土灰  rgb(118, 114, 108)  ██  工业·中性·进程的见证
ЧЕРТЁЖ   机械蓝    rgb( 50,  80, 138)  ██  精确·蓝图·冰冷的理想
ГАЗЕТА   粗纸白    rgb(225, 218, 205)  ░░  载体·大众·反精英的底色
ПЛАКАТ   宣传赭黄  rgb(200, 150,  32)  ██  丰收·乌托邦·未竟的承诺
```

六重美学法则的色彩映射：红黑强撞是结构核心；工业灰承担脊柱；机械蓝提供理性纪律；粗纸白强调大众传播属性；赭黄则把未来许诺压低到历史锈感之中。

### Palette 20 — Constantinople

#### 色彩哲学

君士坦丁堡的颜色必须同时属于希腊-罗马、波斯-伊斯兰、基督教与奥斯曼。金、蓝、紫、赭、象牙与暗绿在这里不是装饰，而是多文明叠压后的物质回声：穹顶金光、海峡深蓝、骨螺帝王紫、城墙赭土、大理石象牙和柏树深绿共同构成一座海都的神圣与世俗。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 普罗科尼索象牙 | Λευκός · Fildişi | `rgb(236,225,207)` | 大理石地面的暖象牙底色 |
| 圣索菲亚金 | Χρυσός · Altın | `rgb(195,150,42)` | 烛烟熏染后的旧金 |
| 狄奥多西赭 | Ώχρα · Toprak | `rgb(170,112,50)` | 城墙与安纳托利亚土地的赭土色 |
| 柏树暗绿 | Κυπαρίσσι · Selvi | `rgb(50,76,58)` | 墓地、庭园与铜绿柱础的深绿 |
| 帝王骨螺紫 | Πορφύρα · Mor | `rgb(102,32,65)` | 权力与宗教之间的深红紫 |
| 博斯普鲁斯蓝 | Βόσπορος · Boğaz | `rgb(30,52,88)` | 海峡在傍晚收拢光线后的深沉蓝 |

#### 完整色板

```text
Χρυσός · Altın       圣索菲亚金      rgb(195, 150,  42)  ██  神圣·永恒·烛火之光
Βόσπορος · Boğaz     博斯普鲁斯蓝    rgb( 30,  52,  88)  ██  深渊·海都·文明交汇
Πορφύρα · Mor        帝王骨螺紫      rgb(102,  32,  65)  ██  权力·奢华·无价之色
Ώχρα · Toprak        狄奥多西赭      rgb(170, 112,  50)  ██  大地·坚守·城墙记忆
Λευκός · Fildişi     普罗科尼索象牙  rgb(236, 225, 207)  ░░  底色·理性·大理石呼吸
Κυπαρίσσι · Selvi    柏树暗绿        rgb( 50,  76,  58)  ██  永恒·死亡·两种信仰的凝视
```

文明交汇的色彩结构：东西冷暖轴由深蓝与赭土构成；神圣三角由金、紫、象牙构成；柏树暗绿则承担最长的历史纵深，使整组配色在华贵之外仍保有时间的阴影。

### Palette 21 — France

#### 色彩哲学

法兰西的颜色不是简单的红白蓝，而是一种“被文化重新训练过的红白蓝”。共和红需要有血与单宁的重量；白不是纯白，而是香槟象牙；蓝则带启蒙理性的深度。再辅以薰衣草、橄榄金与锌灰，整组色才能同时拥有浪漫、理性、贵族、土地与现代城市气质。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 香槟象牙 | Ivoire Champagne | `rgb(232,222,205)` | 含时间杂质的“白” |
| 凡尔赛橄榄金 | Olive Dorée | `rgb(142,133,58)` | 法式园林式的古典金绿 |
| 巴黎锌灰 | Zinc Parisien | `rgb(122,126,132)` | 奥斯曼巴黎屋顶的冷灰 |
| 普罗旺斯薰衣草 | Lavande Provençale | `rgb(143,108,148)` | 南法暖紫 |
| 共和红 | Rouge Marianne | `rgb(180,32,40)` | 沉而有力的革命红 |
| 共和深蓝 | Bleu République | `rgb(44,74,138)` | 启蒙理性与国家权威之蓝 |

#### 完整色板

```text
Rouge Marianne      共和红         rgb(180,  32,  40)  ██  激情·革命·波尔多深处
Bleu République     共和深蓝       rgb( 44,  74, 138)  ██  理性·权威·启蒙的颜色
Ivoire Champagne    香槟象牙       rgb(232, 222, 205)  ░░  底气·时间·含杂质的纯粹
Lavande Provençale  普罗旺斯薰衣草 rgb(143, 108, 148)  ██  浪漫·土地·南北之间的裂缝
Olive Dorée         凡尔赛橄榄金   rgb(142, 133,  58)  ██  秩序·贵族·驯化的自然
Zinc Parisien       巴黎锌灰       rgb(122, 126, 132)  ██  克制·现代·奥斯曼的天际
```

法兰西精神的色彩结构：三色旗被重新解释为文化色而非政治符号；南法暖紫与巴黎锌灰构成南北气质裂缝；橄榄金与深蓝之间则潜伏着王权与共和的深层对立。

### Palette 22 — Kyoto

#### 色彩哲学

京都的颜色从不主动开口。绢白、樱灰粉、青竹灰、枯茶褐、苔绿与暗绀构成“六色底”，共同营造幽玄、柔雾、低饱和、留白克制的古都精神；而朱红只允许以极小面积出现，像茶室里唯一一枝有温度的花。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 绢白 | Kinushiro | `rgb(234,226,212)` | 和纸与绢布的暖白留白 |
| 樱灰粉 | Sakura-nezumi | `rgb(204,184,178)` | 落樱覆石后的灰粉 |
| 青竹灰 | Aotake-nezumi | `rgb(116,126,120)` | 晨雾中竹节的冷暖平衡色 |
| 枯茶褐 | Karacha | `rgb(110,84,64)` | 百年杉木的侘び之褐 |
| 苔色 | Koke-iro | `rgb(80,94,68)` | 禅院石组底部的哑深绿 |
| 暗绀 | Kon | `rgb(34,40,66)` | 能剧与夜色的深靛蓝 |

#### 点睛色

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 朱鸟居 | Shu-hi | `rgb(170,50,36)` | 极小面积使用的朱红点睛色 |

#### 完整色板

```text
絹白  Kinushiro    rgb(234, 226, 212)  ░░  底·呼吸·留白的物质
枯茶  Karacha      rgb(110,  84,  64)  ██  暖·侘び·百年杉木
桜鼠  Sakura-nez   rgb(204, 184, 178)  ░░  柔·物哀·落樱之灰
青竹鼠 Aotake-nez  rgb(116, 126, 120)  ██  冷·平衡·晨雾竹节
苔色  Koke-iro     rgb( 80,  94,  68)  ██  沉·时间·枯山水苔
紺    Kon          rgb( 34,  40,  66)  ██  深·冥想·能剧暗夜
─────────────────────────────────────────
朱緋  Shu-hi ·点睛 rgb(170,  50,  36)  ██  燃·鸟居·冷寂里的热
```

京都精神的色彩结构：留白为骨，冷暖天平靠青竹灰与枯茶褐维持，幽玄来自全部颜色去鲜亮后的柔雾感，而朱红作为唯一破局者，只能在最关键的点上出现。炸裂的红是装饰，克制的朱红才是京都。

### Palette 23 — Siamese Dream

#### 色彩哲学

《Siamese Dream》的封面本身就是一张配色宣言——两个女孩在柔焦的暖白光晕里相依，背景的深绿若隐若现，橙黄的光线像记忆里某个下午，美好得不真实。这不是摇滚专辑封面惯用的高对比冲击美学，而是一种刻意制造的梦境质感：过曝、柔化、带着胶片颗粒的温柔失真——如同 Corgan 把最原始的情感录进了最失真的吉他音墙里。

#### 六色配色组

| 名称 | 英文 | RGB | 说明 |
|---|---|---|---|
| 终章暖白 | Luna | `rgb(238,226,208)` | 封面光晕、专辑收束的余韵：胶片过曝后仍残留的人间温度 |
| 裸露灰紫 | Disarm | `rgb(182,180,193)` | Disarm 卸下所有失真时的颜色：玻璃碎裂前的透明与脆 |
| 可疑旧金 | Today | `rgb(198,158,65)` | Today 表层明媚旋律下的褪色金：美丽而不可信任 |
| 悬浮烟灰 | Hummer | `rgb(150,145,135)` | shoegaze 音墙堆叠出的失重悬浮：梦游者眼中的物质形态 |
| 低温烧橙 | Mayonaise | `rgb(188,105,40)` | 封面光源色、情感核心：积压已久的情绪在低温中缓慢焦化 |
| 深渊暗绿 | Soma | `rgb(42,68,48)` | 封面背景的深绿、九分钟史诗的坍塌：苔藓与腐叶共生的有机黑暗 |

#### 完整色板

```text
Luna       rgb(238, 226, 208)  ░░  终·暖白·胶片过曝后的人间温度
Disarm     rgb(182, 180, 193)  ░░  裸·灰紫·玻璃碎裂前的脆
Today      rgb(198, 158,  65)  ██  悖·旧金·美丽而不可信任
Hummer     rgb(150, 145, 135)  ██  漂·烟灰·梦游者的悬浮
Mayonaise  rgb(188, 105,  40)  ██  核·烧橙·低温焦化的情感
Soma       rgb( 42,  68,  48)  ██  深·暗绿·苔藓与腐叶的有机黑暗
```

Siamese Dream 的色彩结构是青春期情感的悖论：Luna 的暖白与 Hummer 的烟灰构成失焦层，把所有痛苦先过曝、再柔化；Today 的旧金与 Disarm 的灰紫是悖论的两极，用最美的容器装最重的内容；Mayonaise 的烧橙作为 primary 不是燃烧的红，而是已经燃烧过、被时间慢烤的橙；Soma 的暗绿作为 accent，是六色中唯一的“黑色替身”——不是纯黑，而是仍在生长的有机黑暗。整组配色全部退避鲜亮，因为这张专辑的情绪从不爆炸——它渗透。

---

## 参与贡献：添加你自己的配色

**这个模板是开放的，欢迎任何想要在 Tufte 风格书籍版式上继续创作的人参与进来。**
配色是这套模板最有表现力的部分，也是最容易扩展的部分——如果你为某本书、某幅画、某个城市、某段记忆调出了一组让你满意的六色，我希望你愿意把它提交回来，让这个调色板谱系继续生长。

### 添加一组新配色，只需要改动两处文件、三处接口

所有需要修改的位置都已用 `===== ADD-A-PALETTE INTERFACE =====` 注释块标记，全局检索即可定位。

1. **`Thomas-Tufte-bilingual-book.sty`** — 模板运行时的配色逻辑
   - **接口 ①**：`\OUCSetPalette` 宏的 `\or` 分支列表中追加一行
     ```latex
     \or
       \book@setpalettecolors{Your Palette Name}{R1,G1,B1}{R2,G2,B2}{R3,G3,B3}{R4,G4,B4}{R5,G5,B5}{R6,G6,B6}%
     ```
     这是模板在编译期切换配色的入口。六色按 **由浅到深** 排列，分别对应 `pal1` 到 `pal6`（语义化别名见 `\book@setpalettecolors` 的注释）。
   - **接口 ②**：`\bookpaletteguideentries` 宏中追加一行
     ```latex
     \bookpaletteguideentry{N}{Your Palette Name}{R1,G1,B1}{R2,G2,B2}{R3,G3,B3}{R4,G4,B4}{R5,G5,B5}{R6,G6,B6}%
     ```
     `N` 为新配色的索引号（接在最后即可）。这条会在《配色总览》一章作为色卡速查行显示。

2. **`gen_palette_intro.py`** — 配色介绍章节的数据源
   - **接口 ③**：在文件中部的 `P.append(dict(...))` 列表末尾追加一个新的配色条目，按现有条目格式填写中文 / 英文配色哲学、六色表与每色释义。
   - 之后运行 `python3 gen_palette_intro.py`，会自动重写 `palette-intro-zh.tex` 与 `palette-intro-en.tex`。

### 几点小约定

- **六色顺序**：从最浅到最深，即 `pal1` 是页面最亮的浅色（背景 / 浅边栏），`pal6` 是最深色（标题主色 / 强调色）。展示页的「前三浅 / 后三深」规则与文字颜色对比都依赖这个顺序。
- **色彩哲学**：每组配色至少要有一段简短的色彩哲学，说明这组配色想表达的世界观——这是这个项目希望延续的传统，比单纯堆色值更重要。
- **命名风格**：英文配色名建议落到一个具体的文化坐标（一幅画、一张专辑、一座城、一个文学典故），中文译名追求意象等价而非字面直译。
- **贡献方式**：直接 fork → 改三处接口 → 跑一次 `python3 gen_palette_intro.py` → 重新编译两本 demo → 提 PR；或在 issue 中贴出色值与设计文案，由维护者代为合入。

如果你只是想 **使用** 现有的某组配色，依旧只需要在书的入口文件中写一行 `\OUCSetPalette{N}`，N 从 0 到 23。

---

## 备注

- 本仓库是 `OUC-Haide-Book-Template` 项目的公开发布版，以「Thomas Shang's Tufte-Style Book Template」作为完整名称重新品牌。
- 仓库内包含两本预生成的 demo PDF，未安装 TeX 发行版也可以直接打开预览样式。
- `palette-intro-zh.tex` / `palette-intro-en.tex` 由 `gen_palette_intro.py` 自动生成；补充、改动配色说明请编辑脚本后重新运行。
- 原始 beamer 模板与 Tufte 示例文件不随本仓库分发；如需查阅请访问下方「致谢」一节给出的上游链接。

---

## 致谢

本模板的版式与配色机制建立在若干开源工作之上，作者特此致谢：

- **Tufte-LaTeX** —— 本模板所基于的 `tufte-book` 文档类的来源，是整套书籍版式的排印基础。
  <https://github.com/Tufte-LaTeX/tufte-latex>
- **OUC-Haide-Beamer-Template** —— 本书模板的配色机制与视觉语言的直接来源，`\OUCSetPalette` 接口与配色体系均沿袭并扩展自该 beamer 模板。
  <https://github.com/Hatsuyuki017/OUC-Haide-Beamer-Template>
- **Mattia Puddu** —— 其 Tufte 风格书籍版式中受 VDQI 启发的标题页与目录页设计，直接启发了本模板的前置内容（front matter）排版。
  <https://mattiapuddu25.github.io/index.html>
