'''
    [038]、python制作酷炫词云图
        1.使用python来分析电影《冰雪奇缘2》的剧情并以艾莎的形象绘制成词云图。
        2.核心步骤：
            a.open()方法读取文本文件
            b.jieba模块提取关键词,对文本分词进行处理
            c.从图片取色
            d.color_func函数指定图片颜色渲染词云图的颜色
            e.WordCloud模块绘制词云图,使用Matplotlib模块显示词云图
        3.重点知识点
            matplotlib模块：2D绘图库
            matplotlib.pyplot：绘图框架
            jieba模块:中文分词库
            wordcloud：词云生成库,可以实现词频可视化,根据你给出字符串对词频进行统计,以不同的大小显示出来。
            numpy：用于维度数组与矩阵运算。
            PIL：用于对图片进行编辑处理的

'''
# 导入matplotlib模块pyplot函数,并取别名plt
import matplotlib.pyplot as plt
# 导入jieba分词模块
import jieba
# 导入词云图模块
import wordcloud
from wordcloud import ImageColorGenerator
import numpy as np
from PIL import Image

# with open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/elsa.txt','r',encoding='utf-8') as file:
#     line = file.readline()
#     print(line)

# 1.读取elsa.txt文件
text = open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/elsa.txt', 'r', encoding='utf-8').read()
# jieba.cut()：生成一个生成器(generator),可以通过for循环取出每个词
cut_text = jieba.cut(text)
word = ''.join(cut_text)
# 2.读取图片
pic = np.array(Image.open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/aa.png'))
# 生成图片颜色中的颜色
image_colors = ImageColorGenerator(pic)
# 3.绘制词云图
wd = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    background_color='white',
)
wd.generate(word)
plt.imshow(wd.recolor(color_func=image_colors), interpolation='bilinear')
# 关闭显示x轴、y轴下标
plt.axis('off')
plt.figure()
plt.imshow(pic, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
