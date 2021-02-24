'''
    [043]、用python实现文件对比分析并生成报告
    1.通过python实现文件对比分析并生成报告,通过单击"选择文件"按钮选择需对比的文件,
        单击"文件对比"按钮自动生成文件对比分析报告,改文件将保存在程序所在路径下。
        在两个文件对比后,内容不同的地方用红色标记。
    2.核心技术模块
        difflib模块：对比文本、文件间的差异,并可输出html格式的对比分析结果报告,
                     也可使用对比代码和配置文件的差异。
        difflib.HtmlDiff()：创建一个html表格，用来展示文件差异。
        tkinter模块：python自带的gui库,是对图形库tk的封装。
        tkinter.filedialog.askopenfilename()：以选择文件对话框的格式打开和保存图片
'''
# 1.导入模块
import difflib
import tkinter as tk
import tkinter.filedialog


# 2.定义选择文件函数,tk.filedialog.askopenfilename():选择打开什么文件，返回文件名
def button1():
    global file1
    file1 = tk.filedialog.askopenfilename()
    txt_path1.set(file1)


def button2():
    global file2
    file2 = tk.filedialog.askopenfilename()
    txt_path2.set(file2)


# 3.定义对比文件的函数,主要通过difflib.HtmlDiff()方法实现
def Diff():
    with open(file1) as f1, open(file2) as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()
        d = difflib.HtmlDiff()
    with open('result1.html', 'w') as f:
        f.write(d.make_file(text1, text2))


# 4.设计主窗口
# 建立主窗口window
windos = tk.Tk()
# 设置窗口标题栏名称
windos.title('用python实现文件对比分析')
# 设置窗口的大小
windos.geometry('650x200')
# 在主窗口添加标签
label = tk.Label(windos, text='请选择需要对比的文件：', fg='blue', font=('Arial', 12)).place(x=30, y=30)
l1 = tk.Label(windos, text='原 文 件', font=('Arial', 12)).place(x=30, y=80)
l2 = tk.Label(windos, text='目标文件：', font=('Arial', 12)).place(x=30, y=110)
# 在主窗口添加文本框
txt_path1 = tk.StringVar()
text1 = tk.Entry(windos, textvariable=txt_path1, show=None, width=60)
txt_path2 = tk.StringVar()
text2 = tk.Entry(windos, textvariable=txt_path2, show=None, width=60)
text1.place(x=120, y=80)
text2.place(x=120, y=110)
# 在主窗口添加命令按钮
button1 = tk.Button(windos, width=8, height=1, text='选择文件', bg='skyblue', command=button1).place(x=550, y=80)
button2 = tk.Button(windos, width=8, height=1, text='选择文件', bg='skyblue', command=button2).place(x=550, y=110)
button3 = tk.Button(windos, width=20, height=1, text='文件对比', fg='red', bg='orange', command=Diff).place(x=220, y=150)
# 主窗口循环显示
windos.mainloop()
