import websocket
import json
from threading import Timer

PRE_0 = "0"
PRE_40 = "40"
PRE_40_QUOTATION = "40/quotation"
PRE_42_QUOTATION = "42/quotation"

# api url
API_ENDPOINT = "api.bkex.co"

# 币币行情 - k线数据
EVENT_SUB_KLINE = "subKlineByRange"
# 币币行情 - 24小时行情
EVENT_24HOUR = "subQuotationSymbol"
# 币币行情 - 订单深度行情数据
EVENT_SUB_ORDER = "subOrderDepth"
# 币币行情 - 成交明细
EVENT_DEAL = "quotationDealConnect"


def on_message(ws, message):

    if message.startswith(PRE_0):
        ws.send(PRE_40_QUOTATION)
    elif message.startswith(PRE_40) and not message.startswith(PRE_40_QUOTATION):
        get_coin_quotes()

    elif message.startswith(PRE_42_QUOTATION):
        json_str = message[len(PRE_42_QUOTATION) + 1:]
        print('quotation message: ' + json_str)

        json_obj = json.loads(json_str)

        event_type = json_obj[0]

        print(event_type)

    else:
        print(message)


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


# 币币行情
def get_coin_quotes():
    # 币币行情 － k线
    ws.send(
        PRE_42_QUOTATION + ',["' + EVENT_SUB_KLINE + '",{"symbol":"BTC_USDT","period":"5","from":1590131227,"to":1590217687,"no":"159021762728850476"}]')
    # 币币行情 － 24小时行情
    ws.send(PRE_42_QUOTATION + ',["' + EVENT_24HOUR + '"]')
    # 币币行情 － 深度行情
    ws.send(PRE_42_QUOTATION + ',["' + EVENT_SUB_ORDER + '",{"symbol":"BTC_USDT,ETH_USDT","number":50}]')
    # 币币行情 － 成交明细
    ws.send(PRE_42_QUOTATION + ',["' + EVENT_DEAL + '",{"symbol":"BTC_USDT,ETH_USDT","number":50}]')


def send_pong():
    ws.send('pong')


sTimer = Timer(3, send_pong)
sTimer.start()

ws.run_forever()
