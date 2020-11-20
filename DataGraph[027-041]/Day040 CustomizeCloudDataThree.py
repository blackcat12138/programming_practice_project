'''
    [040]、自定义词云图颜色
    1.python实现自定义云图颜色,使用黑红混搭以外星人图案为例
'''
import matplotlib.pyplot as ply
import jieba
import wordcloud
from scipy.misc import imread
from matplotlib import colors

# 1.读取文本文件
str1 = open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/mr.txt', 'r').read()
# 2.对文本进行分词处理
cut_txt = jieba.cut(str1)
word = ''.join(cut_txt)
# 3.自定义词云图颜色
color_list = ['black', 'red']
# matplotlib色图
colormap = colors.ListedColormap(color_list)
# 4.绘制词云图
pic = imread('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/外星人1.png')
wc = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    background_color='white',
    colormap=colormap
)
wc.generate(word)
# 显示词云图
ply.imshow(wc)
ply.axis('off')
ply.show()
