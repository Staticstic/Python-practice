# day07_string_ex03.py

# 문자열 2차원

# 파일 불러오기
name = []
score = []

data = "홍길동/87, 박수홍/20, 하하/13"

tmp = data.split(",")
print(tmp) # ['홍길동/87', ' 박수홍/20', ' 하하/13']

i = 0
while i < len(tmp):
    info = tmp[i].split("/")
    print(info)
    name.append(info[0])
    score.append(int(info[1]))
    i = i + 1
print(name)
print(score)

# 파일 저장하기
name = ["하하", "노홍철", "박명수"]
score = [11, 87, 24]
data = ""

i = 0
while i < len(name):
    data = data + name[i]
    data = data + "/"
    data = data + str(score[i])
    if i != len(name) - 1:
        data = data + ","
    i = i + 1
print(data)
