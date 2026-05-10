import os
import hashlib
import cv2
import shutil
from pathlib import Path


def get_md5(file_path):
    """计算文件MD5哈希值，用于去重"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def is_blurry(image_path, threshold=100.0):
    """检测图片是否模糊（Laplacian方差）"""
    img = cv2.imread(image_path)
    if img is None:
        return True
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < threshold


def list_images(directory):
    """列出目录下所有图片文件"""
    exts = ('.png', '.jpg', '.jpeg', '.bmp')
    return [f for f in os.listdir(directory) if f.lower().endswith(exts)]


def ensure_dir(directory, clean=False):
    """确保目录存在，可选清空"""
    if clean and os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory, exist_ok=True)
    return Path(directory)


def print_stats(title, items, headers=None):
    """格式化输出统计结果"""
    print(f"\n{title}")
    if headers:
        print("\t".join(headers))
    for idx, (name, count) in enumerate(items, 1):
        print(f"{idx}\t{name}\t{count}")
