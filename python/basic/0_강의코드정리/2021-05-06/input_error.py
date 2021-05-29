'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 5
- 혼자 공부하는 파이썬 CH02-3
- input_error.py
'''

# 숫자를 입력으로 받음
string = input("입력>")
# input으로 들어온건 문자형임

# 문자형과 숫자를 연산하려고 했으므로 에러발생
print("입력 + 100:", string + 100)

# map 함수 사용
# 공백 기준으로 분리
a, b = map(int, input("숫자 두개를 입력하세요 :").split())
print(a + b)

# , 기준으로 분리
a, b = map(int, input("숫자 두개를 입력하세요 :").split(','))
print(a + b)
 

# 과제1
# open 함수로 특정 csv 열기
# csv 파일은 콤마로 나누어져있으므로
# name, age = csv파일.split(',')
# for 구문, split(), append() 사용해서
# 파일로 가져다가 해보기 

a = "신동욱, 40"

print(a.split(','))
a_li = a.split(',')

name = a_li[0]
age = a_li[1]
print(name)
print(age)


import pandas as pd
# f = open()
f = pd.read_csv("경로", "r", encoding = "UTF-8")
print(f)
# f.close()