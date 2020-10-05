'''
    填字游戏6
    1.基于GameFive程序改进，增加限时功能，要求用户在90秒内完成游戏，每完成一个成语，提示剩余答题时间。
      答题超时提示 “答题超过90秒答题时间，将退出答题！”，并显示选手得分
    2.输出结果如下：
        成语填填乐
            成语填填乐难度等级菜单
            1:一级难度
            2:二级难度
            3:三级难度
            4:四级难度
            5:五级难度
            6:六级难度
            7:七级难度
            8:八级难度
            9:九级难度
        请输入成语填填乐难度等级菜单的数字，如：3
        2
        直接填写答案，回车进入下一关。什么也不填忽略本成语！！
        剩余答题时间 90 秒
        __今中外
        输入：古
        正确，你真棒！
        剩余答题时间 81 秒
        __手毛脚
        输入：麟
        错了，正确答案： 毛
        剩余答题时间 64 秒
        取长__短
        输入：补
        正确，你真棒！
        选手最后得分： 22
    3.知识积累与回顾：
        datetime.datetime.now()：返回当前系统时间：2019-07-28 15:42:24.765625
        datetime.datetime.timedelta()：用来计算两个datetime.datetime或者datetime.date类型之间的时间差。
        random.choice()：从序列中获取一个随机元素。
        random.randint()：用于随机生成一个指定范围内的整数。
'''
import datetime
import random

print("成语填填乐\n")
print('''
    成语填填乐难度等级菜单
    1:一级难度
    2:二级难度
    3:三级难度
    4:四级难度
    5:五级难度
    6:六级难度
    7:七级难度
    8:八级难度
    9:九级难度    
''')
num = input("请输入成语填填乐难度等级菜单的数字，如：3\n")
filename = "E://06_workspace//jobspace//pythonDemo//tmp//" + "idiom" + num + ".txt"
remain = datetime.datetime.now() + datetime.timedelta(seconds=90)
lists = []

with open(filename, 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        lists.append(line.replace('\n', ''))
print('直接填写答案，回车进入下一关。什么也不填忽略本成语！！')


def idiom(ask, count):
    i = 1
    while True:
        timeis = (remain - datetime.datetime.now()).seconds
        if timeis > 90:
            print("答题超过90秒答题时间，将退出答题！")
            break
        else:
            print("剩余答题时间", timeis, '秒')
            work = random.choice(ask)
            bank = random.randint(0, 3)
            new = work[:bank] + "__" + work[bank + 1:]
            print(new)
            num = input("输入：")
            if not num:
                print("过！")
                continue
            elif num.strip(" ") == work[bank]:
                count += 2
                print("正确，你真棒！")
            else:
                count -= 2
                print("错了，正确答案：", work[bank])
            i += 1
            if i > 3:
                return count


print("选手最后得分：", idiom(lists, 20))
