'''
    彩票抽奖3
    1.七乐彩投注号码范围为01~30,七乐彩每期从30个号码中开出7个基本号码和1个特别号码作为中奖号码,
      顺序不限。输出5柱7乐彩彩票。
    2.输出结果如下：
            ***福彩七乐彩***
            ===============
              基本号码     特别号码
            05 06 14 20 23 30   27
            08 10 14 15 16 24   04
            02 07 12 16 20 23   11
            06 10 12 14 22 29   26
            10 13 16 17 18 24   29
    3.知识点回顾：
        zfill()：指定长度的字符串,原字符串右对齐,前面填充为0.
        join()：将序列中的元素以连接符连接成一个新的字符串。
        sorted()：对所有可迭代的对象进行排序,保留原列表元素顺序。
        sort()：对已存在的列表进行排序操作,无返回值。
        random.sample()：指定序列中随机获取指定长度的片段。
        random.choice()：指定序列返回一个随机的元素。
'''
import random

print("***福彩七乐彩***")
print("===============")
print("  基本号码  ", "  特别号码")
for i in range(5):
    sev = [str(i).zfill(2) for i in (random.sample(range(1, 31), 7))]
    base = sorted(sev[0:6])
    print(' '.join(base) + "   " + sev[6])
