import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

pg.mouse.set_visible(False)  # скрыть курсор, когда мышь находится над экраном игры

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    if pg.mouse.get_focused():  # отслеживание положения курсора
        pos = pg.mouse.get_pos()  # фиксирую координаты курсора
        circle(screen, (255, 0, 0), [pos[0], pos[1]], 10)

    # рисуем тут
    pg.display.update()