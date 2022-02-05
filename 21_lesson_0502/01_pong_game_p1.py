import pygame as pg
from pygame.draw import rect, circle, polygon, ellipse, aaline


def ball_move(speed_x, speed_y, ball):
    """
    Логика передвижения мячика
    :param speed_x: скорость перемещения по горизонтали
    :param speed_y: скорость перемещения по вертикали
    :param ball: игровой объект-мячик
    :return: None
    """
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= H:  # если ударился об верхний или нижний край экрана
        speed_y *= -1  # направить его в противоположную сторону
    elif ball.left <= 0 or ball.right >= W:  # если ударился об правый или левый край экрана
        speed_x *= -1  # направить его в противоположную сторону
    elif ball.colliderect(player) or ball.colliderect(opponent):
        speed_x *= -1
    # TODO: починить движение шарика

W = 1280
H = 960
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game 🏐')
clock = pg.time.Clock()

L_GREY = (230, 230, 230)  # цвет фона
MAGENTA = (255, 110, 94)  # цвет персонажей

# game objects
ball = pg.Rect(W // 2 - 15, H // 2 - 15, 30, 30)  # (x, y, ширина_квадрата, высота_квадрата)
player = pg.Rect(W - 20, H // 2, 10, 140)  # (x, y, ширина_квадрата, высота_квадрата)
opponent = pg.Rect(10, H // 2, 10, 140)  # (x, y, ширина_квадрата, высота_квадрата)


finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # отображение игровых объектов
    screen.fill(L_GREY)  # заливаю экран серым цветом
    rect(screen, MAGENTA, player)  # рисую цветной квадрат на области player
    rect(screen, MAGENTA, opponent)  # рисую цветной квадрат на области opponent
    ellipse(screen, MAGENTA, ball)  # рисую цветной эллипс на области ball
    aaline(screen, MAGENTA, [W // 2, 0], [W // 2, H])

    pg.display.update()

    # Логика перемещения шарика
    ball_move(0, 5, ball)
