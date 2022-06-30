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

def square(side):
    for i in range(4):
        t.fd(side)
        t.rt(90)


def triangle(side):
    for i in range(3):
        t.fd(side)
        t.lt(120)

length = 3
for i in range(70):
    t.circle(length)
    square(length)
    t.rt(10)
    length += 1
    t.color(choice(colors))

done()
