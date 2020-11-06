'''
    数字大小写转换
    1.将输入的数字转换为汉字大写
    2.重点知识点：
        print(value,sep='',end='\n',flush=)：输出参数介绍
            value：要输出的值(不限数量)
           sep=''：键输出的值连接符号,默认为空格
           end=''：输出结束时这个字符结束,默认为'\n',输出不换行为end=''
            flush：是否刷除数据流。
'''

info = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
data = input("请输入数字：")
for i in range(len(data)):
    print(info[int(data[i])], end='')
