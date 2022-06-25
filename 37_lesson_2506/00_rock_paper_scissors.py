from tkinter import *
import random as r


app = Tk()
app.geometry('400x300')
app.title('Камень, ножницы, бумага')

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ''
COMP_CHOICE = ''


def choice_to_num(choice):
    r = {'камень': 0, 'ножницы': 1, 'бумага': 2}
    return r[choice]


def num_to_choice(num):
    r = {0: 'камень', 1: 'ножницы', 2: 'бумага'}
    return r[num]


def random_choice():
    return r.choice(['камень', 'ножницы', 'бумага'])


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_num(human_choice)
    comp = choice_to_num(comp_choice)
    if user == comp:
        print('Ничья!')
    elif (user - comp) % 3 == 1:
        print('Ты победил!')
        USER_SCORE += 1
    else:
        print('Компьютер победил')
        COMP_SCORE += 1

mainloop()

