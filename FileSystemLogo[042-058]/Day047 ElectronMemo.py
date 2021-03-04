'''
    [047]、制作电子便签本
    1.通过python制作电子便签,将记录的信息使用字典保存便签信息,将日期和时间作键保存,内容作为值保存。
    2.核心技术
        write()：可以向文件中写入内容，可以指定打开模式w(可写)、a(追加)
'''
import datetime

notes = []
note = {}

# 1.显示前10条便签的简要内容
# 以只写模式打开文件
file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/note.txt')
for i in range(10):
    line = file.readline().strip(' ').strip('\n')
    if line == "":
        break
    lines = line.split("&")
    if len(lines[1]) > 10:
        notes.append(lines[1][0:10] + "-----" + lines[0])
    else:
        notes.append(lines[1] + "-----" + lines[0])
file.close()
print("\n".join(notes))
# 2.添加便签、查询便签和浏览便签
print("=========便签本===========")
while True:
    choice = input("输入数字1写便签,输入数字2查询便签\n输入数字3浏览全部便签,输入'q'退出系统\n")
    if choice.strip("") == 'q':
        print("退出电子便签")
        break
    if choice.strip("") == '1':
        order = datetime.datetime.now()
        order = format(order, "%Y-%m-%d %H:%M:%S")
        word = input("")
        note[order] = word
        # 以写模式打开文件
        file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/note.txt', 'a')
        file.write('\n' + order + '&' + word)
        file.close()
    elif choice.strip(" ") == '2':
        str = input("请输入要查询的文字：")
        file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/note.txt')
        for i in range(10):
            line = file.readline().strip().strip('\n')
            if line == '':
                break
            if str in line:
                lines = line.split("&")
                print(lines[0])
                print('  ' + lines[1])
        file.close()
    elif choice.strip(" ") == '3':
        file = open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/note.txt')
        while True:
            line = file.readline().strip('').strip('\n')
            if line == '':
                break
            lines = line.split("&")
            print(lines[0])
            print('  ' + lines[1])
        file.close()
