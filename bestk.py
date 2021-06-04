# 최적의 k값 구하기
import pyupbit
import numpy as np

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-OMG",  count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1) 
    # 수수료(fee)는 없다고 가정하고 계산

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


# k값을 0.1~1까지 0.1 간격으로 증가시키긴 뒤, 이를 get_ror 함수와 연계하여 누적 수익률 계산
# 즉, 해당 코드를 통해 k값에 따라서 수익률이 어떻게 되는지 파악할 수 있음
for k in np.arange(0.1, 1.0, 0.1): 
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
# 최근 7일 데이터를 토대로 계산한 결과는 k값이 낮을수록 수익률이 좋은 성향을 확인할 수 있음
# k = 0.1일 때 수익률이 가장 좋은 것을 확인할 수 있음
# 시장 상황에 따라 더 좋은 k값은 변할 수 있음
