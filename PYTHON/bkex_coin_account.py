import websocket
import json
from threading import Timer
from bkex.PYTHON import bkex_api_sign
import time

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

ACCESS_KEY = "自己的Access Key"


def on_message(ws, message):
    if message.startswith(PRE_0):
        ws.send(PRE_40_ACCOUNT)
    elif message.startswith(PRE_40) and not message.startswith(PRE_40_ACCOUNT):
        user_login()

    elif message.startswith(PRE_42_ACCOUNT):
        json_str = message[len(PRE_42_ACCOUNT) + 1:]
        print('account message: ' + json_str)

        jsonObj = json.loads(json_str)

        eventType = jsonObj[0]

        print(eventType)
        # 用户余额变更
        ws.send(PRE_42_ACCOUNT + ',["' + EVENT_SUB_ACCOUNT + '"]')
        # 用户订单变更
        ws.send(PRE_42_ACCOUNT + ',["' + EVENT_SUB_USER_ORDER + '"]')

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


# 登录
def user_login():
    current_time = str(int(round(time.time() * 1000)))
    ws.send(PRE_42_ACCOUNT + ',["userLogin",{"signature":"' + bkex_api_sign.get_sign(API_ENDPOINT + "?timestamp=" + current_time) + '",'
            '"accessKey":"' + ACCESS_KEY + '","timestamp":' + current_time + '}]')


def send_pong():
    ws.send('pong')


sTimer = Timer(3, send_pong)
sTimer.start()

ws.run_forever()
