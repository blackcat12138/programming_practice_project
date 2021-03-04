'''
    [048]、小说词频统计
    1.选择小说文件,输入单词或多词进行词频统计
    2.核心技术
        count()：可以统计指定字符串在某字符串对象中出现的次数。
        find()：可以查询指定字符串在某字符串对象中出现的索引位置。
        replace()：可以进行字符串的替换操作。
'''
# 1.导入tkinter模块并对其初始化
import tkinter.filedialog
from tkinter import *

root = Tk()
# 不显示窗口
root.withdraw()
# 2.读取小说文件内容并输出
filename = tkinter.filedialog.askopenfilename()
with open(filename, 'r') as file:
    list = file.readline()
word = '\n'.join(list)
print(word )
new = word
punct = ', 。' ' ; : ( ) '" "' \n'
list_punct = punct.split(' ')
for item in list_punct:
    new.replace(item, '')
long = len(new)
# 3.统计词频
user = input('输入统计词，如果多词用英文逗号间隔：\n').split(",")
for item in user:
    count = word.count(item)
    order = ''
    size = 0
    for i in range(count):
        size = word.find(item, size + len(item))
        order += str(size) + " "
    print("小说字数（去除标点）：", len(new))
    print(item + '出现次数：', count)
    print(item + "出现位置：", order)
    print(item + "出现频次：", format(count * len(item) / long, '.2f'))
