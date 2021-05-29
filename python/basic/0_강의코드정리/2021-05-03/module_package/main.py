'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 9
- 혼자 공부하는 파이썬 CH07-3 예제
- module_package/main.py
'''
# 패키지 내부의 모듈을 읽어 들입니다.
import test_package.module_a as a
import test_package.module_b as b
# 패키지 디렉토리가 main과 같은 레벨에 있으면, 디렉토리명.파일명 으로 접근가능
# 패키지명.모듈명 으로 접근가능하단것.

print(a.variable_a)
print(b.variable_b)