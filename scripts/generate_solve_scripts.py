#!/usr/bin/env python3
"""批量生成所有题目的解题脚本"""
import os

SOLVE_TEMPLATE = '''#!/usr/bin/env python3
"""自动生成的解题脚本"""
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '../../../../'))
sys.path.insert(0, project_root)

from scripts.lib.{module} import main as run_solution

if __name__ == "__main__":
    os.chdir(os.path.join(project_root, "scripts"))
    print("=" * 60)
    print("  {paper} - {title}")
    print("=" * 60)
    run_solution({paper_num})
'''

CONFIGS = [
    # 模拟试卷1
    (1, "试题1-数据采集和处理/a)业务数据采集", "collect", "试题1-a: 猫狗图片采集"),
    (1, "试题1-数据采集和处理/b)业务数据处理", "classify", "试题1-b: 动物分类"),
    (1, "试题2-数据标注/a)原始数据清洗与标注", "clean", "试题2-a: 吉普车数据清洗"),
    (1, "试题2-数据标注/b)标注后数据分类与统计", "statistics", "试题2-b: 车辆分类统计"),

    # 模拟试卷2
    (2, "试题1-数据采集和处理/a)业务数据采集", "collect", "试题1-a: 丛林/海洋图片采集"),
    (2, "试题1-数据采集和处理/b)业务数据处理", "classify", "试题1-b: 自然风光分类"),
    (2, "试题2-数据标注/a)原始数据清洗与标注", "clean", "试题2-a: 海豚数据清洗"),
    (2, "试题2-数据标注/b)标注后数据分类与统计", "statistics", "试题2-b: 花卉分类统计"),

    # 模拟试卷3
    (3, "试题1-数据采集和处理/a)业务数据采集", "collect", "试题1-a: 玫瑰/向日葵图片采集"),
    (3, "试题1-数据采集和处理/b)业务数据处理", "classify", "试题1-b: 花卉分类"),
    (3, "试题2-数据标注/a)原始数据清洗与标注", "clean", "试题2-a: 海豚数据清洗"),
    (3, "试题2-数据标注/b)标注后数据分类与统计", "statistics", "试题2-b: 花卉分类统计"),
]


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for paper_num, dir_path, module, title in CONFIGS:
        full_dir = os.path.join(project_root, f"模拟试卷{paper_num}", dir_path)
        solve_path = os.path.join(full_dir, "solve.py")

        content = SOLVE_TEMPLATE.format(
            paper=f"模拟试卷{paper_num}",
            title=title,
            module=module,
            paper_num=paper_num
        )

        with open(solve_path, 'w', encoding='utf-8') as f:
            f.write(content)

        os.chmod(solve_path, 0o755)
        print(f"✓ 生成: 模拟试卷{paper_num}/{dir_path}/solve.py")

    print(f"\n完成！共生成 {len(CONFIGS)} 个解题脚本")
    print("\n💡 使用方式:")
    print("  cd 模拟试卷3/试题1-数据采集和处理/a)业务数据采集")
    print("  uv run python solve.py")


if __name__ == "__main__":
    main()
