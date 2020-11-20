'''
    [037]、python统计年度消费账单
        1.python按年统计日常消费数据,实现年账单的分析。
             注意: 若运行报错是一般是缺少xlrd模块,直接导入
        2.重点知识点:
            pandas.to_period()：日期数据处理利器,返回DataFrame对象
                        groupby()：数据分组统计
            pandas模块：是分析结构化数据的工具集,使用基础是Numpy(提高高性能的矩阵运算);
                        用于数据挖掘和数据分析,同时也提供数据清洗功能。
            pandas.set_option()：设置指定选项的值

'''
import pandas as pd

# 1.解决数据输出是列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 2.获取Excel数据
df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/accounts.xlsx')
# 3.按年统计分析年账单数据
# 设置索引,按年份显示数据
df = df.set_index('日期', drop=True)
df = df.to_period('A')
# 按支出类别分组统计
df_year = df.groupby(['日期', '支出类别'])[['金额']].sum()
print(df_year)
