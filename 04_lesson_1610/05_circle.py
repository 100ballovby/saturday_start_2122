from turtle import *  # импортирую саму библиотеку


t = Turtle()  # объект черепашки (то, что будет рисовать)
t.shape('turtle')  # задаю форму объекту
t.color('#ffffff')  # цвет черепашки (рисовать будет им)

s = Screen()  # создаю новый холст для черепашки
s.title('Моя черепашка')  # название окна черепашки
s.bgcolor('#000000')  # цвет фона черепашки

# рисую окружность
t.circle(100)  # 100 - радиус
# рисую круг
t.dot(100, 'red')  # можно указывать цвет

done()  # окно не будет закрываться сразу