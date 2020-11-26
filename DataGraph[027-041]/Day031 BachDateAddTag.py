'''
    [031]、批量为电商数据添加Tag标签
      1.通过tag标签能够检索到相关商品的信息,以电商数据mrbook.xlsx文件,使用python将大量的商品数据标签进行批量添加。

'''
import pandas as pd

# 1.为输出的数据能够对齐设置
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 2.读取Excel数据为DataFrame对象
df = pd.DataFrame(pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/mrbook.xlsx'))


# 3.定义标签函数
def add_tag(data):
    global tag
    tag = ''
    if '零' in data:
        tag = '零基础|' + tag
    if '例' in data:
        tag = '实例|' + tag
    if '项目' in data:
        tag = '项目|' + tag
    if 'C#' in data:
        tag = 'C#|' + tag
    if 'Android' in data:
        tag = 'Android|' + tag
    if 'SQL' in data:
        tag = 'SQL|' + tag
    if 'Python' in data:
        tag = 'Python|' + tag
    if 'Oracle' in data:
        tag = 'Oracle|' + tag
    return tag


# 4.保存并输出数据
# 将添加的抱歉保存到tag列中
df['tag'] = df['图书名称'].apply(add_tag)
print(df)
# 保存数据为Excel
df.to_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/mrbook副本.xlsx')
