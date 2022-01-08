import pygame as pg
from pygame.draw import rect, circle, polygon  # функции для рисования круга и квадрата
import sys  # работа с системными событиями


done = False  # окно не закрыто
screen = pg.display.set_mode((640, 480))  # создаю окно с определенным размером
clock = pg.time.Clock()  # счетчик кадров

rect(screen, '#a8b6e3', [100, 200, 120, 120])
rect(screen, '#42aaff', [95, 195, 130, 130], 5)
# поверхность, цвет, [x, y, ширина, высота], толщина_контура

#polygon(screen, 'white', [[210, 210], [180, 310], [310, 310], [340, 210]])

circle(screen, '#8360a8', [400, 400], 70)
circle(screen, '#cf59b1', [250, 320], 50, 5)
# поверхность, цвет, [х, y], диаметр, толщина линии

# обновление кадров (они могут сменяться)
pg.display.update()
while not done:  # пока окно не закрыто
    clock.tick(30)  # обновляю экран 30 кадров/сек
    for event in pg.event.get():  # для каждого происходящего события
        if event.type == pg.QUIT:  # если нажать на крестик
            done = True  # работа окончена
            sys.exit()  # система должна закрыть окно программы

