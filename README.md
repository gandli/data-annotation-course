# 数据标注课程 - 自动化解题脚本

## 🚀 快速开始

### 1. 环境搭建
```bash
# 安装 uv（如果未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境并安装依赖
uv venv .venv
source .venv/bin/activate  # macOS/Linux
# 或 Windows: .venv\Scripts\activate

uv pip install -r requirements.txt
```

### 2. 运行脚本（三层入口体系）

#### 🌱 第1次使用 - 从根目录开始
```bash
# 查看帮助
python run.py

# 运行试卷3
python run.py 3
```

#### 📑 做整套试卷
```bash
cd 模拟试卷3
python run_all.py    # 一键运行试卷3的全部4道题
```

#### 🎯 做单道题目
```bash
cd 模拟试卷3/试题1-数据采集和处理/b)业务数据处理
python run.py        # 只运行本题目的自动化脚本
```

#### 🔧 开发者方式（scripts 目录）
```bash
cd scripts
python 1_collect_images.py 3   # 数据采集
python 2_classify_images.py 3  # 数据分类
python 3_clean_images.py 3     # 数据清洗
python 4_statistics.py 3       # 数据统计
```

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
