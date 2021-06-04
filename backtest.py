import pyupbit
import numpy as np
#변동성 돌파 전략: 백테스팅

# 7일 동안의 원화 시장의 OMG에 대한 ohlcv(당일 시가, 고가, 저가, 종가, 거래량)를 불러옴
# open: 시가, high: 고가, low: 저가, close: 종가, volume: 거래량 
df = pyupbit.get_ohlcv("KRW-OMG", count =7) 

# 매수가를 구하기 위한 코드
# 변동성 돌파 전략은 어제의 고가와 저가의 차이인 변동폭에 k배만큼 상승이 일어났을 때 매수를 진행하기 때문에 해당 가격을 구해주는 것   
# 변동성 돌파 기준 범위 계산, (고가 -저가) * k값
# k값을 0.5로 잡고 계산
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 컬럼을 한 칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# 수익률을 계산하기 위한 코드
# ror(수익률), np.where(조건문, 조건문이 참이면 참일때 값, 거짓이면 거짓일 때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률(hpr) 계산
df['hpr'] = df['ror'].cumprod()

# Draw Down(dd, 낙폭) 계산(누적 최대 값과 현재 hpr 차이 / 누적 최댓값*100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD(Max Draw Down)값 계산
print("MDD(%): ", df['dd'].max())

# 앞의 모든  결과를 'dd'라는 이름의 엑셀 파일로 나타나게 함
df.to_excel("dd.xlsx") 