#!/usr/bin/env python3
"""运行 试题3-智能系统运维 的 Jupyter Notebook"""
import os
import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print("=" * 60)
        print("  试题3-智能系统运维 - Notebook 运行工具")
        print("=" * 60)
        print("\n📋 用法:")
        print("  uv run python run_notebook.py <试卷号>")
        print("\n📝 示例:")
        print("  uv run python run_notebook.py 1    # 运行试卷1的试题3")
        print("  uv run python run_notebook.py 3    # 运行试卷3的试题3")
        print("\n💡 提示:")
        print("  首次运行需要安装完整依赖:")
        print("  uv pip install tensorflow matplotlib")
        print()
        return

    paper_num = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    paper_dir = os.path.join(project_root, f"模拟试卷{paper_num}")
    notebook_path = os.path.join(paper_dir, "试题3-智能系统运维", "znxtyw-st1.ipynb" if paper_num == "1" else "znxtyw-st4.ipynb")

    if not os.path.exists(notebook_path):
        print(f"❌ 找不到 Notebook: {notebook_path}")
        sys.exit(1)

    print(f"🚀 正在运行 Notebook: {notebook_path}")
    print(f"📂 工作目录: {os.path.dirname(notebook_path)}")
    print()

    # 使用 nbconvert 运行 notebook
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        notebook_path
    ]

    result = subprocess.run(cmd, cwd=os.path.dirname(notebook_path))

    if result.returncode == 0:
        print("\n✅ Notebook 运行完成！")
    else:
        print(f"\n❌ Notebook 运行失败，返回码: {result.returncode}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
