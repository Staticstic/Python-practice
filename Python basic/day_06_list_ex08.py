# day_06_list_ex08.py

# 기억력 게임
# 1. 리스트 front의 값을 섞는다. (shuffle)
# 2. 사용자로부터 같은 숫자의 위치 값 2개를 입력받는다.
# 3. 정답이면 카드의 앞면을 출력한다.
# 4. back의 값이 모두 채워지면 게임은 종료된다.

idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
front = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
back = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

import random
j = 0
while j < 10:
    i = 0
    while i < 10:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if idx[i] == x:
            x = x - 1
            y = y - 1
            tmp = front[x]
            front[x] = front[y]
            front[y] = tmp
        i = i + 1
    j = j + 1
print(front)

run = True
while run:
    ans1 = int(input("카드를 선택하세요."))
    ans2 = int(input("카드를 선택하세요."))
    ans1 = ans1 - 1
    ans2 = ans2 - 1
    if front[ans1] == front[ans2]:
        back[ans1] = front[ans1]
        back[ans2] = front[ans2]
        print(back)
    if front[ans1] != front[ans2]:
        print("다시 선택하세요.")
    if front == back:
        run = False
        print("게임 종료")

# 답
i = 0
while i < 100:
    r_num = random.randint(0, 9)
    tmp = front[0]
    front[0] = front[r_num]
    front[r_num] = tmp
    i = i + 1

cnt = 0
while True:
    print("idx =", idx)
    print("front =", front)
    print("back =", back)

    if cnt == 5:
        print("게임 종료")
        break

    idx1 = int(input("인덱스1 입력"))
    idx2 = int(input("인덱스2 입력"))

    idx1 = idx1 - 1
    idx2 = idx2 - 1

    if front[idx1] == front[idx2]:
        back[idx1] = front[idx1]
        back[idx2] = back[idx2]
        cnt = cnt + 1
