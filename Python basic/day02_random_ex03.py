# day02_random_ex03.py

# 문제 1) 가위(0) 바위(1) 보(2) 게임 [1단계]
# 1. com은 바위만 낼 수 있다.
# 2. me 는 0~2사이의 숫자를 입력받아 저장한다.
# 3. com과 me를 비교해 승패여부를 출력한다.
import random
com = 1
me = int(input("가위(0) 바위(1) 보(2)를 내세요 :"))
if com < me:
    print("승리")
if com > me:
    print("패배")
if com == me:
    print("무승부")

# 답
com = 1
print("치트키 = 바위")

me = int(input("가위(0)바위(1)보(2) 입력 :"))

if me == com:
    print("무승부")
if me == 2:
    print("승리")
if me == 0:
    print("패배")

# 문제 2) 가위(0) 바위(1) 보(2) 게임 [2단계]
# 1. com은 0~2 사이의 랜덤 숫자를 저장한다.
# 2. me는 0~2 사이의 숫자를 입력받아 저장한다.
# 3. com과 me를 비교해 승패여부를 출력한다.
import random
com = random.randint(0,2)
print(com)
me = int(input("가위(0) 바위(1) 보(2)를 내세요 :"))
result = me - com
if result == 1 or result == -2:
    print("승리")
if result == 0:
    print("무승부")
if result == -1 or result == 2:
    print("패배")

# 답
com = random.randint(0,2)
if com == 0:
    print("com = 가위")
if com == 1:
    print("com = 바위")
if com == 2:
    print("com = 보")
    
me = int(input("가위(0)바위(1)보(2) 입력 :"))
if com == me:
    print("무승부")
if com == 0:
    if me == 1:
        print("승리")
    if me == 2:
        print("패배")
if com == 1:
    if me == 2:
        print("승리")
    if me == 0:
        print("패배")
if com == 2:
    if me == 0:
        print("승리")
    if me == 1:
        print("패배")
