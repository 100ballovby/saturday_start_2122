import requests as r

base_currency = 'USD'
symbols = 'EUR,GBP,AED'
endpoint = 'latest'
key = ''
url = f'https://commodities-api.com/api/{endpoint}?access_key={key}&base={base_currency}&symbols={symbols}'

resp = r.get(url)
print(resp.json())

