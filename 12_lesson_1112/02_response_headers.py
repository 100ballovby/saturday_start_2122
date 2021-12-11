import requests

url = 'https://api.github.com/search/repositories'
p = {'q': 'requests',
     'l': 'python'}
response = requests.get(url, params=p)  # подключаюсь к адресу

code = response.status_code  # сохраняю результат подключения в переменной
if response:  # когда приходит код 200 - 304, возвращается True
    json_resp = response.json()  # содержимое ответа, но в виде JSON-объекта
    #print(json_resp)
    rep = json_resp['items'][3]  # достаю первый репозиторий
    print(f'Имя: {rep["name"]}, ссылка: {rep["html_url"]}')
else:  # если возвращается код ошибки
    print('Not found!')
