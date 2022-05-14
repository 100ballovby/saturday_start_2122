"""Напишите функцию, которая получает в качестве аргумента строчку и выводит ее,
преобразовывая все буквы в верхний регистр (делает все буквы большими)."""


def make_uppercase(string):
    return string.upper()

print(make_uppercase('привет, андрей!'))

"""Напишите функцию, которая получает в качестве аргумента строчку и выводит ее, 
преобразовывая все буквы в нижний регистр."""


def make_lowercase(string):
    return string.lower()

print(make_lowercase('ПРИВЕТ, АНДРЕЙ!'))


"""Напишите функцию, которая получает строчку через аргумент и возвращает 
количество символов в этой строке."""


def measure(string):
    return len(string)

print(measure('Привет!'))


def measure_loop(string):
    symbols = 0
    for i in range(len(string)):
        symbols += 1
    return symbols


print(measure('Привет!'))

"""
Написать функцию, которая выводит частотный словарь.
Нужно составить словарь, который будет состоять из: буквы и количества этих букв в строке.

привет 
{
'п': 1,
'р': 1
...
}
"""


def count_symbols(string):
    freq = {}
    for i in range(len(string)):
        if string[i] != ' ':
            if string[i].lower() not in freq:  # если символа нет в словаре
                freq[string[i].lower()] = 1
            else:
                freq[string[i].lower()] += 1
    return freq

print(count_symbols('Привет, как твои дела? У меня есть попыт!'))
