# day04_while_ex07.py

# Up & Down[A.I]
# 1. me는 1 ~ 100 사이의 임의의 숫자를 입력한다.
# 2. com은 me가 입력한 숫자를 맞추는 게임이다.
# 예) me = 50
#     com = 13      Up!     13 < com <= 100
#     com = 97      Up!     13 < com < 97
#     ...
#     com = 50
#     --- Game Over ---

# 답
import random

me = int(input("me 입력 : "))

min_num = 1
max_num = 100

run = True
while run:
    com = random.randint(min_num, max_num)
    print("com = ", com)
    if com < me:
        min_num = com + 1
        print("Up!")
    elif com > me:
        max_num = com - 1
        print("Down!")
    elif com == me:
        print("Bingo!")
        run = False
        

