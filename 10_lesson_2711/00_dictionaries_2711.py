'''Сделать словарь, в котором хранятся
курсы валют по отношению к USD'''

currencies = ['EUR', 'GBP', 'RUB', 'BYN', 'AED', 'JY', 'BTC']  # валюты
rates = [0.88, 0.74, 75.56, 2.6, 3.67, 133.37, 0.000018]  # стоимость (курс) валюты
exchange = {}  # курсы храню в словаре

for index in range(len(currencies)):  # строим последовательность из индексов валют
    exchange[currencies[index]] = rates[index]
    # ^ я достаю код валюты         ^ я достаю курс

print(exchange)

amount = int(input('Сколько денег меняем? '))
cur = input('Введи код валюты: ').upper()  # возводит все в верхний регистр usd -> USD

if cur in exchange:
    print(f'За ${amount} вы получите: {amount * exchange[cur]} {cur}.')
else:
    print('Такой валюты нет!')
