'''
    [028]、堆叠柱形图分析用户体验效果
    1.根据mrtb_data.xlsx文件数据,通过堆叠柱形图反映出不同产品、不同人群的体验效果。

        pip install pandas
        pip install matplotlib
        pip install seaborn

'''
import matplotlib.pyplot as ply
import seaborn as sns
import pandas as pd
import numpy as np

# 1.通过pandas模块对Excel数据进行处理,计算男女比例和他们消费总额
sns.set_style('darkgrid')
file = 'E:/05_job src/programming_practice_project/DataGraph[027-041]/data/mrtb_data.xlsx'
df = pd.DataFrame(pd.read_excel(file))
ply.rc('font', family='SimHei', size=13)
# 通过reset_index()函数将groupby()的分组结果重新设置索引
df1 = df.groupby(['类别'])['买家实际支付金额'].sum()
df2 = df.groupby(['类别', '性别'])['买家会员名'].count().reset_index()
men_df = df2[df2['性别'] == '男']
women_df = df2[df2['性别'] == '女']
men_list = list(men_df['买家会员名'])
women_list = list(women_df['买家会员名'])
# 消费金额
num = np.array(list(df1))
# 计算男性用户比例
ratio = np.array(men_list) / (np.array(men_list) + np.array(women_list))
# 使用set_printoptions设置输出的精度
np.set_printoptions(precision=2)
# 设置男女消费金额
men = num * ratio
women = num * (1 - ratio)
# 去除类别重复的记录
df3 = df2.drop_duplicates(['类别'])
name = (list(df3['类别']))
# 2.生成图表
x = name
width = 0.5
idx = np.arange(len(x))
ply.bar(idx, men, width, color='slateblue', label='男性用户')
ply.bar(idx, women, width, bottom=men, color='orange', label='女性用户')
ply.xlabel('消费类别')
ply.ylabel('男女分布')
ply.xticks(idx + width / 2, x, rotation=20)
# 在图表上显示数字
for a, b in zip(idx, men):
    # 对齐方式'top','bottom','center','baseline','center_baseline'
    ply.text(a, b, '%.0f' % b, ha='center', va='top', fontsize=12)
for a, b, c in zip(idx, women, men):
    ply.text(a, b + c + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12)
ply.legend()
ply.show()
