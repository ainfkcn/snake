import pygame
import os
from time import sleep

from paremter import *
from snake import *


def read_map(map_num):
    maps = ['./map/map0', './map/map1',
            './map/map2', './map/map3', './map/map4']
    fr = open(maps[map_num], 'r')
    snake_map = list(eval(fr.read()))
    fr.close()
    return snake_map


def main():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 70)
    snake_speed_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((windows_width, windows_height))
    screen.fill(white)
    pygame.display.set_caption("Fruit Snake")
    while True:
        game_mode = start_screen(screen)
        map_num = 0
        if game_mode == break_through:
            while map_num < 5:
                snake_map = read_map(map_num)
                (how_end, score) = running_game(
                    screen, snake_speed_clock, snake_map, game_mode)
                map_num += 1
                if how_end == dead:
                    if gameover(screen, score) == 0:  # 返回主界面
                        break
                    map_num = 0
            if how_end != dead:
                game_clear(screen, score) == 0
        elif game_mode == classic or game_mode == endless:
            while True:
                snake_map = read_map(0)
                (how_end, score) = running_game(
                    screen, snake_speed_clock, snake_map, game_mode)
                if how_end == dead:
                    if gameover(screen, score) == 0:  # 返回主界面
                        break


# 开始信息显示
def start_screen(screen):
    while True:
        # 获取鼠标位置显示按钮
        pos = pygame.mouse.get_pos()
        (mouse_x, mouse_y) = (pos[0], pos[1])
        if 297 <= mouse_x <= 297+403 and 331 <= mouse_y <= 331+80:
            button = pygame.image.load('./pic/button1.png')
            screen.blit(button, (0, 0))
            pygame.display.update()
        elif 297 <= mouse_x <= 297+403 and 430 <= mouse_y <= 430+80:
            button = pygame.image.load('./pic/button2.png')
            screen.blit(button, (0, 0))
            pygame.display.update()
        elif 296 <= mouse_x <= 296+403 and 524 <= mouse_y <= 524+80:
            button = pygame.image.load('./pic/button3.png')
            screen.blit(button, (0, 0))
            pygame.display.update()
        else:
            gamestart = pygame.image.load('./pic/gamestart.png')
            screen.blit(gamestart, (1, 0))
            pygame.display.update()

        # 获取键盘鼠标输入
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_q:
                    pass
            elif event.type == MOUSEBUTTONDOWN:
                if 297 <= mouse_x <= 297+403 and 331 <= mouse_y <= 331+80:
                    a = mode_select(screen)
                    if a in [break_through, classic, endless]:
                        return a
                elif 297 <= mouse_x <= 297+403 and 430 <= mouse_y <= 430+80:
                    show_help(screen)
                elif 296 <= mouse_x <= 296+403 and 524 <= mouse_y <= 524+80:
                    high_score(screen, read)


def mode_select(screen):
    screen.fill(black)
    while True:
        # 鼠标指向变色
        pos = pygame.mouse.get_pos()
        (mouse_x, mouse_y) = (pos[0], pos[1])
        if 285 <= mouse_x <= 285+235 and 100 <= mouse_y <= 100+76:
            font = pygame.font.Font('./font/myfont.ttf', 72)
            mode_button1 = font.render('闯关模式', True, orange)
            screen.blit(mode_button1, (285, 100))
            pygame.display.update()
        elif 285 <= mouse_x <= 285+235 and 250 <= mouse_y <= 250+76:
            font = pygame.font.Font('./font/myfont.ttf', 72)
            mode_button2 = font.render('传统模式', True, orange)
            screen.blit(mode_button2, (285, 250))
            pygame.display.update()
        elif 285 <= mouse_x <= 285+235 and 400 <= mouse_y <= 400+76:
            font = pygame.font.Font('./font/myfont.ttf', 72)
            mode_button3 = font.render('无尽模式', True, orange)
            screen.blit(mode_button3, (285, 400))
            pygame.display.update()
        elif 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
            font = pygame.font.Font('./font/myfont.ttf', 40)
            return_button1 = font.render('返回主界面', True, orange)
            screen.blit(return_button1, (630, 550))
            pygame.display.update()
        else:
            font = pygame.font.Font('./font/myfont.ttf', 40)
            return_button = font.render('返回主界面', True, white)
            screen.blit(return_button, (630, 550))
            font = pygame.font.Font('./font/myfont.ttf', 72)
            mode_button1 = font.render('闯关模式', True, white)
            screen.blit(mode_button1, (285, 100))
            mode_button2 = font.render('传统模式', True, white)
            screen.blit(mode_button2, (285, 250))
            mode_button3 = font.render('无尽模式', True, white)
            screen.blit(mode_button3, (285, 400))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_q:
                    return
            elif event.type == MOUSEBUTTONDOWN:
                if 285 <= mouse_x <= 285+235 and 100 <= mouse_y <= 100+76:
                    return break_through
                elif 285 <= mouse_x <= 285+235 and 250 <= mouse_y <= 250+76:
                    return classic
                elif 285 <= mouse_x <= 285+235 and 400 <= mouse_y <= 400+76:
                    return endless
                elif 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
                    return


