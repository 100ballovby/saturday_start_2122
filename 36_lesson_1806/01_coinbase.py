import requests as r
import json

url = 'https://api.coinbase.com/v2/currencies'
response = r.get(url)
response_json = response.json()
codes = []
for currency in response_json['data']:
    codes.append(
        {'code': currency['id'],
         'name': currency['name']}
    )
print(codes)