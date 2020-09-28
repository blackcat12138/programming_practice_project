'''

    1.输入数字号码为18位
    2.数字7~10位数为出生年，11~12位为出生月，13-14 位为出生日期
    3.17位为性别：偶数为 女，奇数为男
    4.数字前2位为所属省区信息.判断输入身份证号码省份的功能
    5.dic={'11':'北京市','12':'天津市','13':'河北省','14':'山西省','15':'内蒙古自治区
','22':'吉林省','23':'黑龙江省','31':'上海市', '32':'江苏省','33':'浙江省','35':'福建
省','36':'江西省','37':'山东省','41':'河南省','42':'湖北省','44':'广东省','45':'广西壮
族自治区','46':'海南省','50':'重庆市','51':'四川省','53':'云南省','54':'西藏自治区
','61':' 陕西省 ','62':' 甘肃省 ','63':' 青 海 省 ','65':' 新 疆 维 吾 尔 自 治 区 ','71':' 台 湾 省
','81':'香港','82':'澳门' }
    460000198403254566
'''

idnum=input('请输入身份证号码\n')

dic={'11':'北京市','12':'天津市','13':'河北省','14':'山西省','15':'内蒙古自治区',
     '22':'吉林省','23':'黑龙江省','31':'上海市', '32':'江苏省','33':'浙江省','35':'福建省',
     '36':'江西省','37':'山东省','41':'河南省','42':'湖北省','44':'广东省','45':'广西壮族自治区',
     '46':'海南省','50':'重庆市','51':'四川省','53':'云南省','54':'西藏自治区',
     '61':' 陕西省 ','62':' 甘肃省 ','63':' 青 海 省 ','65':' 新 疆 维 吾 尔 自 治 区 ','71':' 台 湾 省',
     '81':'香港','82':'澳门'}

if idnum[:16].isdigit() and len(idnum)==18:
    print('你来自:'+dic[idnum[:2]])
    print('你的生日是:'+idnum[6:10]+'年'+idnum[10:12]+'月'+idnum[12:14]+'日')
    gender02=(int(idnum[:16])%2==0 and '女' or '男')
    print('你的性别2是:'+gender02)
else:
    print('%s 输入的身份证号码有误',format(idnum))

