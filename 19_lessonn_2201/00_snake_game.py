import pygame as pg
from pygame.draw import rect
from random import randrange
import time

BLUE = (120, 84, 240)
RED = (240, 84, 84)
GREEN = (74, 224, 74)
VIOLET = (248, 240, 255)
S_WIDTH = 640
S_HEIGHT = 480
SPEED = 5


def show_message(msg, color, surface):
    pg.font.init()  # инициализация шрифта
    font_style = pg.font.SysFont(bold=True, size=10, name='calibri')  # стиль шрифта - жирный, размер 10
    text = font_style.render(msg, True, color)  # отобразить сообщение
    surface.blit(text, [S_WIDTH / 2, S_HEIGHT / 2])


done = False
game_over = False  # переменная, отвечающая за окончание игры, но не ее остановку

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Snake Game v.1')  # название окна
clock = pg.time.Clock()

x_change = 0  # то, насколько изменяются координаты змеи
y_change = 0  # то, насколько изменяются координаты змеи
x1 = 200  # начальные координаты змейки
y1 = 200  # начальные координаты змейки

food_x = randrange(0, S_WIDTH - 10)
food_y = randrange(0, S_HEIGHT - 10)

pg.display.update()
while not done:

    while game_over:  # если "проигрыш"
        screen.fill(VIOLET)
        show_message('Игра окончена! Нажмите C, чтобы сыграть еще раз', BLUE, screen)
        pg.display.update()

    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:  # если нажали на какую-то кнопку
            if event.key == pg.K_LEFT:  # если кнопка - стрелка_влево, то
                x_change = SPEED * -1  # идем влево (уменьшаем х)
                y_change = 0
            elif event.key == pg.K_RIGHT:  # если кнопка - стрелка_вправо, то
                x_change = SPEED  # идем вправо (увеличиваем х)
                y_change = 0
            elif event.key == pg.K_UP:  # если кнопка - стрелка_вверх, то
                x_change = 0
                y_change = SPEED * -1  # идем вверх (уменьшаем у)
            elif event.key == pg.K_DOWN:  # если кнопка - стрелка_вниз, то
                x_change = 0
                y_change = SPEED  # идем вниз (увеличиваем у)
            elif event.key == pg.K_c:  # продолжить игру
                game_over = False
            elif event.key == pg.K_ESCAPE:  # остановить игру
                game_over = True

    x1 += x_change  # заставляю змею двигаться по иксу
    y1 += y_change  # заставляю змею двигаться по игреку

    if x1 > S_WIDTH:
        x1 *= 0
    elif x1 <= 0:
        x1 = S_WIDTH - 10
    elif y1 > S_HEIGHT:
        y1 *= 0
    elif y1 <= 0:
        y1 = S_HEIGHT - 10

    screen.fill(VIOLET)
    rect(screen, GREEN, [x1, y1, 10, 10])
    pg.display.update()

    # TODO: сделать змею другого цвета, если коснется объекта


