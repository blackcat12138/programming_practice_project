'''
    [035]、日常消费数据占比分析总结年消费方向
        1.2019年账单中每一类支出占总支出的百分比,
          使用Pandas模块的groupby()函数结合sum()函数实现。
          公式：占比率=(每类支出的总金额/总体支出金额)*100%
          百分比格式化处理：apply()函数与format()函数结合实现自定义函数格式化数据:
                    apply(lambda x:format(x,'.2%'))
'''
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/accounts_01.xlsx')
# 数据分组统计、占比分析
# 设置索引,按月份显示数据
df = df.set_index('日期', drop=True)
df = df['2019-12'].to_period('M')  # 获取2019年12月数据
# 按支出类别分组统计
df_month = df.groupby(['支出类别', '日期'])[['金额']].sum().reset_index()
# 按金额排序
df_month_sort = df_month[['支出类别', '金额']].sort_values(by='金额', ascending=False)
df_month_sort['占比'] = (df_month_sort['金额'] / df['金额'].sum()).apply(lambda x: format(x, '.2%'))
# 添加行索引
df_month_sort.index = [1, 2, 3, 4, 5, 6]
print('2019年12月总支出:', df_month['金额'].sum(), '元')
print(df_month_sort)
