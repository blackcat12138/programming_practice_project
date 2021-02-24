'''
    [044]、英文短文自动分词写入文本文件
    1.对于大段文章中的单词,可以通过python实现自动分词,
      并去掉特殊符号、空格、空行、数字和重复单词等不符合规范内容,然后形成单词本格式。
    2.核心技术
      string模块：字符串处理模块，可以对字符串进行分割,然后去重、去特殊符号、去空格和数字等
'''
import string

f = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/split.txt')
s = f.read()
str1 = s.title()
print(str1)
print("".join([s for s in str1.splitlines(True) if s.strip()]))
# 采用默认分隔符进行分割
list1 = str1.split()
# 字符串列表去重
l1 = list(set(list1))
l1.sort(key=list1.index)
for i in l1:
    # 去掉特殊符号
    i1 = i.translate(str.maketrans('', '', string.punctuation))
    # 去除字符串中头尾的空格
    i2 = i1.strip(' \t\n\r')
    if not i2.isnumeric():
        i3 = i2
        f1 = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/单词本.txt', 'a')
        f1.write('\n' + i3)
