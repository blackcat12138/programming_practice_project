'''
    彩票抽奖7
    1.强力球玩法设置是从59个白球中选出5个,再从35个红球中选出1个,
        若6个号码全中即可中得头奖,请编写一个程序,随机生成10注强力球彩票。
    2.输出结果如下：
        ---强力球彩票---
        ================
        45 02 57 05 04 19
        13 12 37 53 27 20
        38 51 59 52 07 07
        47 21 48 13 54 01
        05 26 46 47 55 24
        13 04 37 59 09 03
        12 07 39 15 37 06
        57 22 55 19 14 05
        44 56 26 15 50 25
        02 54 16 55 40 15

'''
import random

print("---强力球彩票---")
print("================")
#
# for i in range(10):
#     dig = [str(i).zfill(2) for i in (random.sample(range(1, 60), 5))]
#           + [str(i).zfill(2) for i in(random.sample(range(1, 36), 1))]
#     print(" ".join(dig))

for i in range(10):
    white = [str(i).zfill(2) for i in (random.sample(range(1, 60), 5))]
    red = [str(i).zfill(2) for i in (random.sample(range(1, 36), 1))]
    dig = white + red
    print(" ".join(dig))
