'''
    [033]、可视化分析日常记账数据总结个人消费方向
        1.根据accounts_03.xlsx文件中的消费数据,实现日常消费数据的分析。
'''
import matplotlib.pyplot as ply
import pandas as pd

# 1.DataFrame输出数据对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 2.获取Excel数据
df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/accounts_03.xlsx')
# 设置索引,按月份显示数据
df = df.set_index('日期', drop=True)
# 获取2019年12月数据
df = df['2019-12'].to_period('M')
# 3.按支出类别和日期分组统计数据
# 按支出类别分组统计
df_month = df.groupby(['支出类别', '日期'])[['金额']].sum().reset_index()
# 按金额排序
df_month_sort = df_month[['支出类别', '金额']].sort_values(by='金额', ascending=True)
# 添加行索引
df_month_sort.index = [1, 2, 3, 4, 5, 6]
print('2019年12月总支出:', df_month['金额'].sum(), '元')
print('我最爱把钱花在')
print(df_month_sort.rename(columns={'支出类别': ",'金额':"}))
# 4.绘制环形图表
ply.rcParams['font.sans-serif'] = ['SimHei']
ply.rcParams['axes.unicode_minus'] = False
labels = df_month_sort['支出类别'].values.tolist()
data_percent = df_month_sort['金额'].values.tolist()
colors = ['c', 'r', 'y', 'g', 'gray', 'b']
wedges1, texts1, autotexts1 = ply.pie(data_percent,
                                      autopct='%3.1f%%',
                                      radius=1,
                                      pctdistance=0.85,
                                      colors=colors,
                                      startangle=180,
                                      textprops={'color': 'w'},
                                      wedgeprops={'width': 0.4, 'edgecolor': 'w'})
# 图例
ply.legend(wedges1,
           labels,
           fontsize=12,
           loc='center right',
           borderaxespad=0.,
           frameon=False,
           bbox_to_anchor=(1.3, 0.6))
# 设置文本样式
ply.setp(autotexts1, size=12, weight='bold')
ply.setp(texts1, size=10)
# 标题
ply.title('我最爱把钱花在', fontsize=20)
ply.show()
