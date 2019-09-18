# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure


def find_character_and_keep(imgpath):
    from PIL import Image
    img = Image.open(imgpath).convert('L')
    img_arr = np.array(img)
    # print(img_arr)
    # saveImageTxtRR(img_arr, "gray")

    # 二值图
    threshold = 245
    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)

    photo = img.point(table, "1")
    # 检测所有图形的轮廓
    contours = measure.find_contours(photo, 0.5)

    # 绘制轮廓, 一行两列
    fig, axes = plt.subplots(1, 2, figsize=(8, 8))
    ax0, ax1 = axes.ravel()
    ax0.imshow(photo, plt.cm.gray)
    ax0.set_title('original image')

    rows, cols = img.size
    ax1.axis([0, rows, cols, 0])
    for n, contour in enumerate(contours):
        if len(contour) < 300:
            figure = ax1.plot(contour[:, 1], contour[:, 0], linewidth=2, color='black', antialiased=True)

    # 适应图片大小
    ax1.axis('image')
    ax1.set_title('contours')
    plt.show()


if __name__ == "__main__":
    img_path = r"./test.png"
    find_character_and_keep(img_path)

# https://testerhome.com/topics/20536
