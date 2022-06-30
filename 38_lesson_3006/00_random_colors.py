from random import randint, choice
from turtle import *

def random_colors(quantity):
    colors = []
    alphabet = '0123456789abcdef'
    for code in range(quantity):
        color = '#'
        for symbol in range(6):
            color += choice(alphabet)
        colors.append(color)
    return colors

t = Turtle()
t.speed(0)
colors = random_colors(1000)

for i in range(1000):
    x = randint(-500, 500)
    y = randint(-500, 500)
    d = randint(30, 100)
    col = choice(colors)
    t.up()  # перестать рисовать
    t.goto(x, y)  # перейти в случайные координаты
    t.down()  # начать рисовать
    t.color(col)  # задаем случайный цвет
    t.dot(d)  # нарисовать круг с диаметром d

done()  # чтобы окно сразу не закрывалось
