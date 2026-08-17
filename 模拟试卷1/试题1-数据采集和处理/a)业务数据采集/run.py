#!/usr/bin/env python3
"""自动生成的入口脚本 - 试题1-a: 猫狗图片采集（各20张）"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, "../../../scripts/1_collect_images.py")

print("=" * 60)
print("试题1-a: 猫狗图片采集（各20张）")
print("=" * 60)

subprocess.run([sys.executable, main_script, "1"], cwd=os.path.dirname(main_script))
