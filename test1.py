import pygame
import os
from pygame.locals import *
from paremter import *
from time import sleep

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,70)
screen = pygame.display.set_mode((windows_width, windows_height))
screen.fill(black)
font=pygame.font.Font('./font/myfont.ttf', 72)
mode1=font.render('闯关模式',True,white)
mode2=font.render('传统模式',True,white)
mode3=font.render('无尽模式',True,orange)
screen.blit(mode1,(285,100))
screen.blit(mode2,(285,250))
screen.blit(mode3,(285,400))

pygame.display.update()
sleep(5)