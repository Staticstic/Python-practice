# day01_input_ex01.py

# IO : 입력(Input), 출력(Output)


# 방법1
print("이름을 입력하세요")
name = input()
print("name =", name)

# 방법2
name = input("이름 입력 : ")
print("name =", name)

# Input 함수를 통해서 입력한 변수는 무조건 문자
age = input("나이 입력 : ")
print("age =", age)
# print(age + 1) 입력시 에러뜸

# type() : 데이터의 종류를 알려줌
print(type(age))

# 문자 -> 숫자 : int()
# 숫자 -> 문자 : str()

# 방법1
age = input("나이 입력 : ")
age = int(age)
# 방법2
age=int(input("나이 입력 : "))

