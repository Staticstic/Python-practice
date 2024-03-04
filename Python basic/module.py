# module.py (ex04 ~

# ex04
def change(x, y):
    tmp = x
    x = y
    y = tmp
    return x, y

# ex05
def choice1(cnt1):
    cnt1 += 1
    return cnt1
def choice2(cnt2):
    cnt2 += 1
    return cnt2
def choice3(price1, price2, cnt1, cnt2):
    # ctrl + [ : 내어쓰기
    # ctrl + ] : 들여쓰기
        tot = price1 * cnt1 + price2 * cnt2
        money = int(input("돈을 입력하세요 : "))
        charge = money - tot
        if charge >= 0:
            print("잔돈 %d원입니다." % charge)
        else:
            print("돈이 부족합니다.")
def run ():
    price1 = 8700
    price2 = 5400
    cnt1 = 0
    cnt2 = 0
    while True:
        print("1. 치즈버거 : %d원" % price1)
        print("2. 마샬버거 : %d원" % price2)
        print("3. 계산하기")
        choice = int(input("메뉴선택 :"))
        if choice == 1:
            cnt1 = choice1(cnt1)
        elif choice == 2:
            cnt2 = choice2(cnt2)
        elif choice == 3:
            choice3(price1, price2, cnt1, cnt2)
            break    
