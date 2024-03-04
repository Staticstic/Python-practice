# day01_var_ex02.py

#변수는 오로지 대입연사자(=)를 통해서만이 값의 변화가 이뤄진다.
num = 3
num = 10
print("num = %d" % num)

print(num + 1) # 11
print(num)     # 10

num = num + 1
print(num)

# 문제) x와 y의 값을 교체해 보자.
x = 10
y = 20

# temporary : 임시의
tmp=x 
x = y 
y = tmp
print("x =", x)
print("y =", y)
