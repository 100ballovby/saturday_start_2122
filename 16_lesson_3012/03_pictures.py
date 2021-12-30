import sys
import pygame as pg
from pygame.draw import *

pg.init()  # инициализирую окошко pygame
screen = pg.display.set_mode((500, 500))  # создаю окно с заданным размером
FPS = 30


def draw_tree(x, y, scr):
    rect(scr, (122, 94, 10), (x, y - 100, 50, 100))  # рисую ствол дерева шириной 50 и высотой 100 пикселей
    circle(scr, (21, 122, 10), (x + 25, y - 120), 50)


def draw_house(x, y, scr):
    # коробка дома
    rect(scr, (247, 168, 120), (x, y-100, 200, 100))
    # дверь
    rect(scr, (110, 82, 36), (x + 80, y - 60, 40, 60))
    # ручка двери
    circle(scr, (237, 213, 70), (x + 100, y - 30), 5)
    # крыша
    polygon(scr, (125, 125, 125), ((x - 20, y - 100),
                                   (x + 100, y - 250),
                                   (x + 220, y - 100)))


rect(screen, (201, 252, 255), (0, 0, 500, 400))  # рисую небо
rect(screen, (10, 103, 32), (0, 370, 500, 180))  # рисую землю

draw_house(150, 400, screen)
draw_tree(60, 400, screen)
draw_tree(400, 400, screen)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)  # обновляю экран по количеству кадров в секунду
    for event in pg.event.get():  # перебираю все возможные события
        if event.type == pg.QUIT:
            finished = True
            sys.exit()  # для грамотного закрытия окошка
