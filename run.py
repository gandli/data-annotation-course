#!/usr/bin/env python3
"""数据标注课程 - 总入口脚本

用法:
  python run.py              # 显示帮助
  python run.py 3            # 运行试卷3全部流程
  python run.py all          # 运行所有试卷
"""
import os
import subprocess
import sys


def print_help():
    print("=" * 60)
    print("  数据标注课程 - 自动化解题脚本")
    print("=" * 60)
    print("\n📋 用法:")
    print("  python run.py              # 显示此帮助")
    print("  python run.py 1            # 运行试卷1全部流程")
    print("  python run.py 2            # 运行试卷2全部流程")
    print("  python run.py 3            # 运行试卷3全部流程")
    print("  python run.py all          # 运行所有试卷")
    print("\n💡 其他使用方式:")
    print("  cd 模拟试卷3 && python run_all.py")
    print("  cd 模拟试卷3/试题1-数据采集和处理/b)业务数据处理 && python run.py")
    print("\n🔧 环境搭建:")
    print("  uv venv .venv && source .venv/bin/activate")
    print("  uv pip install -r requirements.txt")
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
