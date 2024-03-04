# day02_if_ex03.py

# 문제 1) 로그인 기능[1단계]
# id와 pw를 입력받아 로그인 성공여부를 출력
dbid=input("아이디를 입력하세요 :")
dbpw=input("패스워드를 입력하세요 :")
db_id = "qwer"
db_pw = "1234"
if dbid == db_id:
    if dbpw == db_pw:
        print("로그인 성공")
if dbid != db_id or dbpw != db_pw:
    print("로그인 실패")

# 답
my_id = input("ID 입력 :")
my_pw = input("PW 입력 :")
if db_id == my_id and db_pw == my_pw:
    print("로그인 성공!")
if db_id != my_id or db_pw != my_pw:
    print("로그인 실패!")
    
# 문제 2) 로그인기능[2단계]
# 1. id를 입력받는다.
# 2. id가 일치하면 pw를 입력받을 수 있다.
# 3. id와 pw가 모두 일치하면 "로그인 성공"
# 4. id가 틀리면, "id를 확인해주세요."
# 5. id는 맞지만 pw가 틀리면, "pw를 확인해주세요."
db_id = "qwer"
db_pw = "1234"
my_id = input("ID 입력 :")
if db_id == my_id:
    my_pw = input("PW 입력 :")
    if db_pw == my_pw:
        print("로그인 성공")
    if db_pw != my_pw:
        print("pw를 확인해주세요.")
if db_id != my_id:
    print("id를 확인해주세요.")

# cf) if문 작성 과정 pass
my_id = input("ID 입력 :")
if db_id == my_id:
    pass                # <-- pass 쓰는 연습하기
if db_id != my_id:
    print("id를 확인해주세요.")

# cf) 좌우 공백 제거
my_id = my_id.strip()

# 최종 답
db_id='qwer'
db_pw='1234'
my_id = input("id 입력:")
my_id = my_id.strip()
if db_id == my_id:
    my_pw = input("pw 입력:")
    my_pw = my_pw.strip()
    if db_pw == my_pw:
        print("로그인 성공!")
    if db_pw != my_pw:
        print("pw를 확인하세요:")
if db_id != my_id:
    print("id를 확인하세요:")
