import pyupbit

access = "xV2mOgXFHwUiuE56Bl3K6SkyxFQRIHwM4W7bZeFb"          # 본인 값으로 변경
secret = "iqBq7IWbwEORgmboLRW5jnozbU9QvBjZOaMSxEPG"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# 잔고 조회
print(upbit.get_balance("KRW-OMG"))     # KRW-OMG 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
