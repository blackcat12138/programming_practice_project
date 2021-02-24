'''
    [045]、背单词程序APP小软件
    1.python制作背单词程序软件,通过线程控制自动切换单词
    2.核心技术
        tkinter界面设计
        使用open方法读取文本文件(单词本)
        通过线程控制自动切换单词,主要使用threading.Thread类
        通过time sleep()函数推迟调用线程的运行
'''
import tkinter as tk
import time
import threading
import random

# 1.通过tkinter模块设计窗体界面
# 建立主窗口window
window = tk.Tk()
# 设置窗口标题栏名称
window.title('轻松背单词')
# 设置窗口的大小
window.geometry('640x765')
# 标记窗体是否运行
window.flag = True
# 设置label背景为图片
image_file = tk.PhotoImage(file='E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/bg.png')
label1 = tk.Label(window, text='', font=("黑体", 60, "normal"), compound='center', image=image_file)
label2 = tk.Label(window, text='', font=("黑体", 15, "normal"))
label1.pack()
label2.place(x=230, y=430)
# 2.读取文本文件(单词本)
words = []
# 3.读取文本(单词本)
f = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/words.txt', 'r', encoding='utf-8')
for s in f.readlines():
    words.append(s)


# 4.自动切换单词
# 定义自动切换单词的方法
def autoChange():
    window.flag = True
    while window.flag:
        i = random.randint(0, len(words) - 1)  # 随机显示单词
        a = words[i].split()  # 文本分割为列表
        b1 = a[0:1]  # 第1列单词
        b2 = a[2:4]  # 第2、3列音标和解释
        # label组件显示文本
        label1['text'] = b1
        label2['text'] = b2
        time.sleep(3)


# 用线程控制自动切换单词
t = threading.Thread(target=autoChange)
t.start()
window.mainloop()
window.flag = False
