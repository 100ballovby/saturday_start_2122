import pygame as pg
from pygame.draw import circle, rect
from random import randint
import sys


def init():
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # окно будет открываться на весь экран
    clock = pg.time.Clock()
    return screen, clock


def main(surf, timer):
    done = False
    snowflakes = []
    for i in range(200):
        x = randint(0, surf.get_width())
        y = randint(0, surf.get_height())
        snowflakes.append((x, y))
    while not done:
        surf.fill(pg.Color('lightskyblue'))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                done = True
                sys.exit()

        for i in range(len(snowflakes)):
            sf = snowflakes[i]
            snowflakes[i] = (sf[0] + randint(-1, 1), sf[1] + randint(1, 3))  # изменяю в цикле х и у снежинки (она падает)
            circle(surf, '#fffafa', [sf[0], sf[1]], randint(2, 6))  # рисую снежинку в измененных координатах
            if sf[1] > surf.get_height():  # если y снежинки больше высоты экрана
                snowflakes[i] = (sf[0], 0)  # х не меняем, у = 0
        pg.display.flip()
        timer.tick(30)

s, t = init()
main(s, t)
