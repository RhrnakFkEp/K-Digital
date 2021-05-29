'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 6
- 혼자 공부하는 파이썬 CH07-3 예제
- module_example/main.py
'''

# main.py 파일
import test_module as test

radius = test.number_input()  # 반지름 입력
print(test.get_circumference(radius))  # 원주?
print(test.get_circle_area(radius))  # 원의 면적

# 이건 당연히 동작. 얘 자신도 메인을 지녔으니까!
if __name__ == "__main__":
    print("get_circumference(20):", test.get_circumference(20))
    print("get_circle_area(20):", test.get_circle_area(20))