'''
    【052】、使用海龟(turtle)模块实现幸运大转盘
    python实现"幸运大转盘",运行程序,通过键盘空格键控制箭头快速旋转后一键锁定目标
'''
from turtle import *
import turtle
from random import randint

# 1.屏幕初始化,定义箭头
screen = turtle.Screen()
screen.title("幸运大转盘 转转转~")
screen.setup(480, 450)
screen.bgpic("E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/转盘.png")
screen.delay(0)
# 指定点位置
list1 = ((8, 30), (20, 50), (0, 120), (-20, 50), (-8, 30))
screen.addshape("myarrow", list1)
# 绘制箭头
arrow = Turtle(shape="myarrow")
arrow.color("purple")
arrow.rt(0)
# 2.定义旋转箭头函数,启动转盘
rotateNumber = randint(50, 100)
angle = 45


def rotate():
    global rotateNumber, angle
    screen.onkeypress(None, "space")
    if rotateNumber > 0:
        if rotateNumber < 20:
            angle = rotateNumber
        arrow.rt(angle)
        rotateNumber = rotateNumber - 1
        screen.ontimer(rotate, 20)
    else:
        rotateNumber = randint(50, 100)
        angle = 45
        screen.onkeypress(rotate, "space")


screen.onkeypress(rotate, "space")
screen.listen()
screen.mainloop()
