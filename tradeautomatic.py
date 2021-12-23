import requests
import json
from numpy import * 
import funciones
import ccxt
import robot
import time
import matplotlib.pyplot as plt


funciones.limpiarordenes()


saldo_inicial = 187000000
#saldo_inicial_dolares = 45000
#preciodolar = funciones.precio_dolar()
preciodolar = 3780
print(preciodolar)
#budaBTCCOP = funciones.btcbuda_bid(saldo_inicial) * preciodolar #cantidad de BTC comprados en Buda
binance = ccxt.binance()
binanceBTCCOP_anterior_ask = 50000
binanceBTCCOP_anterior_bid = 50000

while True:
    orderbook_binance = binance.fetch_order_book('BTC/USDT')
    precioventaBTC_binance_ask = orderbook_binance["asks"][0][0] 
    precioventaBTC_binance_bid = orderbook_binance["bids"][0][0] 

    binanceBTCCOP_ask = int(preciodolar) * int(precioventaBTC_binance_ask)
    binanceBTCCOP_bid = int(preciodolar) * int(precioventaBTC_binance_bid)

    time.sleep(5)

    if ( binanceBTCCOP_anterior_ask != binanceBTCCOP_ask):
        funciones.limpiar_ordenes_ask('btc-cop')
        punta_venta = binanceBTCCOP_ask + (binanceBTCCOP_ask * 10 / 100)
        print(punta_venta)
        funciones.orden_venta_limite('btc-cop', punta_venta, 0.00004)

    if ( binanceBTCCOP_anterior_bid != binanceBTCCOP_bid):
        funciones.limpiar_ordenes_bid('btc-cop')
        punta_compra = binanceBTCCOP_bid - (binanceBTCCOP_bid * 10 / 100)
        print(punta_compra)
        funciones.orden_compra_limite('btc-cop', punta_compra, 0.00004)

    binanceBTCCOP_anterior_ask = binanceBTCCOP_ask
    binanceBTCCOP_anterior_bid = binanceBTCCOP_bid