import pygame as pg
from pygame.draw import rect, circle, polygon

W = 800
H = 900
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('car.png').convert_alpha()
img_rect = img.get_rect()
img_copy = img
img_rect_copy = img_rect

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
paddle1 = pg.Rect(170, 30, 100, 20)  # препятствие


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

    rect(screen, RED, paddle1)  # препятствие

    screen.blit(img_copy, img_rect_copy)
    pg.display.update()

    # Логика игры
    moving(img_rect, car_speed, border_left, border_right)
    paddle1.y += 10
    if paddle1.y >= H:
        paddle1.y = 0