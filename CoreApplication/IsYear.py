'''
    1.实现根据输入出生年月日判断输出对应的生肖
'''
lunar = '子丑寅卯辰巳午未申酉戌亥'
zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
ztime = ['1936(1.24)', '1937(2.11)', '1938(1.31)', '1939(2.19)', '1940(2.08)', '1941(1.27)',
         '1942(2.15)', '1943(2.05)', '1944(1.25)', '1945(2.13)', '1946(2.02)', '1947(1.22)',
         '1948(2.10)', '1949(1.29)', '1950(2.17)', '1951(2.00)', '1952(1.27)', '1953(2.14)',
         '1954(2.03)', '1955(1.24)', '1956(2.12)', '1957(1.31)', '1958(2.18)', '1959(2.08)',
         '1960(1.28)', '1961(2.25)', '1962(2.05)', '1963(1.25)', '1964(2.13)', '1965(2.02)',
         '1966(1.21)', '1967(2.09)', '1968(1.30)', '1970(2.06)', '1971(1.27)', '1972(2.15)',
         '1973(2.03)', '1974(1.23)', '1975(2.11)', '1976(1.31)', '1977(2.18)', '1978(2.07)',
         '1979(1.28)', '1980(2.16)', '1981(2.05)', '1982(1.25)', '1983(2.13)', '1984(2.02)',
         '1985(2.20)', '1986(2.09)', '1987(1.29)', '1988(2.17)', '1989(2.06)', '1990(1.27)',
         '1991(2.15)', '1992(2.04)', '1993(1.23)', '1994(2.10)', '1995(1.31)', '1996(2.19)',
         '1997(2.07)', '1998(1.28)', '1999(2.16)', '2000(2.05)', '2001(1.24)', '2002(2.12)',
         '2003(2.01)', '2004(1.22)', '2005(2.09)', '2006(1.29)', '2007(2.18)', '2008(2.07)',
         '2009(1.26)', '2010(2.14)', '2011(2.03)', '2012(1.23)', '2013(2.10)', '2014(2.04)',
         '2015(2.19)', '2016(2.08)', '2017(1.28)', '2018(2.16)', '2019(2.05)', '2020(1.25)']

birth = input('请输入你的出生年月日,格式为：2000-12-21\n')
cbir = birth.split('-')
cyear = cbir[0]
cmonth = cbir[1]
cdate = cbir[2]
for item in ztime:
    if item[:4] == cyear:
        mdate = item.split('(')         # ['2017','1.28)']
        time = mdate[1].strip(')')      # ['1.28']
        ndate = time.split('.')         # ['1','28']
        smonth = ndate[0]               # ['1']
        sdate = ndate[1]                # ['28']
        break
stime = str(smonth) + str(sdate)        # [128]
ctime = str(cmonth) + str(cdate)        # [112]
if int(ctime) < int(stime):             # 112 < 128
    cyear = int(cyear) - 1              # 2020-1 -->2019
rem = int(cyear) % 12                   # 3
print('要查询的属相是：' + zodiac[rem] + '\n属相对应的年份为：' + lunar[rem] + '年')
