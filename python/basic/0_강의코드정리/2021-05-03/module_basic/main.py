'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 2
- 혼자 공부하는 파이썬 CH07-3 예제
- module_basic/main.py
'''

# main.py 파일
import test_module as test

radius = test.number_input()  # 반지름 입력
print(test.get_circumference(radius))  # 원주?
print(test.get_circle_area(radius))  # 원의 면적
