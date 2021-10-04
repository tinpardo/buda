import requests
import json

def precio_dolar():
    url_aut = 'https://strfeedny02.cma.com.br/execute?JSONRequest={"name":"LoginADVRequest", "sessionId":"", "sync":true, "type":"c", "advUser":"STRFEEDALGOCODEX01","advPsw":"", "id":1}'
    response = requests.get(url_aut)
    sessid = response.json()
    #print(sessid["sessionId"])
    url_precio = 'https://strfeedny02.cma.com.br/execute?JSONRequest={"id":24,"name":"QuotesRequest","sessionId":"' + sessid["sessionId"] + '","type":"n","sync":true,"timeoutHandler":120,"failActionType":"alert","fields":"","realtime":true,"symbols":[{"sourceId":"31","symbol":"DOLAR SPOT"}],"sign":true}'
    response_precio = requests.get(url_precio)
    preciodolarCMA = response_precio.json()
    #print(response_precio.content)
    return (preciodolarCMA["arrQuotes"][0]["arrValues"])

print (precio_dolar())

def btcbuda_ask(cantidad):
    market = 'btc-cop'
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    response = requests.post(url, json={
        'type': 'bid_given_size',
        'amount': cantidad,
    })
    
    respuesta = response.json()
    print(response.content)
    BTC_comprados = respuesta["quotation"]["base_balance_change"][0]
    return float(BTC_comprados)
#while True:
#    print (btcbuda_ask(1))