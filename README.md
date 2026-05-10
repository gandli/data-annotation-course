# 数据标注课程 - 自动化解题脚本

## 🚀 快速开始（uv 工作流）

### 第一步：环境搭建（只需一次）
```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境
uv venv .venv

# 安装核心依赖（试题 1-2 使用）
uv pip install -r requirements.txt

# 如需运行 试题3-智能系统运维 notebook：
# uv pip install tensorflow matplotlib notebook nbconvert
```

---

### 第二步：按照学习路径运行

#### 📑 方式1：做整套试卷（试题 1-2）
```bash
cd 模拟试卷3
uv run python run_all.py    # 一键运行试卷3的试题 1-2
```

#### 🎯 方式2：做单道试题
```bash
cd 模拟试卷3/试题1-数据采集和处理/a)业务数据采集
uv run python run.py        # 只运行 试题1-a 数据采集

cd ../b)业务数据处理
uv run python run.py        # 只运行 试题1-b 数据分类
```

#### 📓 方式3：运行 试题3 Notebook（智能系统运维）
```bash
# 方式1：命令行运行（自动执行并保存结果）
uv run python scripts/run_notebook.py 3

# 方式2：浏览器打开 Notebook
cd 模拟试卷3/试题3-智能系统运维
uv run jupyter notebook
```

#### 🌱 方式4：从根目录快速开始
```bash
# 查看帮助
uv run python run.py

# 直接运行整套试卷
uv run python run.py 3
```

---

### 🔧 开发者常用命令
```bash
uv pip list                 # 查看已安装的包
uv add <package-name>       # 安装新依赖
uv sync                     # 同步依赖（同学协作时）
```

---

### 💡 uv 核心优势

**为什么用 uv？**
- 🚀 比 pip 快 10-100 倍
- 🎯 **无需激活虚拟环境** - `uv run` 自动使用项目环境
- 📦 统一的项目配置（`pyproject.toml`）
- 🔒 可重现的构建（`uv.lock` 锁文件）

| 命令 | 作用 |
|------|------|
| `uv venv .venv` | 创建虚拟环境 |
| `uv pip install -r requirements.txt` | 安装依赖（超快速） |
| `uv run python ...` | 在项目环境中运行脚本 |
| `uv add <package>` | 添加新依赖 |
| `uv pip list` | 查看已安装的包 |

> ✨ **Pro Tip**: 再也不用 `source .venv/bin/activate` 了！任何脚本前面加 `uv run` 就对了。

## 📁 项目结构

```
.
├── scripts/              # 统一解题脚本目录
│   ├── run_all.py        # 🎯 一键运行入口（推荐）
│   ├── 1_collect_images.py    # 试题1-a: 图片采集
│   ├── 2_classify_images.py   # 试题1-b: 图片分类
│   ├── 3_clean_images.py      # 试题2-a: 数据清洗
│   └── 4_statistics.py        # 试题2-b: 分类统计
├── utils/                # 公共工具函数
│   └── image_utils.py
├── 模拟试卷1/           # 试卷1数据目录
├── 模拟试卷2/           # 试卷2数据目录
├── 模拟试卷3/           # 试卷3数据目录
├── requirements.txt     # Python 依赖
├── pyproject.toml       # 项目配置文件
└── .gitignore          # Git 忽略规则
```

## 📝 各试卷考点对应

| 试题 | 功能 | 对应脚本 | 技术方案 |
|------|------|----------|----------|
| **1-a** | 数据采集 | `1_collect_images.py` | Unsplash API |
| **1-b** | 数据分类 | `2_classify_images.py` | CLIP 零样本分类 |
| **2-a** | 数据清洗 | `3_clean_images.py` | MD5去重 + OpenCV模糊检测 + CLIP主体判断 |
| **2-b** | 分类统计 | `4_statistics.py` | 文件名前缀匹配归档 |
| **3** | 智能系统运维 | ipynb | TensorFlow/MNIST |

## 💡 说明

### 关于结果目录
脚本生成的图片结果目录不会提交到 Git 仓库，您需要：
1. 自行运行脚本生成结果
2. 原始待分类/待清洗数据集已作为测试数据保留

### 环境要求
- Python 3.10+
- 约 5GB 磁盘空间（模型下载 + 数据集）
- 推荐 8GB+ 内存

### 常见问题

**Q: CLIP 模型下载慢？**
A: 可以设置国内镜像源：
```bash
export HF_ENDPOINT=https://hf-mirror.com
python run_all.py 3
```

**Q: 如何验证结果准确性？**
A: 脚本执行后会输出分类统计表，您可以手动打开目标文件夹抽样检查分类结果。
