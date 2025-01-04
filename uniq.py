import os
import shutil
from imagehash import ImageHash, average_hash
from PIL import Image

# 设置图片文件夹路径和重复图片存储文件夹路径
image_folder = '/Users/kenneth/codes/python/video-frame-extract'
duplicate_folder = '/Users/kenneth/codes/python/video-frame-extract/duplicate'

# 如果重复图片文件夹不存在，则创建它
if not os.path.exists(duplicate_folder):
    os.makedirs(duplicate_folder)

# 初始化一个字典来存储哈希值和图片路径的映射
hash_dict = {}

# 遍历图片文件夹中的每个文件
for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder, filename)

    # 确保只处理图片文件（可以根据需要扩展文件类型列表）
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        try:
            # 打开图片并计算平均哈希值
            image = Image.open(file_path)
            image_hash = average_hash(image)

            # 检查哈希值是否已经在字典中
            if image_hash in hash_dict:
                # 如果哈希值存在，则将图片移动到重复图片文件夹
                shutil.move(file_path, os.path.join(duplicate_folder, filename))
                print(f"Moved duplicate: {filename}")
            else:
                # 如果哈希值不存在，则将其添加到字典中
                hash_dict[image_hash] = file_path
        except Exception as e:
            # 处理无法打开或处理图片时的异常
            print(f"Error processing {filename}: {e}")

print("Finished processing images.")
