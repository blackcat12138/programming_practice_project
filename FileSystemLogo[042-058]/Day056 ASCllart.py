'''
    [056]、将图片变为字符画
    字符画是一系列字符组合成的文本,通过python将图片转化为字符画,图片可以是黑白片、彩色片。
    Pillow：处理图片的模块
'''
from PIL import Image

# 将图片中的像素转化对应的ASCll码
def get_char(r,g,b,a=256):
    if a==0:
        return ''
    gray=0.2126*r+0.7152*g+0.0722*b
    length=len(ascii_str)
    unit=256/length
    return ascii_str[int(gray/unit)]

if __name__ == "__main__":
    WIDTH = 80
    HEIGHT = 40
    ascii_str = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    im = Image.open('E:/05_job src/programming_practice_project/FileSystemLogo[042-058]/data/face.png')
    im = im.resize((WIDTH,HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i))) # (r,g,b,a)
        txt += '\n'

    print(txt)