import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1000
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('car.png').convert_alpha()
img_rect = img.get_rect()
img_copy = img
img_rect_copy = img_rect

center = W // 2, 500  # координаты центра картинки
img_rect.center = center  # центирую картинку на экране игры
img_rect_copy.center = center  # центирую картинку на экране игры

WHITE = (255, 255, 255)


def moving(obj, speed):
    obj.x += speed


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
                car_speed += 5
                angle = -30
                img_copy = pg.transform.rotate(img, angle)
            if event.key == pg.K_LEFT:
                car_speed -= 5
                angle = 30
                img_copy = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 5
            if event.key == pg.K_LEFT:
                car_speed += 5
            angle = 0
            img_copy = pg.transform.rotate(img, angle)

    screen.fill(WHITE)
    screen.blit(img_copy, img_rect_copy)
    pg.display.update()

    # Логика игры
    moving(img_rect, car_speed)