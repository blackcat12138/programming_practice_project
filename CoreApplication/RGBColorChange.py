'''
    RGB模式颜色转换器
    1.RGB-->R(red)、G(green)、B(blue)是三种颜色又称三原色,
        实现RGB模式的十进制颜色转成十六进制颜色,
        转换方法：将十进制的RGB颜色分别转成十六进制的数字然后按RGB的顺序连接即可
    2.重点知识点：
            hex()：将一个整数转换成16进制数。
        replace()：将原字符串替换成新字符串。
'''

print('RGB模式十进制颜色与十六进制颜色转换'.center(55))
print('=' * 60)


def rgbhex(rgbr, rgbg, rgbb):
    return hex(int(rgbr)).replace('0x', '') + \
           hex(int(rgbg)).replace('0x', '') + \
           hex(int(rgbb)).replace('0x', '')


r = input('请输入定位点RGB颜色值的R值,取值范围0--255！')
g = input('请输入定位点RGB颜色值的G值,取值范围0--255！')
b = input('请输入定位点RGB颜色值的B值,取值范围0--255！')
print('该定位点的16进制颜色值为', rgbhex(r, g, b))
