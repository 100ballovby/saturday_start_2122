import requests

url = 'https://api.github.com'
response = requests.get(url, verify=False)

print(response)


