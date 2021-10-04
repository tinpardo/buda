import requests

market = 'btc-cop'
url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
response = requests.post(url, json={
    'type': 'bid_given_value',
    'amount': 170000000,
})

respuesta = response.json()

BTC_comprados = respuesta["quotation"]["base_balance_change"][0]



print(respuesta["quotation"]["base_balance_change"][0])

