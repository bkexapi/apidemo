import hmac
from hashlib import sha256

# SECRET_KEY = "自己的Secret Key"
SECRET_KEY = "4342537ef584d9bfabff473fc51deb154fb371dc9f2c88d72bd83512e0bf064f"


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
