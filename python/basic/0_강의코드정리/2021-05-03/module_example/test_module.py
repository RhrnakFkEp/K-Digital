'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 5
- 혼자 공부하는 파이썬 CH07-3 예제
- module_example/test.module.py
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

# main에서 실행할 때, 모듈의 이름이 엔트리포인트(메인)가 아니기 때문에,
# 아래 if문을 실행하지 않음. 즉, 메인이 아니라 실행하지 않는것. 
# 이 모듈에서 실행하면, 이모듈 자체에 메인이 있다고 인식하기 때문에
# 이 문장이 실행됨!
if __name__ == "__main__":
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))