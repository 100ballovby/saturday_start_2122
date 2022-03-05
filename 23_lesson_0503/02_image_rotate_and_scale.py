import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('angry-birds.png')  # создаю ссылку на файл с картинкой
img_rect = img.get_rect()  # превращаю картинку в объект
img_rect.center = W // 2, H // 2  # устанавливаю центр картинки в центре окна

img_copy = img  # создаю копию изображения, которую буду изменять
img_rect_copy = img_copy.get_rect()  # создаю клон объекта-изображения
img_rect_copy.center = W // 2, H // 2  # центрирую копию

rotate = 0  # отвечает за поворот изображения
scale = 1  # отвечает за размер изображения

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        img_rect_copy.x -= 20
    if keys[pg.K_RIGHT]:
        img_rect_copy.x += 20
    if keys[pg.K_UP]:
        img_rect_copy.y -= 20
    if keys[pg.K_DOWN]:
        img_rect_copy.y += 20
    if keys[pg.K_r]:  # если нажмут на кнопку r
        rotate += 10  # изменить rotate на 10
        img_copy = pg.transform.rotozoom(img, rotate, scale)
    if keys[pg.K_p]:
        scale *= 1.1  # увеличиваю картинку на 10%
        img_copy = pg.transform.rotozoom(img, rotate, scale)
    if keys[pg.K_m]:
        scale /= 1.1  # уменьшаю картинку на 10%
        img_copy = pg.transform.rotozoom(img, rotate, scale)


    if img_rect_copy.right >= W:
        img_rect_copy.x -= 20
        img_copy = pg.transform.flip(img_copy, True, False)  # разворот изображения (что_развернуть, по_иксу, по_игреку)
    elif img_rect_copy.left <= 0:
        img_rect_copy.x += 20
        img_copy = pg.transform.flip(img_copy, True, False)  # разворот изображения (что_развернуть, по_иксу, по_игреку)

    screen.fill((255, 255, 255))
    screen.blit(img_copy, img_rect_copy)  # отображаю картинку в координатах img_rect
    pg.display.update()