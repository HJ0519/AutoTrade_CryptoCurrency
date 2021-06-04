import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

# ACCESS_KEY = "uQF4cu5Ps4zos1kA0Zxx5tnqJ0Re8yCbV5mzVV8V"
# SECERT_KEY = "aBgJcDuAh2xiNO6OV1CgygGhQZx1VX4be6SLf2KV"


ACCESS_KEY = "xV2mOgXFHwUiuE56Bl3K6SkyxFQRIHwM4W7bZeFb"
SECERT_KEY = "iqBq7IWbwEORgmboLRW5jnozbU9QvBjZOaMSxEPG"
SERVER_URL = "https://api.upbit.com"

payload = {
    'access_key': ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, SECERT_KEY).decode('utf-8')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(SERVER_URL + "/v1/accounts", headers=headers)
    
print(res.json())