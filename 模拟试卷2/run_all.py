#!/usr/bin/env python3
"""试卷1 - 一键运行所有试题"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
runner = os.path.join(script_dir, '../scripts/run_all.py')

print("=" * 60)
print("试卷1 - 数据标注自动化解题")
print("=" * 60)

subprocess.run([sys.executable, runner, "2"], cwd=os.path.dirname(runner))
