import pygame as pg
from pygame.draw import rect, circle, polygon, ellipse, aaline
from random import choice


def ball_start():
    global speed_x, speed_y, ball_moving, score_time

    ball.center = (W // 2, H // 2)  # ставлю мяч посередине
    cur_time = pg.time.get_ticks()  # сохраняю текущее время

    if cur_time - score_time < 700:
        num_3 = my_font.render('3', False, MAGENTA)
        screen.blit(num_3, [W / 2 - 20, H / 2 + 20])
    if 700 < cur_time - score_time < 1400:
        num_2 = my_font.render('2', False, MAGENTA)
        screen.blit(num_2, [W / 2 - 20, H / 2 + 20])
    if 1400 < cur_time - score_time < 2100:
        num_1 = my_font.render('1', False, MAGENTA)
        screen.blit(num_1, [W / 2 - 20, H / 2 + 20])

    if cur_time - score_time < 2100:  # пока не прошло 3 секунды
        speed_x, speed_y = 0, 0  # мячик стоит на месте
    else:  # иначе
        speed_x = 7 * choice([-1, 1])  # направляем мячик в случайную позицию
        speed_y = 7 * choice([-1, 1])  # направляем мячик в случайную позицию
        score_time = None  # отключаем score_time


def ball_move():
    """
    Логика передвижения мячика
    :param speed_x: скорость перемещения по горизонтали
    :param speed_y: скорость перемещения по вертикали
    :param ball: игровой объект-мячик
    :return: None
    """
    global speed_x, speed_y, player_score, opponent_score, score_time
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если ударился об верхний или нижний край экрана
        speed_y *= -1  # направить его в противоположную сторону

    elif ball.left <= 0:  # если ударился об левый край экрана
        score_time = pg.time.get_ticks()
        player_score += 1  # Засчитать очки игроку

    elif ball.right >= W:  # если ударился об правый край экрана
        score_time = pg.time.get_ticks()
        opponent_score += 1  # засчитать очки оппоненту

    if ball.colliderect(player) and speed_x > 0:
        if abs(ball.right - player.left) < 10:
            speed_x *= - 1
        elif abs(ball.bottom - player.top) < 10 or abs(ball.top - player.bottom) < 10:
            speed_y *= -1

    if ball.colliderect(opponent):
        if abs(ball.left - opponent.right) < 10 or abs(ball.right - player.left) < 10:
            speed_x *= -1
        else:
            speed_y *= -1


def player_animation(p_speed):
    """
    Функция будет двигать платформу игрока_1 по вертикали
    :param p_speed: скорость перемещения
    :return: None
    """
    player.y += p_speed

    if player.top <= 0:  # если ушел за верхнюю границу
        player.top = 0  # остановить его наверху
    elif player.bottom >= H:  # если ушел за нижнюю границу
        player.bottom = H  # остановить его внизу


def opponent_ai(o_speed):
    """
    Платформа 2 будет двигаться самостоятельно. Если шарик будет выше, чем верхняя граница
    платформы, то платформа двигается наверх. Если шарик ниже, чем нижняя граница платформы,
    то платформа двигается вниз.
    :param o_speed: скорость перемещения
    :return: None
    """
    if opponent.top < ball.y:  # если шарик выше
        opponent.y += o_speed  # поднять платформу
    elif opponent.bottom > ball.y:  # если шарик ниже
        opponent.y -= o_speed  # опускаем платформу

    if opponent.top <= 0:  # если ушел за верхнюю границу
        opponent.top = 0  # остановить его наверху
    elif opponent.bottom >= H:  # если ушел за нижнюю границу
        opponent.bottom = H  # остановить его внизу

W = 1280
H = 720
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game 🏐')
clock = pg.time.Clock()

L_GREY = (230, 230, 230)  # цвет фона
MAGENTA = (255, 110, 94)  # цвет персонажей

# game objects
ball = pg.Rect(W // 2 - 15, H // 2 - 15, 30, 30)  # (x, y, ширина_квадрата, высота_квадрата)
player = pg.Rect(W - 20, H // 2, 10, 140)  # (x, y, ширина_квадрата, высота_квадрата)
opponent = pg.Rect(10, H // 2, 10, 140)  # (x, y, ширина_квадрата, высота_квадрата)

# game variables
speed_x = 8 * choice([-1, 1])
speed_y = 8 * choice([-1, 1])
p_speed = 0
o_speed = 5
ball_moving = False
score_time = True

# score text
player_score = 0
opponent_score = 0
pg.font.init()  # чтобы шрифты работали
my_font = pg.font.SysFont('comicsans', 64)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                p_speed -= 7
            if event.key == pg.K_DOWN:
                p_speed += 7
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                p_speed += 7
            if event.key == pg.K_DOWN:
                p_speed -= 7

    # отображение игровых объектов
    screen.fill(L_GREY)  # заливаю экран серым цветом
    rect(screen, MAGENTA, player)  # рисую цветной квадрат на области player
    rect(screen, MAGENTA, opponent)  # рисую цветной квадрат на области opponent
    ellipse(screen, MAGENTA, ball)  # рисую цветной эллипс на области ball
    aaline(screen, MAGENTA, [W // 2, 0], [W // 2, H])

    player_score_text = my_font.render(f'{player_score}', True, MAGENTA)
    screen.blit(player_score_text, [660, 270])

    opponent_score_text = my_font.render(f'{opponent_score}', True, MAGENTA)
    screen.blit(opponent_score_text, [580, 270])

    if score_time:  # если время начинает считаться
        ball_start()  # вернуть мяч в центр поля

    pg.display.update()

    # Логика перемещения шарика
    ball_move()
    player_animation(p_speed)
    opponent_ai(o_speed)
