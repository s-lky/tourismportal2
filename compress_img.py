import os
from PIL import Image

#要压缩的根目录
TARGET_DIR = './media' 

#压缩配置
MAX_WIDTH = 1280  #图片宽度限制
QUALITY = 70      #压缩质量70

def compress_images(directory):
    count = 0
    saved_space = 0
    
    print(f"正在扫描 {directory} 下的图片...")

    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理常见图片格式
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                
                try:
                    #获取原文件大小
                    original_size = os.path.getsize(file_path)
                    
                    with Image.open(file_path) as img:
                        #自动处理尺寸
                        
                        #调整尺寸：如果宽度超过 MAX_WIDTH，等比例缩小
                        if img.width > MAX_WIDTH:
                            ratio = MAX_WIDTH / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                        
                        #保存覆盖原文件
                        #optimize=True 是专门用于瘦身的参数
                        img.save(file_path, optimize=True, quality=QUALITY)
                    
                    #计算节省了多少空间
                    new_size = os.path.getsize(file_path)
                    diff = original_size - new_size
                    if diff > 0:
                        saved_space += diff
                        print(f"[已压缩] {file}: 节省 {diff/1024:.2f} KB")
                        count += 1
                        
                except Exception as e:
                    print(f"[跳过] {file}: {e}")

    print("="*30)
    print(f"处理完成！共压缩 {count} 张图片。")
    print(f"总体积减少了: {saved_space / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    #检查文件夹是否存在
    if os.path.exists(TARGET_DIR):
        compress_images(TARGET_DIR)
    else:
        print(f"错误：找不到目录 {TARGET_DIR}，请确认脚本是否放在 manage.py 旁边。")