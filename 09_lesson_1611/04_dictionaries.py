store = {
    'banana': 2.45,
    'cookie': 3.67,
    'milk': 4.89,
    'ham': 7.56,
    'grape': 12.58
}

print(store['ham'])  # обращение к элементам словаря не по индексам, а по ключам

# замена значения
store['grape'] = 15.99
print(store)

# добавление новой пары ключ-значение
store['orange'] = 5.49
print(store)

# удаление пары 
del store['ham']
print(store)
