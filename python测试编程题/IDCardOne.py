
'''
        22010520030705122x
    1.输入数字号码为18位
    2.数字7~10位数为出生年，11~12位为出生月，13-14 位为出生日期
    3.17位为性别：偶数为 女，奇数为男
    220105  2003     07    05      122x
    012345  6789    1011  1213   14151617

'''

idnum=input('请输入身份证号码\n')

if idnum[:16].isdigit() and len(idnum) ==18:
        print('你的生日是:'+idnum[6:10]+'年'+idnum[10:12]+'月'+idnum[12:14]+'日')
        gender01='女' if int(idnum[:16])%2==0 else '男'
        gender02=(int(idnum[:16])%2==0 and '女' or '男')
        #gender03=['女','男'][int(idnum[:16]%2==0)]
        gender04=(int(idnum[:16])%2==0 and ['女'] or ['男'])[0]
        print('你的性别1是:'+gender01)
        print('你的性别2是:'+gender02)
        #print('你的性别3是:'+gender03)
        print('你的性别4是:'+gender04)
else:
    print('{}输入的身份证号码有误'.format(idnum))

