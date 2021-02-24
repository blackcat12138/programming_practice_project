'''
    [046]、竞猜电影主演
    1.用户随机选出一部电影,随机输出6名演员,让用户判断是否为该部电影的主演,
      回车确认是,按下任意键回车否决,判断正确加三分,判断错误减三分,最后输出选手得分（选手起始分为30分）
    2.在python中打开文件后,除了可以写入或追加内容,还可以读取文件中的内容。读取文件内容主要如下：
        (a).读取指定字符
            file.read([size])：读取指定个数的字符,若省略则一次性读取所有内容。
                    例如：with open('message.txt','r') as file:
                                string=file.read(9)
                                print(string)
        (b).读取一行
            file.readline()：每次读取一行数据,打开文件需指定打开模式,可以使用while语句读取文件内容。
                    例如：
                          f=open('film.txt')
                          while True:
                             line=f.readline()
                             print(line)
                             if line=='':
                                break
                          f.close()
        (d).读取全部行
            file.readlines()：读取全部行,返回的是一个字符串列表,每个元素为文件的一行内容。
                    例如：
                        print('\n','='*20,"Python经典应用","="*20,"\n")
                        with open('message.txt','r') as file:
                             message=file.readlines()
                             print(message)
                             print("\n","="*25,"over","="*25,"\n")
'''
import random

dict_film = {}
list_film = []

file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/film.txt')
while True:
    line = file.readline().strip(' ').strip('\n')
    if line == '':
        break
    filmline = line.strip(":")
    list_film.append(filmline[0])
    list_acter = filmline[1].split(',')
    dict_film[filmline[0]] = list_acter
file.close()
file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/acter.txt')
while True:
    line = file.readline().strip(' ').strip('\n')
    if line == '':
        break
    actall = line.split(",")
file.close()
film = random.choice(list_film)
acter = dict_film.get(film)
count = 30
print("电影：", film)
print('判断演员是否本部电影的演员。回车确认"是",输入任意键确定"不是"')
for i in range(6):
    new = random.choice(actall)
    actall.remove(new)
    print(new)
    num = input("").strip()
    if not num:
        if new not in acter:
            count -= 3
            print("答错了,减三分！")
        else:
            count += 3
            print("答对了,加三分！")
        print("当前分数：", count)
    else:
        if new not in acter:
            count += 3
            print("答对了,加三分！")
        else:
            count -= 3
            print("答错了,减三分!")
        print("当前分数：", count)
else:
    print("竞猜最高分为48分,你的最后分数：", count)
