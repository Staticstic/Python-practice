# day05_list_ex05.py

# 값 교체하기[2단계]
hakbun = [1001, 1002, 1003, 1004, 1005]
score = [87, 11, 32, 94, 25]

# 문제 1) 방번호(index)를 2개 입력받아 성적 교체
# 예
# 인덱스1 입력 : 1
# 인덱스2 입력 : 2
# [87, 32, 11, 94, 25]

idx1 = int(input("인덱스1 입력 :"))
idx2 = int(input("인덱스2 입력 :"))

tmp = score[idx1]
score[idx1] = score[idx2]
score[idx2] = tmp
print(score)

# 문제 2) 학번을 2개 입력받아 성적 교체
x = int(input("학번1을 입력 :"))
y = int(input("학번2를 입력 :"))

idx1 = 0
idx2 = 0
i = 0
while i < 5:
    if x == hakbun[i]:
        idx1 = i
    if y == hakbun[i]:
        idx2 = i
    i = i + 1
print(idx1)
print(idx2)

tmp = score[idx1]
score[idx1] = score[idx2]
score[idx2] = tmp

print(score)
