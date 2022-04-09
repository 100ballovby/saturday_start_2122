import csv
import matplotlib.pyplot as plt

with open('salaries.csv') as file:
    reader = csv.reader(file)  # читаю и сохраняю содержимое таблицы
    headers = next(reader)  # получает первую строчку таблицы и выбрасывает ее из общей выборки

    years = []
    sal_rub = []
    sal_dol = []
    for row in reader:  # просмотреть каждую строку таблицы
        years.append(int(row[1]))  # записываю год в список
        sal_rub.append(float(row[2]))  # записываю зарплату в рублях в список
        sal_dol.append(float(row[4]))  # записываю зарплату в $ в список


