# 최적의 k값 구하기 - ETH
import pyupbit
import numpy as np

def get_crr(k=0.5):
    df = pyupbit.get_ohlcv("KRW-ETH",  count=7)
    df['range'] = df['high'].shift(1) - df['low'].shift(1) 
    df['target'] = df['open'] + df['range'] * k 
    # 수수료(fees)는 업비트의 거래수수료 0.05%를 적용함
    fees = 0.0005

    df['ror'] = np.where(df['high'] > df['target'],
                         (df['close'] / (1 + fees)) / (df['target'] * (1 + fees)),
                          0)

    crr = (df['ror'] + 1).cumprod()[-2] - 1
    # cumprod()[-1]을 할 경우 당일까지의 누적수익률을 계산하는데, 
    # 이 때 당일은 매매를 진행해야 하는 시점이므로 전날의 누적수익률로 산출됨
    # 따라서 cumprod()[-2]를 입력하여 전일까지의 누적수익률이 계산되게 설정함
    return crr


# k값을 0.1~1까지 0.1 간격으로 증가시키긴 뒤, 이를 get_ror 함수와 연계하여 누적 수익률 계산
# 즉, 해당 코드를 통해 k값에 따라서 수익률이 어떻게 되는지 파악할 수 있음
for k in np.arange(0.1, 1.0, 0.1): 
    crr = get_crr(k)
    print("%.1f %f" % (k, crr))
# 시장 상황에 따라 더 좋은 k값은 변할 수 있음