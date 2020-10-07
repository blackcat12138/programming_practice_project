'''
    文件读取3
    1.向go.txt文件的末尾追加内容"面朝大海,春暖花开！"
'''
with open("E://06_workspace//jobspace//pythonDemo//tmp//go.txt", 'a', encoding="UTF-8") as file:
    string = "\n面朝大海，春暖花开！"
    file.write(string)
with open("E://06_workspace//jobspace//pythonDemo//tmp//go.txt", 'r', encoding="UTF-8") as file:
    var = file.read()
    print(var)
