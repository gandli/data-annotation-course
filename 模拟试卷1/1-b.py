import os
import shutil
from collections import defaultdict
import numpy as np

# Set environment variable to reduce TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

def get_category(description):
    desc = description.lower()
    if 'cat' in desc or 'tabby' in desc:
        return '猫'
    if any(word in desc for word in ['dog', 'hound', 'terrier', 'spaniel', 'retriever', 'pug', 'corgi', 'poodle', 'husky', 'malamute', 'collie', 'chihuahua', 'beagle', 'mastiff', 'schnauzer', 'pinscher', 'setter', 'pointer', 'sheepdog', 'shiba', 'samoyed', 'dingo', 'dhole', 'chow', 'papillon', 'dalmatian', 'leonberg', 'affenpinscher', 'schipperke', 'groenendael', 'briard', 'komondor', 'kuvasz', 'kelpie', 'malinois', 'pomeranian', 'pekinese']):
        return '狗'
    if any(word in desc for word in ['cock', 'hen', 'chicken', 'bantam', 'partridge', 'rooster']):
        return '鸡'
    if any(word in desc for word in ['sheep', 'ram', 'bighorn', 'ibex', 'ewe']):
        return '羊'
    if any(word in desc for word in ['horse', 'sorrel', 'zebra', 'pony', 'mare']):
        return '马'
    return '未知'

def main():
    base_dir = "试题1-数据采集和处理/b)业务数据处理"
    src_dir = os.path.join(base_dir, "需要分类统计的动物数据集")
    
    # 按照题目要求的顺序
    categories = ["马", "狗", "鸡", "猫", "羊"]
    
    # 确保目标文件夹存在
    for cat in categories:
        os.makedirs(os.path.join(base_dir, cat), exist_ok=True)
        
    print("Loading model MobileNetV2...")
    model = MobileNetV2(weights='imagenet')
    
    counts = {cat: 0 for cat in categories}
    counts['未知'] = 0
    
    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return

    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Found {len(files)} images to classify.")

    for f in files:
        img_path = os.path.join(src_dir, f)
        try:
            img = image.load_img(img_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            
            preds = model.predict(x, verbose=0)
            # 获取前10个预测结果以提高匹配概率
            decoded = decode_predictions(preds, top=10)[0]
            
            predicted_cat = '未知'
            for _, desc, score in decoded:
                cat = get_category(desc)
                if cat != '未知':
                    predicted_cat = cat
                    break
            
            if predicted_cat == '未知':
                print(f"Warning: {f} could not be classified confidently. Top predictions: {[d[1] for d in decoded[:3]]}")
                # 简单退避策略：若未知，则归入最有可能的（但本数据集应该是明确的五种之一）
            
            if predicted_cat in categories:
                dst_path = os.path.join(base_dir, predicted_cat, f)
                shutil.copy2(img_path, dst_path)
                counts[predicted_cat] += 1
                
        except Exception as e:
            print(f"Error processing {f}: {e}")
            
    print("\n分类完成，统计结果如下：")
    print("序号\t动物类别\t张数")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}\t{cat}\t{counts[cat]}")

if __name__ == "__main__":
    main()
