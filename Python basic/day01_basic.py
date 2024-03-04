# day1_basic.py

# 한 줄 주석 (comment)

"""
여
러
줄
주
석
"""

# 실행 : F5
# 저장 : Ctrl + S
# 영어단어 + () : 함수
# print() 함수 : 괄호안의 내용이 shell 창에 뜸
# 문자열(string) 표현시 : " " , ' ' 사용
print("hello")
print('hello')
# 숫자 표현시 그냥 사용
print(3) # decimal (10진수의 정수)
print(3.14) # float (실수)

print("내 나이는 %d살 입니다." %10)
# 데이터가 2개 이상일 경우, 반드시 ()로 묶어줘야 한다.
print("국어 성적은 %d점이고, 학점은 %s입니다." %(100, "A"))

print("python","class")
print(11,10)
print(1,"day")

# 숫자+숫자 : 덧셈
print(1+2)
# 문자+문자 : 연결
print("python"+"class")
# 숫자+문자 : 에러발생
# print(1+"day")
