# day03_if_ex07.py

# 영수증 출력

money = 3000
price1 = 3500
price2 = 2500
price3 = 1000

print("===맘스터치===")
print("1.싸이버거 : %d원" %price1)
print("2.마샬라버거 : %d원" %price2)
print("3.콜라 : %d원" %price3)

choice = int(input("메뉴를 선택하세요."))
if choice == 1:
    charge = money - price1
if choice == 2:
    charge = money - price2
if choice == 3:
    charge = money - price3

if charge >= 0:
    print("잔돈은 %d원입니다." % charge)
if charge < 0:
    print("현금이 부족합니다.")
