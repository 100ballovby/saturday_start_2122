import json
import requests


url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)  # подключаюсь к сайту в переменной url
todo = json.loads(response.text)
# ^ превращаю ответ сервера в json-файл
for smth in todo:
    if (smth['userId'] == 4) and (not smth['completed']):
        print(smth)
"""Выводить задачи пользователя с ID=4, которые он не выполнил"""
