#!/usr/bin/env python3
"""批量生成各试题目录下的入口脚本 run.py"""
import os

SCRIPT_TEMPLATE = '''#!/usr/bin/env python3
"""自动生成的入口脚本 - {description}"""
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, "{rel_path}scripts/{script_name}")

print("=" * 60)
print("{description}")
print("=" * 60)

subprocess.run([sys.executable, main_script, "{paper_num}"], cwd=os.path.dirname(main_script))
'''

ENTRY_POINTS = [
    # 试卷1
    (1, "模拟试卷1/试题1-数据采集和处理/a)业务数据采集", "1_collect_images.py", "试题1-a: 猫狗图片采集（各20张）"),
    (1, "模拟试卷1/试题1-数据采集和处理/b)业务数据处理", "2_classify_images.py", "试题1-b: 5种动物分类统计"),
    (1, "模拟试卷1/试题2-数据标注/a)原始数据清洗与标注", "3_clean_images.py", "试题2-a: 吉普车数据清洗（去重/模糊/非主体）"),
    (1, "模拟试卷1/试题2-数据标注/b)标注后数据分类与统计", "4_statistics.py", "试题2-b: 5种车辆分类统计"),

    # 试卷2
    (2, "模拟试卷2/试题1-数据采集和处理/a)业务数据采集", "1_collect_images.py", "试题1-a: 丛林/海洋图片采集（各20张）"),
    (2, "模拟试卷2/试题1-数据采集和处理/b)业务数据处理", "2_classify_images.py", "试题1-b: 5种自然风光分类统计"),
    (2, "模拟试卷2/试题2-数据标注/a)原始数据清洗与标注", "3_clean_images.py", "试题2-a: 海豚数据清洗（去重/模糊/非主体）"),
    (2, "模拟试卷2/试题2-数据标注/b)标注后数据分类与统计", "4_statistics.py", "试题2-b: 5种花卉分类统计"),

    # 试卷3
    (3, "模拟试卷3/试题1-数据采集和处理/a)业务数据采集", "1_collect_images.py", "试题1-a: 玫瑰/向日葵图片采集（各20张）"),
    (3, "模拟试卷3/试题1-数据采集和处理/b)业务数据处理", "2_classify_images.py", "试题1-b: 5种花卉分类统计"),
    (3, "模拟试卷3/试题2-数据标注/a)原始数据清洗与标注", "3_clean_images.py", "试题2-a: 海豚数据清洗（去重/模糊/非主体）"),
    (3, "模拟试卷3/试题2-数据标注/b)标注后数据分类与统计", "4_statistics.py", "试题2-b: 5种花卉分类统计"),
]


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for paper_num, target_dir, script_name, description in ENTRY_POINTS:
        full_dir = os.path.join(project_root, target_dir)
        if not os.path.exists(full_dir):
            print(f"⚠️  目录不存在，跳过: {target_dir}")
            continue

        depth = len(target_dir.split('/'))
        rel_path = '../' * depth

        run_script = os.path.join(full_dir, "run.py")
        with open(run_script, 'w', encoding='utf-8') as f:
            f.write(SCRIPT_TEMPLATE.format(
                description=description,
                rel_path=rel_path,
                script_name=script_name,
                paper_num=paper_num
            ))

        os.chmod(run_script, 0o755)
        print(f"✓ 已生成: {target_dir}/run.py")

    print(f"\n完成！共生成 {len(ENTRY_POINTS)} 个入口脚本")
    print("\n💡 使用方式:")
    print("  cd 模拟试卷3/试题1-数据采集和处理/b)业务数据处理")
    print("  python run.py  # 直接运行本题目对应脚本")


if __name__ == "__main__":
    main()
