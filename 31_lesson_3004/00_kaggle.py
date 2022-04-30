import csv
import matplotlib.pyplot as plt

filename = 'bestsellers_with_categories_2022_03_27.csv'
with open(filename) as table:
    reader = csv.reader(table, delimiter=',')
    # объект для чтения csv получает таблицу и разделитель внутри таблицы
    # reader представляет собой массив с массивами
    lines = 0
    for row in reader:
        lines += 1
        print(f'Genre: {row[6]}')
    print(f'В таблице {lines} строк.')

