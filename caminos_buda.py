import requests
import json
from numpy import * 
import funciones
import robot



camino = []
camino = array( [
    ["btc-cop","btc-clp","ltc-clp","ltc-cop"], 
    ["btc-cop","btc-clp","bch-clp","bch-cop"], 
    ["btc-cop","btc-clp","eth-clp","eth-cop"],
    ["btc-cop","btc-clp","usdc-clp","usdc-cop"],

    ["btc-cop","btc-pen","ltc-pen","ltc-cop"], 
    ["btc-cop","btc-pen","bch-pen","bch-cop"], 
    ["btc-cop","btc-pen","eth-pen","eth-cop"],
    ["btc-cop","btc-pen","usdc-pen","usdc-cop"],

    ["btc-cop","btc-ars","ltc-ars","ltc-cop"], 
    ["btc-cop","btc-ars","bch-ars","bch-cop"], 
    ["btc-cop","btc-ars","eth-ars","eth-cop"],
    ["btc-cop","btc-ars","usdc-ars","usdc-cop"],

    ["eth-cop","eth-clp","ltc-clp","ltc-cop"], 
    ["eth-cop","eth-clp","bch-clp","bch-cop"], 
    ["eth-cop","eth-clp","eth-clp","eth-cop"],
    ["eth-cop","eth-clp","usdc-clp","usdc-cop"],

    ["eth-cop","eth-pen","ltc-pen","ltc-cop"], 
    ["eth-cop","eth-pen","bch-pen","bch-cop"], 
    ["eth-cop","eth-pen","eth-pen","eth-cop"],
    ["eth-cop","eth-pen","usdc-pen","usdc-cop"],

    ["eth-cop","eth-ars","ltc-ars","ltc-cop"], 
    ["eth-cop","eth-ars","bch-ars","bch-cop"], 
    ["eth-cop","eth-ars","eth-ars","eth-cop"],
    ["eth-cop","eth-ars","usdc-ars","usdc-cop"],

    ["ltc-cop","ltc-clp","ltc-clp","ltc-cop"], 
    ["ltc-cop","ltc-clp","bch-clp","bch-cop"], 
    ["ltc-cop","ltc-clp","eth-clp","eth-cop"],
    ["ltc-cop","ltc-clp","usdc-clp","usdc-cop"],

    ["ltc-cop","ltc-pen","ltc-pen","ltc-cop"], 
    ["ltc-cop","ltc-pen","bch-pen","bch-cop"], 
    ["ltc-cop","ltc-pen","eth-pen","eth-cop"],
    ["ltc-cop","ltc-pen","usdc-pen","usdc-cop"],

    ["ltc-cop","ltc-ars","ltc-ars","ltc-cop"], 
    ["ltc-cop","ltc-ars","bch-ars","bch-cop"], 
    ["ltc-cop","ltc-ars","eth-ars","eth-cop"],
    ["ltc-cop","ltc-ars","usdc-ars","usdc-cop"],

    ["bch-cop","bch-clp","ltc-clp","ltc-cop"], 
    ["bch-cop","bch-clp","bch-clp","bch-cop"], 
    ["bch-cop","bch-clp","eth-clp","eth-cop"],
    ["bch-cop","bch-clp","usdc-clp","usdc-cop"],

    ["bch-cop","bch-pen","ltc-pen","ltc-cop"], 
    ["bch-cop","bch-pen","bch-pen","bch-cop"], 
    ["bch-cop","bch-pen","eth-pen","eth-cop"],
    ["bch-cop","bch-pen","usdc-pen","usdc-cop"],

    ["bch-cop","bch-ars","ltc-ars","ltc-cop"], 
    ["bch-cop","bch-ars","bch-ars","bch-cop"], 
    ["bch-cop","bch-ars","eth-ars","eth-cop"],
    ["bch-cop","bch-ars","usdc-ars","usdc-cop"],


    ]
    )


saldo_inicial = 100000


while True:
    for y in camino:
        comp1 = funciones.cotizacion_bid(saldo_inicial,y[0])
        vend1 = funciones.cotizacion_ask(comp1,y[1])
        comp2 = funciones.cotizacion_bid(vend1,y[2])
        vend2 = funciones.cotizacion_ask(comp2,y[3])

        #print(" " + str(comp1) + " " + str(vend1) + " "+ str(comp2) + " "+ str(vend2))

        if (vend2 > saldo_inicial):
                        funciones.dump (funciones.green(str(y)) + "  Saldo final  \t" + str(vend2) + "  \t"+ funciones.green(str(int(vend2 - saldo_inicial )))+ "--------Opordunidad--------")
                        robot.mensaje(str(y) + str(int(vend2 - saldo_inicial)))

        else:
                        funciones.dump (funciones.red(str(y)) + "  Saldo final  \t" + str(vend2) + "  \t" + funciones.red(str(int(vend2 - saldo_inicial))))
                        #robot.mensaje(str(y) + str(int(vend2 - saldo_inicial)))