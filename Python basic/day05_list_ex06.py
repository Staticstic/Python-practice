# day05_list_ex06.py

# 캐릭터 이동하기
# 1. 문자 "읓"은 캐릭터이다.
# 2. 숫자1을 입력하면 캐릭터가 왼쪽으로 이동한다.
# 3. 숫자2를 입력하면 캐릭터가 오른쪽으로 이동한다.
# 4. 단, 좌우 끝에 도달했을 때 움직이지 못하도록 처리한다.

game = [0, 0, 0, "읓", 0, 0, 0]

i = 0
while i < 7:
    if game[i] != 0:
        loc = i
    i = i + 1
print(loc)

run = True
while run:
    num = int(input("숫자를 입력하세요 : "))
    if num == 1:
        if loc == 6:
            print("더 이상 움직일 수 없습니다.")
            continue        
        tmp = game[loc]
        game[loc] = game[loc + 1]
        game[loc + 1] = tmp
        loc = loc + 1
        print(game)
    if num == 2:
        if loc == 0:
            print("더 이상 움직일 수 없습니다.")
            continue
        tmp = game[loc]
        game[loc] = game[loc - 1]
        game[loc - 1] = tmp
        loc = loc - 1
        print(game)
    if num != 1 and num != 2:
        print("방향을 다시 입력하세요")
    
     
# 답
player = 3

while True:
    print(game)
    move = int(input("왼쪽(1), 오른쪽(2) 입력 :"))

    if move == 1:
        if player == 0:
            print("더 이상 움직일 수 없어요!")
            continue
        game[player] = 0
        game[player - 1] = "읓"
        player = player - 1
    elif move == 2:
        if player == 6:
            print("더 이상 움직일 수 없어요!")
            continue
        game[player] = 0
        game[player + 1] = "읓"
        player = player + 1
    
    
        
        
     
    
