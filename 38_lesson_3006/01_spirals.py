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

length = 3
for i in range(400):
    t.fd(length)
    t.rt(144)
    length += 3
    t.color(choice(colors))

done()
