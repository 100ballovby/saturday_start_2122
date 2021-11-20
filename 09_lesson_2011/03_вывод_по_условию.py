fridge = {
    'ham': 6.78,
    'cucumber': 2.35,
    'orange': 2.54,
    'grape': 7.99,
    'melon': 12.87,
}

# вывести продукты, которые стоят меньше 7 долларов
for key, value in fridge.items():  # перебираю все содержимое словаря
    if value <= 7:
        print(f'{key} costs ${value}.')

