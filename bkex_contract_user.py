import websocket
import json
from threading import Timer
import requests
from bkex import bkex_api_sign

# api url
API_ENDPOINT = "https://api.bkex.co"
WSS_ENDPOINT = "api.bkex.co/contract/u/ws/"
LISTEN_KEY_URL = "/v2/contract/ws/dataStream/create"

ACCESS_KEY = "83b640bae45698056761db3d74a9ed8de8e82d822fa955c48cb12a2692c8d890"
SECRET_KEY = "4342537ef584d9bfabff473fc51deb154fb371dc9f2c88d72bd83512e0bf064f"


# 获取签名
# def get_sign(url):
#     params_arr = url.split("?")
#     source = ""
#     if len(params_arr) > 1:
#         param = params_arr[1]
#         unsorted_arr = param.split("&")
#         source = "&".join(sorted(unsorted_arr))
#         print(source)
#     sign = hmac.new(bytes(SECRET_KEY, encoding='utf-8'), bytes(source, encoding='utf-8'), sha256).hexdigest()
#     print("sign: " + sign)
#     return sign


# 创建listen_key
def get_listen_key():
    url = API_ENDPOINT + LISTEN_KEY_URL + "?recvWindow=500"
    data = {
        'recvWindow': 500,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    # 调用创建listen_key接口
    response = requests.post(url=API_ENDPOINT + LISTEN_KEY_URL, headers=headers, data=data)

    # 转换为json解析
    res = json.loads(response.text)
    listen_key = ''
    if res['code'] == 0:
        obj = res['data']
        listen_key = obj['listenKey']
        print("listen_key: " + listen_key)
    return listen_key


def on_message(ws, message):
    print("onMessage: " + message)
    get_contract_user()


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://" + WSS_ENDPOINT + get_listen_key(),
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)


# 合约用户
def get_contract_user():
    # 账户更新
    ws.send('outboundAccountInfo')
    ws.send('contractExecutionReport')
    ws.send('outboundContractPositionInfo')


def send_pong():
    ws.send('pong')


sTimer = Timer(3, send_pong)
sTimer.start()

ws.run_forever()
