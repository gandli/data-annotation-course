import os
import sys
import shutil
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import ensure_dir, print_stats

PAPER_CONFIGS = {
    1: {
        "src_dir": "../模拟试卷1/试题2-数据标注/b)标注后数据分类与统计/需要进行分类统计的车辆数据集",
        "dst_dir": "../模拟试卷1/试题2-数据标注/b)标注后数据分类与统计/数据分类后的车辆数据集",
        "categories": ["taxi", "SUV", "Bus", "fireengine", "racingcar"],
        "chinese_names": ["出租车", "SUV", "公交车", "消防车", "赛车"]
    },
    2: {
        "src_dir": "../模拟试卷2/试题2-数据标注/b)标注后数据分类与统计/需要进行分类统计的花卉数据集",
        "dst_dir": "../模拟试卷2/试题2-数据标注/b)标注后数据分类与统计/数据分类后的花卉数据集",
        "categories": ["daisy", "dandelion", "rose", "sunflower", "tulip"],
        "chinese_names": ["雏菊", "蒲公英", "玫瑰", "向日葵", "郁金香"]
    },
    3: {
        "src_dir": "../模拟试卷3/试题2-数据标注/b)标注后数据分类与统计/需要进行分类统计的花卉数据集",
        "dst_dir": "../模拟试卷3/试题2-数据标注/b)标注后数据分类与统计/数据分类后的花卉数据集",
        "categories": ["daisy", "dandelion", "rose", "sunflower", "tulip"],
        "chinese_names": ["雏菊", "蒲公英", "玫瑰", "向日葵", "郁金香"]
    }
}


def main(paper_num):
    if paper_num not in PAPER_CONFIGS:
        print(f"错误：试卷 {paper_num} 配置不存在")
        print(f"可用试卷: {list(PAPER_CONFIGS.keys())}")
        sys.exit(1)

    config = PAPER_CONFIGS[paper_num]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(script_dir, config["src_dir"])
    dst_dir = os.path.join(script_dir, config["dst_dir"])

    for cat in config["categories"]:
        ensure_dir(os.path.join(dst_dir, cat))

    from glob import glob
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        image_files.extend(glob(os.path.join(src_dir, ext)))

    print(f"找到 {len(image_files)} 张待统计图片")

    counts = {cat: 0 for cat in config["categories"]}

    for img_path in image_files:
        f = os.path.basename(img_path)
        name_part = f.split('(')[0].strip().lower()

        matched_cat = None
        for cat in config["categories"]:
            if cat.lower() == name_part:
                matched_cat = cat
                break

        if matched_cat:
            counts[matched_cat] += 1
            shutil.copy2(img_path, os.path.join(dst_dir, matched_cat, f))
        else:
            print(f"警告: 无法分类 {f}")

    display_items = list(zip(config["chinese_names"], counts.values()))
    print_stats("分类统计结果：", display_items, headers=["序号", "类别", "数量"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python 4_statistics.py <试卷号: 1|2|3>")
        sys.exit(1)
    main(int(sys.argv[1]))
