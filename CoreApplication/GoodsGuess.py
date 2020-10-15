'''
    商品竞猜游戏
    1.用户可以选择竞猜商品,然后根据竞猜的商品竞猜价格
        小于指定数字的,提示'猜的价格小了...'
        大于指定数字的,提示'猜的价格大了...'
        输入的价格等于商品价格,提示'恭喜,猜对了！'
    2.重点知识点：
        isalnum()：判断所有字符都是数字或字母。
        isalpha()：判断所有字符都是字母。
        isdigit()：判断所有字符都是数字,并为整型数字。
        isspace()：判断所有字符都是空白字符、\t、\n、\r
'''
list = ['小米手环4', 209], ['荣耀手环5', 199], ['华为手环B5', 849], ['ZNNCO智能血压手环', 379]
order = 0
price = 0
print('数字竞猜游戏')
print('可以竞猜的商品如下：\n', '1', list[0][0], '\n 2', list[1][0], '\n 3', list[2][0], '\n 4', list[3][0])

number = input('请输入竞猜商品前的数字:')
if number.isdigit() == True:
    order = int(number)
    if order < 4 and order > 0:
        print('您选择的竞猜商品是：', list[order - 1][0])  # 商品名称
        price = list[order - 1][1]                       # 商品价格
guess = -1
while guess != price:
    guess = input("请输入竞猜价格(只能输入整数价格)：")
    if guess.isdigit() == True:
        guess = int(guess)
        if guess == price:
            print("恭喜,你猜对了！")
        elif guess < price:
            print("猜的价格小了...")
        elif guess > price:
            print("猜的价格大了...")
    else:
        print("输入价格非法,请重新输入！")
