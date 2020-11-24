'''
    [036]、python分析月平均消费金额
        1.根据accounts.xlsx文件中的数据,使用python分析月的平均支出金额
        2.重点知识点:
            mean()：求平均值的函数
            applymap()：DataFrame中的各个浮点值保留两位小数
                    applymap(lambda x:'%.2f' %x)
'''
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/accounts.xlsx')
# 月平均消费统计
df = df.set_index('日期', drop=True)
# 获取2019年每个月的数据
df = df['2019'].to_period('M')
# 月平均消费统计
df_month = df.groupby(['日期'])[['金额']].mean().applymap(lambda x: '%.2f%x')
print(df_month)
