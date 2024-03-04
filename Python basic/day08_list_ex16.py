# day08_list_ex16.py

# MAX 게임
# 1. lst에서 최대값을 검색한다.
# 2. 사용자는 최대값을 입력해 정답을 맞추면,
#    최대값은 0으로 변경된다.
# 3. lst의 모든 값이 0으로 변경되면, 게임은 종료된다.
# 예) [87, 11, 7, 100, 42]
#     입력 : 100
#     [87, 11, 7, 0, 42]
#     입력 : 87
#     [0, 11, 7, 0, 42]
#     ....

lst = [87, 11, 7, 100, 42]

cnt = 0
while True:
    print(lst)
    max_num = 0
    max_idx = 0
    i = 0
    while i < len(lst):
        if max_num < lst[i]:
            max_num = lst[i]
            max_idx = i
        i += 1
    ans = int(input("최대값 입력: "))
    if max_num == ans:
        lst[max_idx] = 0
        cnt += 1
    if cnt == 5:
        print("게임종료")
        break
