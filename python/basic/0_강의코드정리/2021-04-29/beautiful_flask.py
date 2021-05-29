'''
작성일자 : 2021-04-29
작성자 : 이예희
작성내용 : 예제 3
- 혼자 공부하는 파이썬 예제
- beautiful_flask.py
'''

# 모듈을 읽어 들입니다.
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup
    soup = BeautifulSoup(target, "html.parser")

    # location?
    output = ""
    for location in soup.select("location"):
        output += f"<h3>{location.select_one('city').string}</h3>"
        print(f"<h3>{location.select_one('city').string}</h3>")
        output += f"날씨 : {location.select_one('wf').text}<br/>"
        output += f"최저/최고 기온: {location.select_one('tmn').get_text()}/\
        {location.select_one('tmx').string}"
        output += "<hr/>"
    return output

if __name__ == "__main__":
    app.run(debug = True)
# 이거있으면 set run 안해도 됨.
