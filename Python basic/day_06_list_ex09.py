# day06_list_ex09.py

# 즉석복권
# 1. 3이 "연속해서" 3번 등장하면 당첨복권이다.
# 2. 아래 3개의 복권들의 당첨여부를 출력해보자.

# 로또[1단계]
# 힌트) 3이 나올 때마다 카운팅을 한다.
lotto = [0, 0, 0, 0, 3, 3, 3]
cnt = 0
i = 0
while i < 7:
    if lotto[i] == 3:
        cnt = cnt + 1
    i = i + 1
if cnt == 3:
    print("당첨")
else:
    ("꽝!")
#로또[2단계]
# 힌트) 3이 나올 때마다 카운팅을 하다가
#       0을 만나면 카운트 값을 0으로 초기화한다.
lotto = [0, 0, 0, 3, 3, 0, 3]
cnt = 0
i = 0
while i < 7:
    if lotto[i] == 3:
        cnt = cnt + 1
    if lotto[i] == 0:
        cnt = 0
    i = i + 1
if cnt == 3:
    print("당첨")
else:
    print("꽝!")
#로또[3단계]
# 힌트) check변수를 활용해 카운팅 값이 3이 되는 순간
#       1로 표기해 놓는다.
lotto = [0, 0, 3, 3, 3, 0, 0]
cnt = 0
check = -1
i = 0
while i < 7:
    if lotto[i] == 3:
        cnt = cnt + 1
    if cnt == 3:
        check = 1
    if lotto[i] == 0:
        cnt = 0
    i = i + 1
if check == 1:
    print("당첨")
else:
    print("꽝!")
    
