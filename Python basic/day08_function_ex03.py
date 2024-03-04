# day08_function_ex03.py

'''
함수
1) return X
def 함수명(parameter, 매개변수):
    ...
함수명(argument, 인자[인수])

2) return O
def 함수명():
    ...
    return 값
값 = 함수명()
'''

# x부터 y까지의 합을 리턴해주는 함수
def tot(x, y):
    total = 0
    i = x
    while i <= y:
        total += i
        i += 1
    return total

result = tot(1, 5)
print(result)

def get_max(lst):
    i = 0
    max_num = lst[0]
    while i < len(lst):
        if max_num < lst[i]:
            max_num = lst[i]
        i += 1
    return max_num

lst = [23, 59, 98, 7]
result = get_max(lst)
print(result)
