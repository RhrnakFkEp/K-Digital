'''
작성일자 : 2021-05-03
작성자 : 이예희
작성내용 : 파이썬 예제 12
- 점프 투 파이썬 CH07-2 예제
- mod1.py
'''

# mod1.py
def sum(a, b):
    return a+b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
    return result


if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))
    
# import만 해도 프린트가 동작
# 그래서 __name__ == __main__을 주는것
# if문에 넣어 print()실행되지 않도록 제어해줌
# 모듈자체를 실행하지 않는한 메인이 아니라 모듈의 
# 이름이 출력되기때문에 저걸로 걸어놓으면 
# 실행되지않음

