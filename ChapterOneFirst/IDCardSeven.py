#-*-coding:GBK-*-
'''
    1.ʵ�ָ�����������֤��������������������Ӧ���������֤��Ϣ
    2.���֤��ʡ�е�������(���֤ǰ 6 λ)�ļ� sfz.txt
    3.�����ӡ�����
        ======���֤��������ϵͳ======
        ******************************
        ������Ҫ���ɵ����֤����������5
         341203200105042659
         360222198610211283
         411723195803088222
         140426199805074248
         140212199104211291
         370203199812069132

    4.��غ�����
        random.choice()����ָ��������ѡȡһ�����ѡ���Ԫ�ء�
        random.randint()������ָ����Χ�����ⷶΧ�����������
         time.strftime()����ȡ��ǰ����ʱ�䡣
                 zfill()������ָ�����ȵ��ַ�����ԭ�ַ����Ҷ��룬ǰ�����0��

'''
import random
import time

card = []
def opefile():
    # 1.��ȡsfz.txt�ļ�ÿ�����ݵ�ǰ7λ���֣�����Ϊ��������
    with open('E://06_workspace//jobspace//pythonDemo//tmp//sfz.txt', 'r', encoding='UTF-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            card.append(line[0:7])

def region():
    # 2.���ѡȡcard�б��е�Ԫ��
    opefile
    first = random.choice(card)
    #print(first)
    return first

def birth():
    # 3.������ɳ���������
    now = time.strftime('%Y')
    year = str(random.randint(1948, int(now) - 15))
    month = str(random.randint(1, 12)).zfill(2)
    if month in ["1", "3", "5", "7", "8", "10", "12"]:
        day = random.randint(1, 32)
    elif month in ["4", "6", "9", "11"]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 29)
    day = str(day).zfill(2)
    return year + month + day

def order():
    # 4.����������֤�ĺ�4λ��
    randis = str(random.randint(1, 9999)).zfill(4)
    return randis

def main():
     rancard = region() + birth() + order()
     print('������ɵ����֤����Ϊ��' + rancard)
opefile()
print("======���֤��������ϵͳ======")
print("*" * 30)
count = int(input("������Ҫ���ɵ����֤����������"))
for i in range(count + 1):
    rancard = region() + birth() + order()
    print(rancard)
