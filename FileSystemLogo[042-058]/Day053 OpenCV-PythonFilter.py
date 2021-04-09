'''
    【053】、使用OpenCV-Python批量为照片应用灰度滤镜
    为照片应用灰度滤镜,将原本彩色照片,转换为黑白照片;使用OpenCV-Python模块实现对图片的处理。
    OpenCV-Python.imread()：读取源图片。
    OpenCv-Python.cvtColor()：将其转换为灰度。
    NumPy：调整亮度和对比度。
'''
import cv2
import os
import numpy as np


# 1.应用滤镜的图片的路径(为图片应用灰度滤镜,并保存图片到指定路径)
def filter(filein, picture_name):
    # 源文件路径
    imgI_filename = os.path.join(filein, picture_name)
    # 目标文件路径
    img0_filename = os.path.join(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/out/',
                                 picture_name)
    # 读取源图片
    img_rgb = cv2.imread(imgI_filename)
    # 转换为灰度
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # 调整亮度和对比度
    res = np.uint8(np.clip((1.2 * img_gray + 0), 0, 255))
    # 保存转换后的图片
    cv2.imwrite(img0_filename, res)


# 2.编写程序入口
if __name__ == '__main__':
    # 创建空列表
    imagelist = []
    # 循环读取指定路径下的文件名
    for filename in os.listdir(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/'):
        # 将文件名添加到imagelist
        imagelist.append(filename)
        print(filename)
        # 为图片应用灰度滤镜
        filter(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/', filename)
