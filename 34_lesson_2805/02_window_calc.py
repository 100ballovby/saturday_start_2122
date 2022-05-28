from tkinter import *

window = Tk()

def test():
    try:
        float(f1.get())  # пытаюсь преобразовать значения из полей в числа
        float(f2.get())  # пытаюсь преобразовать значения из полей в числа
        return True
    except:
        banner['text'] = 'Error'
        return False


def summary():
    if test():  # если нам ввели числа
        banner['text'] = float(f1.get()) + float(f2.get())


def difference():
    if test():  # если нам ввели числа
        res = float(f1.get()) - float(f2.get())
        banner['text'] = round(res, 2)  # округлить до двух знаков после запятой


def multiply():
    if test():  # если нам ввели числа
        res = float(f1.get()) * float(f2.get())
        banner['text'] = round(res, 2)  # округлить до двух знаков после запятой


def division():
    if test():
        try:
            res = float(f1.get()) / float(f2.get())
            banner['text'] = round(res, 2)
        except ZeroDivisionError:  # если попытались поделить на 0
            banner['text'] = 'Zero error!'

f1 = Entry(width=10)
f1.pack()
f2 = Entry(width=10)
f2.pack()
btn_summ = Button(text='+', width=10, command=summary)
btn_diff = Button(text='-', width=10, command=difference)
btn_mult = Button(text='*', width=10, command=multiply)
btn_div = Button(text='/', width=10, command=division)
btn_summ.pack()
btn_diff.pack()
btn_mult.pack()
btn_div.pack()

banner = Label(width=15)
banner.pack()

window.mainloop()



