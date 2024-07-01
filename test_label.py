import cv2
import os


def annotate_images(image_dir, txt_dir, output_dir):
    image_files = os.listdir(image_dir)
    txt_files = os.listdir(txt_dir)

    for image_file in image_files:
        txt_file = os.path.splitext(image_file)[0] + '.txt'

        if txt_file in txt_files:
            image_path = os.path.join(image_dir, image_file)
            txt_path = os.path.join(txt_dir, txt_file)
            output_path = os.path.join(output_dir, image_file)

            img = cv2.imread(image_path)

            with open(txt_path, 'r') as f:
                lines = f.readlines()

            for line in lines:
                values = line.strip().split()
                x, y, w, h = map(float, values[1:])
                xmin = int((x - w / 2) * img.shape[1])
                ymin = int((y - h / 2) * img.shape[0])
                xmax = int((x + w / 2) * img.shape[1])
                ymax = int((y + h / 2) * img.shape[0])

                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

            cv2.imwrite(output_path, img)
            print("已在图片上标注：", image_file)
        else:
            print("找不到与图片对应的文本文件：", image_file)


# 指定图片文件夹、YOLO格式文本文件夹和输出文件夹
image_folder = r'D:\atool\pycharm\pythonProject\Fire_YOLOv7\datasets\forestfiredata\images\train'
txt_folder = r'D:\atool\pycharm\pythonProject\Fire_YOLOv7\datasets\forestfiredata\labels\train'
output_folder = r'D:\atool\yolov7'

annotate_images(image_folder, txt_folder, output_folder)