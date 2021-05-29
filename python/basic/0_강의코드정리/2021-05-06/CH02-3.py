'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 2
- 혼자 공부하는 파이썬 CH02-3
- CH02-3.py
'''

pi = 3.14159265
pi

# -------------------


pi = 3.14159265
print(pi+2)
print(pi-2)
print(pi*2)
print(pi/2)
print(pi%2) 
print(pi*pi)


# -------------------------


a = 10 

a += 10
a = a + 10

number = 100
number += 10
number += 20
number += 30
print("number : ", number)


# ----------------------------------


input("인사말을 입력하세요>")
# 안내메세지에 해당하는 것을 넣을 수 있음

hello = input("인사말을 입력하세요>")
# input 넣을 때, 프로그래밍 실행도중 잠시 멈추는걸 블록이라고 함
print(hello)
# input으로 넣어서 출력되는걸 리턴값이라고 하고
# 변수에 담아둘 수 있음

print(type(hello))
# input으로 받는건 str로 받아짐

number = input("숫자를 입력하세요>")
print(number)    # 제대로 숫자가 찍힘
print(type(number))
# 보기에는 int였지만, input으로 받았으므로 str임
# 정수로 사용하려면 int() 로 형을 변환해주어야함
number = int(number)
print(number)
print(type(number))
# number의 자료형이 정수형으로 바뀜


# -------------------------------------


int("안녕하세요")
float("안녕하세요")

int("52.273")


#-----------------------------------------