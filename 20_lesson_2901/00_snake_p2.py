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
SNAKE_BLOCK = 10  # фактический размер квадратика змеи


def show_message(msg, color, surface):
    pg.font.init()  # инициализация шрифта
    font_style = pg.font.SysFont(bold=True, size=10, name='calibri')  # стиль шрифта - жирный, размер 10
    text = font_style.render(msg, True, color)  # отобразить сообщение
    surface.blit(text, [S_WIDTH / 2, S_HEIGHT / 2])

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Snake Game v.1.1')  # название окна
clock = pg.time.Clock()


def game_loop():  # главный игровой цикл
    x_change = 0  # то, насколько изменяются координаты змеи
    y_change = 0  # то, насколько изменяются координаты змеи
    x1 = 200  # начальные координаты змейки
    y1 = 200  # начальные координаты змейки

    food_x = round(randrange(0, S_WIDTH - SNAKE_BLOCK) / 10) * 10
    food_y = round(randrange(0, S_HEIGHT - SNAKE_BLOCK) / 10) * 10

    done = False
    game_over = False  # переменная, отвечающая за окончание игры, но не ее остановку

    pg.display.update()
    while not done:

        while game_over:  # если "проигрыш"
            screen.fill(VIOLET)
            show_message('Игра окончена! Нажмите C, чтобы сыграть еще раз', BLUE, screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = False  # отключаем цикл "паузы"
                        done = True  # закрываем игру
                    elif event.key == pg.K_c:
                        game_loop()  # перезапускаем игру

        clock.tick(SPEED)
        for event in pg.event.get():  # управляем змеей
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:  # если нажали на какую-то кнопку
                if event.key == pg.K_LEFT:  # если кнопка - стрелка_влево, то
                    x_change = -SNAKE_BLOCK  # идем влево (уменьшаем х)
                    y_change = 0
                elif event.key == pg.K_RIGHT:  # если кнопка - стрелка_вправо, то
                    x_change = SNAKE_BLOCK  # идем вправо (увеличиваем х)
                    y_change = 0
                elif event.key == pg.K_UP:  # если кнопка - стрелка_вверх, то
                    x_change = 0
                    y_change = -SNAKE_BLOCK  # идем вверх (уменьшаем у)
                elif event.key == pg.K_DOWN:  # если кнопка - стрелка_вниз, то
                    x_change = 0
                    y_change = SNAKE_BLOCK  # идем вниз (увеличиваем у)

        if x1 >= S_WIDTH or x1 < 0 or y1 >= S_HEIGHT or y1 < 0:
            game_over = True

        x1 += x_change  # заставляю змею двигаться по иксу
        y1 += y_change  # заставляю змею двигаться по игреку

        screen.fill(VIOLET)
        rect(screen, GREEN, [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])
        pg.display.update()

        # TODO: сделать змею другого цвета, если коснется объекта

game_loop()