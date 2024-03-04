# day03_if_ex05.py

# 지하철 요금 계산 [과제]
# 정거장 수를 입력받아 요금을 출력해보자.
# 1) 1 ~ 5 : 500원
# 2) 6 ~ 10 : 600원
# 3) 11 : 650원
# 4) 12 : 650원
# 5) 13 : 700원
# 6) 14 : 700원
# 7) 15 : 750원
# ...

station = int(input("정거장 수 :"))
fee = 0
if 1 <= station and station <= 5:
    fee = 500
if 6 <= station and station <= 10:
    fee = 600
if station > 10:
    if station % 2 == 1:
        fee = fee + 50
    fee = fee + 600 + (station - 10) // 2 * 50
print(fee)
