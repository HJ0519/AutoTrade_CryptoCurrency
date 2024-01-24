# 60분 시세캔들이 정상적으로 출력되는지 테스트
import requests

# 60분 시세캔들을 조회할 수 있는 URL
url = "https://api.upbit.com/v1/candles/minutes/60?market=KRW-OMG&count=1"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)