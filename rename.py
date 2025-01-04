import os

# 设置图片所在的文件夹路径
folder_path = '/'

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    # 检查文件是否以'frame_'开头，并以'.png'结尾
    if filename.startswith('frame_') and filename.endswith('.png'):
        # 分离文件名中的数字部分和非数字部分
        base, ext = os.path.splitext(filename)
        num_str = base.split('_')[-1]  # 获取数字部分

        # 检查数字部分是否小于4位，如果是则前面补0
        if len(num_str) < 4:
            num_str = num_str.zfill(4)  # 使用zfill方法补0

        # 构造新的文件名
        new_filename = f"frame_{num_str}{ext}"

        # 获取旧文件和新文件的完整路径
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

print("Finished renaming files.")
