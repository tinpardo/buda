import os
import sys
import config
import requests
import json
from numpy import * 


def cotizacion_ask(cantidad, market):
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    response = requests.post(url, json={
        'type': 'ask_given_size',
        'amount': cantidad,
    })
    respuesta = response.json()
    #print(response.content)
    BTC_comprados = respuesta["quotation"]["quote_balance_change"][0]
    return float(BTC_comprados)

def cotizacion_bid(cantidad, market):
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    response = requests.post(url, json={
        'type': 'bid_given_value',
        'amount': cantidad,
    })
    respuesta = response.json()
    #print(response.content)
    BTC_comprados = respuesta["quotation"]["base_balance_change"][0]
    return float(BTC_comprados)

resultado = cotizacion_bid(1000000, 'btc-cop')
print (resultado)
resultado1 = cotizacion_ask(resultado, 'btc-clp')
print (resultado1)
