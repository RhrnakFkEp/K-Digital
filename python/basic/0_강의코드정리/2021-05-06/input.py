'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 4
- 혼자 공부하는 파이썬 CH02-3
- input.py
'''

string = input("입력>")

print("자료 :", string)
print("자료형 :", type(string))

# 불형으로 변환할 수 있음
string = bool(string)
print(string)
print(type(string))

 