import pygame
import time
import numpy as np

import paremter as pa

def draw_grid(screen):
    for x in range(0, pa.windows_width, pa.cell_size):  # draw 水平 lines
        pygame.draw.line(screen, pa.dark_gray, (x, 0), (x, pa.windows_height))
    for y in range(0, pa.windows_height, pa.cell_size):  # draw 垂直 lines
        pygame.draw.line(screen, pa.dark_gray, (0, y),(pa.windows_width, y))

fr = open("./map/map2",'r')
map_dic = eval(fr.read())   #读取的str转换为字典
print(map_dic)
fr.close()

pygame.init()  # 模块初始化
snake_speed_clock = pygame.time.Clock()  # 创建Pygame时钟对象
screen = pygame.display.set_mode((800, 600))
screen.fill(pa.black)
while True:
    draw_grid(screen)
    for i in range(len(map_dic)):
        map_block = pygame.Rect(map_dic[i]['x']*20, map_dic[i]['y']*20, pa.cell_size, pa.cell_size)
        pygame.draw.rect(screen, pa.white, map_block)
    pygame.display.update()
    time.sleep(10)
    break