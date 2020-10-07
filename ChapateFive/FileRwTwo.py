'''
    文件读取2
    1.将two.txt文件中的指定内容输出并保存到新文件go.txt文件中
    2.输出结果内容：
        成功人的两会：开会、培训会
        奋斗的人两会：必须会，一定得会！
'''
with open("E://06_workspace//jobspace//pythonDemo//tmp//two.txt", 'r', encoding='UTF-8') as file1:
    var = file1.read()
    new = var.split("；")
    with open("E://06_workspace//jobspace//pythonDemo//tmp//go.txt", 'w', encoding='UTF-8') as file2:
        string = new[0] + "\n" + new[3]
        file2.write(string)
        print(string)
