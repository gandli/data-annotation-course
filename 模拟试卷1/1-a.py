import os
import requests

ACCESS_KEY = "reFbI9D7jRArU0ns4Bf9168fDgTLYdHAj71IpagfUIU"

CAT_DIR = "试题1-数据采集和处理/a)业务数据采集/猫（20张）"
DOG_DIR = "试题1-数据采集和处理/a)业务数据采集/狗（20张）"

os.makedirs(CAT_DIR, exist_ok=True)
os.makedirs(DOG_DIR, exist_ok=True)

def download_images(keyword, save_dir, count=20):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }
    params = {
        "query": keyword,
        "per_page": count,
        "page": 1
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()

    for i, item in enumerate(data["results"][:count], start=1):
        img_url = item["urls"]["regular"]
        img_data = requests.get(img_url).content
        with open(os.path.join(save_dir, f"{keyword}_{i}.jpg"), "wb") as f:
            f.write(img_data)

download_images("cat", CAT_DIR, 20)
download_images("dog", DOG_DIR, 20)