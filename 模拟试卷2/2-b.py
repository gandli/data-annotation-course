import os
import shutil

def main():
    base_dir = "试题2-数据标注/b)标注后数据分类与统计"
    src_dir = os.path.join(base_dir, "需要进行分类统计的花卉数据集")
    dst_dir = os.path.join(base_dir, "数据分类后的花卉数据集")
    
    # 目标分类 (按题目顺序)
    categories = ["daisy", "dandelion", "rose", "sunflower", "tulip"]
    
    # 初始化计数器
    counts = {cat: 0 for cat in categories}
    
    # 创建目标文件夹
    for cat in categories:
        os.makedirs(os.path.join(dst_dir, cat), exist_ok=True)
        
    if not os.path.exists(src_dir):
        print(f"Directory not found: {src_dir}")
        return
        
    # 获取所有图片文件
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    for f in files:
        # 解析文件名，提取类别前缀
        # 例如: "daisy (1).jpg" -> "daisy", "dandelion (10).jpg" -> "dandelion"
        name_part = f.split('(')[0].strip().lower()
        
        # 匹配到目标类别 (忽略大小写)
        matched_cat = None
        for cat in categories:
            if cat.lower() == name_part:
                matched_cat = cat
                break
                
        if matched_cat:
            counts[matched_cat] += 1
            src_path = os.path.join(src_dir, f)
            dst_path = os.path.join(dst_dir, matched_cat, f)
            shutil.copy2(src_path, dst_path)
        else:
            print(f"Warning: Could not classify file {f}")
            
    print("分类完成，统计结果如下：")
    print("序号\t花卉种类\t数量")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}\t{cat}\t{counts[cat]}")

if __name__ == "__main__":
    main()
