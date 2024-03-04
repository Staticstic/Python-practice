# day07_for_ex02.py

# 반복문 기본문제 5가지
# for문으로 풀어보기

# 문제 1) 5 ~ 1까지 출력
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 문제 2) 1 ~ 5까지의 합 출력
tot = 0
for i in range(1, 6):
    tot = tot + i
print("합 = ", tot)

# 문제 3) 0 ~ 10 사이의 홀수 출력
for i in range(0, 11):
    if i % 2 == 1:
        print(i, end=" ")
print()

# 문제 4) 0 ~ 10 사이의 짝수의 개수 출력
cnt = 0
for i in range(0, 11):
    if i % 2 == 0:
        cnt = cnt + 1
print("짝수의 개수 = ", cnt)

# 문제 5) 0 ~ 10 사이의 3의 배수의 합 출력
tot = 0
for i in range(0, 11):
    if i % 3 == 0:
        tot = tot + i
print("합 =", tot)
