# day06_list_ex12.py

# 리스트 컨트롤러

lst = []

# 리스트의 길이 : len()함수 활용
size = len(lst)
print(size)

while True:
    print(lst)

    print("1. 추가하기")
    print("2. 삭제하기")
    print("3. 삽입하기")
    print("4. 종료하기")

    choice = int(input("메뉴를 선택하세요. :"))

    if choice == 1:
        add_value = int(input("추가할 값을 입력하세요."))
        lst.append(add_value)
    elif choice == 2:
        del_value = int(input("삭제할 값을 입력하세요."))
        # 값의 유효성 검사
        # = 리스트 lst에 존재하는 값인지 체크하기
        check = -1
        i = 0
        while i < len(lst):
            if lst[i] == del_value:
                check = i
            i = i + 1
        if check == -1:
            print("입력 오류")
        else:
            tmp = lst
            lst = []
            i = 0
            while i < len(tmp):
                if i != check:
                    lst.append(tmp[i])
                i = i + 1
    elif choice == 3:
        insert_idx = int(input("삽입할 인덱스 입력 :"))
        insert_value = int(input("삽입할 값 입력:"))

        # 삽입할 위치 전까지 값 복사
        tmp = []
        i = 0
        while i < insert_idx:
            tmp.append(lst[i])
            i = i + 1
        # 삽입
        tmp.append(insert_value)
        #삽입할 위치 이후 값 복사
        i = insert_idx
        while i < len(lst):
            tmp.append(lst[i])
            i = i + 1

        lst = tmp 
    elif chocie == 4:
        break
    
