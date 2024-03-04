# day_06_list_ex07.py

# 영화관 좌석예매
# 1. 숫자0은 공석을 의미한다.
# 2. 사용자는 방번호(index)를 입력해, 좌석을 예매할 수 있다.
# 3. 예매가 완료되면 해당 좌석의 값은 1로 변경된다.
# 4. 한 좌석당 금액이 12,000원이다.
# 5. 오늘 하루 영화관의 매출액을 출력해보자.
# 예) [0, 0, 0, 0, 0, 0, 0]
#     예매하기 : 1
#     [0, 1, 0, 0, 0, 0, 0]
#     예매하기 : 1
#     이미 예매가 완료된 좌석입니다.

movie = [0, 0, 0, 0, 0, 0, 0]
cnt = 0

while True:
    print("1.예매하기")
    print("2.종료하기")

    choice = int(input("메뉴를 선택하세요 :" ))
    if choice == 1:
        i = 0
        while i < 7:
            if movie[i] == 0:
                print("[X]", end = "")
            elif movie[i] == 1:
                print("[O]", end = "")
            i = i + 1
        print()
        seat = int(input("좌석번호를 선택하세요 :"))
        seat = seat - 1
        if movie[seat] == 0:
            print("예매가 완료되었습니다.")
            movie[seat] = 1
            cnt = cnt + 1
        else:
            print("이미 예매가 완료된 좌석입니다.")                                    
    elif choice == 2:
        print("프로그램 종료")
        money = cnt * 12000
        print("=== 영화관 매출현황 ===")
        print("예매 관객수 : %d명" %cnt)
        print("매       출 : %d원" %money)
        break
