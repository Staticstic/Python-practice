# 시작시간 5:21
# 1. 연봉계산
월급=int(input("월급을 입력 : "))
세전연봉=월급*12
세금=세전연봉/10
세후연봉=세전연봉-세금
print("연봉=%d원" %세후연봉)

# 2. 최소 화폐매수 (800원)
돈=int(input("돈을 입력 :"))
오백원=돈//500
백원=돈%500//100
print("%d원=500원 %d개, 100원 %d개" %(돈, 오백원, 백원))

# 3. 값 교체 (1단계)
x=int(input("x 입력 : "))
y=int(input("y 입력 : "))

tmp=x
x=y
y=tmp
print("x=%d, y=%d" %(x,tmp))
# 4. 과락 
kor=int(input("국어점수 입력 :"))
eng=int(input("영어점수 입력 :"))
math=int(input("수학점수 입력 :"))

tot=kor+eng+math
avg=tot/3
print(avg>=60 and kor>=50 and eng>=50 and math>=50)
