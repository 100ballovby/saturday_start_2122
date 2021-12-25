from turtle import *
from shapes import *


t = Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green',
          'cyan', 'blue', 'purple', 'pink']

for i in range(8):
    t.color(colors[i])
    t.fd(100)

    x = t.xcor()
    y = t.ycor()

    t.rt(30)
    t.begin_fill()  # заливка фигуры
    draw_triangle(t, x, y, colors[i], 50)
    t.end_fill()
    t.lt(30)

    t.down()
    t.fd(-100)
    t.rt(45)

done()