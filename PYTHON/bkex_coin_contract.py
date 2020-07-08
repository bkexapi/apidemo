import requests
from urllib import parse
from PYTHON import bkex_api_sign

# 合约交易

API_ENDPOINT = "https://api.bkex.co"
ACCESS_KEY = "自己的Access Key"

# 公共 - Broker交易信息(合约)
COMMON_BROKER_INFO = "/v2/contract/common/brokerInfo"
# 公共 - 指数价格
INDEX_PRICE = "/v2/contract/q/index"
# 公共 - 订单簿
ORDER_BOOK = "/v2/contract/q/depth"
# 公共 - 最新成交
LATEST_DEAL = "/v2/contract/q/trades"
# 公共 - KLINE
KLINE = "/v2/contract/q/kline"
# 公共 - ticker24小时价格变化
TICKER_24HR = "/v2/contract/q/ticker24hr"

# 合约 - 创建新订单
TRADE_ORDER = "/v2/contract/trade/order"
# 合约 - 订单信息
TRADE_GET_ORDER = "/v2/contract/trade/getOrder"
# 合约 - 撤销订单
TRADE_CANCEL_ORDER = "/v2/contract/trade/orderCancel"
# 合约 - 当前订单
CURRENT_ORDER = "/v2/contract/trade/openOrders"
# 合约 - 历史订单
TRADE_HISTORY_ORDERS = "/v2/contract/trade/historyOrders"
# 合约 - 交易记录
TRADE_RECORD = "/v2/contract/trade/myTrades"
# 合约 - 当前持仓
TRADE_POSITIONS = "/v2/contract/trade/positions"
# 合约 - 更改仓位保证金
TRADE_MODIFY_MARGIN = "/v2/contract/trade/modifyMargin"
# 合约 - 账户信息
USER_ACCOUNT = "/v2/contract/u/account"


def get_common_broker_info():
    res = requests.get(API_ENDPOINT + COMMON_BROKER_INFO)
    print(res.text)


def get_index_price():
    res = requests.get(API_ENDPOINT + INDEX_PRICE)
    print(res.text)


def get_order_book():
    res = requests.get(API_ENDPOINT + ORDER_BOOK + "?symbol=BTC-SWAP&limit=30")
    print(res.text)


def get_lasted_deal():
    res = requests.get(API_ENDPOINT + LATEST_DEAL + "?symbol=BTC-SWAP&limit=30")
    print(res.text)


def get_kline():
    res = requests.get(API_ENDPOINT + KLINE + "?symbol=BTC-SWAP&interval=1m")
    print(res.text)


def get_ticker_24hr():
    res = requests.get(API_ENDPOINT + TICKER_24HR + "?symbol=BTC-SWAP")
    print(res.text)


def trade_order():
    url = API_ENDPOINT + TRADE_ORDER
    data = {
      "symbol": "BTC-SWAP",
      "side": "BUY_OPEN",
      "orderType": "LIMIT",
      "quantity": 10,
      "leverage": 10,
      "clientOrderId": "100011111100001",
      "price": 7928.6,
      "priceType": "INPUT"
    }
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url + "?" + data),
    }
    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)


def get_trade_orders():
    url = API_ENDPOINT + TRADE_GET_ORDER + "?orderId=507904211109878016&orderType=LIMIT"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def trade_cancel_order():
    url = API_ENDPOINT + TRADE_CANCEL_ORDER
    data = {
      "orderType": "LIMIT",
      "orderId": "507904211109878016",
      "clientOrderId": "100011111100001"
    }
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url + "?" + data),
    }
    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)


def get_current_order():
    url = API_ENDPOINT + CURRENT_ORDER + "?symbol=BTC-SWAP&orderType=LIMIT"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def get_history_orders():
    url = API_ENDPOINT + TRADE_HISTORY_ORDERS + "?symbol=BTC-SWAP&orderType=LIMIT"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def get_trade_record():
    url = API_ENDPOINT + TRADE_RECORD + "?symbol=BTC-SWAP&side=LIMIT"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def get_trade_positions():
    url = API_ENDPOINT + TRADE_POSITIONS + "?symbol=BTC-SWAP&side=LONG"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def trade_modify_margin():
    url = API_ENDPOINT + TRADE_MODIFY_MARGIN
    data = {
      "symbol": "BTC-SWAP",
      "amount": 0.2564,
      "side": "LONG"
    }
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url + "?" + data),
    }
    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)


def get_user_account():
    url = API_ENDPOINT + USER_ACCOUNT
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


# get_common_broker_info()
# get_index_price()
# get_order_book()
# get_lasted_deal()
# get_kline()
# get_ticker_24hr()
# trade_order()
# get_trade_orders()
# trade_cancel_order()
# get_current_order()
# get_history_orders()
# get_trade_record()
# get_trade_positions()
# trade_modify_margin()
get_user_account()
