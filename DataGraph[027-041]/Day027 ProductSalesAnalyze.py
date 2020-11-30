'''
    [027]、双Y轴可视化分析产品销量增长速度及趋势
        1.根据mrbook_01.xlsx文件数据,DateFrame的两个列进行双Y轴画图,通过Y轴看出发展情况同时看出其增长速度,
            通过该图看出产品销量也可以看出产品销量增长趋势。
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/mrbook_01.xlsx')
x = [1, 2, 3, 4, 5, 6]
y1 = df['销量']
y2 = df['rate']
fig = plt.figure()
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 添加子图
ax1 = fig.add_subplot(111)
# 图表标题
plt.title('销量情况对比')
# 图表x轴标题
plt.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月'])
ax1.bar(x, y1, label='left')
# y轴标签
ax1.set_ylabel('销量（册）')
# 共享x轴添加一条y轴坐标轴
ax2 = ax1.twinx()
ax2.plot(x, y2,
         color='black',
         linestyle='--',
         marker='o',
         linewidth=2,
         label=u'增长率')
ax2.set_ylabel(u'增长率')
for a, b in zip(x, y2):
    plt.text(a, b + 0.02, '%.2f' % b, ha='center', va='bottom', fontsize=10, color='red')
plt.show()
