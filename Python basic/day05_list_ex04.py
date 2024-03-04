# day05_list_ex04.py

# 학생성적관리

hakbun = [1001, 1002, 1003, 1004, 1005]
mega = [11, 87, 92, 27, 45]
name = ["james", "tom", "sam", "scott", "anne"]

# 문제 1) 전교생의 총점과 평균 출력
i = 0
tot = 0
cnt = 0
while i < 5:
    tot = tot + mega[i]
    cnt = cnt + 1
    i = i + 1
avg = tot / cnt
print("총점 : %d, 평균 : %d" %(tot, avg))

# 문제 2) 학번을 입력하면 성적 출력
i = 0
num = int(input("학번을 입력하세요. : "))
while i < 5:
    if num == hakbun[i]:
        print("점수는 %d점 입니다." %(mega[i]))
    i = i + 1
    
# 문제 3) 1등 학생의 학번과 이름 출력
i = 0
max_score = mega[i]
max_name = name[i]
max_idx = idx[i]
while i < 5:
    if max_score < mega[i]:
        max_score = mega[i]
        max_name = name[i]
        max_idx = idx[i]
    i = i + 1    
print(max_score, max_name, idx)

#답
max_score = mega[0]
max_idx = 0
i = 0
while i < 5:
    if max_score < mega[i]:
        max_score = mega[i]
        max_idx = i
        i = i + 1
print(">>> 1등 학생 정보")
print("학번 : ", hakbun[max_idx])
print("이름 :", name[max_idx])

# 문제 4) 2번 문제에서 없는 학번 입력시, 예외처리
i = 0
num = int(input("학번을 입력하세요. : "))
check = -1
while i < 5:
    if num == hakbun[i]:
        check = i 
    i = i + 1
if check == -1:
    print("학번 입력 오류!")
else:
    print("%d학번의 점수는 %d점 입니다." %(num, mega[check]))
    
