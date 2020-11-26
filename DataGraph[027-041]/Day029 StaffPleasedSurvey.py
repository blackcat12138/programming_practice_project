'''
    [029]、多图表实现员工满意度调查数据分析
    1.各项内容满意度分析,通过水平条形图体现,
        满意度分5个类别:很满意100分,满意80分,基本满意60分,不太满意30分,不满意0分
        其中某一项的满意率=(很满意人数*100+满意人数*80+基本满意人数*60+不太满意人数*30+不满意人数*0)/总人数
        程序使用图形化界面,图表嵌入窗体的思路:先将图表保存为图片,然后在显示
        通过Matplotlib模块设计饼形图、航向水平条形图和雷达图
'''
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.read_excel('E:/05_job src/programming_practice_project/DataGraph[027-041]/data/employee_data.xlsx')
main=tk()
main.title('员工满意度调查数据分析')
# 设置窗口的大小