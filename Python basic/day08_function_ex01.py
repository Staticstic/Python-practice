# day08_function_ex01.py

# 함수
# 1) 특별한 기능을 갖고 있다.
# 2) 반복되는 구조를 함수로 모듈화하기 위함이다.
# 3) 내장 함수, 사용자 정의 함수가 있다.
#    ex) print(), lend(), append(),...
# 4) 구조
#    def 함수명():
#       기능코드 작성
# 5) 사용 : 함수의 호출
#   함수명()

# 1. 1부터 5까지의 합을 출력해주는 함수
def tot():
    total = 0
    i = 1
    while i <= 5:
        # 복합 대입연산자 : +=, -=, *=, /=, %=
        total += i   # total = total + i
        i +=  1
    print("1부터 5까지의 합 =", total)
    return   # 생략 가능
# --------------------------------------------------
tot()

# 2. x부터 y까지의 합을 출력해주는 함수
def tot2(x, y):
    total = 0
    i = x
    while i <= y:
        total += i
        i += 1
    print("%d부터 %d까지의 합 = %d" %(x, y, total))
    return
# --------------------------------------------------
tot2(1, 10)

# 3. 값 2개를 전달받아 사칙연산의 결과를 출력해주는 함수
def sum(x, y):
    print("%d + %d = %d" %(x, y, x + y))
def sub(x, y):
    print("%d - %d = %d" %(x, y, x - y))
def multi(x, y):
    print("%d * %d = %d" %(x, y, x * y))
def div(x, y):
    # ZeroDivisionError: division by zero
    if y == 0:
        print("0으로 나눌수 없습니다.")
    else:
        print("%d / %d = %.2f" %(x, y, x / y)) # .2f : 소수 2자리까지 출력
    
def calc():
    x = int(input("정수1 입력 :"))
    y = int(input("정수2 입력 :"))
    sum(x,y)
    sub(x,y)
    multi(x,y)
    div(x,y)
# --------------------------------------------------
calc()
    

