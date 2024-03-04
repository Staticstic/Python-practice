# day01_var_ex01.py

# 변수(variable)
# 1. 값을 한 개만 저장 할 수 있다.
# 2. 숫자로 시작할 수 없다.
# 3. 특수문자는 _(언더스코어)만을 허용한다. , 공백대신 _를 사용한다.(snake표기법)
# 4. 알파벳의 대소문자를 구분한다.
# 5. 예약어(keyword)는 변수명으로 사용할 수 없다.
#    ex) def, if, for, while, ...

_1top=100
num = 1
Num = 2
print(num)
print(Num)

cur_pos = -1 # current position

# 예) 현금을 1000원 갖고 있다. 200원짜리 과자를 구매했을 때 잔돈은?
cash = 1000
snack = 200
change = cash - snack
print("change = %dwon" %change)

# 문제 1) 가로가 2이고 세로가 4인 삼각형의 넓이 출력
가로=2
세로=4
넓이=2*4/2
print("넓이=%d" %넓이)
# 답
width = 2
height = 4
tri_area = width * height / 2
pritn("삼각형의 넓이 = %d" %tri_area)
# 문제 2) 월급이 1000원이다. 연봉 출력 (단 세금 10% 제외)
월급=1000
_1년=12
_1년수입=월급*_1년
세금=_1년수입*0.1
연봉=_1년수입-세금
print("연봉=%d" %연봉)
# 답
월급 = 1000
세전연봉 = 월급 * 12
세금 = 세전연봉 / 10
세후연봉 = 세전연봉 - 세금
print("연봉 = %d원" % 세후연봉)
# 문제 3) 800원 = 500원 (1개), 100원(3개)
_500원_개수=800//500
_100원_개수=800%500//100
print("800원=500원 %d개, 100원 %d개" %(_500원_개수, _100원_개수))
# 답
돈 = 800
오백원 = 돈 // 500
백원 = 돈 % 500 // 100
print("오백원(%d개), 백원(%d개)" % (오백원, 백원))
