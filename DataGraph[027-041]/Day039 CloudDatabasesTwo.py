'''
    [039]、按图片轮廓绘制词云图
        1.根据图片形状绘制词云图
        2.python读取图片的方式,如下：
            利用Pillow(PIL)中的Image函数
            利用Matplotlib模块的imread函数
            利用opencv-python接口
            图像处理图Scipy
            imageio类操作图片
'''
import matplotlib.pyplot as plt
import jieba
import wordcloud
from scipy.misc import imread

# 1.读取文件文件
str1 = open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/ycy.txt', 'r').read()
# print(str1)
# 2.实现分词处理
cut_text = jieba.cut(str1)
word = ''.join(cut_text)
# 3.以图片为背景绘制词云图
pic = imread('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/ycy.png')
wd = wordcloud.WordCloud(
    mask=pic,
    background_color='white'
)
# 生成词云
wd.generate(word)
plt.imshow(wd)
plt.axis('off')
plt.show()
