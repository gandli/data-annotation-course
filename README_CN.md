# 数据标注课程 - 自动化解题脚本

使用 Python + CLIP 模型，自动完成数据标注课程的练习题。

## 🚀 快速开始

### 环境搭建

```bash
# 1. 安装 uv (超快速 Python 包管理工具)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 创建虚拟环境 (推荐 Python 3.11+)
uv venv .venv --python 3.11

# 3. 安装核心依赖 (试题 1-2)
uv pip install -r requirements.txt

# 如需运行试题3 Notebook (可选):
# uv pip install tensorflow matplotlib notebook nbconvert
```

---

## 📁 项目结构

```
.
├── run.py                      # 🌱 根目录入口
├── requirements.txt            # 📦 依赖清单
├── pyproject.toml             # ⚙️ 项目配置
├── .gitignore                 # 🚫 Git 忽略规则
│
├── scripts/                   # 📜 脚本目录
│   ├── lib/                   # 🧠 核心算法库
│   │   ├── collect.py         # 试题1-a: 图片采集
│   │   ├── classify.py        # 试题1-b: CLIP 图片分类
│   │   ├── clean.py           # 试题2-a: 数据清洗
│   │   └── statistics.py      # 试题2-b: 分类统计
│   └── generate_solve_scripts.py
│
├── 模拟试卷1/
│   ├── run_all.py             # 📑 试卷一键运行
│   ├── 试题1-数据采集和处理/
│   │   ├── a)业务数据采集/solve.py
│   │   └── b)业务数据处理/solve.py
│   ├── 试题2-数据标注/
│   │   ├── a)原始数据清洗与标注/solve.py
│   │   └── b)标注后数据分类与统计/solve.py
│   └── 试题3-智能系统运维/
│       └── *.ipynb           # 📓 Jupyter Notebook
│
├── 模拟试卷2/                 # 结构同试卷1
└── 模拟试卷3/                 # 结构同试卷1
```

---

## 🎯 三种使用方式

### 方式1: 根目录快速运行

```bash
# 查看帮助
uv run python run.py

# 一键运行试卷3
uv run python run.py 3
```

### 方式2: 整套试卷运行

```bash
cd 模拟试卷3
uv run python run_all.py    # 自动运行试题1-a → 1-b → 2-a → 2-b
```

### 方式3: 单道试题运行

```bash
cd 模拟试卷3/试题1-数据采集和处理/a)业务数据采集
uv run python solve.py      # 只运行这一道题
```

---

## 📝 各试题功能说明

| 试题 | 功能 | 技术方案 |
|------|------|----------|
| **试题1-a** | 图片采集 | Unsplash API 批量下载指定类别图片 |
| **试题1-b** | 图片分类 | OpenAI CLIP 零样本图像分类模型 |
| **试题2-a** | 数据清洗 | MD5去重 + OpenCV模糊检测 + CLIP主体判断 |
| **试题2-b** | 分类统计 | 文件名前缀匹配 + 分类归档 |
| **试题3** | 智能系统运维 | Jupyter Notebook + TensorFlow/MNIST |

---

## 💡 技术特性

1. **CLIP 模型统一**
   - 所有图片识别任务统一使用 CLIP 模型
   - 吉普车识别: 识别"含 jeep logo 的图片"而非车型
   - 准确率高，对角度/光线鲁棒性好

2. **优雅的目录结构**
   - 在哪里做题，脚本就在哪里
   - 每个题目目录下都有独立的 `solve.py`
   - 核心逻辑只写一次，统一在 `scripts/lib/`

3. **Git 友好**
   - 脚本生成的结果目录自动忽略
   - 原始测试数据集保留在仓库
   - 只提交代码，不提交生成的图片

---

## ⚠️ 注意事项

- **Python 版本**: 试题1-2 支持 Python 3.10+，试题3 Notebook 需要 Python 3.11+ (tensorflow 依赖要求)
- **首次运行**: CLIP 模型会自动下载 (~600MB)，请耐心等待
- **网络问题**: 如遇 HuggingFace 下载慢，可配置镜像:
  ```bash
  export HF_ENDPOINT=https://hf-mirror.com
  uv run python solve.py
  ```

---

## 🔧 开发者命令

```bash
# 重新生成所有解题脚本
python scripts/generate_solve_scripts.py

# 查看已安装的包
uv pip list

# 添加新依赖
uv add <package-name>
```
