import random  # подключил библиотеку рандом

print(random.randint(1, 5))  # при таком виде импорта нужно всегда писать название библиотеки перед вызовом функции

import random as r  # подключаю библиотеку рандом с алиасом
print(r.randint(1, 5))  # при таком виде импорта нужно всегда писать название сокращения перед вызовом функции

from math import ceil  # из библиотеки math я подключаю функцию округления в большую сторону
print(ceil(2.43))  # название библиотеки больше писать не нужно

from tkinter import *  # импортировать из библиотеки tkinter ВСË
t = Tk()
btn = Button()
l = Label()
l.pack()
