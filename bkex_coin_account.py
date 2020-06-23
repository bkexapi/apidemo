import websocket
import json
from threading import Timer

PRE_0 = "0"
PRE_40 = "40"
PRE_40_ACCOUNT = "40/account"
PRE_42_ACCOUNT = "42/account"

# api url
API_ENDPOINT = "api.bkex.co"

# 币币用户 - 账户余额
EVENT_SUB_ACCOUNT = "subUserAccountInfo"
# 币币用户 - 订单变更
EVENT_SUB_USER_ORDER = "subUserOrderDeal"


def on_message(ws, message):

    if message.startswith(PRE_0):
        ws.send(PRE_40_ACCOUNT)
    elif message.startswith(PRE_40) and not message.startswith(PRE_40_ACCOUNT):
        get_coin_account()

    elif message.startswith(PRE_42_ACCOUNT):
        json_str = message[len(PRE_42_ACCOUNT) + 1:]
        print('account message: ' + json_str)

        jsonObj = json.loads(json_str)

        eventType = jsonObj[0]

        print(eventType)

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


# 币币用户
def get_coin_account():
    # 币币用户 － 账户余额
    ws.send(PRE_42_ACCOUNT + ',["' + EVENT_SUB_ACCOUNT + '"]')
    # 币币用户 － 24小时行情
    ws.send(PRE_42_ACCOUNT + ',["' + EVENT_SUB_USER_ORDER + '"]')


def send_pong():
    ws.send('pong')


sTimer = Timer(3, send_pong)
sTimer.start()

ws.run_forever()
