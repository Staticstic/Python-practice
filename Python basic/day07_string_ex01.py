# day07_string_ex01.py

# 문자열(문자의 배열(리스트))

#       01234
text = "hello"

#문자의 인덱싱(indexing)
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[-1])

# 문제) hello를 olleh로 출력하시오.
i = len(text) - 1
while i >= 0:
    print(text[i], end="")
    i = i - 1
print()
    
# 문자의 개수 확인 : len()
size = len(text)
print(size)

# 문자의 슬라이싱(slicing)
text = "megait academy"
print(text[0:6])        # megait 출력, 마지막 인덱스의 문자는 출력 안함

# 주민번호를 통해 남성 여성을 판단해보자.
jumin = "971203-1018223"
if jumin[7] == "1" or jumin[7] == "3":
    print("남성")
elif jumin[7] == "2" or jumin[7] == "4":
    print("여성")

birthm = (jumin[2], jumin[3])
birthd = (jumin[4], jumin[5])
print(birthm)
print("생일은 %d월 %d일 입니다.")
