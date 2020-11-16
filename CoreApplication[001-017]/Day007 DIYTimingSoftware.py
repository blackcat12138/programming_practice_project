'''
    DIY高考倒计时小软件
    1.实现对2021年、2020年高考时间进行倒计时(精确到天)显示
    2.重点知识点：
        datetime.strftime()：用于格式化datetime对象。
    3.输出结果如下：
        高考倒计时
        今天是： 2020-10-14 Wednesday
        距离2021年高考还有235天
        距离2022年高考还有600天
'''
import datetime

print("高考倒计时")
now = datetime.datetime.today()
print("今天是：", now.strftime("%Y-%m-%d %A"))
# 2021年、2022年高考日期
time1 = datetime.datetime(2021, 6, 7)
time2 = datetime.datetime(2022, 6, 7)
print("距离2021年高考还有" + str((time1 - now).days) + "天")
print("距离2022年高考还有" + str((time2 - now).days) + "天")
