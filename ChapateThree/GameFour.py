'''
    填字游戏4
    1.在GameThree程序基础上改进，将网络中的成语复制到文件(idiom.txt)中,使用时从文件中读取到列表。
    2.输出结果如下：
        成语填填乐
        直接填写答案，回车进入下一关。什么也不填忽略本成语！
        __灯结彩
        输入：张
        正确,你真棒！
        人__人往
        输入：来
        正确,你真棒！
        自__自在
        输入：由
        正确,你真棒！
        选手最后得分： 26
'''
import random

lists = []
with open('E://06_workspace//jobspace//pythonDemo//tmp//idiom.txt', 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        # print(line)
        lists.append(line.replace('\n', ''))
print("成语填填乐\n")


def idiom(ask, count):
    i = 1
    print('直接填写答案，回车进入下一关。什么也不填忽略本成语！')
    while True:
        word = random.choice(ask)
        bank = random.randint(0, 3)
        new = word[:bank] + "__" + word[bank + 1:]
        print(new)
        num = input("输入：")
        if not num:
            print("过！")
            continue
        elif num.strip(" ") == word[bank]:
            count += 2
            print("正确,你真棒！")
        else:
            count -= 2
            print("错了,正确答案：", word[bank])
        i += 1      # 定义计算器,表示第几关
        if i > 3:   # 如果小于第三关,则返回得分
            return count


print("选手最后得分：", idiom(lists, 20))
