'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 예제 module_sys.py
'''

import sys
# system 관련 모듈을 불러옴

# 명령 매개변수 출력
print(sys.argv)   # arg : argument의 약자. v : value?

print("-------------------------")

# 컴퓨터 환경과 관련된 정보 출력
print("getwindowsversion() :", sys.getwindowsversion())
print("-------")
print("copyright : ", sys.copyright)
print("-------")
print("version : ", sys.version)

# 프로그램 강제 종료
sys.exit()