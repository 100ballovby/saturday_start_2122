import requests as r


def get_rates(base, target):
    url = 'https://api.coinbase.com/v2/exchange-rates'
    params = {'currency': base}
    response = r.get(url, params=params)
    rates = response.json()
    if target in rates['data']['rates']:
        return rates['data']['rates'][target]
    else:
        return 'Error!'

rates = get_rates('USD', 'CHF')
print(rates)
