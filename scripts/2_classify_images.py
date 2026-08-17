import os
import sys
import shutil
from PIL import Image
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import ensure_dir, print_stats

PAPER_CONFIGS = {
    1: {
        "src_dir": "../模拟试卷1/试题1-数据采集和处理/b)业务数据处理/需要分类统计的动物数据集",
        "dst_base": "../模拟试卷1/试题1-数据采集和处理/b)业务数据处理",
        "categories": ["马", "狗", "鸡", "猫", "羊"],
        "labels": [
            "a photo of a horse",
            "a photo of a dog",
            "a photo of a chicken",
            "a photo of a cat",
            "a photo of a sheep"
        ],
        "use_mobilenet": True
    },
    2: {
        "src_dir": "../模拟试卷2/试题1-数据采集和处理/b)业务数据处理/需要分类统计的自然风光数据集",
        "dst_base": "../模拟试卷2/试题1-数据采集和处理/b)业务数据处理",
        "categories": ["丛林", "冰川", "山", "海", "街道"],
        "labels": [
            "a photo of a forest or jungle",
            "a photo of a glacier or ice",
            "a photo of a mountain",
            "a photo of a sea or ocean or beach",
            "a photo of a street or road"
        ]
    },
    3: {
        "src_dir": "../模拟试卷3/试题1-数据采集和处理/b)业务数据处理/需要分类统计的花卉数据集",
        "dst_base": "../模拟试卷3/试题1-数据采集和处理/b)业务数据处理",
        "categories": ["雏菊", "蒲公英", "玫瑰", "向日葵", "郁金香"],
        "labels": [
            "a photo of a daisy flower",
            "a photo of a dandelion flower",
            "a photo of a rose flower",
            "a photo of a sunflower",
            "a photo of a tulip flower"
        ]
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
    dst_base = os.path.join(script_dir, config["dst_base"])

    for cat in config["categories"]:
        ensure_dir(os.path.join(dst_base, cat), clean=True)

    print("Loading CLIP model...")
    classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

    label_to_cat = dict(zip(config["labels"], config["categories"]))
    counts = {cat: 0 for cat in config["categories"]}

    if not os.path.exists(src_dir):
        print(f"目录不存在: {src_dir}")
        sys.exit(1)

    from glob import glob
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        image_files.extend(glob(os.path.join(src_dir, ext)))

    print(f"找到 {len(image_files)} 张待分类图片")

    for img_path in image_files:
        try:
            img = Image.open(img_path)
            preds = classifier(img, candidate_labels=config["labels"])
            predicted_cat = label_to_cat[preds[0]['label']]
            dst_path = os.path.join(dst_base, predicted_cat, os.path.basename(img_path))
            shutil.copy2(img_path, dst_path)
            counts[predicted_cat] += 1
        except Exception as e:
            print(f"处理失败 {os.path.basename(img_path)}: {e}")

    print_stats("分类完成，统计结果：", list(counts.items()), headers=["序号", "类别", "张数"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python 2_classify_images.py <试卷号: 1|2|3>")
        sys.exit(1)
    main(int(sys.argv[1]))
