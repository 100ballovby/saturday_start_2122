"""Словарь - это коллекция, хранящая набор пар
ключ: значение"""

fridge = {
    'ham': 6.78,
    'cucumber': 2.35,
    'orange': 2.54,
    'grape': 7.99,
    'melon': 12.87,
}

# получить значение
print(fridge['grape'])  # чтобы получить значение, надо обратиться к ключу

# добавление пары ключ: значение
print(fridge)
fridge['apple'] = 6.55  # добавляю новый ключ и сразу присваиваю ему новое значение
print(fridge)

# замена значения ключа
fridge['orange'] = 4.12  # обращаюсь к существующему ключу и присваиваю ему новое значение
print(fridge)

# удаление пары
del fridge['grape']
print(fridge)
