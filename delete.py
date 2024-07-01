import os

def delete_files_after_threshold(image_folder, label_folder, prefix, threshold):
    # 获取文件列表并排序
    image_files = sorted(os.listdir(image_folder))
    label_files = sorted(os.listdir(label_folder))

    # 检查文件数量是否一致
    if len(image_files) != len(label_files):
        raise ValueError(f"Image and label folders contain a different number of files.")

    # 遍历文件列表，删除超过阈值的文件
    for image_file, label_file in zip(image_files, label_files):
        # 确保图像和标签的文件名一致
        image_name, image_ext = os.path.splitext(image_file)
        label_name, label_ext = os.path.splitext(label_file)

        if image_name != label_name:
            raise ValueError(f"Image and label file names do not match: {image_file} != {label_file}")

        # 提取编号部分并比较
        if image_name.startswith(prefix):
            file_number = int(image_name[len(prefix):])
            if file_number > threshold:
                # 构造完整的文件路径
                image_path = os.path.join(image_folder, image_file)
                label_path = os.path.join(label_folder, label_file)

                # 删除文件
                os.remove(image_path)
                os.remove(label_path)

                print(f"Deleted {image_file} and {label_file}")

# 定义文件夹路径
image_folder = 'D:/atool/pycharm/pythonProject/Fire_YOLOv7/datasets/forestfiredata/images/train'
label_folder = 'D:/atool/pycharm/pythonProject/Fire_YOLOv7/datasets/forestfiredata/labels/train'
test_prefix = 'train_'
threshold = 600

# 删除编号超过阈值的文件
delete_files_after_threshold(image_folder, label_folder, test_prefix, threshold)

print("Deletion completed successfully.")
