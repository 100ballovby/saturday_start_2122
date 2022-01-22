import pygame as pg
from pygame.draw import rect

BLUE = (120, 84, 240)
RED = (240, 84, 84)
GREEN = (74, 224, 74)
S_WIDTH = 640
S_HEIGHT = 480

done = False

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Snake Game v.1')  # название окна
clock = pg.time.Clock()

x_change = 0  # то, насколько изменяются координаты змеи
y_change = 0  # то, насколько изменяются координаты змеи
x1 = 200  # начальные координаты змейки
y1 = 200  # начальные координаты змейки

pg.display.update()
while not done:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:  # если нажали на какую-то кнопку
            if event.key == pg.K_LEFT:  # если кнопка - стрелка_влево, то
                x_change = -10  # идем влево (уменьшаем х)
                y_change = 0
            elif event.key == pg.K_RIGHT:  # если кнопка - стрелка_вправо, то
                x_change = 10  # идем вправо (увеличиваем х)
                y_change = 0
            elif event.key == pg.K_UP:  # если кнопка - стрелка_вверх, то
                x_change = 0
                y_change = 10  # идем вверх (увеличиваем у)
            elif event.key == pg.K_DOWN:  # если кнопка - стрелка_вниз, то
                x_change = 0
                y_change = -10  # идем вниз (уменьшаем у)

    rect(screen, GREEN, [200, 150, 10, 10])
    pg.display.update()


