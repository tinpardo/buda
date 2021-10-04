import requests
import json
from numpy import * 
import funciones
import ccxt
import robot
import time
import matplotlib.pyplot as plt


i = 0
x = 0
y = 0
#bids = lo compran, asks= lo venden
while True:
    saldo_inicial = 5000000
    #saldo_inicial_dolares = 45000
    preciodolar = 3780

    budaBTCCOP = funciones.btcbuda_bid(saldo_inicial)


    binance = ccxt.binance()
    orderbook_binance = binance.fetch_order_book('BTC/USDT')
    precioventaBTC_binance = orderbook_binance["asks"][0][0]
    time.sleep(1)
    #preciocompraBTC_binance = orderbook_binance["bids"][0][0]
    #cantidadBTC_binance = saldo_inicial_dolares / preciocompraBTC_binance
    #budaCOPBTC = funciones.btcbuda_ask(cantidadBTC_binance)
    #print("Saldo final COP BUDA" + str(budaCOPBTC))
    #time.sleep(1)
    binanceBTCUSDT = float(budaBTCCOP) * float(precioventaBTC_binance)
    final = binanceBTCUSDT * preciodolar
    
    print("Tasa Implicita BTC:" + str(int(saldo_inicial / binanceBTCUSDT)) + " Tasa Implicita USD:" + str(int(final / binanceBTCUSDT)))
    print("Inicial: " + str(saldo_inicial) + " BTC Buda : " + str(budaBTCCOP) + " USD Binance " + str(binanceBTCUSDT) + " a precio " + str(precioventaBTC_binance))
    if (saldo_inicial > final):
        funciones.dump(funciones.red("Final desde Buda: " + str(int(final)) + "  ->> " + str(int(final - saldo_inicial)) + "\n"))
        #robot.mensaje(str("Final  : " + str(int(final)) + "  ->> " + str(int(final - saldo_inicial))))
    else:
        funciones.dump(funciones.green("Final desde Buda : " + str(int(final)) + "  ->> " + str(int(final - saldo_inicial)) + "\n\n\n"))
        robot.mensaje(str("Hay arbitraje Final  : " + str(int(final)) + "  ->> " + str(int(final - saldo_inicial))))


    #print("Binance bids: " + str(orderbook_binance["bids"][0][0]))
    #print("Binance asks: " + str(orderbook_binance["asks"][0][0]))




    


