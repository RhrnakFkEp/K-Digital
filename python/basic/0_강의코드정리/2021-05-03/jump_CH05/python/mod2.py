'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 13
- 점프 투 파이썬 CH07-2 예제
- mod2.py
'''

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)

def sum(a, b):
    return a+b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))

# python import mod2
# 로 진입할경우, __name__ == "__main__"부분이
# 거짓이 되므로 실행되지 않음!
# 어디서 접근하냐에 따라 실행되냐 되지않냐는듯.