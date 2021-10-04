import requests
import json
from numpy import * 
import funciones
import ccxt
import robot
import time
import matplotlib.pyplot as plt


binance = ccxt.binance()
orderbook_binance = binance.fetch_order_book('BTC/USDT')
precioventaBTC_binance = orderbook_binance["asks"][0][0]


buda = ccxt.buda()
orderbook_buda = buda.fetch_order_book('BTC/COP')
precioventaBTC_buda = orderbook_buda["asks"][0][0]
print("Precio BTC/COP Buda: " + str(precioventaBTC_buda))

#dolar = float(funciones.precio_dolar())
dolar = 3780


#venta
#190.000.000 + 5% - dinámico     (offer 49460 * 3780) + 10%

#Binance 186955020  -----> compra 49459 bid     offer 49460 * 3780

#compra  = Binance - 5%   --- dinámico    precio de compra     (bid 49459 * 3780) - 10%
#170.000.000




print(str(dolar))

precioequivalente = int(precioventaBTC_binance) * int(dolar)

print("Precio equivalente BTC/COP Binance: " + str(int(precioequivalente)) + " -> dolar a: " + str(dolar) + " precio BTC/USD" + str(precioventaBTC_binance) + " diferencia: " + str(int(precioequivalente - precioventaBTC_buda)))