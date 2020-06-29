import requests

# 行情数据

API_ENDPOINT = "https://api.bkex.co"

# k线数据
KLINE_URL = "/v2/q/kline"
# 24小时行情
HOURS_24_URL = "/v2/q/tickers"
# 最新成交价
PRICE_URL = "/v2/q/ticker/price"
# 交易对深度数据
DEPTH_URL = "/v2/q/depth"
# 最近成交记录
DEALS_URL = "/v2/q/deals"

res = requests.get(API_ENDPOINT + KLINE_URL + '?period=1m&size=200&symbol=BTC_USDT&from=1529739295000&to=1532331295000')
print(res.text)

res = requests.get(API_ENDPOINT + HOURS_24_URL + '?symbol=BTC_USDT')
print(res.text)

res = requests.get(API_ENDPOINT + PRICE_URL + '?symbol=BTC_USDT')
print(res.text)

res = requests.get(API_ENDPOINT + DEPTH_URL + '?symbol=BTC_USDT&depth=20&precision=4')
print(res.text)

res = requests.get(API_ENDPOINT + DEALS_URL + '?symbol=BTC_USDT&size=20')
print(res.text)
