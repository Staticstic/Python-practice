# gugudan_game.py

import random

rank = [3, 2, 1]
file_name = "rank.txt"

while True:
    
    print("1.구구단 게임")
    print("2.랭킹 확인")
    print("3.게임 종료")

    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        i = 0
        cnt = 0
        while i < 10:
            x = random.randint(2, 9)
            y = random.randint(1, 9)
            answer = x * y
            print("%d x %d = ?" %(x, y))
            my_answer = int(input(": "))
            if answer == my_answer:
                print("정답")
                cnt += 1
            if answer != my_answer:
                print("땡")
            i += 1
        print("총 %d개의 문제를 맞췄습니다." % cnt)

        # 랭킹등록 여부
        if cnt > rank[-1]:
            rank[-1] = cnt

            # 정렬하기
            i = 0
            while i < len(rank):
                max_score = rank[i]
                max_idx = i
                j = i
                while j < len(rank):
                    if max_score < rank[j]:
                        max_score = rank[j]
                        max_idx = j
                    j += 1
                tmp = rank[i]
                rank[i] = rank[max_idx]
                rank[max_idx] = tmp
                i += 1
    elif choice == 2:
        print(rank)
    elif choice == 3:
        break
print(cnt)
