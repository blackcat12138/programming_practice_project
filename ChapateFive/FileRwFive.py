'''
    文件读取5
    1.提取当前目录下的所有文件的大小、访问时间和更新时间信息保存到一个新文件rec.txt。
    2.重点知识点
        os.listdir()：用于返回指定文件夹包含的文件或文件夹的名字的列表。(不包括"."和".."符号的文件夹)
          os.lstat()：返回一个包含文件信息的stat_result对象。
                    st_mtime:最后修改时间
                    st_atime:上次访问时间
          os.open()：用于打开一个文件,并设置需要的打开选项(描述符),多个选项用"|"分隔。
                    os.O_CREAT:创建并打开一个新文件
                     os.O_RDWR:以读写的方式打开
         os.write()：用于写入字符串到文件描述符fd中。
'''
import datetime
import os

record = ""
path = ''                   # 指定目标路径空,则当前目录为"."
files = os.listdir()        # 获取指定路径下的所有文件名
for file in files:          # 遍历所有文件
    info = os.lstat(path + file)
    record += file + "--文件大小：" \
              + str(info.st_size) + "--修改时间：" \
              + datetime.datetime.fromtimestamp(info.st_mtime).strftime('%Y-%m-%d %H:%M:%S') + "--访问时间：" \
              + datetime.datetime.fromtimestamp(info.st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n"
fd = os.open("../../tmp/rec.txt", os.O_RDWR | os.O_CREAT)         # 以新建\读写方式打开文件
os.write(fd, bytes(record, "UTF-8"))                              # 写入信息到文件
os.close(fd)
