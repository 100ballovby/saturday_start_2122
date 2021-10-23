from turtle import *

t = Turtle()
t.shape('turtle')

angles = int(input('Сколько углов? '))
steps = 100  # длина стороны многоугольника
if angles <= 3:  # не даю ввести меньше 3 углов
    t.write('Нельзя вводить меньше 3 углов!')
    angles = 3
elif angles > 30:  # если фигура слишком большая
    steps = 5  # уменьшить количество шагов

for line in range(angles):
    t.fd(steps)
    t.rt(360 / angles)

done()
