# 2일차 정리
# 시작시간 ~ 마침시간(소요시간) 5:32 ~ 5:37
# 문제 1) 로그인기능[2단계]
# 1. id를 입력받는다.
# 2. id가 일치하면 pw를 입력받을 수 있다.
# 3. id와 pw가 모두 일치하면 "로그인 성공"
# 4. id가 틀리면, "id를 확인해주세요."
# 5. id는 맞지만 pw가 틀리면, "pw를 확인해주세요."
db_id = "qwer"
db_pw = "1234"
my_id = input("ID를 입력하세요 :")
my_id = my_id.strip()
if db_id == my_id:
    my_pw = input("PW를 입력하세요 :")
    my_pw = my_pw.strip()
    if db_pw == my_pw:
        print("로그인 성공")
    if db_pw != my_pw:
        print("PW를 확인해주세요.")
if db_id != my_id:
    print("ID를 확인해주세요.")
    
# 시작시간 ~ 마침시간(소요시간) 5:38~5:42
# 연산자 기호 맞추기 게임
# 1. 1~100 사이의 랜덤 숫자 2개를 저장한다.
# 2. 1~4 사이의 랜덤 숫자 1개를 저장한다.
#    위 랜덤 숫자는 연산자 기호에 해당한다.
#    1(더하기) 2(빼기) 3(곱하기) 4(나누기[몫])
# 3. 3개의 숫자를 확인하여 연산자 기호를 맞추는 게임이이다.
# 예) 3 5 15
#     1)+ 2)- 3)* 4)//
#     입력 : 3
#     정답!
import random
x = random.randint(1,100)
y = random.randint(1,100)
op = random.randint(1,4)

if op == 1:
    z = x + y
if op == 2:
    z = x - y
if op == 3:
    z = x * y
if op == 4:
    z = x // y

print("%d %d %d" %(x, y, z))
print("1) +")
print("2) -")
print("3) *")
print("4) //")

answer= int(input("입력 :"))
if answer == op:
    print("정답")
if answer != op:
    print("오답")
