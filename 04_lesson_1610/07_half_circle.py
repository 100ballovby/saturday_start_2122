from turtle import *  # импортирую саму библиотеку


t = Turtle()  # объект черепашки (то, что будет рисовать)
t.shape('turtle')  # задаю форму объекту
t.color('#ffffff')  # цвет черепашки (рисовать будет им)

s = Screen()  # создаю новый холст для черепашки
s.title('Моя черепашка')  # название окна черепашки
s.bgcolor('#000000')  # цвет фона черепашки

for hc in range(4):
    t.lt(90)
    t.circle(50, 180)

for hc in range(12):
    t.lt(180)
    t.circle(50, 180)

done()  # окно не будет закрываться сразу