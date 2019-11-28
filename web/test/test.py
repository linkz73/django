from BybitWebsocket import BybitWebsocket
import json
import logging
from time import sleep

# ccxt fork install
# pip install git+https://github.com/bybit-exchange/ccxt.git#egg=ccxt



# websocket server address
# Testnet
wsURL = "wss://stream-testnet.bybit.com/realtime"
# Mainnet
# wsURL = "wss://stream.bybit.com/realtime"

def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("[%(asctime)s] %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    logger = setup_logger()
    ws = BybitWebsocket(wsURL=wsURL, api_key=None, api_secret=None)

    # logger.info(ws.ping())
    # {
    #     "success": true,
    #     "ret_msg": "pong",
    #     "request": {
    #         "op": "ping",
    #         "args": null
    #     }
    # }

    # ws.subscribe_orderBookL2("BTCUSD")
    # ws.subscribe_kline("BTCUSD", '1m')
    # ws.subscribe_order()
    # ws.subscribe_execution()
    # ws.subscribe_position()
    # ws.subscribe_instrument_info('BTCUSD')
    # ws.subscribe_insurance()
    # while(1):
    #     logger.info(ws.get_data("orderBookL2_25.BTCUSD"))
    #     logger.info(ws.get_data('kline.BTCUSD.1m'))
    #     logger.info(ws.get_data('order'))
    #     logger.info(ws.get_data("execution"))
    #     logger.info(ws.get_data("position"))
    #     logger.info(ws.get_data("instrument_info.100ms.BTCUSD"))
    #     logger.info(ws.get_data('insurance.BTC'))
    #     logger.info(ws.get_data('insurance.EOS'))
    #     sleep(1)

    # https: // github.com / bybit - exchange / bybit - official - api - docs / blob / master / en / websocket.md  # kline
    # candlechart get
    ws.subscribe_kline("BTCUSD", '1m')
    while (1):
        logger.info(ws.get_data('kline.BTCUSD.1m'))
        sleep(1)

        """
        []
        {'id': 0, 'symbol': 'BTCUSD', 'open_time': 1574940420, 'open': 7481, 'high': 7481, 'low': 7481, 'close': 7481, 'volume': 0, 'turnover': 0, 'interval': '1m'}
        """
