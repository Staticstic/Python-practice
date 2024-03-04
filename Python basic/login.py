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
