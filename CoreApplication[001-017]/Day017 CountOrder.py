'''
    [017]、混合加减法出题程序
      1.根据输入出题数量随机输出100以内混合加减法的计算题。
        出题试卷分为不带答案和带答案两个部分,分别输出到屏幕和文件(math.txt和key.txt)中。
'''
import random

# 定义多个变量并赋值
exp1, exp2 = "", ""
str1, str2 = "", ""
j = 0
count = int(input('请输入出题数量:'))
while j < count:
    if j < count:
        flag = random.choice(['+', '-'])
        if flag == '+':
            a = random.randint(0, 100)
            b = random.randint(0, 100 - a)
            result = a + b
        # 若是减法,被减数和减数都应小于100
        else:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            # a和b比较,较大的数为被减数
            if a < b:
                a, b = b, a
            result = a - b
        a = str(a).ljust(2, ' ')
        b = str(b).ljust(2, ' ')
        exp1 = a + ' ' + flag + ' ' + b + ' ='
        exp2 = a + ' ' + flag + ' ' + b + ' =' + str(result)
        # 点j为偶数,不换行,为奇数就换行
        if j % 2 == 0:
            str1 = str1 + exp1 + '\t'
            str2 = str2 + exp2 + '\t'
        else:
            str1 = str1 + exp1 + '\n'
            str2 = str2 + exp2 + '\n'
        j = j + 1
with open('/CoreApplication[001-017]//tmp//math.txt', 'w') as f:
    f.write(str1)
with open('/CoreApplication[001-017]//tmp//key.txt', 'w') as f:
    f.write(str2)
print(count, '道混合加减法题：')
print(str1)
print(count, '道混合加减法题(带答案)：')
print(str2)
