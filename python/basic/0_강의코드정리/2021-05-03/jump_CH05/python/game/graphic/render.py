'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 16
- 점프 투 파이썬 CH07-2 예제
- game/graphic/render.py
'''

# render.py

# from game.sound.echo import echo_test
from ..sound.echo import echo_test
# relative(상대적인. 즉, 상대경로) 적용가능

def render_test():
    print("render")
    echo_test()
