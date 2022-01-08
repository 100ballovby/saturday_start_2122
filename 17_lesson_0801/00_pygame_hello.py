import pygame as pg
import sys  # работа с системными событиями


done = False  # окно не закрыто
screen = pg.display.set_mode((640, 480))  # создаю окно с определенным размером
clock = pg.time.Clock()  # счетчик кадров

# обновление кадров (они могут сменяться)
pg.display.update()
while not done:  # пока окно не закрыто
    clock.tick(30)  # обновляю экран 30 кадров/сек
    for event in pg.event.get():  # для каждого происходящего события
        if event.type == pg.QUIT:  # если нажать на крестик
            done = True  # работа окончена
            sys.exit()  # система должна закрыть окно программы

