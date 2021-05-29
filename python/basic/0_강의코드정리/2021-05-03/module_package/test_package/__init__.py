'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 10
- 혼자 공부하는 파이썬 CH07-3 예제
- module_package/test_pacage/__init__.py
'''

# "from test_package import *"로
# 모듈을 읽어들일 때 가져올 모듈

__all__ = ["module_a", "module_b"]
# 사용시 읽어들일 모듈의 목록

# 패키지를 읽어들일 때 처리를 작성할 수도 있음.
print("test_pacakge를 읽어 들였습니다.")