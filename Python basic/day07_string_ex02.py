# day07_string_ex02.py

# 문자열 1차원
data = "11,32,29,100,87"

# 파일 불러오기
# split()
tmp = data.split(",")
print(tmp)
# 길이 저장하기
size = len(tmp)
# 저장소 생성하기
score = []

i = 0
while i < size:
    num = int(tmp[i])
    score.append(num)
    i = i + 1
print(score)

# 파일 저장하기
score = [87, 10, 23, 49, 100]
data = ""

i = 0
while i < len(score):
    data = data + str(score[i])
    if i != len(score) - 1:
        data = data + ","
    i = i + 1
print(data)


