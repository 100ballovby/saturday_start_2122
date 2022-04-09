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
        sal_rub.append(float(row[2]) / 10000)  # записываю зарплату в рублях в список
        sal_dol.append(float(row[4]))  # записываю зарплату в $ в список

    plt.title('Зарплаты Белорусов 2002-2022')
    plt.xlabel('Годы')
    plt.ylabel('Сумма')
    plt.grid()
    plt.plot(years, sal_rub, c='red')  # строю график на основе двух списков - годы и зарплаты
    plt.plot(years, sal_dol, c='blue')  # строю вторую линию на графике - зарплаты в долларах

    plt.fill_between(years, sal_rub, sal_dol,
                     facecolor='red', alpha=0.1)
    """
    facecolor - цвет закрашенной области 
    alpha - прозрачность (0.1 - 10%)
    """

    plt.show()


