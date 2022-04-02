import json


with open('salaries.json') as obj:
    data = json.loads(obj.read())  # читаю файл и преобразовываю его
    print(type(data))  # словарь
    print('Год | з/п в руб. | курс $ | з/п в $')

    for col in data:  # перебираю ключи в словаре data
        fee = data[col]['fee']  # словарь[2001]['fee'] - обращаюсь к ключу с зарплатой для каждого года
        rate = data[col]['dollar_rate']  # словарь[2001]['dollar_rate'] - обращаюсь к ключу с курсом доллара для каждого года
        fee_dollar = fee / rate  # чтобы узнать зарплату в долларах, делю ее на курс
        if data[col]['denominated']:  # если зарплата отражена в деноминированных рублях
            fee = fee * 10000  # умножаю на 10.000, чтобы получить "старые" рубли (BYR)
        print(f'{col} | {fee} | {rate} | {fee_dollar}')

