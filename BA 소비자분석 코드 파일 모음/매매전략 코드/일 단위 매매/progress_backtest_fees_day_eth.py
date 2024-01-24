#변동성 돌파 전략: 백테스팅
import pyupbit
import numpy as np

# ETH(이더리움)에 대한 3년치 일별 시세캔들 ohlcv(당일 시가, 고가, 저가, 종가, 거래량)를 불러옴
# open: 시가, high: 고가, low: 저가, close: 종가, volume: 거래량, value: 해당 시점에 거래된 가격 
df = pyupbit.get_ohlcv("KRW-ETH", "day", count =1095) 

# 매수가를 구하기 위한 코드
# 변동성 돌파 전략은 어제의 고가와 저가의 차이인 변동폭에 k배만큼 상승이 일어났을 때 매수를 진행하기 때문에 해당 가격을 구해주는 것   

# 변동성 돌파 기준 범위('range') 계산, (고가 -저가) 
# 어제의 고가와 저가를 이용하므로 전일 데이터를 사용하도록 고가와 저가 데이터에 shift(1)을 적용함
df['range'] = df['high'].shift(1) - df['low'].shift(1)

# 매수가('target') = 당일 시가 + range * k 
# search_bestk.py 프로그램을 통해 가장 높은 수익률이 나타나는 k값을 선정
df['target'] = df['open'] + df['range'] * 0.1

# 수익률을 계산하기 위한 코드
# ror(수익률), np.where(조건문, 조건문이 참이면 참일때 값, 거짓이면 거짓일 때 값)
# 업비트 거래수수료 0.05%를 적용하여 계산
df['ror'] = np.where(df['high'] > df['target'], 
                     (df['close'] / (1 + 0.0005)) / (df['target'] * (1 + 0.0005)) - 1, 
                      0)


# 누적 곱 계산(cumprod) => 누적 수익률(crr) 계산
df['crr'] = (df['ror'] + 1).cumprod() - 1

# 앞의 모든  결과를 'ETH_mock_inv_day'라는 이름의 엑셀 파일로 나타나게 함
df.to_excel("ETH_mock_inv_day.xlsx") 
