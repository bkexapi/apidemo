import websocket
import json
from threading import Timer

# api url
API_ENDPOINT = "api.bkex.cc/contract/q/ws"


def on_message(ws, message):
    print("onMessage: " + message)
    get_contract_quotation()


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://" + API_ENDPOINT + "/socket.io/?EIO=3&transport=websocket",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)


# 合约行情
def get_contract_quotation():
    # 全量深度
    ws.send(get_json_str('depth'))

    # symbol的ticker信息
    ws.send(get_json_str('realtimes'))

    # 逐笔交易
    ws.send(get_json_str('trade'))

    # 订单簿ticker信息
    ws.send(get_json_str('bookTicker'))

    # K线/蜡烛图
    data = {
        "topic": "kline",
        "event": "sub",
        "params": {
            "binary": "false",
            "symbol": "BTC-SWAP-USDT",
            "klineType": "1m"
        }
    }
    ws.send(json.dumps(data, indent=2))


def send_pong():
    ws.send('pong')


def get_json_str(topic):
    data = {
        "topic": topic,
        "event": "sub",
        "params": {
            "binary": "false",
            "symbol": "BTC-SWAP-USDT"
        }
    }
    return json.dumps(data, indent=2)


sTimer = Timer(3, send_pong)
sTimer.start()

ws.run_forever()
