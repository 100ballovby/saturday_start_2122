import random as r  # импортирую библиотеку с аббревиатурой

num = r.randint(1, 3)
# print(num)  <- распечатать значение переменной num

question = input('Задай вопрос: ')

if num == 1:  # если сгенерировалось число 1, то
    print('Да!')  # написать Да!
elif num == 2:  # если сгенерировалось число 2, то
    print('Нет!')  # написать Нет!
else:  # иначе (если сгенерировалось число 3), то
    print('Наверное...')  # написать Наверное...

