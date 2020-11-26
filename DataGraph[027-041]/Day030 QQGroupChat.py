'''
    [030]、QQ群聊天数据分析
        1.python分析QQ群聊天中有价值的数据,
          将导出的QQ群聊天记录数据保存到qun.txt中后进行处理,筛选词频高,通过词云图进行展示。
'''
import re
import matplotlib.pyplot as plt
from matplotlib import colors
import jieba
import wordcloud

# 1.按行读取群聊天记录(文件文件)
f = open('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/qun.txt', 'r', encoding='utf-8')
fl = f.readlines()
# 2.使用del()方法删除头数据（前8行数据）
del fl[:8]  # del删除切片（前8行数据）
fl = fl[1::3]  # 提取下标为1,步长为3的切片
str1 = ''.join(fl)
# 3.数据处理,滤除无用的文本数据
str1 = str1.replace('[QQ红包]请使用新版手机QQ查收红包。', '')
str1 = str1.replace('[群签到]请使用新版QQ进行查看。', '')
# 通过re模块的findall将[表情]和图片转义成字符,然后使用replace滤除
list1 = re.findall(r'\[.+?\]', str1)
for item in list1:
    str1 = str1.replace(item, '')
# 4.对群聊天数据进行分词处理,绘制词云图
# 自定义颜色
color_list = ['#CD853F', '#DC143C', '#00FF7F', '#FF6347',
              '#8B008B', '#00FFFF', '#0000FF', '#8B0000',
              '#FF8C00', '#1E90FF', '#00FF00', '#FFD700',
              '#008080', '#008B8B', '#8A2BE2', '#228B22', '#FA8072', '#808080']
colormap = colors.ListedColormap(color_list)
# 分词制作词云图
word_list = jieba.cut(str1, cut_all=True)
word = ''.join(word_list)
Mywordcloud = wordcloud.WordCloud(mask=None,
                                  font_path='simhei.ttf',
                                  width=4000,
                                  colormap=colormap,
                                  height=3000,
                                  background_color='#383838').generate(word)
plt.imshow(Mywordcloud)
plt.axis('off')
plt.show()
