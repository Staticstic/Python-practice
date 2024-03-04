# day06_list_ex11.py

# 리스트 삭제하기(알고리즘편)

# 방법1) 인덱스로 삭제하기
# 예) 1번째 값을 삭제하기 (= 값 20 삭제하기)
lst = [10, 20, 30, 40, 50]
del_idx = 1

# 1-1) tmp에 lst값을 저장한다.
tmp = lst
print("tmp = ",tmp)
# 1-2) lst를 빈 리스트로 초기화한다.
lst = []
# 1-3) 삭제할 값을 제외한 나머지 값을
#      lst에 다시 추가한다.
i = 0
while i < 5:
    if i != del_idx:
        lst.append(tmp[i])
    i = i + 1
print(lst)

# 방법2) 값으로 삭제하기
# 예) 값 20 삭제하기
lst = [10, 20, 30, 40, 50]
del_value = 20

# 2-1) 값 20의 인덱스 검색하기
del_idx = -1
i = 0
while i < 5:
    if lst[i] == 20:
        del_idx = i
    i = i + 1
print("del_idx =", del_idx)
# 2-2) tmp에 lst값을 저장한다.
tmp = lst
print("tmp =", tmp)
# 2-3) lst를 빈 리스트로 초기화한다.
lst = []
# 2-4) 삭제할 값을 제외한 나머지 값을
#      lst에 다시 추가한다.
i = 0
while i < 5:
    if i != del_idx:
        lst.append(tmp[i])
    i = i + 1
print(lst)
