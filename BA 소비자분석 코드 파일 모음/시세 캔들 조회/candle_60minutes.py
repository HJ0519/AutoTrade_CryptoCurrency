import pyupbit

# 3년치의 60분 시세캔들을 가져옴
# 24(24시간)*365(365일)*3(3년) = 26280
df = pyupbit.get_ohlcv("KRW-OMG", "minute60", count=26280)

# 해당 데이터를 엑셀 파일로 나타나게 함
# 시가/고가/저가/종가/거래량/거래금액의 데이터가 데이터프레임 형태로 나타남
df.to_excel("candle_60minutes_3years.xlsx")