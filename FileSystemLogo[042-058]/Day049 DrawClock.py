'''
    [049]、使用海龟模块绘制动态时钟
    1.模拟石英钟实现动态指针的计时表盘,通过海龟(turtle)模块实现动态计时表盘的绘制
    2.核心技术
        turtle：海龟绘图模块
        datetime：日期时间模块
'''
import turtle
import datetime


# 1.实现在不绘制的情况下进行移动
def skip(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()


# 2.用于实现绘制时钟表盘
def draw_clock_dial():
    turtle.reset()
    turtle.hideturtle()
    for i in range(60):
        skip(160)
        if i % 5 == 0:
            turtle.pensize(20)
            skip(-20)
        else:
            turtle.pensize(1)
            turtle.dot()
        skip(-160)
        turtle.right(6)


# 3.用于实现获取星期
def get_week(t):
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return week[t.weekday()]


# 4.用于实现创建指针
def create_pointer(length, name):
    turtle.reset()
    skip(-length * 0.1)
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    # 注册多边形状
    turtle.register_shape(name, turtle.get_poly())


# 5.用于实现初始化指针
def init_pointer():
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")
    create_pointer(135, "secHand")
    create_pointer(110, 'minHand')
    create_pointer(90, "hurHand")
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 5)
        hand.speed(0)
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()


# 6.用于实现移动指针
def move_pointer():
    # 不停地获取时间
    t = datetime.datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60
    hour = t.hour + minute / 60
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    turtle.tracer(False)
    printer.forward(65)
    # 绘制星期
    printer.write(get_week(t), align="center", font=("Courier", 14, "bold"))
    printer.back(130)
    # 绘制年、月、日
    printer.write(t.strftime('%Y-%m-%d'), align="center", font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)
    turtle.ontimer(move_pointer, 10)


if __name__ == '__main__':
    turtle.setup(450, 450)
    init_pointer()
    turtle.tracer(False)
    draw_clock_dial()
    move_pointer()
    turtle.mainloop()
