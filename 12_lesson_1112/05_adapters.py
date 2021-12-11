import requests
from requests.adapters import HTTPAdapter  # набор конфигураций для службы

git_a = HTTPAdapter(max_retries=4)  # адаптер подключения
session = requests.Session()  # сессия подключения

url = 'https://api.github.com'
session.mount(url, git_a)  # использую HTTP адаптер при подключении к данному URL

session.get(url)
