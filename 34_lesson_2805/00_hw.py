"""Напишите функцию, которая получает строку в
качестве аргумента. Если строка начинается на
'abc', то заменить их на 'www', иначе добавить
в конец строки 'zzz'."""


def add_w(string):
    if string.startswith("abc"):
        string = string.replace("abc", 'www')
    else:
        string += 'zzz'
    return string


print(add_w('abcdef'))
print(add_w('hello'))


"""
Напишите функцию, которая генерирует строку, где на месте четных 
индексов стоят четные цифры, а на месте нечетных индексов - 
случайные буквы. 0 - четный индекс.
"""


from random import choice  # выбирает случайное из последовательности
from string import ascii_letters  # позволяет сгенерировать английский алфавит


def generate_string():
    res = ''
    letters = ascii_letters
    digits = '02468'
    for i in range(10):
        if i % 2 == 0:  # если индекс четный
            res += choice(digits)  # добавляю случайное из четных чисел
        else:
            res += choice(letters)  # добавляю случайную букву
    return res

print(generate_string())


"""
Напишите функцию, которая получает строку в качестве аргумента. 
Определите общее количество символов '+' и '-' в строке. А также 
сколько таких символов, после которых следует цифра ноль
"""

s = '3n2kv-kj+023;kwce-3r,+12+0+wkefmkwrnf-f'
# - (3), + (4), ->0 (2)


def plus_minus(string):
    p = 0
    m = 0
    pm = 0
    for i in range(len(string)):
        if string[i] == '+':
            p += 1
            if string[i + 1] == '0':  # если следующий за ним элемент равен 0
                pm += 1
        elif string[i] == '-':
            m += 1
            if string[i + 1] == '0':  # если следующий за ним элемент равен 0
                pm += 1
    return p, m, pm

print(plus_minus(s))


