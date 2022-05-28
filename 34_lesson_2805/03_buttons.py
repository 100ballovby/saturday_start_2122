from tkinter import *

window = Tk()
btn = Button(text='Изменить', width=15, height=5)


def change():
    btn['text'] = 'Изменено'
    btn['bg'] = '#000000'  # цвет фона кнопки
    btn['activebackground'] = '#555555'  # цвет фона, когда курсор над кнопкой
    btn['fg'] = '#ffffff'  # цвет текста кнопки
    btn['activeforeground'] = '#ffffff'  # цвет текста, когда курсор над кнопкой

btn.config(command=change)
btn.pack()
window.mainloop()
