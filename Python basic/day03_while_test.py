# day03_while_test.py 

# 반복문 기본문제 5가지 (소요시간 : 5:30 ~ 5:33)
# 문제 1) 5 ~ 1 까지 출력
i = 5
while i >= 1:
    print(i)
    i = i - 1
# 문제 2) 1 ~ 5 까지의  합 출력
i = 1
tot = 0
while i <= 5:
    tot = tot + i
    i = i + 1
print(tot)
# 문제 3) 0 ~ 10 사이의 홀수 출력
i = 0
while i <= 10:
    if i % 2 == 1:
        print(i)
    i = i + 1
# 문제 4) 0 ~ 10 사이의 짝수의 개수 출력
i = 0
cnt = 0
while i <= 10:
    if i % 2 == 0 and i != 0:
        cnt = cnt + 1
    i = i + 1
print(cnt)
# 문제 5) 0 ~ 10 사이의 3의 배수의 합 출력
i = 0
tot = 0
while i <= 10 :
    if i % 3 == 0 and i != 0:
        tot = tot + i
    i = i + 1
print(tot)
# 구구단 게임[2단계] (소요시간 : 5:34 ~ 5:37)
# 1. 구구단 게임을 5회 진행한다.
# 2. user가 정답을 맞춘 횟수를 출력한다.
import random
i = 1
cnt = 0
while i <= 5:
    x = random.randint(2,9)
    y = random.randint(1,9)
    ans = x * y
    print("%d x %d = ?" %(x,y))
    my_ans = int(input("정답을 입력하세요 :"))
    if my_ans == ans:
        cnt = cnt + 1
    i = i + 1
print(cnt)
# Up & Down 게임 [2단계](소요시간 : 5:38 ~ 5:41)
# 1. com은 1 ~ 100 사이의 랜덤 숫자를 저장한다.
# 2. me가 com이 저장한 숫자를 맞추면 게임은 종료된다.
# 3. 게임 종료 후, 몇 회에 정답을 맞췄는지 출력한다.
import random
com = random.randint(1,100)
print(com)
me = 0
cnt = 0
while me != com:
    me = int(input("정답을 입력하세요:"))
    if me > com:
        print("down!")
    if me < com:
        print("up!")
    if me == com:
        print("bingo!")
    cnt = cnt + 1
print(cnt)
    
