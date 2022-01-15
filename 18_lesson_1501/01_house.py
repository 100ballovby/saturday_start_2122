import pygame as pg
import sys  # работа с системными событиями
from pygame.draw import lines, arc, rect, circle

COLORS = {
    'red': (255, 78, 51),
    'green': (0, 230, 0),
    'blue': (173, 214, 255),
    'dark_blue': (102, 102, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'pink': (252, 190, 182),
}


def draw_house(x, y, width, height, surface, color):
    """
    Функция рисует коробку дома по заданным параметрам.
    :param x: положение по иксу
    :param y: положение по игреку
    :param width: ширина коробки дома
    :param height: высота коробки дома
    :param surface: поверхность, на которой рисуется дом
    :param color: цвет дома
    :return: None
    """
    points = [(x, y - ((2 / 3) * height)), (x, y),
              (x + width, y), (x + width, y - ((2 / 3) * height)),
              (x, y - ((2 / 3) * height)), (x + width / 2, y - height),
              (x + width, y - ((2 / 3) * height))
              ]
    line_thickness = 3
    lines(surface, color, False, points, line_thickness)

done = False  # окно не закрыто
screen = pg.display.set_mode((640, 480))  # создаю окно с определенным размером
clock = pg.time.Clock()  # счетчик кадров

# обновление кадров (они могут сменяться)
pg.display.update()
while not done:  # пока окно не закрыто
    clock.tick(30)  # обновляю экран 30 кадров/сек
    for event in pg.event.get():  # для каждого происходящего события
        if event.type == pg.QUIT:  # если нажать на крестик
            done = True  # работа окончена
            sys.exit()  # система должна закрыть окно программы

