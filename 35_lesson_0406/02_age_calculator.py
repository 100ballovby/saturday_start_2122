from tkinter import *


def close():
    window.destroy()  # закрыть окно приложения

window = Tk()
window.geometry('600x400')  # размер окна приложения
window.config(background='#fff1e3')  # устанавливаю фон окна приложения
window.resizable(width=False, height=False)  # запрещаю изменять размер окна по ширине и высоте
window.title('Age calculator')  # название окна приложения

l1 = Label(text='Age calculator', font=('Comic Sans', 24, 'bold'), bg='#fff1e3')
l1.pack()
l2 = Label(text='Enter your birth date', bg='#fff1e3')
l2.pack()

l_d = Label(text='Day:', bg='#fff1e3', font=('Comic Sans', 18))
l_m = Label(text='Month:', bg='#fff1e3', font=('Comic Sans', 18))
l_y = Label(text='Year:', bg='#fff1e3', font=('Comic Sans', 18))
e_d = Entry(width=12)  # день
e_m = Entry(width=12)  # месяц
e_y = Entry(width=12)  # год

l_d.place(x=180, y=90)
l_m.place(x=180, y=115)
l_y.place(x=180, y=140)
e_d.place(x=250, y=90)
e_m.place(x=250, y=115)
e_y.place(x=250, y=140)

btn = Button(text='Calculate age')
l3 = Label(text='The calculated age is', bg='#fff1e3', font=('Comic Sans', 18))
l4 = Label(text='', bg='#fff1e3', font=('Comic Sans', 18))
btn2 = Button(text='Close app', command=close)

btn.place(x=250, y=175)
l3.place(x=180, y=210)
l4.place(x=370, y=210)
btn2.place(x=250, y=235)

window.mainloop()
