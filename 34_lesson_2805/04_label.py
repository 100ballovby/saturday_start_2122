from tkinter import *

window = Tk()
label1 = Label(text='Machine learning', font='Arial 32')  # font = стиль и размер шрифта
label2 = Label(text='Recognition', font=('Comic Sans', 24, 'bold'))
# font = (Название шрифта, размер, стиль (жирный, курсив, подчекрнутый))
label1.config(bd=20, bg='#f2ac34')
label2.config(bd=20, bg='#c1e594')  # bd = размер рамок вокруг текста в пикселях

label1.pack()
label2.pack()
window.mainloop()
