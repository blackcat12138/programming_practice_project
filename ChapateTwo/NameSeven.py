'''
    1.根据重名文件 names.txt，对重名名字的姓氏进行统计，按统计结果降序排列重名的姓氏.

'''

names = []
name_set = set()
name_sort = []
with open('E://06_workspace//jobspace//pythonDemo//tmp//names.txt', 'r', encoding='UTF-8') as file:
    while True:
        line = file.readline()
        if line == '':
            break
            # 1.读取文件内容,将文件中的姓氏切割放到集合中
        new = line.split(" ")
        names.append(new[1][0])
        name_set.add(new[1][0])
for item in name_set:
    # 2.遍历集合中的姓氏,聚合重复姓氏,组合放在name_sort-->[107,'李'],[7,'刘']
    counts = names.count(item)
    name_sort.append([counts, item])
    # 3.对统计的姓氏结果进行降序排序
name_sort.sort(reverse=True)
for it in name_sort:
    print(it[1], it[0])
