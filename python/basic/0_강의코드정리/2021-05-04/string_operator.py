'''
작성일자 : 2021-05-04
작성자 : 이예희
작성내용 : 파이썬 예제 2
- 혼자 공부하는 파이썬 CH02-1
- string_operator.py
'''

# 탭의 결과는 OS따라 다르게 나옴.
# 탭만큼의 공간을 할당하고, 글자가 들어감.
# 탭 공간에서 글자가 차지하는 공간을 뺀 나머지 공간만큼 띄워짐
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")  # 오빠
print("윤아린\t24\t강서구")  # 여동생
print("구름\t3\t강서구")     # 강아지?


# 둘이 같음.
print("동해물과 백두산이 마르고 닳도록\n\
하느님이 보우하사 우리나라 만세\n\
무궁화 삼천리 화려강산\n\
대한사람 대한으로 길이 보전하세")

# """은 주석의 역할도 있지만, 출력할 때, 여러줄 출력이 가능하게 함
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이보전하세""")

# 이렇게 쓰면 전부 붙여나옴
print("""동해물과 백두산이 마르고 닳도록 \
하느님이 보우하사 우리나라 만세 \
무궁화 삼천리 화려강산 \
대한사람 대한으로 길이보전하세""")



print("신동욱" + "강사님")

name = "신동욱"
position = "강사님"
print(name + position)

name = ["신동욱", "권기범"]
position = ["강사님", "매니저"]

for n, p in name, position:
    print(n, p)

for n, p in zip(name, position):
    print(n, p)


# print(1. + "신동욱 강사님") 
# 이건 안됨


print("오빠"*3)   #  오빠 세번 반복
print([0] * 3)   # 문자열 느낌으로 들어감. 이건 리스트형태
print(0 * 3)     # 수치. 즉, 정수형임
print(type([0]))