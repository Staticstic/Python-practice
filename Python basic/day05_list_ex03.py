# day05_list_ex03.py

# OMR카드
# 1. 리스트 answer는 정답이다.
# 2. 리스트 hgd과 answer를 비교해 정오표를 출력한다.
# 3. 한 문제당 20점으로 성적도 함께 출력한다.
# ex) 60점
#     X O O O X

answer = [3,1,2,1,4]
hgd = [1,1,2,1,3]

i = 0
score = 0
while i < 5:
    if answer[i] == hgd[i]:
        print("O")
        score = score + 20
    if answer[i] != hgd[i]:
        print("X")
    i = i + 1
print(score)

# 답
cnt = 0
i = 0
while i < 5:
    if answer[i] == hgd[i]:
        print("O", end = " ") # 줄바꿈 제거 및 공백 추가
        cnt = cnt + 1
    else:
        print("X", end = " ")
    i = i + 1

print() # 줄바꿈

score = cnt * 20
print (score)
