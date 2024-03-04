# day03_if_ex06.py

# 짝수이면서 3의 배수이면 True 출력
num = 12
print(num % 2 == 0 and num % 3 == 0)

# Up & Down Game
# 1. com은 1~10 사이의 랜덤 숫자 저장
# 2. me는 com이 저장한 숫자를 맞추는 게임
# 3. 힌트 출력
# 예) com = 5
#     me = 3   -> Up!
#     me = 8   -> Down!
#     me = 5   -> Bingo!

import random

com = random.randint(1,10)
print("치트키 =", com)

me = int (input("me(1~10) :"))
if com > me:
    print("Up!")
if com < me:
    print("Down!")
if com == me:
    print("Bingo!")
