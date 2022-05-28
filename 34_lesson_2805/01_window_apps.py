from tkinter import *

window = Tk()  # окно приложения
# виджеты
field = Entry(window, width=20)  # поле для ввода
btn = Button(window, text='Преобразовать')  # кнопка
banner = Label(window,
               bg='green',  # цвет фона блока
               fg='white',  # цвет текста на блоке
               width=20)  # блок с текстом

# обработчик событий
def make_bigger(event):
    """
    Функция получает строку и преобразовывает ее в верхний регистр
    :param event: событие окна программы
    :return: преобразованная строчка
    """
    res = field.get()  # получить из поля для ввода текст
    res = res.upper()
    banner['text'] = res  # передаю получившийся текст на баннер приложения

# события (привязать обработчик к элементу)
btn.bind('<Button-1>', make_bigger)  # привязываю функцию к кнопке

# расположение элементов на экране
field.pack()  # "упаковать"/расположить элемент в окне
btn.pack()
banner.pack()

# запуск цикла обработки событий
window.mainloop()  # вызываю цикл
