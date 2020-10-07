'''
    文件读取1
    1.读取two.txt文件内容,输出文件内容信息
    2.输出结果所示：
        成功人的两会：开会、培训会
        普通人的两会：约会、聚会
        穷人的两会：这也不会，那也不会
        奋斗的人两会：必须会，一定得会！
    3.知识点回顾：
        open()：用于打开文件,返回一个文件读写对象,然后对文件进行相关操作
        split()：将一个字符串按照指定的分隔符切分成字符串列表。
        join()：将序列中的元素指定连接符连接成一个新的字符串。
        read()：读取文件中指定的字符数,若未给定或为负则读取所有。(包括"\n"字符)
'''
with open('E://06_workspace//jobspace//pythonDemo//tmp//two.txt', 'r', encoding="UTF-8") as file:
    var = file.read()
    new = var.split("；")
    print("\n".join(new))
