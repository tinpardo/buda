import requests
import json
import keyboard

for x in range(3):


    pesos_iniciales = 10000

    #compramos LTC de COP
    market_id = 'ltc-cop'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_ltc_cop = solicitud["ticker"]["min_ask"][0]
    cantidad_ltc = int(pesos_iniciales) / float(precio_ltc_cop)
    print("\n\nCompra de LTC con COP: \t" + str(cantidad_ltc) + " \t\t-- Precio: " + precio_ltc_cop)


    #vendemos LTC-CLP
    market_id = 'ltc-clp'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_ltc_clp = solicitud["ticker"]["max_bid"][0]
    cantidad_clp = cantidad_ltc * float(precio_ltc_clp)
    print("Venta LTC a CLP: \t" + str(cantidad_clp) + " \t\t-- Precio: " + precio_ltc_clp)

    #compramos BCH-CLP
    market_id = 'bch-clp'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_bch_clp = solicitud["ticker"]["min_ask"][0]
    cantidad_bch = cantidad_clp / float(precio_bch_clp)
    print("Compra BCH con CLP: \t" + str(cantidad_bch) + " \t\t-- Precio: " + precio_bch_clp)

    #vendemos BCH-COP
    market_id = 'bch-cop'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_bch_cop = solicitud["ticker"]["max_bid"][0]
    cantidad_cop = cantidad_bch * float(precio_bch_cop)
    print("Venta de BCH en COP: \t" + str(cantidad_cop) + " \t\t-- Precio: " + precio_bch_cop)






    pesos_iniciales = 10000

    #compramos BCH de COP
    market_id = 'bch-cop'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_bch_cop = solicitud["ticker"]["min_ask"][0]
    cantidad_bch = int(pesos_iniciales) / float(precio_bch_cop)
    print("\n\nXXXXXX -----Compra de LTC con COP: \t" + str(cantidad_bch) + " \t\t-- Precio: " + precio_bch_cop)


    #vendemos BCH-CLP
    market_id = 'BCH-clp'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_bc_clp = solicitud["ticker"]["max_bid"][0]
    cantidad_clp = cantidad_bch * float(precio_bch_clp)
    print("Venta LTC a CLP: \t" + str(cantidad_clp) + " \t\t-- Precio: " + precio_bch_clp)

    #compramos ETH-CLP
    market_id = 'eth-clp'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_eth_clp = solicitud["ticker"]["min_ask"][0]
    cantidad_eth = cantidad_clp / float(precio_eth_clp)
    print("Compra BCH con CLP: \t" + str(cantidad_eth) + " \t\t-- Precio: " + precio_eth_clp)

    #vendemos BCH-COP
    market_id = 'eth-cop'
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    solicitud = requests.get(url).json()
    precio_eth_cop = solicitud["ticker"]["max_bid"][0]
    cantidad_cop = cantidad_eth * float(precio_eth_cop)
    print("Venta de BCH en COP: \t" + str(cantidad_cop) + " \t\t-- Precio: " + precio_eth_cop)

    print("\n\n\n" + str(solicitud) + "\n\n\n\n")