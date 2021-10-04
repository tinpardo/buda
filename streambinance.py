import asyncio

from binance_chain.websockets import BinanceChainSocketManager
from binance_chain.environment import BinanceEnvironment

testnet_env = BinanceEnvironment.get_testnet_env()

address = 'tbnb...'
loop = None

async def main():
    global loop

    async def handle_evt(msg):
        """Function to handle websocket messages
        """
        print(msg)

    # connect to testnet env
    bcsm = await BinanceChainSocketManager.create(loop, handle_evt, address, env=testnet_env)

    # subscribe to relevant endpoints
    await bcsm.subscribe_orders(address)
    await bcsm.subscribe_market_depth(["FCT-B60_BNB", "0KI-0AF_BNB"])
    await bcsm.subscribe_market_delta(["FCT-B60_BNB", "0KI-0AF_BNB"])
    await bcsm.subscribe_trades(["FCT-B60_BNB", "0KI-0AF_BNB"])
    await bcsm.subscribe_ticker(["FCT-B60_BNB", "0KI-0AF_BNB"])

    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(20, loop=loop)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())