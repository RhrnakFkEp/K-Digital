'''
작성일자 : 2021-04-29
작성자 : 이예희
작성내용 : 예제 5
- 혼자 공부하는 파이썬 예제
- func_deco.py
'''

# 함수 데코레이터 생성
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")

# 함수 호출
hello()