# day08_function_ex02.py

# 문제 1) 숫자 1개를 입력받아
#        짝수 또는 홀수 판별해주는 함수
def test():
    x = int(input("숫자를 입력하세요 :"))
    if x % 2 == 0:
        print("짝수")
    elif x % 2 == 1:
        print("홀수")
test()
# 문제 2) 숫자 3개를 입력받아
#        최대값을 출력해주는 함수
def a():
    x = int(input("정수 1 입력 :"))
    y = int(input("정수 2 입력 :"))
    z = int(input("정수 3 입력 :"))
    max_num = x
    if x < y:
        max_num = y
    if x < z:
        max_num = z
    print(max_num)

def b(x, y, z):
    lst = []
    lst.append(x)
    lst.append(y)
    lst.append(z)
    max_score = lst[0]
    i = 0
    while i < 3:
        if max_score < lst[i]:
            max_score = lst[i]
        i = i + 1
    print(max_score)
b(10, 100, 30)

def show_max():
    lst = []
    i = 0
    while i < 3:
        num = int(input("숫자 %d입력 : " %(i+1)))
        lst.append(num)
        i += 1
    i = 0
    max_num = lst[0]
    while i < 3:
        if max_num < lst[i]:
            max_num = lst[i]
        i += 1
    print("최대값 = ", max_num)
show_max()
