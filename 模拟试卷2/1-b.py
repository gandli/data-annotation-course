import os
import shutil
from PIL import Image
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

def main():
    base_dir = "试题1-数据采集和处理/b)业务数据处理"
    src_dir = os.path.join(base_dir, "需要分类统计的自然风光数据集")
    
    categories = ["丛林", "冰川", "山", "海", "街道"]
    
    # 清理之前由于旧模型分错的旧文件
    for cat in categories:
        cat_dir = os.path.join(base_dir, cat)
        if os.path.exists(cat_dir):
            shutil.rmtree(cat_dir)
        os.makedirs(cat_dir, exist_ok=True)
        
    print("Loading CLIP model for high-precision zero-shot image classification...")
    classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
    
    candidate_labels = [
        "a photo of a forest or jungle", 
        "a photo of a glacier or ice", 
        "a photo of a mountain", 
        "a photo of a sea or ocean or beach", 
        "a photo of a street or road"
    ]
    label_to_cat = {
        "a photo of a forest or jungle": "丛林",
        "a photo of a glacier or ice": "冰川",
        "a photo of a mountain": "山",
        "a photo of a sea or ocean or beach": "海",
        "a photo of a street or road": "街道"
    }
    
    counts = {cat: 0 for cat in categories}
    
    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return

    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Found {len(files)} images to classify.")

    for f in files:
        img_path = os.path.join(src_dir, f)
        try:
            img = Image.open(img_path)
            preds = classifier(img, candidate_labels=candidate_labels)
            
            # 取最高置信度的结果
            top_label = preds[0]['label']
            predicted_cat = label_to_cat[top_label]
            
            dst_path = os.path.join(base_dir, predicted_cat, f)
            shutil.copy2(img_path, dst_path)
            counts[predicted_cat] += 1
                
        except Exception as e:
            print(f"Error processing {f}: {e}")
            
    print("\n分类完成，统计结果如下：")
    print("序号\t自然风光类别\t张数")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}\t{cat}\t{counts[cat]}")

if __name__ == "__main__":
    main()
