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

    text_area = Text(app, height=12, width=32, bg='#d6e6ff')
    text_area.grid(column=0, row=4)
    ans = f'Your choice: {USER_CHOICE}\nComputer choice: {COMP_CHOICE}\nScore: {USER_SCORE}\nComputer score: {COMP_SCORE}'
    text_area.insert(END, ans)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'камень'
    COMP_CHOICE = random_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'бумага'
    COMP_CHOICE = random_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'ножницы'
    COMP_CHOICE = random_choice()
    result(USER_CHOICE, COMP_CHOICE)


button_rock = Button(app, text='Камень', bg='#9e9080', command=rock)
button_rock.grid(column=0, row=1)
button_scissor = Button(app, text='Ножницы', bg='#9e8580', command=scissor)
button_scissor.grid(column=0, row=2)
button_paper = Button(app, text='Бумага', bg='#809c9e', command=paper)
button_paper.grid(column=0, row=3)

mainloop()

