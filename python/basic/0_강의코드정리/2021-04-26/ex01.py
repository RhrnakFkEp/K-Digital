'''
작성일자 : 2021-04-26
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH01-2 확인문제 ex01.py
'''

print("Hello! " * 3)
print("혼자 공부하다 모르면 동영상 강의를 참고하세요!")

import keyword
print(keyword.kwlist)

print("Hello python programming")
print(52)
print(273)
print(52, 272, "Hello")

print(52+272+"Hello") # 타입에러. 문자와 숫자를 연결할 수 없음
print("52" + str(272) + "Hello") # 정수를 문자형으로 변환해야함.


