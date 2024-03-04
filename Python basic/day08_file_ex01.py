# day08_file_ex01.py

# open("파일명", "모드")

# 파일 쓰기(write)
f = open("test.txt", "wt")
data = input("메모장에 작성할 내용을 입력하세요 : ")
f.write(data)
f.close()

# 파일 불러오기(read)
f = open("test.txt", "rt")
data = f.read()
f.close
print(data)
