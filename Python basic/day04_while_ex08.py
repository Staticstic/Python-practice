# day04_while_ex08.py

# 배달의 민족(배달 서비스)
# 1. 목적지는 -10 ~ 10 사이의 랜덤 숫자로 저장
# 2. 방향과 속도 설정을 통해
# 3. 목적지까지 안전하게 치킨을 배달하는 게임

import random

# 목적지
des_x = random.randint(-10, 10)
des_y = random.randint(-10, 10)

# 방향
direct = ""

# 속도
speed = 0

# 기사님 현 위치
x = 0
y = 0

run = True
while run:
    print("=== 배달의 민족 ===")
    print("목적지 : %d, %d" % (des_x, des_y))
    print("방  향 : %s" % direct)
    print("속  도 : %d" % speed)
    print("현위치 : %d, %d" % (x, y))
    print("===================")

    print("1. 방향설정")
    print("2. 속도설정")
    print("3. 이동하기")

    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        direct = input("방향 입력 : ")
    elif choice == 2:
        speed = int(input("속도 입력 :"))
    elif choice == 3:
        if direct == "동":
            x = x + speed
        if direct == "서":
            x = x - speed
        if direct == "남":
            y = y - speed
        if direct == "북":
            y = y + speed
    if x == des_x and y == des_y:
        run = False
        print("배달이 완료되었습니다.")
            
