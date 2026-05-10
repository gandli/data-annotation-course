#!/usr/bin/env python3
"""自动生成的入口脚本 - 试题1-b: 5种自然风光分类统计"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, "../../../scripts/2_classify_images.py")

print("=" * 60)
print("试题1-b: 5种自然风光分类统计")
print("=" * 60)

subprocess.run([sys.executable, main_script, "2"], cwd=os.path.dirname(main_script))
