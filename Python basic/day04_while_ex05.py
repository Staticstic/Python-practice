# day04_while_ex05.py

# 반복문
# 1) 반복 횟수를 알 때 : for

# 2) 반복 횟수를 모를 때 : while

run = True
while run == 1:
    num = int(input("숫자입력(종료 : -100) : "))
    if num == -100:
        run = False

# 영수증
# 1. 결제하기를 누르기 전까지 주문을 받을 수 있다.
# 2. 결제하기를 누르면, 프로그램이 종료되고 현금을 입력받아 영수증을 출력한다.
# 출력예시)
# 1. 마라탕 : 3개
# 2. 마라샹궈 : 1개
# 3. 꿔바로우 : 1개
# 총 금액 : 14800
# 잔   돈 : 
price1 = 3700
price2 = 2500
price3 = 1200

tot = 0
run = True
while run:
    print("===중식당===")
    print("1.마라탕 : %d원" %price1)
    print("2.마라샹궈 : %d원" %price2)
    print("3.꿔바로우 : %d원" %price3)
    print("4.결제하기")
    choice = int(input("메뉴를 선택하세요 : "))
    if choice == 1:
        x = int(input("수량을 선택해 주세요. :"))
        tot = tot + price1 * x
    if choice == 2:
        x = int(input("수량을 선택해 주세요. :"))
        tot = tot + price2 * x
    if choice == 3:
        x = int(input("수량을 선택해 주세요. :"))
        tot = tot + price3 * x
    if choice == 4:
        run = False
        print("총 금액은 %d원 입니다." %tot)
        pay = int(input("지불 금액을 입력해 주세요. :"))
        charge = pay - tot
        if charge >= 0:
            print("거스름돈은 %d원 입니다." %charge)
        else:
            print("현금이 부족합니다.")

# 답
price1 = 3700
price2 = 2500
price3 = 1200

cnt1 = 0
cnt2 = 0
cnt3 = 0

run = True
while run:
    print("===중식당===")
    print("1.마라탕 : %d원" %price1)
    print("2.마라샹궈 : %d원" %price2)
    print("3.꿔바로우 : %d원" %price3)
    print("4.결제하기")

    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        cnt1 = cnt1 + 1
    elif choice == 2:
        cnt2 = cnt2 + 1
    elif choice == 3:
        cnt3 = cnt3 + 1
    elif choice == 4:
        run = False
        money = int(input("현금을 입력하세요. : "))
        total = price1 * cnt1 + price2 * cnt2 + price3 * cnt3
        charge = money - total
        if charge >= 0:
            print("===영수증===")
            print("1. 마라탕 : %d개" % cnt1)
            print("2. 마라샹궈 : %d개" % cnt2)
            print("3. 꿔바로우 : %d개" % cnt3)
            print("총 금액 : %d원" % total)
            print("잔   돈 : %d원" % charge)
        else:
            print("현금이 부족합니다.")
