import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

# 강의 실습용 접근키 시크릿키
# ACCESS_KEY = "uQF4cu5Ps4zos1kA0Zxx5tnqJ0Re8yCbv5mzVV8V"
# SECERT_KEY = "aBgJcDuAh2xiNO6OV1CgygGhQZx1VX4be6SLf2KV"

# 내 접근키 시크릿키
ACCESS_KEY = "xV2mOgXFHwUiuE56Bl3K6SkyxFQRIHwM4W7bZeFb"
SECERT_KEY = "iqBq7IWbwEORgmboLRW5jnozbU9QvBjZOaMSxEPG"
SERVER_URL = "https://api.upbit.com"

def get_currency_balance(currency, field):
    payload = {
        'access_key': ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, SECERT_KEY).decode('utf-8')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(SERVER_URL + "/v1/accounts", headers=headers)
    result = res.json()
    for currency_info in result:
        if currency_info["currency"] == currency:
            return float(currency_info[field]) # 원하는 필드 값만 리턴
    raise Exception('check currency or field') # 요청받은 화폐가 필드나 화폐가 없어 아무 결과가 없으면 에러를 발생하도록 함

if __name__ == '__main__':
    krw_balance = get_currency_balance('KRW',  'balance')
    print('krw-balance:', krw_balance)

    # eth_balance = get_currency_balance('ETH', 'balance')
    # print('eth-balance', eth_balance)






