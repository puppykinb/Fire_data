import os

def rename_files(image_folder, label_folder, prefix):
    # 获取文件列表并排序
    image_files = sorted(os.listdir(image_folder))
    label_files = sorted(os.listdir(label_folder))

    # 检查文件数量是否一致
    if len(image_files) != len(label_files):
        raise ValueError(f"Image and label folders contain a different number of files.")

    # 重命名文件
    for i, (image_file, label_file) in enumerate(zip(image_files, label_files)):
        # 确保图像和标签的文件名一致
        image_name, image_ext = os.path.splitext(image_file)
        label_name, label_ext = os.path.splitext(label_file)

        if image_name != label_name:
            raise ValueError(f"Image and label file names do not match: {image_file} != {label_file}")

        # 新的文件名
        new_name = f"{prefix}{i:04d}"

        # 构造完整的文件路径
        old_image_path = os.path.join(image_folder, image_file)
        new_image_path = os.path.join(image_folder, f"{new_name}{image_ext}")

        old_label_path = os.path.join(label_folder, label_file)
        new_label_path = os.path.join(label_folder, f"{new_name}{label_ext}")

        # 重命名文件
        os.rename(old_image_path, new_image_path)
        os.rename(old_label_path, new_label_path)

        print(f"Renamed {image_file} to {new_name}{image_ext}")
        print(f"Renamed {label_file} to {new_name}{label_ext}")

# 定义文件夹路径
image_folder = 'D:/atool/pycharm/pythonProject/Fire_YOLOv7/datasets/forestfiredata/images/train'
label_folder = 'D:/atool/pycharm/pythonProject/Fire_YOLOv7/datasets/forestfiredata/labels/train'
test_prefix = 'train_'

# 重命名测试集文件
rename_files(image_folder, label_folder, test_prefix)

print("Renaming completed successfully.")
