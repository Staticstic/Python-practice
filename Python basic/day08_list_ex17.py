# day08_list_ex17.py

# 타자연습 게임[2단계]
# 1. 단어를 랜덤하게 출제한다.
# 2. 이 때 단어의 랜덤한 위치에 단어 대신 *을 출력한다.
# 3. 정답을 맞추면 다음 문제가 출제된다.
# 4. 모든 정답을 다 맞추면 게임은 종료된다.
# 예) 문제1. p*ython
#     입력1 :python
#     문제2. *sp
#     입력2 :php
#     문제2. j*p
#     ...

import random
words = ["python", "java", "jsp", "android", "html"]
# 단어 셔플
i = 0
while i < 100:
    r = random.randint(0, len(words)-1)
    tmp = words[0]
    words[0] = words[r]
    words[r] = tmp
    i += 1
    
# 단어 전체 출력
i = 0
while i < len(words):
    print(words[i])
    i = i + 1
print()

# 단어 한글자씩 출력
i = 0
while i < len(words[0]):
    print(words[0][i])
    i = i + 1
print()

# 한글자에 *출력하고 한글자씩 출력
idx = random.randint(0, len(words[i])-1)
i = 0
while i < len(words[0]):
    if i == idx:
        print("*")
    else:
        print(words[0][i])
    i += 1
print()

# 답
i = 0
while i < 100:
    r = random.randint(0, len(words)-1)
    tmp = words[0]
    words[0] = words[r]
    words[r] = tmp
    i += 1
i = 0
while i < len(words):
    print("문제%d. " %(i+1), end=" ")
    r = random.randint(0, len(words[i])-1)
    j = 0
    while j < len(words[i]):
        if j == r:
            print("*", end=" ")
        else:
            print(words[i][j], end=" ")
        j = j + 1
    my_word = input(": ")

    if words[i] == my_word:
        i = i + 1
