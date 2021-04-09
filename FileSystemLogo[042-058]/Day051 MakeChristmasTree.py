'''
    [051]、使用海龟模块绘制圣诞树
        通过海龟(turtle)模块实现圣诞树的绘制。
'''
import turtle

# 首先设置窗体大小,创建画笔对象并为其初始化
turtle.setup(500, 600)
tree = turtle.Turtle()
tree.shape('triangle')
tree.color('green')
tree.right(30)
tree.up()


# 通过循环实现圣诞树每层的绘制工作,通过is_square参数前函数绘制的树叶部分还是树干部分
def drawing_tree(start, stop, move, is_square=False):
    if is_square:
        tree.left(30)
        tree.shape('square')
        tree.color('brown')
    for r in range(start, stop):
        a = r
        if is_square:
            a = 1
        y = 20 * r
        for c in range(a):
            x = 20 * c
            tree.goto(x, -y + move)
            tree.stamp()
            tree.goto(-x, -y + move)
            tree.stamp()


# 实现圣诞树的绘制工作
drawing_tree(1, 4, 160)
drawing_tree(2, 5, 120)
drawing_tree(3, 6, 80)
drawing_tree(4, 9, 40, True)

# 创建用于写入文字的turtle对象,goto()方法将画笔移动至需要书写文字的位置,调用write()方法实现文字的写入
word = turtle.Turtle()
word.up()
word.goto(-150, 200)
word.color('red')

# 写入文字"圣"
word.write("圣", font=(u"黑体", 48, "normal"), align="center")
word.goto(-50, 200)
# 写入文字"诞"
word.write(arg="诞", move=True, font=(u"黑体", 48, "normal"), align="center")
word.goto(50, 200)
# 写入文字"快"
word.write("快", font=(u"黑体", 48, "normal"), align="center")
word.goto(150, 200)
# 写入文字"乐"
word.write("乐", font=(u"黑体", 48, "normal"), align="center")
word.hideturtle()
turtle.mainloop()
