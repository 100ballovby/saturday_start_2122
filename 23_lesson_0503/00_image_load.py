import pygame as pg
from pygame.draw import rect, circle, polygon

W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('angry-birds.png')  # создаю ссылку на файл с картинкой
img_rect = img.get_rect()  # превращаю картинку в объект
img_rect.center = W // 2, H // 2  # устанавливаю центр картинки в центре окна

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.blit(img, img_rect)  # отображаю картинку в координатах img_rect
    pg.display.update()