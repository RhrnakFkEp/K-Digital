'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 1
- 혼자 공부하는 파이썬 CH07-3 예제
- module_basic/test_module.py
'''

# test_module.py 파일
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius
