# day08_function_ex04.py

# 내장(built-in) 모듈 불러오기
import random

# 내가 만든 모듈 불러오기
# *(애스터리스크) : 모두(all)
from module import *
x = 10
y = 20
x, y = change(x, y)
print("x =", x)
print("y =", y)

