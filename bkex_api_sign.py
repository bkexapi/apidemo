import hmac
from hashlib import sha256

SECRET_KEY = "自己的Secret Key"


# 获取签名
def get_sign(url):
    params_arr = url.split("?")
    source = ""
    if len(params_arr) > 1:
        param = params_arr[1]
        unsorted_arr = param.split("&")
        source = "&".join(sorted(unsorted_arr))
        print(source)
    sign = hmac.new(bytes(SECRET_KEY, encoding='utf-8'), bytes(source, encoding='utf-8'), sha256).hexdigest()
    print("sign: " + sign)
    return sign
