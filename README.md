# Data Annotation Course - Automation Scripts

Automatically solve data annotation course exercises using Python + CLIP model.

[中文文档](README_CN.md) | English Documentation

## 🚀 Quick Start

### Environment Setup

```bash
# 1. Install uv (ultra fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create virtual environment (Python 3.11+ recommended)
uv venv .venv --python 3.11

# 3. Install core dependencies (for Questions 1-2)
uv pip install -r requirements.txt

# To run Question 3 Notebook (optional):
# uv pip install tensorflow matplotlib notebook nbconvert
```

---

## 📁 Project Structure

```
.
├── run.py                      # 🌱 Root entry point
├── requirements.txt            # 📦 Dependencies
├── pyproject.toml             # ⚙️ Project config
├── .gitignore                 # 🚫 Git ignore rules
│
├── scripts/                   # 📜 Scripts directory
│   ├── lib/                   # 🧠 Core algorithm library
│   │   ├── collect.py         # Question 1-a: Image collection
│   │   ├── classify.py        # Question 1-b: CLIP image classification
│   │   ├── clean.py           # Question 2-a: Data cleaning
│   │   └── statistics.py      # Question 2-b: Classification statistics
│   └── generate_solve_scripts.py
│
├── paper_01/
│   ├── run_all.py             # 📑 One-click run for entire paper
│   ├── question_01_data_collection/
│   │   ├── a)business_data_collection/solve.py
│   │   └── b)business_data_processing/solve.py
│   ├── question_02_data_annotation/
│   │   ├── a)raw_data_cleaning/solve.py
│   │   └── b)labeled_data_classification/solve.py
│   └── question_03_intelligent_system_operations/
│       └── *.ipynb           # 📓 Jupyter Notebook
│
├── paper_02/                 # Same structure as paper 1
└── paper_03/                 # Same structure as paper 1
```

---

## 🎯 Three Usage Methods

### Method 1: Quick Run from Root

```bash
# Show help
uv run python run.py

# Run paper 3 with one command
uv run python run.py 3
```

### Method 2: Run Entire Paper

```bash
cd paper_03
uv run python run_all.py    # Auto-run: Question 1-a → 1-b → 2-a → 2-b
```

### Method 3: Run Single Question

```bash
cd paper_03/question_01_data_collection/a)business_data_collection
uv run python solve.py      # Run only this question
```

---

## 📝 Question Functionality

| Question | Feature | Technical Solution |
|----------|---------|--------------------|
| **Question 1-a** | Image Collection | Unsplash API batch download for specified categories |
| **Question 1-b** | Image Classification | OpenAI CLIP zero-shot image classification model |
| **Question 2-a** | Data Cleaning | MD5 deduplication + OpenCV blur detection + CLIP subject judgment |
| **Question 2-b** | Classification Statistics | Filename prefix matching + classification archiving |
| **Question 3** | Intelligent System Ops | Jupyter Notebook + TensorFlow/MNIST |

---

## 💡 Technical Features

1. **Unified CLIP Model**
   - All image recognition tasks use the CLIP model
   - Jeep recognition: identifies "images with jeep logo" rather than car models
   - High accuracy, robust to angle/lighting variations

2. **Elegant Directory Structure**
   - Scripts are located exactly where you work on the questions
   - Each question directory has its own independent `solve.py`
   - Core logic written once, centrally maintained in `scripts/lib/`

3. **Git Friendly**
   - Generated result directories automatically ignored
   - Original test datasets preserved in repository
   - Only commit code, not generated images

---

## ⚠️ Notes

- **Python Version**: Questions 1-2 support Python 3.10+, Question 3 Notebook requires Python 3.11+ (tensorflow dependency requirement)
- **First Run**: CLIP model downloads automatically (~600MB), please be patient
- **Network Issues**: If HuggingFace download is slow, configure mirror:
  ```bash
  export HF_ENDPOINT=https://hf-mirror.com
  uv run python solve.py
  ```

---

## 🔧 Developer Commands

```bash
# Regenerate all solution scripts
python scripts/generate_solve_scripts.py

# List installed packages
uv pip list

# Add new dependency
uv add <package-name>
```
