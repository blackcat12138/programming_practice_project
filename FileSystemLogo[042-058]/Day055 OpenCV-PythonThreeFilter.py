'''
    【055】、使用OpenCV-Python批量为照片应用卡通动漫滤镜
    将自动为多张照片应用卡通动漫滤镜。
'''
import cv2
import os
import numpy as np


def filter(filein, picture_name):
    # 源文件路径
    imgI_filename = os.path.join(filein, picture_name)
    # 目标文件路径
    imgI0_filename = os.path.join(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/out/',
                                  picture_name)
    # 读取图片
    img_rgb = cv2.imread(imgI_filename)
    # 转换为灰度
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    # 增加模糊效果。值越大越模糊(取奇数)
    img_blur = cv2.medianBlur(img_gray, 5)
    # 检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur, 128,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=8)
    # 彩色图像转为灰度图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    # 灰度图像转为彩色图像
    img_cartoon = cv2.bitwise_and(img_rgb, img_edge)
    # 调整亮度和对比度
    res = np.uint8(np.clip((2.0 * img_cartoon + 16), 0, 255))
    # 保存转换后的图片
    cv2.imwrite(imgI0_filename, res)


if __name__ == '__main__':
    imagelist = []
    # 循环读取指定路径下的文件名
    for filename in os.listdir(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/'):
        # 将文件名添加到imagelist
        imagelist.append(filename)
        print(filename)
        # 为图片应用卡通动漫滤镜
        filter(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/', filename)
