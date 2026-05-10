import os
import cv2
import hashlib
import shutil
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import easyocr

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
    src_dir = os.path.join(base_dir, "需要清洗标注的吉普车数据集")
    dst_dir = os.path.join(base_dir, "清洗后进行标注的吉普车数据集")
    
    # 清空之前的数据集以防止有残留
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir, exist_ok=True)
    
    print("Loading MobileNetV2 model for composition confidence...")
    model = MobileNetV2(weights='imagenet')
    
    print("Loading EasyOCR for text detection...")
    reader = easyocr.Reader(['en'])
    
    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return
        
    files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    seen_md5 = set()
    valid_count = 0
    
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
            
        try:
            # 3. 剔除：非吉普车（以检测到 'jeep' 品牌字样为准）
            ocr_results = reader.readtext(img_path)
            has_jeep_text = any('jeep' in text[1].lower() for text in ocr_results)
            
            if not has_jeep_text:
                print(f"[{f}] 剔除：非吉普车 (未检测到 'jeep' 品牌字样)")
                continue

            # 4. 剔除：非主要构图（借用模型置信度进行主体判断）
            img = image.load_img(img_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            
            preds = model.predict(x, verbose=0)
            decoded = decode_predictions(preds, top=3)[0]
            top1_score = decoded[0][2]
            
            # 如果置信度过低，视为非主要构图（主体太小或不明显）
            if top1_score < 0.20:
                print(f"[{f}] 剔除：非主要构图 (最高置信度过低: {top1_score:.2f})")
                continue
                
        except Exception as e:
            print(f"[{f}] 剔除：无法处理的图片 ({e})")
            continue
            
        # Passed all checks
        seen_md5.add(md5)
        valid_count += 1
        
        # Rename and copy
        new_name = f"jeep({valid_count}).jpg"
        dst_path = os.path.join(dst_dir, new_name)
        shutil.copy2(img_path, dst_path)
        print(f"[{f}] -> 保留为 {new_name}")

    print(f"\n清洗完毕。共保留 {valid_count} 张有效吉普车图片，保存在 '{dst_dir}'")

if __name__ == "__main__":
    main()
