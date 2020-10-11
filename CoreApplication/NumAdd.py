'''
    1.制作简易的数字累加器,累加的数字数据进行累加计算.
        即输入数字进行累加计算,按下Enter或Q键退出程序.
    2.重要知识点：
       unicodedata.numeric(char,default)：将数字的字符串转换成浮点数返回,若不合法的字符串将抛出异常ValueError
            例：print(unicodedata.numeric('四',None)) --> 4.0
                        format(x,'.2f')：将数字保留2位小数.以下写法都是一样的
                            '{:.2%}'.format(x)
                             '{.2%}'.format(x)
'''

all = 0.0
alladd = 0.0


# 累加两个整数
def add(addin, data):
    addone = 0
    addone = addin + data
    return addone


# 判断数字是否为浮点数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


while True:
    indig = input('输入：').strip('')
    if indig == 'q' or indig == 'Q':
        break
    elif is_number(indig) == True:
        alladd = add(float(all), float(indig))
        all = format(alladd, '.3f')
        print(all)
    else:
        print('输入了非数字,请重新输入！')
