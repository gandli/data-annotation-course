#!/usr/bin/env python3
"""命令行入口 - uv run data-anno"""
import subprocess
import sys
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    runner = script_dir / "run_all.py"

    args = sys.argv[1:]
    if not args or args[0] in ['-h', '--help', 'help']:
        print("=" * 60)
        print("  数据标注课程 - 自动化解题脚本")
        print("=" * 60)
        print("\n📋 用法:")
        print("  uv run data-anno              # 显示此帮助")
        print("  uv run data-anno 1            # 运行试卷1全部流程")
        print("  uv run data-anno 2            # 运行试卷2全部流程")
        print("  uv run data-anno 3            # 运行试卷3全部流程")
        print("  uv run data-anno all          # 运行所有试卷")
        print("\n💡 uv 快捷命令:")
        print("  uv sync                       # 同步依赖环境")
        print("  uv run python ...             # 使用项目环境运行 Python")
        print()
        return

    subprocess.run([sys.executable, str(runner)] + args, cwd=str(script_dir))


if __name__ == "__main__":
    main()
