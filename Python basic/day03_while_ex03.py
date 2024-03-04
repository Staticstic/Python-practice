# day03_while_ex03.py

# Up & Down 게임 [2단계]
# 1. com은 1 ~ 100 사이의 랜덤 숫자를 저장한다.
# 2. me가 com이 저장한 숫자를 맞추면 게임은 종료된다.
# 3. 게임 종료 후, 몇 회에 정답을 맞췄는지 출력한다.
import random
com = random.randint(1,100)
print(com)
i = 1
cnt = 0
while i:
    me = int(input("숫자를 입력하세요 :"))
    if me == com:
        print("정답!")
        i = 0
    elif me != com:
        if me > com:
            print("Down!")
        if me < com :
            print("Up!")
    cnt = cnt + 1
print(cnt)

# 답

import random

com = random.randint(1,100)
print("com =", com)

cnt = 0
me = 0
while com != me:
    me = int(input("me 입력 :"))
    if com > me:
        print("Up!")
    elif com < me:
        print("Down!")
    else:
        print("Bingo!")
    cnt = cnt + 1
print("%d회만에 정답을 맞추셨어요!" %cnt)
