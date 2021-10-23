from turtle import *

t = Turtle()
t.shape('turtle')

angles = int(input('Сколько углов? '))
if angles <= 3:  # не даю ввести меньше 3 углов
    t.write('Нельзя вводить меньше 3 углов!')
    angles = 3

for line in range(angles):
    t.fd(50)
    t.rt(360 / angles)

done()
