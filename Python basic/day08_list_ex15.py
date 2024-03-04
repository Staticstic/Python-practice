# day08_list_ex15.py

# 정렬하기

lst = [11, 24, 7, 98, 3]
# [98, 24, 7, 11, 3]
# [98, 24, 7, 11, 3]
# [98, 24, 11, 7, 3] 순으로 정렬

i = 0
while i < len(lst):
    max_num = lst[i]
    max_idx = i
    # 최대값 구하기
    j = i
    while j < len(lst):
        if max_num < lst[j]:
            max_num = lst[j]
            max_idx = j
        j += 1
    # 값 교체하기
    tmp = lst[i]
    lst[i] = lst[max_idx]
    lst[max_idx] = tmp
    i += 1
print(lst)
