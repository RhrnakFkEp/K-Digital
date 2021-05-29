'''
작성일자 : 2021-04-29
작성자 : 이예희
작성내용 : 예제 4, 6
- 혼자 공부하는 파이썬 예제
- 343p(371p) 
- 346p(374p)
'''

# 예제 4

from math import sin, cos, tan, floor, ceil

# print(sin(1))
# print(cos(1))
# print(tan(1))

# print(floor(2.5))
# print(ceil(2.5))

#-------------------------------------------------------
# 예제 6

# # 모듈을 가져옴
from functools import wraps

# 함수로 데코레이터를 생성
# def test(fucntion):
#     @wraps(function)
#     def wrapper(*arg, **kwargs):
#         print("인사가 시작되었습니다.")
#         function(*arg, **kwargs)
#         print("인사가 종료되었습니다.")
#         return wrapper


from functools import wraps

def test(function):
  @wraps(function)
  def wrapper(*arg, **kwargs):
    print("인사 시작")
    result = function(*arg, **kwargs)
    print("인사 종료")
    return result
  return wrapper

def add(a,b):
  return a+b

add = test(add)
print(add(3,4))
