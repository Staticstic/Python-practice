# while
# 반복문 기본문제 5가지
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
while i <= 10:
    if i % 3 == 0 and i != 0:
        tot = tot + i
    i = i + 1
print (tot)
