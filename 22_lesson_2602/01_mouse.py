import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

m_x = 0
m_y = 0

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            print(event.button)
            print(f'x: {event.pos[0]}, y: {event.pos[1]}')
            m_x = event.pos[0]
            m_y = event.pos[1]

    screen.fill((0, 0, 0))
    r = rect(screen, (255, 255, 255), [m_x, m_y, 200, 200])
    if r.x == m_x or r.y == m_y:
        print('pressed')

    pg.display.update()