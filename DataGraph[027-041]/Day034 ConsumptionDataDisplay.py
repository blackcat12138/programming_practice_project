'''
    [034]、环比分析日常消费数据掌握月支出增减情况
        1.根据accounts_02.xlsx文件中的消费数据,使用环比分析方法,
            分析个人日常消费数据,对比分析每月消费增减情况。
        2.重点知识点
            环比公式：本月数-上月数=环比差值 (反映本月比上月增长或减少的差值)
            pandas.series.shift()：返回向下位移后的结果,数据位移。
            DataFrame对象.to_period()：日期数据处理。
'''
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/accounts_02.xlsx')
# 数据分组统计、环比分析
# 设置索引,按月份显示数据
df = df.set_index('日期', drop=True)
# 获取2019年每个月的数据
df = df['2019'].to_period('M')
# 按月统计支出
df_month = df.groupby(['日期'])[['金额']].sum().reset_index()
# 环比差值
df_month['差值'] = df_month.金额 - df_month.金额.shift()
print(df_month)
