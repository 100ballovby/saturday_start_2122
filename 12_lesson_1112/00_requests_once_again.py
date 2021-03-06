"""Коды подключения HTTP
1xx - запрос отправлен, но сервер его еще обрабатывает
2хх - успешное подключение
3хх - редирект (перенаправление)
4хх - неправильный/неполный/отсутствующий адрес
5xx - ошибка сервера (502 gateway)
"""
import requests

url = 'https://api.github.com/'
response = requests.get(url)  # подключаюсь к адресу

code = response.status_code  # сохраняю результат подключения в переменной
if response:  # когда приходит код 200 - 304, возвращается True
    print('Successfully!')
else:  # если возвращается код ошибки
    print('Not found!')

