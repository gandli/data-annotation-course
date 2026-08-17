import os
import sys
import shutil
from PIL import Image
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import get_md5, is_blurry, list_images, ensure_dir

PAPER_CONFIGS = {
    1: {
        "src_dir": "../模拟试卷1/试题2-数据标注/a)原始数据清洗与标注/需要清洗标注的吉普车数据集",
        "dst_dir": "../模拟试卷1/试题2-数据标注/a)原始数据清洗与标注/清洗后进行标注的吉普车数据集",
        "object_name": "jeep",
        "use_ocr": True,
        "labels": None
    },
    2: {
        "src_dir": "../模拟试卷2/试题2-数据标注/a)原始数据清洗与标注/需要清洗标注的海豚数据集",
        "dst_dir": "../模拟试卷2/试题2-数据标注/a)原始数据清洗与标注/清洗后进行标注的海豚数据集",
        "object_name": "dolphin",
        "labels": [
            "a photo of a dolphin",
            "a photo of a shark or whale",
            "a photo of a different animal",
            "a photo of scenery or people"
        ],
        "confidence_threshold": 0.60
    },
    3: {
        "src_dir": "../模拟试卷3/试题2-数据标注/a)原始数据清洗与标注/需要清洗标注的海豚数据集",
        "dst_dir": "../模拟试卷3/试题2-数据标注/a)原始数据清洗与标注/清洗后进行标注的海豚数据集",
        "object_name": "dolphin",
        "labels": [
            "a photo of a dolphin",
            "a photo of a shark or whale",
            "a photo of a different animal",
            "a photo of scenery or people"
        ],
        "confidence_threshold": 0.60
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

    ensure_dir(dst_dir, clean=True)
    files = sorted(list_images(src_dir))
    print(f"找到 {len(files)} 张待清洗图片")

    if config["labels"]:
        print("Loading CLIP model...")
        classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
    else:
        import easyocr
        print("Loading EasyOCR...")
        reader = easyocr.Reader(['en'])
        classifier = None

    seen_md5 = set()
    valid_count = 0

    for f in files:
        img_path = os.path.join(src_dir, f)
        print(f"[{f}] ", end="")

        md5 = get_md5(img_path)
        if md5 in seen_md5:
            print("剔除：重复数据")
            continue

        if is_blurry(img_path, threshold=100.0):
            print("剔除：图片模糊")
            continue

        try:
            if classifier:
                img = Image.open(img_path)
                preds = classifier(img, candidate_labels=config["labels"])
                top_label = preds[0]['label']
                conf_score = preds[0]['score']

                if "dolphin" not in top_label:
                    print(f"剔除：非海豚 (Top1: {top_label})")
                    continue
                if conf_score < config["confidence_threshold"]:
                    print(f"剔除：非主要构图 (置信度: {conf_score:.2f})")
                    continue
            else:
                ocr_results = reader.readtext(img_path)
                has_jeep = any('jeep' in text[1].lower() for text in ocr_results)
                if not has_jeep:
                    print("剔除：非吉普车 (未检测到 jeep 标识)")
                    continue

            valid_count += 1
            dst_name = f"{config['object_name']}({valid_count}).jpg"
            shutil.copy2(img_path, os.path.join(dst_dir, dst_name))
            print(f"保留 -> {dst_name}" + (f" (置信度: {preds[0]['score']:.2f})" if classifier else ""))

        except Exception as e:
            print(f"处理失败: {e}")

    print(f"\n清洗完成：共 {len(files)} 张，保留 {valid_count} 张，剔除 {len(files) - valid_count} 张")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python 3_clean_images.py <试卷号: 1|2|3>")
        sys.exit(1)
    main(int(sys.argv[1]))
