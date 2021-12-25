from turtle import *
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'cyan', 'purple'])  # cycle() позволяет бегать по списку циклично


def draw_circle(turtle, size, angle, shift):
    """
    Рисует спираль из кругов
    :param turtle: объект черепашки
    :param size: радиус круга
    :param angle: градус поворота
    :param shift: расстояние между кругами
    :return: None
    """
    turtle.color(next(colors))  # прошу следующий цвет из списка
    turtle.circle(size)
    turtle.rt(angle)
    turtle.fd(shift)

    draw_circle(turtle, size + 5, angle + 1, shift + 1)

t = Turtle()
t.speed(0)
t.pensize(4)
draw_circle(t, 10, 0, 1)
