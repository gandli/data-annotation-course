import os
import sys
import subprocess

SCRIPTS = [
    ("1_collect_images.py", "数据采集"),
    ("2_classify_images.py", "数据分类"),
    ("3_clean_images.py", "数据清洗"),
    ("4_statistics.py", "数据统计"),
]

def run_script(script_name, paper_num, desc):
    print(f"\n{'='*60}")
    print(f"运行: {desc} ({script_name})")
    print(f"{'='*60}")

    script_path = os.path.join(os.path.dirname(__file__), script_name)
    result = subprocess.run(
        [sys.executable, script_path, str(paper_num)],
        capture_output=False,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ 脚本执行失败，返回码: {result.returncode}")
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print("=" * 60)
        print("  数据标注课程 - 自动化解题脚本")
        print("=" * 60)
        print("\n用法: python run_all.py <试卷号: 1|2|3|all>")
        print("\n示例:")
        print("  python run_all.py 1      # 运行试卷1全部流程")
        print("  python run_all.py all    # 运行所有试卷")
        print("\n分步运行:")
        print("  python 1_collect_images.py 3   # 只运行试卷3的数据采集")
        print("  python 2_classify_images.py 3  # 只运行试卷3的数据分类")
        print("  python 3_clean_images.py 3     # 只运行试卷3的数据清洗")
        print("  python 4_statistics.py 3       # 只运行试卷3的数据统计")
        print()
        sys.exit(1)

    paper_arg = sys.argv[1]
    papers = [1, 2, 3] if paper_arg == "all" else [int(paper_arg)]

    for paper in papers:
        print(f"\n{'#'*60}")
        print(f"# 开始处理试卷 {paper}")
        print(f"{'#'*60}")

        for script, desc in SCRIPTS:
            if not run_script(script, paper, desc):
                print(f"\n⚠️  试卷 {paper} 在 {desc} 步骤失败，跳过后续步骤")
                break

    print(f"\n{'='*60}")
    print("✅ 所有试卷处理完成")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
