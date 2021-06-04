import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

ACCESS_KEY = "JtntDg86QLhrvsGkmkJolHLCixzWJYJyTokVAOyH"
SECRET_KEY = "xDmm960159IOlDL9Lo3tvydAhZC3xBYpnaL3zZas"
SERVER_URL = "https://api.upbit.com"


payload = {
    'access_key': ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(SERVER_URL + "/v1/accounts", headers=headers)

print(res.json())