# 导入相关模块
import random
import sys
import time

import numpy as np
import pygame
from pygame.locals import *

from paremter import *


# 游戏运行主体
def running_game(screen, snake_speed_clock, snake_map, mode):
    food = {'x': 0, 'y': 0, 'type': normal}
    special_effcet = {'cut': False, 'cross': False}
    direction = [RIGHT]  # 开始方向
    score = [0]
    snake_coords = [{'x': 3, 'y': 1},  # 初始贪吃蛇坐标
                    {'x': 2, 'y': 1},
                    {'x': 1, 'y': 1}]
    food_generation(snake_coords, snake_map, food,
                    special_effcet, mode)  # 食物随机位置
    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./sound/TheBlueDanube.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while True:
        get_dirction(direction)
        move_snake(direction, snake_coords)  # 移动蛇
        snake_is_eat_food(snake_coords, snake_map, food, score,
                          special_effcet, mode)  # 判断蛇是否吃到食物

        alive = snake_is_alive(snake_coords, direction,
                               snake_map, special_effcet, score)
        if not alive:
            pygame.mixer.music.stop()
            return (dead, score[0])
        if len(snake_coords) >= 30 and mode==break_through:
            return (change_map, score[0])

        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_snake(screen, snake_coords)
        draw_map(screen, snake_map)
        draw_food(screen, food)
        draw_info(snake_coords, screen, score, special_effcet)
        pygame.display.update()
        snake_speed_clock.tick(snake_speed)  # 控制fps


# 获取前进方向
def get_dirction(direction):
    for event in pygame.event.get():  # 接收方向指令
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and direction[-1] != RIGHT and direction[-1] != LEFT:
                direction.append(LEFT)
            elif (event.key == K_RIGHT or event.key == K_d) and direction[-1] != LEFT and direction[-1] != RIGHT:
                direction.append(RIGHT)
            elif (event.key == K_UP or event.key == K_w) and direction[-1] != DOWN and direction[-1] != UP:
                direction.append(UP)
            elif (event.key == K_DOWN or event.key == K_s) and direction[-1] != UP and direction[-1] != DOWN:
                direction.append(DOWN)
            elif event.key == K_ESCAPE:
                terminate()
        if len(direction) > 3:
            return


# 将食物画出来
def draw_food(screen, food):
    x = food['x'] * cell_size
    y = food['y'] * cell_size
    food_block = pygame.Rect(x, y, cell_size, cell_size)
    if food['type'] == normal:
        pygame.draw.rect(screen, red, food_block)
    elif food['type'] == cut:
        pygame.draw.rect(screen, light_blue, food_block)
    elif food['type'] == cross:
        pygame.draw.rect(screen, orange, food_block)


