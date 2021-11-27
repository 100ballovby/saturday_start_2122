import json
import requests


url = 'https://api.github.com/users/GreatRaksin/repos'
response = requests.get(url)  # подключаюсь к сайту в переменной url
repositories = json.loads(response.text)
print(repositories)
for repo in repositories:
    print(repo['svn_url'])  # получаю ссылку на репозиторий

"""Необходимо найти все репозитории, где главным язком программирования
является Python. А затем вывести эти репозитории в формате: 

Name: {name}
URL: {svn_url}
Language: {language}

!!!!🤩🤩🤩🤩!!!!
Сделать список словарей, который будет хранить всю 
информацию из первой части задачи 
"""
