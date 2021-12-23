import requests
import json
from numpy import * 
import funciones
import ccxt
import robot
import time
import matplotlib.pyplot as plt

while True:
    time.sleep(10)
    BTC = funciones.tasaimplicita('BTC','COP')
    LTC = funciones.tasaimplicita('LTC','COP')
    ETH = funciones.tasaimplicita('ETH','COP')
    BCH = funciones.tasaimplicita('BCH','COP')

    if LTC >= 4100 :
        print("--Arbitraje con LTC--")
    print ("BTC/COP : " + str(BTC)+ " LTC : " + str(LTC) + " ETH : " + str(ETH) + " BCH : " + str(BCH) + " BTC-LTC:" + str(BTC-LTC) + " LTC-ETH: " + str(LTC - ETH) + " BTC-ETH:" + str(BTC-ETH) + " BCH-BTC:" + str(BCH-BTC))
    #print ("BTC/CLP : " + str(funciones.tasaimplicita('BTC','CLP'))+ " LTC : " + str(funciones.tasaimplicita('LTC','CLP')) + " ETH : " + str(funciones.tasaimplicita('ETH','CLP')))
    #print ("BTC/ARS : " + str(funciones.tasaimplicita('BTC','ARS'))+ " LTC : " + str(funciones.tasaimplicita('LTC','ARS')) + " ETH : " + str(funciones.tasaimplicita('ETH','ARS')))
    #print ("BTC/PEN : " + str(funciones.tasaimplicita('BTC','PEN'))+ " LTC : " + str(funciones.tasaimplicita('LTC','PEN')) + " ETH : " + str(funciones.tasaimplicita('ETH','PEN')))
    #print("\n\n")