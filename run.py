#!/usr/bin/env python3
"""数据标注课程 - 总入口"""
import os
import subprocess
import sys


def print_help():
    print("=" * 60)
    print("  数据标注课程 - 自动化解题脚本")
    print("=" * 60)
    print("\n📁 项目结构:")
    print("  模拟试卷3/")
    print("    ├── run_all.py              ← 一键运行整套试卷")
    print("    ├── 试题1-数据采集和处理/")
    print("    │   ├── a)业务数据采集/solve.py")
    print("    │   └── b)业务数据处理/solve.py")
    print("    ├── 试题2-数据标注/")
    print("    │   ├── a)原始数据清洗与标注/solve.py")
    print("    │   └── b)标注后数据分类与统计/solve.py")
    print("    └── 试题3-智能系统运维/*.ipynb")
    print("\n🎯 推荐使用方式:")
    print()
    print("  方式1: 做整套试卷")
    print("    cd 模拟试卷3")
    print("    uv run python run_all.py")
    print()
    print("  方式2: 做单道试题")
    print("    cd 模拟试卷3/试题1-数据采集和处理/a)业务数据采集")
    print("    uv run python solve.py")
    print()
    print("  方式3: 根目录快速运行")
    print("    uv run python run.py 3")
    print("\n📦 环境命令:")
    print("  uv venv .venv --python 3.11")
    print("  uv pip install -r requirements.txt")
    print()


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        return

    paper_arg = sys.argv[1]
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"模拟试卷{paper_arg}")
    runner = os.path.join(script_dir, 'run_all.py')

    if not os.path.exists(runner):
        print(f"❌ 找不到试卷 {paper_arg}")
        sys.exit(1)

    subprocess.run([sys.executable, runner], cwd=script_dir)


if __name__ == "__main__":
    main()
