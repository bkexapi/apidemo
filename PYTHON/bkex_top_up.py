import requests
import json
import bkex_api_sign

# 账户相关，充值与提现

ACCESS_KEY = "自己的Access Key"

API_ENDPOINT = "https://api.bkex.co"

# API Key
API_KEY_URL = "/v2/u/api/info"
# 账户余额
ACCOUNT_BALANCE_URL = "/v2/u/account/balance"
# 充币地址查询
WALLET_ADDRESS_URL = "/v2/u/wallet/address"
# 充值记录
WALLET_DEPOSIT_RECORD_URL = "/v2/u/wallet/depositRecord"
# 提现记录
WALLET_WITHDRAW_RECORD_URL = "/v2/u/wallet/withdrawRecord"


# API Key权限信息
def get_api_key():
    url = API_ENDPOINT + API_KEY_URL
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    response = requests.get(url=url, headers=headers)

    res = json.loads(response.text)
    print(res['data'])


# 账户余额
def get_account_balance():
    url = API_ENDPOINT + ACCOUNT_BALANCE_URL
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    response = requests.get(url=url, headers=headers)

    res = json.loads(response.text)
    print(res['data'])


# 充币地址查询
def get_wallet_address():
    url = API_ENDPOINT + WALLET_ADDRESS_URL + "?currency=BTC"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    response = requests.get(url=url, headers=headers)

    res = json.loads(response.text)
    print(str(res['data']))


# 获取充值记录
def get_deposit_record():
    url = API_ENDPOINT + WALLET_ADDRESS_URL + "?currency=BTC&size=10"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    response = requests.get(url=url, headers=headers)

    res = json.loads(response.text)
    print(str(res))


# 获取提现记录
def get_withdraw_record():
    url = API_ENDPOINT + WALLET_WITHDRAW_RECORD_URL + "?currency=BTC&size=10&from=1532331295000&page=1"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X_ACCESS_KEY': ACCESS_KEY,
        'X_SIGNATURE': bkex_api_sign.get_sign(url),
    }

    response = requests.get(url=url, headers=headers)

    res = json.loads(response.text)
    print(str(res))


get_api_key()
get_account_balance()
get_wallet_address()
get_deposit_record()
get_withdraw_record()


