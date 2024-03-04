# day02_random_ex02.py

# 문제 1) 구구단 게임
# 1. 2~9 사이의 랜덤숫자 저장 ex) 3
# 2. 1~9 사이의 랜덤숫자 저장 ex) 5
# 3. 문제 출제 ex) 3 x 5 =?
# 4. 정답 입력받기
# 5. 정답 일치여부 출력
import random
front = random.randint(2,9)
back = random.randint(1,9)
comans = front * back
print("%d x %d" %(front, back))
answer = int(input("정답을 입력하세요:"))
if answer == comans:
    print("정답")
if answer != comans:
    print("땡")

# 답
import random
x = random.randint(2,9)
y = random.randint(1,9)
answer = x * y

print("%d x %d =?" %(x , y))
my_answer = int(input(":"))

if answer == my_answer:
    print("정답")
if answer != my_answer:
    print("땡")
