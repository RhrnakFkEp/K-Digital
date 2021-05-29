'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 예제 module_urllib.py
'''

from urllib import request
# request : 요청
# 리스턴스 : 응답
# 클라이언트-서버 구조

target = request.urlopen("https://google.com")
# https://google.com 에 해당하는 url을 open하는 것을 서버에 요청하는걸 target이라는 변수에 담음
print(target)
# http 클라이언트에게서 응답받은것을 target이란 변수에 객체의 형태로 담음
output = target.read()
print(output)
# 해당 URL의 html코드를 가져옴.
# 결과값의 맨 앞에 b가 붙어있으므로 바이너리 데이터를의미.
# 2진데이터. 0과 1로 되어있는걸의미