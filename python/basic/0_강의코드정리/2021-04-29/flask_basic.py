'''
작성일자 : 2021-04-29
작성자 : 이예희
작성내용 : 예제 2
- 혼자 공부하는 파이썬 예제
- flask_basic.py
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

# 실행할 때 띄어쓰기 하면 안됨.
# 서버가 만들어졌고, 내가 원하는 결과물도 나옴.
# 127.0.0.1 : Local host
# local host의 5000번 포트 사용

# tracert www.naver.com