import pygame as pg
from pygame.draw import rect

BLUE = (120, 84, 240)
RED = (240, 84, 84)
GREEN = (74, 224, 74)
S_WIDTH = 640
S_HEIGHT = 480

done = False

screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Snake Game v.1')  # название окна
clock = pg.time.Clock()


pg.display.update()
while not done:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True


