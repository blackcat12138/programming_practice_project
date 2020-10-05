'''
    填字游戏5
    1.基于GameFour程序改进,将成语文件分9个等级,让用户选择难度等级,程序根据难度等级调用对应的成语文件,
        实现成语填填乐(设置难度等级)。成语文件包括 idiom1.txt~idiom9.txt。
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
        直接填写答案，回车进行下一关。什么也不忽略本成语！！
        非__非故
        输入：亲
        正确，你真棒！！
        快__快语
        输入：言
        正确，你真棒！！
        __底之蛙
        输入：井
        正确，你真棒！！
        选手最后得分： 26
'''
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
lists = []
with open(filename, 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        lists.append(line.replace('\n', ''))
print('直接填写答案，回车进行下一关。什么也不忽略本成语！！')


def idiom(ask, count):
    i = 1
    while True:
        work = random.choice(ask)
        bank = random.randint(0, 3)
        new = work[:bank] + "__" + work[bank + 1:]
        print(new)
        num = input("输入：")
        if not num:
            print("过")
            continue
        elif num.strip(" ") == work[bank]:
            count += 2
            print("正确，你真棒！！")
        else:
            count -= 2
            print("错了,正确答案:", work[bank])
        i += 1
        if i > 3:
            return count


print("选手最后得分：", idiom(lists, 20))
