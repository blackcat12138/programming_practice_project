'''
    自动计算消耗能量的虚拟跑步机
    1.输入体重、运动速度、运动时间后、可以实时显示剩余运动时间、运动距离和消耗热量。
        消耗热量=体重(kg)*运动时间(小时)*指数K
            指数K=30/速度(分钟/400米)
    2.重点知识点：
        divmod()：可以接受除数和被除数,返回一个包含商和余数的元组。
        sys.stdin.readline()：标准输入的方法,与input()输入类似。
        sys.stdin.readlines()：对统一处理批量输入的数据。
        sys.stdout.write()：横向输出内容到屏幕,与print()打印类似。
'''
import sys
import time

leave = 0
print("==========虚拟跑步机========")
print(30 * "#")
weight = float(input("输入您的体重(kg)："))    # 输入体重为浮点数
speed = float(input("速度(千米/小时)："))      # 输入速度为浮点数
times = int(input("跑步时间(分钟)："))         # 输入的跑步时间为整数，为分钟
times = times * 60                           # 将分钟转换为秒
while leave < times:
    leave += 1
    min, sec = divmod(times - leave, 60)                                 # 将转换为分钟和秒
    leave_time = str(min) + '分' + str(sec) + '秒'
    dista = leave / 3600 * speed                                         # 计算跑步距离
    calor = weight * 30 / (400 / (speed * 1000 / 60)) * leave / 60 / 60  # 计算热量
    sys.stdout.write('\r')
    sys.stdout.write('剩余时间:{} 跑步距离：{:.2f}千米 消耗热量：{:.2f}千米'.format(leave_time, dista, calor))
    sys.stdout.flush()
    time.sleep(1)
