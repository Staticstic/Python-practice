# day03_while_ex02.py

# 구구단 게임[2단계]
# 1. 구구단 게임을 5회 진행한다.
# 2. user가 정답을 맞춘 횟수를 출력한다.

import random
i = 1
cnt = 0
while i <= 5:
    x = random.randint(2,9)
    y = random.randint(1,9)
    ans = x * y
    print("%d x %d =?" %(x,y))
    my_ans = int(input("정답을 입력하세요"))
    if my_ans == ans:
        cnt = cnt + 1
    i = i + 1
print("정답을 맞춘 횟수=", cnt)
    
