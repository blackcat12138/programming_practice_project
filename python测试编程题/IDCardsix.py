#-*-coding:GBK-*-
'''
    1.读取 birth.txt 文件中的身份证信息，并获取当前日期，生成未来生日提醒列表
    2.将生日在当前日期之后的身份证信息按生日日期(月、日)先后排序后依次输出(备注：身份证信息文件 birth.txt在tmp目录下)
    3.输出如下内容：
            当前日期:0927
            未来生日提醒列表
            10月09日
            ******196810098156
            10月11日
            ******196910117115
            10月15日
            ******194910152621
            11月04日
            ******195711045483
            11月05日
            ******198411055652

    ******195602082947
'''
#Python的默认编码格式是UTF-8 
import time
card=[]
bir=[]
with open('E:/06_workspace/jobspace/pythonDemo/tmp/birth.txt','r',encoding='UTF-8') as file:
    while True:
        line = file.readline().strip()
        if line =='':
            break
        card.append(line)
        bir.append(line[10:14])
bir = list(set(bir))
bir.sort(key=lambda x:int(x))
today=time.strftime('%m%d')
print(f"当前日期:{today}\n未来生日提醒列表")
for item  in bir:
    if int(item)>int(today):
        print(item[0:2]+"月"+item[2:4]+"日")
        for each in card:
            if each[10:14]==item:
                print(each)


