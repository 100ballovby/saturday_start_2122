import sys
import pygame as pg
from pygame.draw import *

pg.init()  # инициализирую окошко pygame
screen = pg.display.set_mode((500, 500))  # создаю окно с заданным размером
FPS = 30

# здесь будем рисовать

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)  # обновляю экран по количеству кадров в секунду
    for event in pg.event.get():  # перебираю все возможные события
        if event.type == pg.QUIT:
            finished = True
            sys.exit()  # для грамотного закрытия окошка
