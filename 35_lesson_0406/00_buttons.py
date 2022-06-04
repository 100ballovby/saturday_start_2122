from tkinter import *


def clear_entry(code, name):
    entry.delete(0, END)
    entry.insert(0, code)  # вставляю текст в поле (с какого символа, что вставить)
    label['text'] = name


def insertRed():
    clear_entry('#eb4034', 'RED')


def insertBlue():
    clear_entry('#34a4eb', 'BLUE')


def insertPurple():
    clear_entry('#c334eb', 'PURPLE')


def insertGreen():
    clear_entry('#34eb3d', 'GREEN')


def insertPink():
    clear_entry('#ff85eb', 'PINK')

window = Tk()

label = Label(width=20)
label.pack()
entry = Entry(width=20, justify=CENTER)  # текст будет располагаться посередине
entry.pack()

red = Button(width=20, command=insertRed, highlightbackground='#eb4034').pack()
blue = Button(width=20, command=insertBlue, highlightbackground='#34a4eb').pack()
purple = Button(width=20, command=insertPurple, highlightbackground='#c334eb').pack()
green = Button(width=20, command=insertGreen, highlightbackground='#34eb3d').pack()
pink = Button(width=20, command=insertPink, highlightbackground='#ff85eb').pack()

window.mainloop()