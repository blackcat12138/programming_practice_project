#-*-coding:GBK-*-
'''
    1.��ȡ birth.txt �ļ��е����֤��Ϣ������ȡ��ǰ���ڣ�����δ�����������б�
    2.�������ڵ�ǰ����֮������֤��Ϣ����������(�¡���)�Ⱥ�������������(��ע�����֤��Ϣ�ļ� birth.txt��tmpĿ¼��)
    3.����������ݣ�
            ��ǰ����:0927
            δ�����������б�
            10��09��
            ******196810098156
            10��11��
            ******196910117115
            10��15��
            ******194910152621
            11��04��
            ******195711045483
            11��05��
            ******198411055652

    ******195602082947
'''
#Python��Ĭ�ϱ����ʽ��UTF-8 
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
print(f"��ǰ����:{today}\nδ�����������б�")
for item  in bir:
    if int(item)>int(today):
        print(item[0:2]+"��"+item[2:4]+"��")
        for each in card:
            if each[10:14]==item:
                print(each)


