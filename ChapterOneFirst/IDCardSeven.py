#-*-coding:GBK-*-
'''
    1.实现根据输入的身份证生成数量，批量生成相应的虚拟身份证信息
    2.身份证各省市地区编码(身份证前 6 位)文件 sfz.txt
    3.输出打印结果：
        ======身份证批量生成系统======
        ******************************
        请输入要生成的身份证号码数量：5
         341203200105042659
         360222198610211283
         411723195803088222
         140426199805074248
         140212199104211291
         370203199812069132

    4.相关函数：
        random.choice()：从指定序列中选取一个随机选择的元素。
        random.randint()：生成指定范围或任意范围的随机整数。
         time.strftime()：获取当前日期时间。
                 zfill()：返回指定长度的字符串，原字符串右对齐，前面填充0。

'''
import random
import time

card = []
def opefile():
    # 1.读取sfz.txt文件每行内容的前7位数字，若读为空则跳出
    with open('E://06_workspace//jobspace//pythonDemo//tmp//sfz.txt', 'r', encoding='UTF-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            card.append(line[0:7])

def region():
    # 2.随机选取card列表中的元素
    opefile
    first = random.choice(card)
    #print(first)
    return first

def birth():
    # 3.随机生成出生年月日
    now = time.strftime('%Y')
    year = str(random.randint(1948, int(now) - 15))
    month = str(random.randint(1, 12)).zfill(2)
    if month in ["1", "3", "5", "7", "8", "10", "12"]:
        day = random.randint(1, 32)
    elif month in ["4", "6", "9", "11"]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 29)
    day = str(day).zfill(2)
    return year + month + day

def order():
    # 4.随机生成身份证的后4位数
    randis = str(random.randint(1, 9999)).zfill(4)
    return randis

def main():
     rancard = region() + birth() + order()
     print('随机生成的身份证号码为：' + rancard)
opefile()
print("======身份证批量生成系统======")
print("*" * 30)
count = int(input("请输入要生成的身份证号码数量："))
for i in range(count + 1):
    rancard = region() + birth() + order()
    print(rancard)
