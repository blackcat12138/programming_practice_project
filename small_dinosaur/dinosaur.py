'''
    实现谷歌小恐龙的游戏代码
'''
import pygame
from pygame.locals import *

SCREENWIDTH=822     # 窗体宽度
SCREENHEIGHT=260    # 窗体高度
FPS=30              # 更新画面的时间

def mainGame():
    score=0                 # 得分
    over=False
    global SCREEN,FPSCLOCK
    pygame.init()           # 经过初始化以后我们就可以尽情地使用pygame了
    # 使用pygame时钟之前，必须先创建Clock对象的一个实例
    # 控制每个循环多长时间运行一次
    FPSCLOCK=pygame.time.Clock()
    # 通常来说我们需要先创建一个窗体，方便我们与程序的交互
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('小恐龙')           # 设置窗体标题
    while True:
        # 判断是否单击了关闭窗体
        for event in pygame.event.get():
            # 如果单击了关闭窗体就将窗体关闭
            if event.type==QUIT:
                exit()              # 关闭窗体
    pygame.display.update()         # 更新整个窗体
    FPSCLOCK.tick(FPS)              # 循环应该多长时间运行一次

if __name__=='__main__':
    mainGame()