'''
    【054】、使用OpenCV-Python批量为照片应用写生素描滤镜
    指定一个保存了多张照片的路径,再指定一个目标路径,运行程序,自动为多张照片应用写生素描滤镜。
'''
import cv2
import os


# 1.应用滤镜的图片的路径
def filter(filein, pivture_name):
    # 源文件路径
    imgI_filename = os.path.join(filein, pivture_name)
    # 目标文件路径
    img0_filename = os.path.join(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/out/',
                                 pivture_name)
    # 读取源图片
    img_rgb = cv2.imread(imgI_filename)
    # 缩减像素采样的数目
    num_down = 2
    # 定义双边滤波的数目
    num_bilateral = 9
    # 用高斯金字塔降低取样
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    # 重复使用小的双边虑波代替一个大的虑波
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=4, sigmaColor=8, sigmaSpace=4)
    # 生采样图片到原始大小
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)
    # 转换为灰度
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    # 增加模糊效果,值越大越模糊(取奇数)
    img_blur = cv2.medianBlur(img_gray, 19)
    # 检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur, 256,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=2)
    # 彩色图像转为灰度图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    # 保存图片
    cv2.imwrite(img0_filename, img_edge)


# 2.编写程序入口
if __name__ == '__main__':
    # 创建空列表
    imagelist = []
    # 循环读取指定路径下的文件名
    for filename in os.listdir(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/'):
        # 将文件名添加到imagelist
        imagelist.append(filename)
        print(filename)
        # 为图片应用写生素描滤镜
        filter(r'E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/in/', filename)
