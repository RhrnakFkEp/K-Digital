'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 math모듈
'''

import math    # 수학과 관련된 모듈 전체를 불러옴

# VS Code에서 실행될 때 보이는 PS는 Power Shell의 약자.
# 삼각함수 함수
print(math.sin(1))          # sin 함수
print(math.cos(1))          # cos 함수
print(math.tan(1))          # tan 함수

# 소수관련 함수
print(math.floor(2.5))   # 소수점 아래 내림     
print(math.ceil(3.5))    # ceiling. 소수점 아래 올림
print(math.trunc(3.5))   # truncate. 소수점 아래 내림
print(round(2.5))        # round(a, b). a:반올림 적용할 수. b : 소수점 b번째 자리 이하로 반올림하겠단뜻.
# 반올림 할 자리의 수가 5면, 사사오입의 원칙이 적용됨
# 앞자리 수가 짝수면 내림, 홀수면 올림

# floor, trunc 차이?
print(math.floor(-1.7))    # -2. 음수가 더 커지는 방향
print(math.trunc(-1.7))    # -1. 0에 가까워지는 방향
print(math.floor(1.6))     # 1. 일반적인 반내림
print(math.trunc(1.6))     # 1. 일반적인 반내림

# 음수에서는 round도 일반적인 반올림 형식
print(round(-1.7))      # -2. 앞이 홀수. 반올림(값이 커지는 방향)
print(round(-1.3))      # -1  앞이 홀수. 반올림(값이 작아지는 방향)
print(round(-2.7))      # -3. 앞이 짝수. 반올림(값이 커지는 방향)
print(round(-2.3))      # -2. 앞이 짝수. 반올림(값이 작아지는 방향)

# 음수에서의 ceil, trunc 결과 같음
print(math.ceil(-1.3))  # -1. trunc의 음수연산과 같음
print(math.ceil(-1.7))  # -1
print(math.trunc(-1.3)) # -1

# ---------------------

from math import sin, cos, tan, floor, ceil
# math 모듈에서 원하는 함수/변수만 불러옴

from math import *
# math 모듈에서 모든 함수/변수를 불러옴

# ---------------------

import math as m
# math를 m이라는 별명으로 불러옴

print(m.sin(1))

# ----------------------

import random
# random.