# day05_list_ex01.py

# 리스트(배열)
# 1. 여러 개의 값을 저장하기 위한 기술
# 2. 값의 종류 구분 없이 저장된다.
# 3. 크기의 제약이 없다.
# 4. 0부터 시작하는 방번호(index)가 생성된다.
# 5. 사용법
#             0 1 2 3 4 <- index
#    변수명 = [1,2,3,4,5]
#    3 출력 : print(변수명[2])
# 대괄호 : [ ]
# 중괄호 : { }
# 소괄호 : ( )

scores = [13, 87, 34, 72, 98]
print(scores[0])

# IndexError: list index out of range
# print(scores[5])

i = 0
while i < 5:
    print(scores[i])
    i = i + 1
