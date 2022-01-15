import pygame as pg
import sys  # работа с системными событиями
from pygame.draw import circle   # импортирую функцию рисования круга

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

# радиус круга
rad = 50
# координаты
x = 0 - rad  # круг появится за пределами экрана (слева)
y = 240  # середина экрана

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

    screen.fill(WHITE)  # заливаю экран
    circle(screen, ORANGE, (x, y), rad)  # рисую круг

    pg.display.update()  # обновляю кадры на экране

    # если круг окажется за правой границей экрана
    if x >= (640 + rad):
        # переместим круг влево
        x = 0 - rad
    else:
        x += 3


