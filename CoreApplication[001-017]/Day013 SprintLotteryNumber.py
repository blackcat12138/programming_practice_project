'''
    模拟生成福彩双色球号码
    1.每注投注号码由6个红色号码球和1个蓝色号码球组成。
        红色号码球1~33中选择;蓝色号码球1~16中选择。输出福利彩票,实现以下功能：
            (a).输入要生成的福利彩票双色球组数。随即批量产生福彩双色球号码
            (b).将幸运号码作为蓝色球,按输入的幸运号码既要生成的双色球彩票组数,输出福彩双色球号码。
    2.重点知识点：
        random.randin(start,stop)：用于随机获取一个指定范围内的整数。
        random.choice(seq)：从序列中获取一个随机元素。
        random.random()：用于随机生成一个0到1的小数。
        random.sample(seq,k)：从指定序列中随机获取指定长度的片段并随机排序。（随机获取序列中指定个数的元素）
        random.randrange(start,stop,step)：从指定范围内,递增集合中获取一个随机数。
        zfill()：向左指定个数填充字符0
'''
# 输入要生成的福彩双色球号码组数,随机批量产生福彩双色球号码
import random

print("********福彩双色球号码*******")
print("===========================")
red = [str(i).zfill(2) for i in (random.sample(range(1, 31), 6))]
print(','.join(red) + ',' + str(random.choice(range(1, 16))).zfill(2))
# 输入幸运号码及要生成的双色球彩票组数,输出福利彩票号码。
luck = input("请输入您的幸运数字（1~16）:\n")
inputx = int(input("请输入双色球彩票组数：\n"))
for i in range(inputx):
    red = [str(i).zfill(2) for i in (random.sample(range(1, 31), 6))]
print(','.join(red) + ',' + luck.zfill(2))
