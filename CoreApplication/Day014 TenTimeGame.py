'''
    [014]、挑战10秒小游戏程序
    1.实例描述:
        用户单击'开始挑战'按钮则开始计时,单击'停止'按钮则停止计时,
        当计时时间刚好为10秒,则会提示'挑战成功,您目前消费可全部免单！！'
        当计算时间不等于10秒将提示'挑战失败,您可以领取30元代金劵一张'。
    2.核心技术
        sys.stdout：该对象实现同一位置动态输出实时秒数。在使用print()方法打印输出时,
            底层会将内容传递给sys.stdout标准输出,然后通过sys.stdout.write()方法进行输出,
        sys.stdout.write()：输出完光标会停留在输出内容的最后位置。
        print()：输出后光标会跳到下一行行首。
            print('hello') 等价于  sys.stdout.write('hello'+'\n')
'''

import random
import time
from tkinter import *
from tkinter.messagebox import *

root = Tk()
rans = [0.1, 0.08, 0.06, 0.04]
count = 0
start = False


# 游戏主题函数
# 通过按钮（Button）控件fight控制挑战10秒游戏的开始和停止
def ten():
    global start  # 定义全局变量start,记录游戏状态
    global count  # 定义全局变量count,记录秒数
    num = random.choice(rans)  # 随机产生间隔时间,增加游戏难度
    fight['text'] = '停止'
    # 如果是停止状态
    if not start:
        start = True
        # 通过while语句控制进行计时,当游戏停止时,通过判断计时时间是否为10秒来判断用户是否挑战成功
        while start:
            time.sleep(num)
            count += 0.2
            show['text'] = format(count, '.1f')
            show.update()
            # 如果等于10秒,即挑战成功
        if show['text'] == str(10.0):
            warn = showwarning(title='挑战10秒', message='挑战成功,您目前消费可全部免单！！')
        else:
            warn = showwarning(title='挑战10秒', message='挑战失败,您可以领取30元代金劵一张')
    else:
        start = False
        fight['text'] = '继续挑战'
        count = 0


# 定义主窗口属性及需要添加的控件
root.title('挑战10秒')              # 设置窗口标题
root.wm_attributes('-topmost', 1)  # 设置窗体置顶
root.geometry('200x80')                    # 设置窗体大小
root.resizable(width=False, height=False)  # 设置窗体尺寸不可改变
topic = Label(root, text='挑战10秒')        # 设置窗体中游戏标题
topic.pack()
show = Label(root, text=str(count))
show.pack()
fight = Button(root, text='开始挑战', command=ten)
fight.pack()
mainloop()
