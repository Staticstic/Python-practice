# day04_if_ex11.py

# 3 6 9 게임
# 1. com 은 1 ~ 50사이의 랜덤 숫자 저장
# 2. 해당 숫자에
# 1) 3, 6, 9가 2번 등장하면 "짝짝"
# 2) 3, 6, 9가 1번 등장하면 "짝"
# 3) 등장하지 않으면 해당 숫자 출력
# 예) 37 : 짝
#     12 : 12

import random
com = random.randint(1,50)
print(com)
x = com // 10
y = com % 10

if x % 3 == 0 and y % 3 == 0 and y != 0 and :
    print("짝짝")
elif x % 3 == 0 or y % 3 == 0:
    print("짝")
else:
    print(com)

