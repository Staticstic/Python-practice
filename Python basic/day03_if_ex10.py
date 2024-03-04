# day03_if_ex10.py

# ATM(입금/이체)
# 1. 입금액을 입력 받아 my_money에 입금
# 2. 이체
# 1) 이체할 계좌번호를 입력받아 유효성 검사
# 2) 이체할 금액 <= my_money : 이체 가능
#    이체할 금액 > my_money : 이체 불가

my_acc = 1001
my_money = 18000
your_acc = 1002
your_money = 37000

print("==메가IT ATM==")
print("1.입금하기")
print("2.이체하기")

choice = int(input("메뉴 선택 :"))
if choice == 1:
    money = int(input("입금할 금액 : "))
    amoney = my_money + money
    print("계좌의 금액은 %d원입니다." %amoney)
elif choice == 2:
    acc = int(input("이체할 계좌번호를 입력해 주세요."))
    if acc == your_acc:
        money = int(input("이체할 금액 :"))
        if money > my_money:
            print("이체할 금액이 부족합니다.")
        if money <= my_money:
            amoney = my_money - money
            bmoney = your_money + money
            print("당신의 잔액은 %d원이고 송금한 계좌의 잔액은 %d원 입니다." %(amoney,bmoney))
    if acc != your_acc:
        print("계좌번호를 확인해주세요.")
# 답
my_acc = 1001
my_money = 18000
your_acc = 1002
your_money = 37000

print("==메가IT ATM==")
print("1.입금하기")
print("2.이체하기")
choice = int(input("메뉴 선택 :"))
if choice == 1:
    input_money = int(input("입금할 금액 : "))
    my_money = my_money + input_money
    print("입금을 완료하였습니다.")
elif choice == 2:
    trans_acc = int(input("이체할 계좌번호를 입력해 주세요."))
    if trans_acc == your_acc:
        trans_money = int(input("이체할 금액 :"))
        if trans_money <= my_money:
            my_money = my_money - trans_money
            your_money = your_money + trans_money
            print("이체를 완료하였습니다.")
        else:
            print("계좌잔액이 부족합니다.")
    else:
        print("계좌번호를 확인해주세요.")
print("my_money =", my_money)
print("your_money =", your_money)
