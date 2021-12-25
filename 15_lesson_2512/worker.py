from shapes import *
from turtle import *

t = Turtle()
t.shape('turtle')
t.up()

draw_square(t, 100, 50, '#4f2ce9', 75)
draw_square(t, 310, 240, '#ffe2a3', 35)

for i in range(1, 6):
    draw_square(t, i * 50, 100, '#00ffe2', 40)
    draw_triangle(t, i * 50, 100, '#00ffe2', 40)

draw_star(t, -310, -200, 'yellow', 100)

x_angle(t, 0, 0, 3, 'red', 50)

t.circle(50)

done()
