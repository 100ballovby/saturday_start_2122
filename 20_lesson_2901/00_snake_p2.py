import pygame as pg
from pygame.draw import rect
from random import randrange
import time

BLUE = (120, 84, 240)
RED = (240, 84, 84)
GREEN = (74, 224, 74)
VIOLET = (248, 240, 255)
ORANGE = (252, 186, 3)
S_WIDTH = 400
S_HEIGHT = 400
SPEED = 5
SNAKE_BLOCK = 10  # фактический размер квадратика змеи

pg.font.init()
font_style = pg.font.SysFont(bold=True, size=10, name='calibri')  # стиль шрифта - жирный, размер 10
score_font = pg.font.SysFont('arial', 20)


def show_score(score):
    """
    Отображает очки на экране игры
    :param score: количество очков
    :return: None
    """
    value = score_font.render(f'Your score: {score}', True, ORANGE)
    screen.blit(value, [0, 0])


def show_message(msg, color, surface):
    pg.font.init()  # инициализация шрифта
    text = font_style.render(msg, True, color)  # отобразить сообщение
    surface.blit(text, [S_WIDTH / 2, S_HEIGHT / 2])

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Snake Game v.1.1')  # название окна
clock = pg.time.Clock()


def our_snake(s_block, s_list):
    """
    Увеличивает размер змеи путем добавления координат в список нового блока змеи, когда она съест еду
    :param s_block: размер змеи
    :param s_list:  список блоков змеи
    :return: None
    """
    for x in s_list:  # для каждой пары координат в списке
        rect(screen, GREEN, [x[0], x[1], s_block, s_block])


def game_loop():  # главный игровой цикл
    x_change = 0  # то, насколько изменяются координаты змеи
    y_change = 0  # то, насколько изменяются координаты змеи
    x1 = 200  # начальные координаты змейки
    y1 = 200  # начальные координаты змейки

    food_x = round(randrange(0, S_WIDTH - SNAKE_BLOCK) / 10) * 10
    food_y = round(randrange(0, S_HEIGHT - SNAKE_BLOCK) / 10) * 10

    done = False
    game_over = False  # переменная, отвечающая за окончание игры, но не ее остановку

    snake_list = []  # список блоков змеи
    snake_length = 1  # размер змеи

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
        # rect(screen, GREEN, [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])  # рисую змею

        snake_head = []  # храню голову змеи
        snake_head.append(x1)  # добавляю координаты головы в список
        snake_head.append(y1)  # добавляю координаты головы в список
        snake_list.append(snake_head)  # список координат добавляю в список объектов тела змеи
        if len(snake_list) > snake_length:  # если список станет длиннее, чем длина змеи
            snake_list.pop(0)  # удаляю первый элемент списка

        for block in snake_list[:-1]:
            if block == snake_head:  # если, когда змея идет вправо, пойти влево, игра закончится
                game_over = True

        our_snake(SNAKE_BLOCK, snake_list)  # перебираю блоки змеи и отрисовываю их
        show_score(snake_length - 1)

        rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])  # рисую еду
        pg.display.update()

        if x1 == food_x and y1 == food_y:  # если координаты змеи равны координатам еды
            food_x = round(randrange(0, S_WIDTH - SNAKE_BLOCK) / 10) * 10  # переместить еду на новую позицию
            food_y = round(randrange(0, S_HEIGHT - SNAKE_BLOCK) / 10) * 10  # переместить еду на новую позицию
            snake_length += 1

        # TODO: сделать змею другого цвета, если коснется объекта

game_loop()