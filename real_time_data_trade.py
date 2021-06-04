import websocket, json, time, requests
import hashlib, jwt, uuid
from urllib.parse import urlencode
import os

try:
    import thread
except ImportError:
    import _thread as thread

API_KEY = "xV2mOgXFHwUiuE56Bl3K6SkyxFQRIHwM4W7bZeFb"
SECRET_KEY = "iqBq7IWbwEORgmboLRW5jnozbU9QvBjZOaMSxEPG"

price = 0

def on_message(ws, message):
    json_data = json.loads(message)
    global price
    if price == 0:
        price = json_data['trade_price']
        print(price)
        price('코인의 가격 설정')
    else:
        percent = (price - json_data['trade_price']) / json_data['trade_price'] * 100
        print(price)
        print('시작 가격보다', percent, '변화')
        if percent > 0:
            query = {
                'market': 'KRW-OMG',
                'side': 'ask',
                'volume': '1',
                'price': json_data['trade_price'],
                'ord_type': 'market',
            }
            query_string = urlencode(query).encode()

            m = hashlib.sha512()
            m.update(query_string)
            query_hash = m.hexdigest()

            payload = {
                'access_key': API_KEY,
                'nonce': str(uuid.uuid4()),
                'query_hash': query_hash,
                'query_hash_alg': 'SHA512',    
            }

            jwt_token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
            authorize_token = 'Bearer {}'.format(jwt_token)
            headers = {"Authorization": authorize_token}

            res = requests.post('https://api.upbit.com/v1/orders', params=query, headers=headers)
            print(res.json()) 
