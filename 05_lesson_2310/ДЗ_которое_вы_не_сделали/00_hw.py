from turtle import *

t = Turtle()
t.shape('turtle')

angles = int(input('Сколько углов? '))

for line in range(angles):
    t.fd(50)
    t.rt(360 / angles)

done()
