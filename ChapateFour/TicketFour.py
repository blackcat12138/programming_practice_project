'''
    彩票抽奖4
    1.体彩投注是从01~35共三十五个号码中任选五个号码,
      从由01~12共十二个号码组成任选两个号码的组合进行投注。
      每注投注金额2元,输出5柱体彩。
    2.输出结果如下：
        ***超级大乐透***
        ================
        15,16,02,04,11,03,12
        20,34,01,19,35,01,08
        21,31,27,17,10,03,10
        02,11,25,21,23,11,02
        35,17,27,34,10,06,11
    3.知识点回顾：
        zfill()：指定长度的字符串,原字符串右对齐,前面填充为0.
        join()：将序列中的元素以连接符连接成一个新的字符串。
        range()：生成指定范围的整数。
        random.sample()：指定序列中随机获取指定长度的片段。
        random.choice()：指定序列返回一个随机的元素。

'''
import random

print("***超级大乐透***")
print("================")
for i in range(5):
    one = [str(i).zfill(2) for i in (random.sample(range(1, 36), 5))]
    two = [str(i).zfill(2) for i in (random.sample(range(1, 13), 2))]
    print(','.join(one) + "," + ','.join(two))