def show_help(screen):
    while True:
        pos = pygame.mouse.get_pos()
        (mouse_x, mouse_y) = (pos[0], pos[1])
        if 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
            return_button1 = font.render('返回主界面', True, orange)
            screen.blit(return_button1, (630, 550))
            pygame.display.update()
        else:
            screen.fill(black)
            font = pygame.font.Font('./font/myfont.ttf', 28)
            help_lines = [
                '1.键位',
                '  使用上下左右或者WASD键控制蛇的前进方向，ESC键退出，',
                '  按Q退回主界面；死亡后，按R或空格键重新开始。',
                '2.果实及效果',
                '  果实分为三类，普通：红色；切断：浅蓝；跨越：土黄。',
                '  全部果实吃到时加1分，已获得的特效在左上角显示',
                '  切断：会从身体交叉处切断蛇身，触发时加切断节数的分；',
                '  跨越：可以交叉一次身体而不死，触发时减10分。',
                '3.游戏模式',
                '  闯关模式：身长达到30时自动切换地图且身长初始化，地图共五张',
                '  经典模式：只有普通果实、一张地图',
                '  无尽模式：三种果实都有，但只有一张地图']
            for i in range(0, len(help_lines)):
                help_line = font.render(help_lines[i], True, green)
                screen.blit(help_line, (30, 20+35*i))

            font = pygame.font.Font('./font/myfont.ttf', 40)
            return_button = font.render('返回主界面', True, white)
            screen.blit(return_button, (630, 550))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_q:
                    return
            elif event.type == MOUSEBUTTONDOWN:
                if 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
                    return


# 记录及显示最高分
def high_score(screen, mode, score=0):
    try:
        score_file = open('./score.tcs', 'r')
        scores = score_file.readlines()
        for i in range(0, len(scores)):
            scores[i] = int(scores[i].strip())

    except:
        score_file = open('./score.tcs', 'w')
        score_file.close()
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if mode == write:
        scores.append(score)
        scores.sort(reverse=True)
        if 0 in scores:
            scores.remove(0)
        else:
            scores.pop(-1)
        score_file = open('./score.tcs', 'w')
        for ele in scores:
            print(ele, file=score_file)
        score_file.close()
    elif mode == read:
        while True:
            pos = pygame.mouse.get_pos()
            (mouse_x, mouse_y) = (pos[0], pos[1])
            if 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
                return_button1 = font.render('返回主界面', True, orange)
                screen.blit(return_button1, (630, 550))
                pygame.display.update()
            else:
                screen.fill(black)
                font = pygame.font.Font('./font/myfont.ttf', 30)
                for i in range(0, 10):
                    record = font.render(
                        '%d、 %d' % (i+1, scores[i]), True, green)
                    screen.blit(record, (30, 20+35*i))

                font = pygame.font.Font('./font/myfont.ttf', 40)
                return_button = font.render('返回主界面', True, white)
                screen.blit(return_button, (630, 550))
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    elif event.key == K_q:
                        return
                elif event.type == MOUSEBUTTONDOWN:
                    if 630 <= mouse_x <= 790 and 550 <= mouse_y <= 590:
                        return


# 游戏结束信息显示
def gameover(screen, score):
    # 播放死亡音效
    pygame.mixer.init()
    sound=pygame.mixer.Sound('./sound/gameover.wav')
    sound.play()
    # 显示死亡信息
    font = pygame.font.Font('./font/myfont.ttf', 40)
    tip1 = font.render('按Q返回主界面,ESC退出', True, (65, 105, 225))
    tip2 = font.render('R或者SPACE重新开始游戏', True, (65, 105, 225))
    game_over = pygame.image.load('./pic/gameover.png')
    screen.blit(game_over, (0, 0))
    screen.blit(tip1, (220, 475))
    screen.blit(tip2, (205, 525))
    pygame.display.update()
    # 记载最高分
    high_score(screen, write, score)
    # 键盘监听事件
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_q:
                    return 0
                elif event.key == K_r or event.key == K_SPACE:
                    return


# 闯关成功
def game_clear(screen, score):
    pygame.mixer.music.stop()
    font = pygame.font.Font('./font/myfont.ttf', 72)
    test1 = font.render('恭喜通关', True, red)
    screen.blit(test1, (285, 250))
    font = pygame.font.Font('./font/myfont.ttf', 40)
    tip1 = font.render('按Q返回主界面,ESC退出', True, (65, 105, 225))
    screen.blit(tip1, (220, 525))
    pygame.display.update()
    # 记载最高分
    high_score(screen, write, score)
    # 键盘监听事件
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_q:
                    return


if __name__ == "__main__":
    main()
