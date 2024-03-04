# day06_list_ex10.py

# 리스트 추가하기 : append() 함수 활용
lst = []

print(lst)          # []
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)          # [10, 20, 30]

# 리스트 삭제하기(함수 활용편)

# 방법1) 값으로 삭제하기
# remove(값) 함수 활용
lst = [10, 20, 30, 40, 50]
lst.remove(20)
print(lst)          # [10, 30, 40, 50]

# 방법2) 인덱스로 삭제하기
# del 명령어 활용
lst = [10, 20, 30, 40, 50]

del lst[1]
print(lst)          # [10, 30, 40, 50]
