'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 예제 module_os.py
'''

import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 내부 폴더 요소 : ", os.listdir())

# directory 생성/제거
os.mkdir("hello")  # os.mkdir 같은 파일이 존재하면 만들 수 없음.(중복생성불가)
os.rmdir("hello")

with open("origin.txt", 'w') as file:
    file.write("hello")
# origin 이라는 파일을 쓰기모드로 file이라는 이름으로 가져옴.
# 파일에 hello라고 쓰고 닫음(with)
# 파일이 존재하지 않을 시 가져온 파일 이름으로 파일을 새로 생성.

os.rename("origin.txt", "new.txt")
# origin.txt를 new.txt로 이름을 변경.
# 기본 파일에서 복제되어 같은 내용의 파일이 새로 생성되어 이름이 변경되는게 아닌
# 기존에 있던 파일의 이름을 바꾸는 것.
# 원본 파일의 네임이 변경됨.

os.remove("new.txt")
# 파일제거. directory제거와 다름.
# new.txt라는 파일을 제거.

# 디렉토리 내용 출력
os.system("dir")

