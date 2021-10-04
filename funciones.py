import os
import sys
import config
import requests
import json
from numpy import * 
import base64
import hmac
import time
import requests.auth

class BudaHMACAuth(requests.auth.AuthBase):
    """Adjunta la autenticación HMAC de Buda al objeto Request."""

    def __init__(self, api_key: str, secret: str):
        self.api_key = api_key
        self.secret = secret

    def get_nonce(self) -> str:
        # 1. Generar un nonce (timestamp en microsegundos)
        return str(int(time.time() * 1e6))

    def sign(self, r, nonce: str) -> str:
        # 2. Preparar string para firmar
        components = [r.method, r.path_url]
        if r.body:
            encoded_body = base64.b64encode(r.body).decode()
            components.append(encoded_body)
        components.append(nonce)
        msg = ' '.join(components)
        # 3. Obtener la firma
        h = hmac.new(key=self.secret.encode(),
                        msg=msg.encode(),
                        digestmod='sha384')
        signature = h.hexdigest()
        return signature

    def __call__(self, r):
        nonce = self.get_nonce()
        signature = self.sign(r, nonce)
        # 4. Adjuntar API-KEY, nonce y firma al header del request
        r.headers['X-SBTC-APIKEY'] = self.api_key
        r.headers['X-SBTC-NONCE'] = nonce
        r.headers['X-SBTC-SIGNATURE'] = signature
        return r

def btcbuda_bid(cantidad):
    market = 'btc-cop'
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    try:
        response = requests.post(url, json={
            'type': 'bid_given_value',
            'amount': cantidad,
        }, auth=BudaHMACAuth(config.apiKey, config.secret))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    #print (response.content)
    respuesta = response.json()
    #print(response)
    BTC_comprados = respuesta["quotation"]["base_balance_change"][0]
    return float(BTC_comprados)

def btcbuda_ask(cantidad):
    market = 'btc-cop'
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    response = requests.post(url, json={
        'type': 'ask_given_value',
        'amount': cantidad,
    })
    
    respuesta = response.json()
   # print(response)
    BTC_comprados = respuesta["quotation"]["base_balance_change"][0]
    return float(BTC_comprados)

def cotizacion_bid(cantidad, market):
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    try:
        response = requests.post(url, json={
            'type': 'bid_given_value',
            'amount': cantidad,
        })
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    time.sleep(0.2)
    respuesta = response.json()
    #print(response.content)
    BTC_comprados = respuesta["quotation"]["base_balance_change"][0]
    return float(BTC_comprados)

def cotizacion_ask(cantidad, market):
    url = f'https://www.buda.com/api/v2/markets/{market}/quotations'
    try:
        response = requests.post(url, json={
            'type': 'ask_given_size',
            'amount': cantidad,
        })
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    time.sleep(0.2)
    respuesta = response.json()
    #print(response.content)
    BTC_comprados = respuesta["quotation"]["quote_balance_change"][0]
    return float(BTC_comprados)

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


exchange = ccxt.buda({
    'apiKey': config.apiKey,
    'secret': config.secret,
    'enableRateLimit': True,
})

exchange_binance = exchange = ccxt.binance({
    'apiKey_Binance': config.apiKey,
    'secret_Binance': config.secret,
    'enableRateLimit': True,
})


# def orden_compra_mercado(simbolo,cantidad):
#     symbol = simbolo
#     type = 'market'  # or 'market'
#     side = 'buy'  # or 'buy'
#     amount = cantidad
#     #price = 3700  # or None
#     # extra params and overrides if needed
#     params = {
#         'test': True,  # test if it's valid, but don't actually place it
#     }
#    # order = exchange.create_market_buy_order(symbol, float(cantidad))
#   #  print(order)

# def orden_venta_mercado(simbolo,cantidad):
#     symbol = simbolo
#     type = 'market'  # or 'market'
#     side = 'sell'  # or 'buy'
#     amount = float(cantidad)
#     #price = 3700  # or None

#     # extra params and overrides if needed
#     params = {
#         'test': True,  # test if it's valid, but don't actually place it
#     }

  #  order = exchange.create_market_sell_order(symbol, amount)

   # print(order)


# url = 'https://www.buda.com/api/v2/markets'
# response = requests.get(url).json()
# total = {}

# for x in response["markets"]:
#     url = f'https://www.buda.com/api/v2/markets/{x["name"]}/order_book'
#     res = requests.get(url).json()
#     #print(x["name"])
#     total[x["name"]] = res["order_book"]

# def comprar(cantidad, mercado):
#     precio = float(total[mercado]['asks'][0][0])
#     #print (mercado + " Precio compra: " + str(precio) + "   " + str(cantidad))
#     return float(cantidad) / precio

# def vender(cantidad, mercado):
#     precio = float(total[mercado]['bids'][0][0])
#     #print (mercado + " Precio venta: " + str(precio)  + "   " + str(cantidad))
#     return float(cantidad) * precio

def dump(*args):
    print(' '.join([str(arg) for arg in args]))

def style(s, style):
    return style + s + '\033[0m'

def green(s):
    return style(s, '\033[92m')


def blue(s):
    return style(s, '\033[94m')


def yellow(s):
    return style(s, '\033[93m')


def red(s):
    return style(s, '\033[91m')


def pink(s):
    return style(s, '\033[95m')


def obtenerpreciodolarCMA():
    url_aut = 'https://strfeedny02.cma.com.br/execute?JSONRequest={"name":"LoginADVRequest", "sessionId":"", "sync":true, "type":"c", "advUser":"STRFEEDALGOCODEX01","advPsw":"", "id":1}'
    response = requests.post(url_aut)
    print(response.content)

def precio_dolar():
    url_aut = 'https://strfeedny02.cma.com.br/execute?JSONRequest={"name":"LoginADVRequest", "sessionId":"", "sync":true, "type":"c", "advUser":"STRFEEDALGOCODEX01","advPsw":"", "id":1}'
    response = requests.get(url_aut)
    sessid = response.json()
    #print(sessid["sessionId"])
    url_precio = 'https://strfeedny02.cma.com.br/execute?JSONRequest={"id":24,"name":"QuotesRequest","sessionId":"' + sessid["sessionId"] + '","type":"n","sync":true,"timeoutHandler":120,"failActionType":"alert","fields":"","realtime":true,"symbols":[{"sourceId":"31","symbol":"DOLAR SPOT"}],"sign":true}'
    response_precio = requests.get(url_precio)
    preciodolarCMA = response_precio.json()
    #print(response_precio.content)
    return (preciodolarCMA["arrQuotes"][0]["arrValues"][9]["14"])