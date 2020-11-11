'''
    [016]、摄氏温度和其他温度换算
    1.输入摄氏温度,将输出华氏温度、开氏温度、列氏温度、兰氏温度,
        输入温度时只能输入数字温度值,若输入非数字温度值,将提示'输入温度错误！'
'''
import unicodedata

print('=====================')
print("   摄氏温度转换器")
print("===================")
she = input('请输入摄氏温度：').strip('')


# 判断输入的数字是否为浮点数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


if is_number(she):
    she = 100               # 摄氏温度
    hua = she * 1.8 + 32    # 华氏温度
    kai = she + 273.15      # 开氏温度
    lie = she * 0.8         # 列氏温度
    lan = (she + 273.15) * 1.8  # 兰金温度

    print('摄氏温度：', she)
    print('华氏温度：', hua)
    print('开氏温度：', kai)
    print('列氏温度：', lie)
    print('兰金温度：', lan)
else:
    print('输入温度错误！')
