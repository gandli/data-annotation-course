#!/usr/bin/env python3
"""数据标注课程 - 总入口脚本"""
import os
import subprocess
import sys


def print_help():
    print("=" * 60)
    print("  数据标注课程 - 自动化解题脚本")
    print("=" * 60)
    print("\n📁 项目结构（按照学习路径）:")
    print("  模拟试卷1/")
    print("    ├── run_all.py              ← 一键运行整套试卷")
    print("    ├── 试题1-数据采集和处理/")
    print("    │   ├── a)业务数据采集/run.py")
    print("    │   └── b)业务数据处理/run.py")
    print("    ├── 试题2-数据标注/")
    print("    │   ├── a)原始数据清洗与标注/run.py")
    print("    │   └── b)标注后数据分类与统计/run.py")
    print("    └── 试题3-智能系统运维/")
    print("")
    print("  模拟试卷2/      结构同上")
    print("  模拟试卷3/      结构同上")
    print("\n🎯 推荐使用方式（按照学习顺序）:")
    print("")
    print("  第1步：选择试卷")
    print("    cd 模拟试卷3")
    print("    uv run python run_all.py")
    print("")
    print("  第2步：选择试题（单独练习）")
    print("    cd 模拟试卷3/试题1-数据采集和处理/a)业务数据采集")
    print("    uv run python run.py")
    print("\n⚡ 根目录快速运行:")
    print("  uv run python run.py 1        # 运行试卷1")
    print("  uv run python run.py 2        # 运行试卷2")
    print("  uv run python run.py 3        # 运行试卷3")
    print("  uv run python run.py all      # 运行所有试卷")
    print("\n📦 环境命令:")
    print("  uv venv .venv                 # 创建虚拟环境")
    print("  uv pip install -r requirements.txt  # 安装依赖")
    print()


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        return

    paper_arg = sys.argv[1]
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
    runner = os.path.join(script_dir, 'run_all.py')

    subprocess.run([sys.executable, runner, paper_arg], cwd=script_dir)


if __name__ == "__main__":
    main()
