'''
    [015]、验证输入的IP地址是否正确
    1.实例描述
        ip地址一般为0~255间的整数,并且提供了子网掩码,即255.255.255.0为备用地址。
        实现对用户输入的ip地址判断（判断输入的ip地址最高位不能超过255，最低位不能低于零）
        当输入正确的ip地址时，打印'输出ip地址输入正确';
        当输入错误的ip地址是，打印'ip地址段输入大于255或小于0错误,将退出';
        当输入的ip地址段不足4段出错，打印'ip地址输入多于或少于4段地址错误,将退出'
'''
# 设置判断网址是否正确的标志变量为真
cause = False
ip = input('请输入IP地址：\n').strip(' ')
line = ip.split('.')
# 若果网址按'.'分为4段
if len(line) == 4:
    # 对网址各段进行判断
    for item in line:
        # 是否为数字
        if item.isdigit():
            if int(item) > 255 or int(item) < 0:
                print('ip地址段输入大于255或小于0错误,将退出!!')
                # 网址错误,判断网址标志变量为假
                cause = False
                break
        else:
            print('ip地址段输入非数字错误（只能输入数字或.）,将退出!!')
            cause = False
            break
    if cause == True:
        print('ip地址输入正确！！')
else:
    print('ip地址输入多于或少于4段地址错误,将退出!!')
