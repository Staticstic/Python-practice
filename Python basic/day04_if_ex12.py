# day04_if_ex12.py

# 최대값 구하기(MAX)
# 1. 정수 3개를 입력받아
# 2. 가장 큰 수를 출력한다.

num1 = int(input("정수1 입력 :"))
num2 = int(input("정수2 입력 :"))
num3 = int(input("정수3 입력 :"))

if num1 >= num2 and num1 >= num3:
    x = num1
if num2 >= num1 and num2 >= num3:
    x = num2
if num3 >= num1 and num3 >= num2:
    x = num3

print(x)

# 답
num1 = int(input("정수1 입력 :"))
num2 = int(input("정수2 입력 :"))
num3 = int(input("정수3 입력 :"))

max_num = num1
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3

print("최대값 = ", max_num)
