import pygame as pg
from pygame.draw import rect, circle, polygon, ellipse, aaline


def ball_move():
    """
    Логика передвижения мячика
    :param speed_x: скорость перемещения по горизонтали
    :param speed_y: скорость перемещения по вертикали
    :param ball: игровой объект-мячик
    :return: None
    """
    global speed_x, speed_y
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если ударился об верхний или нижний край экрана
        speed_y *= -1  # направить его в противоположную сторону
    elif ball.left <= 0 or ball.right >= W:  # если ударился об правый или левый край экрана
        speed_x *= -1  # направить его в противоположную сторону
    elif ball.colliderect(player) or ball.colliderect(opponent):
        speed_x *= -1


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

speed_x = 7
speed_y = 7
p_speed = 0
o_speed = 5

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

    pg.display.update()

    # Логика перемещения шарика
    ball_move()
    player_animation(p_speed)
    opponent_ai(o_speed)
