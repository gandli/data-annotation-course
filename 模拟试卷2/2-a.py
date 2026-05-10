import os
import cv2
import hashlib
import shutil
from PIL import Image
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def is_blurry(image_path, threshold=100.0):
    img = cv2.imread(image_path)
    if img is None:
        return True
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < threshold

def main():
    base_dir = "试题2-数据标注/a)原始数据清洗与标注"
    src_dir = os.path.join(base_dir, "需要清洗标注的海豚数据集")
    dst_dir = os.path.join(base_dir, "清洗后进行标注的海豚数据集")
    
    os.makedirs(dst_dir, exist_ok=True)
    
    print("Loading CLIP model for high-precision zero-shot classification...")
    classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
    
    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return
        
    files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    seen_md5 = set()
    valid_count = 0
    
    # 建立分类标签，精准区分海豚、其他海洋生物、风景等
    candidate_labels = [
        "a photo of a dolphin", 
        "a photo of a shark or whale",
        "a photo of a different animal",
        "a photo of scenery or people"
    ]
    
    for f in files:
        img_path = os.path.join(src_dir, f)
        
        # 1. 剔除：重复数据
        md5 = get_md5(img_path)
        if md5 in seen_md5:
            print(f"[{f}] 剔除：重复数据")
            continue
        
        # 2. 剔除：图片模糊
        if is_blurry(img_path, threshold=100.0):
            print(f"[{f}] 剔除：图片模糊")
            continue
            
        # 3. 剔除：非海豚 & 非主要构图
        try:
            img = Image.open(img_path)
            preds = classifier(img, candidate_labels=candidate_labels)
            
            top_label = preds[0]['label']
            top_score = preds[0]['score']
            
            dolphin_score = 0
            for p in preds:
                if 'dolphin' in p['label']:
                    dolphin_score = p['score']
                    break
            
            # 如果主要识别出的对象不是海豚，即非海豚
            if top_label != "a photo of a dolphin":
                print(f"[{f}] 剔除：非海豚 (Top1: {top_label})")
                continue
                
            # 如果是海豚，但置信度较低（< 0.6），说明海豚可能在背景中或是很小，即非主要构图
            if dolphin_score < 0.60:
                print(f"[{f}] 剔除：非主要构图 (Dolphin Score: {dolphin_score:.2f})")
                continue
                
        except Exception as e:
            print(f"[{f}] 剔除：无法处理的图片 ({e})")
            continue
            
        # 保留符合要求的数据
        seen_md5.add(md5)
        valid_count += 1
        
        # 顺序重命名并拷贝
        new_name = f"dolphin({valid_count}).jpg"
        dst_path = os.path.join(dst_dir, new_name)
        shutil.copy2(img_path, dst_path)
        print(f"[{f}] -> 保留为 {new_name}")

    print(f"\n清洗完毕。共保留 {valid_count} 张有效海豚图片，保存在 '{dst_dir}'")

if __name__ == "__main__":
    main()
