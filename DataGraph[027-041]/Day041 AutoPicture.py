'''
    [041]、自行构造词云图中中文停用词
'''

# 1.导入相关模块和函数
import re
import matplotlib.pyplot as plt
from matplotlib import colors
import jieba
import wordcloud
from wordcloud import WordCloud
import imageio
# 2.读取文本文件
str1=open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/joker.txt','r').read()
# 3.处理文本中的特殊符号
pattern=re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|\[|\]|  ；|，|。|"')
str1=re.sub(pattern, '',str1)
# 4.自定义小丑颜色
color_list=['darkslategray','red','orange','darkred']
colormap=colors.ListedColormap(color_list)
# 5.对文本进行分词处理
cut_text=jieba.cut(str1)
word=' '.join(cut_text)
# 6.读取图片,作为词云图背景图片
pic=imageio.imread('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/小丑.png')
# 7.读取停止词文件并保存到列表中
stopwords = [line.strip() for line in open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/stopwords.txt').readlines()]
newword=''
# 8.过滤停用词
for s in word:
    if s not in stopwords:
        newword+=s
wd = wordcloud.WordCloud(
    mask=pic,
    font_path='simhei.ttf',
    colormap=colormap,
    background_color='white'
    )
wd.generate(newword)
plt.imshow(wd)
plt.axis('off')
plt.show()