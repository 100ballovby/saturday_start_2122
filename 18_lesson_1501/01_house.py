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


def make_house_frame(x, y, width, height):
    """
    Функция рисует коробку дома по заданным параметрам.
    :param x: положение по иксу
    :param y: положение по игреку
    :param width: ширина коробки дома
    :param height: высота коробки дома
    :param surface: поверхность, на которой рисуется дом
    :param color: цвет дома
    :return: список точек для рисования очертания дома
    """
    points = []  # начнем с пустого списка точек

    points.append( (x, y - ((2 / 3) * height)) )  # верх этажа (левый верхний угол
    points.append( (x, y) )  # нижний левый угол
    points.append( (x + width, y) )  # нижний правый угол
    points.append( (x + width, y - ((2 / 3) * height)) )  # правый верхний угол
    points.append( (x, y - ((2 / 3) * height)) )  # верхняя часть первого этажа
    points.append( (x + width / 2, y - height) )  # вершина крыши
    points.append( (x + width, y - ((2 / 3) * height)) )  # верхняя правая точка (соединяю крышу с домом)
    return points  # возвращаю список точек


def draw_house(x, y, width, height, surface, color):
    line_thickness = 3
    lines(surface, color, False, make_house_frame(x, y, width, height), line_thickness)


def make_house_window_frame(x, y, width, height):
    points = []

    points.append((x + 0.5 * width, y - 0.5 * height))
    points.append((x + 0.9 * width, y - 0.2 * height))
    # TODO: дорисовать точки окна
    return points


def draw_house_window(x, y, width, height, surface, color):
    line_thickness = 3
    lines(surface, color, False, make_house_window_frame(x, y, width, height), line_thickness)

done = False  # окно не закрыто
screen = pg.display.set_mode((640, 480))  # создаю окно с определенным размером
clock = pg.time.Clock()  # счетчик кадров

draw_house(150, 200, 100, 150, screen, COLORS['red'])
draw_house_window(190, 230, 50, 50, screen, COLORS['dark_blue'])

# обновление кадров (они могут сменяться)
pg.display.update()
while not done:  # пока окно не закрыто
    clock.tick(30)  # обновляю экран 30 кадров/сек
    for event in pg.event.get():  # для каждого происходящего события
        if event.type == pg.QUIT:  # если нажать на крестик
            done = True  # работа окончена
            sys.exit()  # система должна закрыть окно программы

