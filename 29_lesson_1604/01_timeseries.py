import requests as r
import json

base_currency = 'USD'
symbols = 'NG'  # XAU - золото, SUGAR - сахар, COTTON - хлопок, NG - газ
endpoint = 'timeseries'
key = ''
start = '2021-04-15'
end = '2022-04-15'
url = f'https://commodities-api.com/api/{endpoint}?access_key={key}&start_date={start}&end_date={end}&symbols={symbols}'


resp = r.get(url)
with open('series_NG.json', 'w') as file:
    res = resp.text
    file.write(res)

