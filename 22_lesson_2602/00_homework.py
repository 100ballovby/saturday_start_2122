import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()