# 将贪吃蛇画出来
def draw_snake(screen, snake_coords):
    # 画蛇身
    for coord in snake_coords:
        x = coord['x'] * cell_size
        y = coord['y'] * cell_size
        body_block = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, dark_blue, body_block)
        body_inner_block = pygame.Rect(
            x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(screen, blue, body_inner_block)
    # 画蛇头
    xhead = snake_coords[HEAD]['x'] * cell_size
    yhead = snake_coords[HEAD]['y'] * cell_size
    head_block = pygame.Rect(xhead, yhead, cell_size, cell_size)
    pygame.draw.rect(screen, dark_green, head_block)
    head_inner_block = pygame.Rect(
        xhead + 4, yhead + 4, cell_size - 8, cell_size - 8)
    pygame.draw.rect(screen, green, head_inner_block)


# 画地图
def draw_map(screen, snake_map):
    for obstruct in snake_map:
        x = obstruct['x'] * cell_size
        y = obstruct['y'] * cell_size
        obs_block = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, gray, obs_block)
        obs_inner_block = pygame.Rect(
            x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(screen, white, obs_inner_block)


# 画网格(可选)
def draw_grid(screen):
    for x in range(0, windows_width, cell_size):  # draw 水平 lines
        pygame.draw.line(screen, dark_gray, (x, 0), (x, windows_height))
    for y in range(0, windows_height, cell_size):  # draw 垂直 lines
        pygame.draw.line(screen, dark_gray, (0, y), (windows_width, y))


# 画信息
def draw_info(snake_coords, screen, score, special_effcet):
    # 右上角画成绩
    font = pygame.font.Font('./font/myfont.ttf', 30)
    score_surf = font.render('得分: %s' % score[0], True, green)
    score_rect = score_surf.get_rect()
    score_rect.topleft = (windows_width - 140, 10)
    screen.blit(score_surf, score_rect)
    # 和长度
    length_surf = font.render('长度: %s' % len(snake_coords), True, green)
    length_rect = length_surf.get_rect()
    length_rect.topleft = (windows_width - 280, 10)
    screen.blit(length_surf, length_rect)
    # 左上角画特效
    if special_effcet['cut'] == True:
        font = pygame.font.Font('./font/myfont.ttf', 15)
        tip = font.render('CUT', True, (65, 105, 225))
        screen.blit(tip, (30, 10))
    if special_effcet['cross'] == True:
        font = pygame.font.Font('./font/myfont.ttf', 15)
        tip = font.render('CROSS', True, (65, 105, 225))
        screen.blit(tip, (20, 25))


# 移动贪吃蛇
def move_snake(direction, snake_coords):
    if len(direction) != 1:
        direction.pop(0)
    if direction[0] == UP:
        newHead = {'x': snake_coords[HEAD]['x'] % map_width,
                   'y': (snake_coords[HEAD]['y'] - 1) % map_height}
    elif direction[0] == DOWN:
        newHead = {'x': snake_coords[HEAD]['x'] % map_width,
                   'y': (snake_coords[HEAD]['y'] + 1) % map_height}
    elif direction[0] == LEFT:
        newHead = {'x': (snake_coords[HEAD]['x'] - 1) % map_width,
                   'y': snake_coords[HEAD]['y'] % map_height}
    elif direction[0] == RIGHT:
        newHead = {'x': (snake_coords[HEAD]['x'] + 1) % map_width,
                   'y': snake_coords[HEAD]['y'] % map_height}

    snake_coords.insert(0, newHead)


# 判断蛇死了没
def snake_is_alive(snake_coords, direction, snake_map, special_effcet, score):
    flag = True
    # 蛇撞墙
    for obs in snake_map:
        if snake_coords[HEAD]['x'] == obs['x'] and snake_coords[HEAD]['y'] == obs['y']:
            flag = False
    # 蛇撞自己
    for snake_body in snake_coords[1:]:
        if snake_body['x'] == snake_coords[HEAD]['x'] and snake_body['y'] == snake_coords[HEAD]['y']:
            # 切断特效 加切断身体节数的分
            if special_effcet['cut'] == True:
                pre_length = len(snake_coords)
                del snake_coords[snake_coords.index(snake_body, 1):]
                sur_length = len(snake_coords)
                special_effcet['cut'] = False
                score[0] += pre_length-sur_length
                break
            # 跨越特效 减10分
            elif special_effcet['cross'] == True:
                special_effcet['cross'] = False
                direction.insert(1, direction[0])
                score[0] -= 10
                break
            # 无特效 死
            else:
                flag = False
    return flag


# 判断贪吃蛇是否吃到食物
def snake_is_eat_food(snake_coords, snake_map, food, score, special_effcet, mode):
    if snake_coords[HEAD]['x'] == food['x'] and snake_coords[HEAD]['y'] == food['y']:
        if food['type'] == cut:
            special_effcet['cut'] = True
        elif food['type'] == cross:
            special_effcet['cross'] = True
        score[0] += 1
        food_generation(snake_coords, snake_map, food,
                        special_effcet, mode)  # 食物重新生成
    else:
        del snake_coords[-1]  # 如果没有吃到食物, 就删掉尾部一格


# 食物生成
def food_generation(snake_coords, snake_map, food, special_effcet, mode):
    # 寻找空位置
    coord = np.ones((map_width, map_height), dtype=np.bool)
    for sc in snake_coords:
        coord[sc['x'], sc['y']] = 0
    for obs in snake_map:
        coord[obs['x'], obs['y']] = 0
    empty_place = np.nonzero(coord)
    # 于空位置随机生成果实
    p = random.randint(0, len(empty_place[0]))
    food['x'] = empty_place[0][p]
    food['y'] = empty_place[1][p]
    # 果实种类控制
    type_ctrl = random.randint(0, 50)
    if type_ctrl < 6:
        if special_effcet['cut'] == False and type_ctrl % 2 == 0 and mode != classic:
            food['type'] = cut
        elif special_effcet['cross'] == False and type_ctrl % 2 == 1 and mode != classic:
            food['type'] = cross
        else:
            food['type'] = normal
    else:
        food['type'] = normal


# 程序终止
def terminate():
    pygame.quit()
    sys.exit()
