import requests
from urllib import parse
import json
from bkex.PYTHON import bkex_api_sign

# 币币交易

API_ENDPOINT = "https://api.bkex.co"
ACCESS_KEY = "自己的Access Key"

# 下单
CREATE_ORDER = "/v2/u/order/create"
# 撤销下单
CANCEL_ORDER = "/v2/u/order/cancel"
# 查询当前未完成订单
OPEN_ORDERS = "/v2/u/order/openOrders"
# 查询未完成订单订单
OPEN_ORDER_DETAIL = "/v2/u/order/openOrder/detail"
# 查询历史订单
HISTORY_ORDER = "/v2/u/order/historyOrders"
# 批量下单
BATCH_CREATE_ORDER = "/v2/u/order/batchCreate"
# 批量撤销订单
BATCH_CANCEL_ORDER = "/v2/u/order/batchCancel"


def create_order():
    url = API_ENDPOINT + CREATE_ORDER
    data = {
      "volume": 0.1,
      "price": 7000.12,
      "direction": "ASK",
      "symbol": "BTC_USDT",
      "source": "WALLET",
      "type": "STOP_LIMIT",
      "stopPrice": 6900,
      "operator": "gte",
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


def cancel_order():
    url = API_ENDPOINT + CANCEL_ORDER + "?orderId=2213"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.post(url=url, headers=headers)
    print(res.text)


def get_open_orders():
    url = API_ENDPOINT + OPEN_ORDERS
    data = {
       "symbol": "BTC_USDT",
       "direction": "ASK",
       "source": "WALLET",
       "type": "LIMIT",
       "sortingWay": "TIME_ASC",
       "page": 1,
       "size": 10
    }
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url + "?" + data),
    }
    res = requests.get(url=url + "?" + data, headers=headers)
    print(res.text)


def get_open_order_detail():
    url = API_ENDPOINT + OPEN_ORDER_DETAIL + "?orderId=2213"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.get(url=url, headers=headers)
    print(res.text)


def get_history_orders():
    url = API_ENDPOINT + HISTORY_ORDER
    data = {
        "symbol": "BTC_USDT",
        "direction": "ASK",
        "type": "LIMIT",
        "sortingWay": "TIME_ASC",
        "filterCancelAll": "true",
        "page": 1,
        "size": 10,
        "startTime": 1532331292000,
        "endTime": 1532331295000
    }
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url + "?" + data),
    }
    res = requests.get(url=url + "?" + data, headers=headers)
    print(res.text)


def batch_create_order():
    data = [
        {
            "volume": 0.1,
            "price": 7000.12,
            "direction": "ASK",
            "symbol": "BTC_USDT",
            "source": "WALLET",
            "type": "STOP_LIMIT",
            "stopPrice": "6900",
            "operator": "lte"
        },
        {
            "volume": 0.1,
            "price": 7000.12,
            "direction": "ASK",
            "symbol": "BTC_USDT",
            "source": "WALEET",
            "type": "STOP_LIMIT",
            "stopPrice": "6900",
            "operator": "lte"
        }
    ]
    url = API_ENDPOINT + BATCH_CREATE_ORDER + "?orders=" + json.dumps(data)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.post(url=url, headers=headers)
    print(res.text)


def batch_cancel_order():
    order_ids = [
        "2018062321121231231", "2018062321121231232"
    ]
    url = API_ENDPOINT + BATCH_CANCEL_ORDER + "?orders=" + json.dumps(order_ids)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }
    res = requests.post(url=url, headers=headers)
    print(res.text)


# create_order()
# cancel_order()
# get_open_orders()
# get_open_order_detail()
# get_history_orders()
# batch_create_order()
batch_cancel_order()
