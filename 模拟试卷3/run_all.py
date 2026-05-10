#!/usr/bin/env python3
"""模拟试卷3 - 一键运行所有试题"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("=" * 60)
print("  模拟试卷3 - 自动化解题")
print("=" * 60)
print()

steps = [
    ("试题1-a: 玫瑰/向日葵图片采集", "试题1-数据采集和处理/a)业务数据采集/solve.py"),
    ("试题1-b: 5种花卉分类", "试题1-数据采集和处理/b)业务数据处理/solve.py"),
    ("试题2-a: 海豚数据清洗", "试题2-数据标注/a)原始数据清洗与标注/solve.py"),
    ("试题2-b: 5种花卉分类统计", "试题2-数据标注/b)标注后数据分类与统计/solve.py"),
]

for i, (title, script_path) in enumerate(steps, 1):
    print(f"[{i}/{len(steps)}] {title}")
    print("-" * 60)

    result = subprocess.run([sys.executable, script_path], capture_output=False)

    if result.returncode != 0:
        print(f"\n❌ 步骤失败，停止执行")
        sys.exit(result.returncode)

    print()

print("=" * 60)
print("✅ 模拟试卷3 所有试题完成！")
print("=" * 60)
print("\n💡 接下来可以运行 试题3-智能系统运维 Notebook:")
print("   cd 试题3-智能系统运维 && uv run jupyter notebook")
