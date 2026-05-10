#!/usr/bin/env python3
"""自动生成的入口脚本 - 试题2-b: 5种花卉分类统计"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, "../../../scripts/4_statistics.py")

print("=" * 60)
print("试题2-b: 5种花卉分类统计")
print("=" * 60)

subprocess.run([sys.executable, main_script, "2"], cwd=os.path.dirname(main_script))
