#!/usr/bin/env python3
"""自动生成的解题脚本"""
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '../../../../'))
sys.path.insert(0, project_root)

from scripts.lib.classify import main as run_solution

if __name__ == "__main__":
    os.chdir(os.path.join(project_root, "scripts"))
    print("=" * 60)
    print("  模拟试卷1 - 试题1-b: 动物分类")
    print("=" * 60)
    run_solution(1)
