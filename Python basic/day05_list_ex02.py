# day05_list_ex02.py

# 리스트 기본문제 5가지
# 문제 1) 총점과 평균 출력
scores = [13, 87, 34, 72, 98]
i = 0
tot = 0
cnt = 0
while i < 5:
    tot = tot + scores[i]
    cnt = cnt + 1
    i = i + 1
avg = tot / cnt
print(tot)
print(avg)
# 문제 2) 35점 이상의 성적만 출력
scores = [13, 87, 34, 72, 98]
i = 0
while i < 5:
    if scores[i] >= 35:
        print(scores[i])
    i = i + 1
# 문제 3) 35점 이상의 성적의 개수 출력
scores = [13, 87, 34, 72, 98]
i = 0
cnt = 0
while i < 5:
    if scores[i] >= 35:
        cnt = cnt + 1
    i = i + 1
print(cnt)
# 문제 4) 방번호(index)를 입력하면 성적 출력
scores = [13, 87, 34, 72, 98]
idx = int(input("인덱스를 입력 :"))
i = 0
while i < 5:
    if i == idx:
        print(scores[idx])
    i = i + 1
# 문제 5) 성적을 입력하면 방번호(index)를 출력
scores = [13, 87, 34, 72, 98]
score = int(input("성적을 입력하세요 :"))
i = 0
while i < 5:
    if scores[i] == score:
        print(i)
    i = i + 1
