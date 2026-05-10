#!/usr/bin/env python3
"""自动生成的入口脚本 - 试题2-a: 海豚数据清洗（去重/模糊/非主体）"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, "../../../scripts/3_clean_images.py")

print("=" * 60)
print("试题2-a: 海豚数据清洗（去重/模糊/非主体）")
print("=" * 60)

subprocess.run([sys.executable, main_script, "2"], cwd=os.path.dirname(main_script))
