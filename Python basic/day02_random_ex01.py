# day02_random_ex01.py

# random 모듈
import random

# 코인 게임(동전의 앞면[0], 뒷면맞추기[1])
coin = random.randint(0, 1) # 0부터 1사이의 랜덤숫자 발생
print(coin)

if coin == 0:
    print("coin = 앞면")
if coin == 1:
    print("coin = 뒷면")

my_coin = int(input("앞면[0] or 뒷면[1] :"))
if coin == my_coin:
    print("정답")
if coin != my_coin:
    print("땡")


