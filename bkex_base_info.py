import requests

# 基础信息

API_ENDPOINT = "https://api.bkex.co"

# 所有交易对
SYMBOLS_URL = "/v2/common/symbols"
# 所有币种
CURRENCYS_URL = "/v2/common/currencys"
# 服务器时间戳
TIMESTAMP_URL = "/v2/common/timestamp"

res = requests.get(API_ENDPOINT + SYMBOLS_URL)
print(res.text)

res = requests.get(API_ENDPOINT + CURRENCYS_URL)
print(res.text)

res = requests.get(API_ENDPOINT + TIMESTAMP_URL)
print(res.text)

