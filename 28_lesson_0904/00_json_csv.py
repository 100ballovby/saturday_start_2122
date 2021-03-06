import json
import csv  # библиотека для работы с таблицами


with open('salaries.json') as obj:
    data = json.loads(obj.read())  # читаю файл и преобразовываю его
    print(type(data))  # словарь
    head = ['№', 'Год',  'з/п в руб.', 'Курс $', 'з/п в $']  # будущие заголовки таблицы
    number = 1  # счетчик строк в таблице
    with open('salaries.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)  # объект, который записывает информацию в файл csv
        writer.writerow(head)  # записываю первую строчку - заголовки таблицы

        for col in data:
            fee = data[col]['fee']
            rate = data[col]['dollar_rate']
            fee_dollar = fee / rate
            if data[col]['denominated']:  # если зарплата отражена в деноминированных рублях
                fee = fee * 10000  # умножаю на 10.000, чтобы получить "старые" рубли (BYR)
            row = [number, col, fee, rate, fee_dollar]  # превращаю каждый год из json-файла в строку таблицы
            writer.writerow(row)  # записываю информацию из JSON в таблицу
            number += 1  # увеличиваю порядковый номер строки таблицы

""" Алгоритм работы с файлами для трансфера информации из JSON в CSV 
1. Открыть и прочитать JSON, а также трансформировать JSON-строчку в Python словарь 
2(*). Прописать заголовки таблицы
3. Создать саму таблицу (то есть откыть файл ____.csv в режиме записи (w) 
4. Циклом пройтись по всему словарю 
5. Сформировать список для каждого элемента из словаря 
6. Записать список в качестве строки в таблицу 
"""