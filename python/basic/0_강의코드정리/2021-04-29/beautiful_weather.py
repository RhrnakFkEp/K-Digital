'''
작성일자 : 2021-04-29
작성자 : 이예희
작성내용 : 예제 1
- 혼자 공부하는 파이썬 예제
- beautiful_weather.py
'''

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
# print(target)  
# <http.client.HTTPResponse object at 0x0000028346BD98E0>
# 응답받아서 메모리에 객체를 생성함

# BeautifulSoup
soup = BeautifulSoup(target, "html.parser")
# print(soup)

# pip install lxml
loc_list = soup.select("location")
# 지정한 태그를 모두 가져옴
# print(loc_list)


for location in soup.select("location"):
    print(location.select_one("city"))
    print("도시 :", location.select_one("city").string)
    print("날씨 :", location.select_one("wf").string)
    print("최저기온 :", location.select_one("tmn").text)
    print("최고기온 :", location.select_one("tmx").get_text())
    print()

# select_one("태그") : 태그에 해당하는 것을 1개 가져옴

# BeautifulSoup : 함수가 아니라 클래스의 생성자이기 때문에 대문자로 되어있음.
