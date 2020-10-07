'''
    文件读取4
    1.获取并输出 go.txt 文件的重要信息，如文件大小（字 节）、访问时间及更新时间等。
    2.输出结果如下：
          文件大小(字节)：151
            文件访问时间：2020-10-07 17:21:32
            文件更新时间：2020-10-07 17:2132

    3.重点知识点：
        os.lstat()：返回一个包含文件信息的stat_result对象
                st_atime:上次访问时间
                st_mtime:最后修改时间
                st_ctime:状态最后一次修改的时间
                st_size:总大小，以字节为单位
        datetime.datetime.fromtimestamp()：返回指定时间戳转换成对应的时间
             datetime.datetime.strftime()：日期格式与字符串格式相互间转换

'''
import datetime
import os

file = "E://06_workspace//jobspace//pythonDemo//tmp//go.txt"
info = os.lstat(file)
# print(info)
vist = datetime.datetime.fromtimestamp(info.st_atime).strftime('%Y-%m-%d %H:%M:%S')
upda = datetime.datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M%S")
print("文件大小(字节)：" + str(info.st_size), "\n文件访问时间：" + vist, "\n文件更新时间：" + upda)
