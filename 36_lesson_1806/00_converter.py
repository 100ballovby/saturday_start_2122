from optparse import Option
from tkinter import *

app = Tk()
app.title('Конвертер валют')
app.configure(bg='#e8fffb', padx=20, pady=20)

amountField1 = Entry(app).grid(row=1, column=1, pady=3, padx=25)
amountField2 = Entry(app).grid(row=5, column=1, pady=3, padx=25)
headLabel = Label(app, text='Конвертер валют',
                  font=('Calibri', 24, 'bold'), bg='#e8fffb').grid(row=0, column=1, padx=5, pady=5)
amountLabel = Label(app, text='Сколько денег переводим',
                    font=('Calibri', 12, 'bold'), bg='#e8fffb').grid(row=1, column=0)
fromLabel = Label(app, text='Из какой валюты переводим?',
                    font=('Calibri', 12, 'bold'), bg='#e8fffb').grid(row=2, column=0)
toLabel = Label(app, text='В какую валюту переводим',
                    font=('Calibri', 12, 'bold'), bg='#e8fffb').grid(row=3, column=0)
resultLabel = Label(app, text='После конвертации вы получаете',
                    font=('Calibri', 12, 'bold'), bg='#e8fffb').grid(row=5, column=0)

cur_codes = ['USD', 'EUR']
var1 = StringVar(app)
var2 = StringVar(app)
var1.set('Валюта')
var2.set('Валюта')
from_cur_option = OptionMenu(app, var1, *cur_codes).grid(row=2, column=1, ipadx=25, pady=3)
to_cur_option = OptionMenu(app, var2, *cur_codes).grid(row=3, column=1, ipadx=25, pady=3)

conv_button = Button(app, text='Конвертировать', font=('Calibri', 12, 'bold'),
                     width=17, height=2).grid(row=6, column=0, pady=2)
reset_button = Button(app, text='Очистить все поля', font=('Calibri', 12, 'bold'),
                     width=17, height=2).grid(row=6, column=1, pady=2)

app.mainloop()
