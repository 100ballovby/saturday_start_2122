from turtle import *
from shapes import *

t = Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green',
          'cyan', 'blue', 'purple', 'pink']

for i in range(8):
    t.color(colors[i])
    t.fd(100)

    t.begin_fill()  # заливка фигуры
    t.circle(30)
    t.end_fill()

    t.fd(-100)
    t.rt(45)

done()