# day05_while_ex09.py

# 반복문 종료
# 숫자를 계속 입력받다가
# -100을 입력하면 프로그램이 종료된다.

run = True
while run:
    number = int(input("숫자를 입력하세요 : "))
    if number == -100:
        print("프로그램 종료")
        run = False
        
