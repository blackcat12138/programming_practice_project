'''
    文件读取7
    1.在处理数据时,有时需要将文件内容分解成多个文件进行保存, 将gdp.txt文件内容分解成多个文件
'''
new = []
with open("E://06_workspace//jobspace//pythonDemo//tmp//gdp.txt", "r", encoding="UTF-8") as file:
    for line in file:
        var = line.split(" ")
        new.append(var)
for i in range(len(new)):
    with open(new[i][0] + ".txt", "w", encoding='UTF-8') as file:
        file.write("\n".join(new[i]))
