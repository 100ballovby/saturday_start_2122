import requests

url = 'https://api.github.com/'
response = requests.get(url)  # подключаюсь к адресу

code = response.status_code  # сохраняю результат подключения в переменной
if response:  # когда приходит код 200 - 304, возвращается True
    print(response.content)  # содержимое ответа в битовом виде
    # print(response.text)  содержимое ответа в виде текста
    json_resp = response.json()  # содержимое ответа, но в виде JSON-объекта
else:  # если возвращается код ошибки
    print('Not found!')