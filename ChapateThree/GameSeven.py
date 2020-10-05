'''
    填字游戏7
    1.基于GameSix程序改进，实现程序选择填空功能。成语随机位置空格输出需要选择的一个字，
        随机从所有成语的词汇中选择三个假答案，结合正确答案让用户选择，用户只需输入正确答案前面的字母即可，
        如果输入非 A、 B、C、D，将提示“输入错误，将重新选择！”
    2.输出结果如下：
        成语填填乐
        成语填填乐难度等级菜单
        1：一级难度
        2：二级难度
        3：三级难度
        4：四级难度
        5：五级难度
        6：六级难度
        7：七级难度
        8：八级难度
        9：九级难度
        请输入成语填填乐难度等级菜单的数字，如：3
        2
        剩余答题时间 87 秒
        ___华秋实
        A: 春
        B: 红
        C: 张
        D: 跳
        请输入正确答案前面的字母，如：B
        a
        正确，你真棒！
        选手最后得分： 22
    2.知识积累与回顾
               append()：用于在列表末尾添加新的对象。
        random.shuffle()：打乱列表中元素,并随机排序列表(洗牌)。
        random.sample()：从序列中随机抽取指定个数的元素。
               update()：对字典中的键值对进行更新、修改、添加操作。
               upper()：将字符串中的小写字母转为大写字母。
'''
import datetime
import random

listid = []
ansall = set()

# 限时90秒完成
remain = datetime.datetime.now() + datetime.timedelta(seconds=90)
print('成语填填乐\n')
print('''成语填填乐难度等级菜单
1：一级难度
2：二级难度
3：三级难度
4：四级难度
5：五级难度
6：六级难度
7：七级难度
8：八级难度
9：九级难度''')
num = input("请输入成语填填乐难度等级菜单的数字，如：3\n")
filename = "E://06_workspace//jobspace//pythonDemo//tmp//" + "idiom" + num + ".txt"
with open(filename, 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        line = line.replace('\n', '')
        line = line.replace('、', '')
        listid.append(line)
        nnn = list(line)
        ansall.update(nnn)


def idiom(l, count):
    i = 1
    while True:
        timeis = (remain - datetime.datetime.now()).seconds
        if timeis > 90:
            print("答题超过90秒答题时间，将退出答题！")
            break
        else:
            print("剩余答题时间", timeis, '秒')
            anssel = []
            flag = False
            word = random.choice(l)
            bank = random.randint(0, 3)
            anssel.append(word[bank])
            rndsel = random.sample(ansall, 3)
            anssel.append(rndsel[0])
            anssel.append(rndsel[1])
            anssel.append(rndsel[2])
            random.shuffle(anssel)

            new = word[:bank] + "___" + word[bank + 1:]
            print(new)
            print("A:", anssel[0])
            print("B:", anssel[1])
            print("C:", anssel[2])
            print("D:", anssel[3])

            sel = input("请输入正确答案前面的字母，如：B\n").upper()

            if sel not in ["A", "B", "C", "D"]:
                print("输入错误，将重新选择！")
                continue
            elif sel == "A":
                if anssel[0] == word[bank]:
                    count += 2
                    flag = True
                    print("正确，你真棒！")
            elif sel == "B":
                if anssel[1] == word[bank]:
                    count += 2
                    flag = True
                    print("正确，你真棒！")
            elif sel == "C":
                if anssel[2] == word[bank]:
                    count += 2
                    flag = True
                    print("正确，你真棒！")
            elif sel == "D":
                if anssel[3] == word[bank]:
                    count += 2
                    flag = True
                    print("正确，你真棒！")
            if flag == False:
                count -= 2
                print("错了，正确答案：", word[bank])
            i += 1
            if i > 1:
                return count


print("选手最后得分：", idiom(listid, 20))
