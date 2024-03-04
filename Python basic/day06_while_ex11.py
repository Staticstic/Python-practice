# day06_while_ex11.py

# 소수찾기[1단계]
# 1. 소수란, 1과 자기자신으로만 나눠지는 수
# 2. 예) 2, 3, 7, ...
# 3. 입력받은 수를 1부터 자기 자신까지 나눴을 때,
#    그 나머지가 0인 경우가 2번이면 소수이다.

cnt = 0
i = 1
num = int(input("숫자를 입력하세요 :"))
while i <= num:
    if num % i == 0:
        cnt = cnt + 1
    i = i + 1
if cnt == 2:
    print("%d는 소수" %num)
else:
    print("%d는 소수가 아닙니다." %num)
    
