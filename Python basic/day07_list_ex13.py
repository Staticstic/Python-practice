# day07_list_ex13.py

# 참조변수(주소를 참조한다.) : reference variable
lst = [1, 2, 3, 4, 5]
tmp = lst
tmp[1] = 100

print("lst =", lst)
print("tmp =", tmp)
