# day01_op_ex02.py

# (대소)비교 연산자
# 참(True), 거짓(False)로 결과가 나옴
# 1) 크니? : >
# 2) 작니? : <
# 3) 같니? : ==
# 4) 다르니? : !=      ,!(not)

print(True)
print(False)
print(10 > 3)
print(10 < 3)
print(10 == 3)
print(10 != 3)

# 국어, 영어, 수학 성적이
# 100, 81, 90점이다.
# 평균이 60점 이상이면 True 출력
kor = 100
eng = 81
math = 90
tot = kor + eng + math
avg = tot / 3
print("tot=", tot)
# %.2f : 소수점 이하 2자리만 출력
print("avg=%.2f" % avg)

# 논리 연산자
# 1) and : 양쪽 모두 참이어야 참
print(10 == 10 and 10 < 3)
print(10 == 10 and 10 > 3)
print(10 != 10 and 10 < 3)
print(10 != 10 and 10 > 3)

# 2) or : 어느 한쪽만 참이어도 참
print(10 == 10 or 10 < 3)
print(10 == 10 or 10 > 3)
print(10 != 10 or 10 < 3)
print(10 != 10 or 10 > 3)



# 과락
# 3과목의 평균이 60점 이상이면 True
# 단 어느 한 과목이라도 50점 미만이면 False
score1 = 100
score2 = 80
score3 = 49
tot = score1 + score2 + score3
avg = tot / 3
print(avg >= 60 and score1 >= 50 and score2 >= 50 and score3 >= 50)
