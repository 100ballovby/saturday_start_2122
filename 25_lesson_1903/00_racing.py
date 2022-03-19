import pygame as pg
from pygame.draw import rect, circle, polygon
import random as r

W = 800
H = 900
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Car
img = pg.image.load('car.png').convert_alpha()
img_rect = img.get_rect()
img_copy = img
img_rect_copy = img_rect

# Tree
tree1 = pg.image.load('tree-3.png').convert_alpha()
tree1_rect = tree1.get_rect()
tree1 = pg.transform.scale(tree1, [W * 0.1, H * 0.2])

tree2 = pg.image.load('tree-3.png').convert_alpha()
tree2_rect = tree2.get_rect()
tree2 = pg.transform.scale(tree2, [W * 0.1, H * 0.2])

tree1_rect.x = 10
tree2_rect.x = W - 90
tree1_rect.y = -200
tree2_rect.y = -500

center = W // 2, H * 0.8  # координаты центра картинки
img_rect.center = center  # центирую картинку на экране игры
img_rect_copy.center = center  # центирую картинку на экране игры

WHITE = (255, 255, 255)
GRASS = (35, 145, 50)
SAND = (255, 245, 181)
GRAY = (61, 61, 61)
RED = (209, 4, 66)

background = pg.Rect(0, 0, W, H)  # фон
road = pg.Rect(0, 0, W / 2, H)  # дорога
road.center = W // 2, H // 2  # выставляю дорогу посередине
border_left = pg.Rect(road.x - W * 0.12, 0, W * 0.12, H)  # левая обочина
border_right = pg.Rect(road.right, 0, W * 0.12, H)  # правая обочина
paddle1 = pg.Rect(road.x, 0, 100, 20)  # препятствие №1
paddle2 = pg.Rect(road.x, -500, 100, 20)  # препятствие №2


def moving(obj, speed, l_side, r_side):
    obj.x += speed
    if obj.right >= r_side.left:  # если машина коснулась правой обочины
        obj.right = r_side.left - 10
    elif obj.left <= l_side.right:  # если машина коснулась левой обочины
        obj.left = l_side.right + 10


car_speed = 0  # начальная скорость машины
angle = 0  # угол поворота картинки изначально

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += 10
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 10
                angle = 10
            img_copy = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 10
            if event.key == pg.K_LEFT:
                car_speed += 10
            angle = 0
            img_copy = pg.transform.rotate(img, angle)

    screen.fill(WHITE)

    # отрисовываю декорации
    rect(screen, GRASS, background)  # фон игры
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [W // 2, 0, 5, H])  # полоса разметки
    rect(screen, RED, paddle1)  # препятствие №1
    rect(screen, RED, paddle2)  # препятствие №2

    screen.blit(img_copy, img_rect_copy)
    screen.blit(tree1, tree1_rect)
    screen.blit(tree2, tree2_rect)
    pg.display.update()

    # Логика игры
    moving(img_rect, car_speed, border_left, border_right)
    num = r.randint(1, 3)  # генерирую число от 1 до 3
    paddle1.y += 10
    paddle2.y += 10

    if paddle1.y >= H:
        if num == 1:
            paddle1.x = road.x
        elif num == 2:
            paddle1.center = road.center
        else:
            paddle1.right = road.right
        paddle1.y = 0

    num = r.randint(1, 3)  # генерирую число от 1 до 3
    if paddle2.y >= H:
        if num == 1:
            paddle2.x = road.x
        elif num == 2:
            paddle2.center = road.center
        else:
            paddle2.right = road.right
        paddle2.y = 0

    tree1_rect.y += 10
    tree2_rect.y += 10
    if tree1_rect.y >= H:
        tree1_rect.y = -200
    elif tree2_rect.y >= H:
        tree2_rect.y = -500
