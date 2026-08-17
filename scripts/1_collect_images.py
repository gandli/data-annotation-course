import os
import sys
import requests

ACCESS_KEY = "reFbI9D7jRArU0ns4Bf9168fDgTLYdHAj71IpagfUIU"

PAPER_CONFIGS = {
    1: {
        "keywords": [("cat", "猫（20张）"), ("dog", "狗（20张）")],
        "base_dir": "../模拟试卷1/试题1-数据采集和处理/a)业务数据采集"
    },
    2: {
        "keywords": [("jungle forest", "丛林（20张）"), ("ocean sea beach", "海洋（20张）")],
        "base_dir": "../模拟试卷2/试题1-数据采集和处理/a)业务数据采集"
    },
    3: {
        "keywords": [("rose flower", "玫瑰（20张）"), ("sunflower", "向日葵（20张）")],
        "base_dir": "../模拟试卷3/试题1-数据采集和处理/a)业务数据采集"
    }
}


def download_images(keyword, save_dir, count=20):
    url = "https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    params = {"query": keyword, "per_page": count, "page": 1}

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()

    for i, item in enumerate(data["results"][:count], start=1):
        img_url = item["urls"]["regular"]
        img_data = requests.get(img_url).content
        with open(os.path.join(save_dir, f"{keyword.split()[0]}_{i}.jpg"), "wb") as f:
            f.write(img_data)
    print(f"✓ 已下载 {count} 张 {keyword} 图片")


def main(paper_num):
    if paper_num not in PAPER_CONFIGS:
        print(f"错误：试卷 {paper_num} 配置不存在")
        print(f"可用试卷: {list(PAPER_CONFIGS.keys())}")
        sys.exit(1)

    config = PAPER_CONFIGS[paper_num]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, config["base_dir"])

    for kw, dir_name in config["keywords"]:
        save_dir = os.path.join(base_dir, dir_name)
        os.makedirs(save_dir, exist_ok=True)
        download_images(kw, save_dir, 20)

    print(f"\n试卷 {paper_num} 图片采集完成")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python 1_collect_images.py <试卷号: 1|2|3>")
        sys.exit(1)
    main(int(sys.argv[1]))
