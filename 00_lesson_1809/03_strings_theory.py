'''
f-string - formatted string - форматированная строка
Это строка, в которую можно вставить значение переменной.

Чтобы сделать f-строчку, надо поставить букву f перед кавычками,
а внутри строки поместить переменную в {}
'''

my_cat = 1
cat_name = 'Liza'

print(f'I have {my_cat} cat. Her name is {cat_name}.')

############
name = input('Как тебя зовут? ')
print(f'Привет, {name}!')
############

print('2' + 'a')  # строчки можно складывать, но ТОЛЬКО со строчками
print('a' * 5)  # строчки можно умножать ТОЛЬКО НА ЧИСЛА

