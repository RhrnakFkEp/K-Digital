'''
작성일자 : 2021-05-04
작성자 : 이예희
작성내용 : 파이썬 예제 5
- 혼자 공부하는 파이썬 CH02-2
- CH02-2.py
'''

print(type(52))
print(type(52.273))

print(0)
print(type(0))
print(0.0)
print(type(0.0))

# 사칙연산 가능
print(5+7)
print(5-7)
print(5*7)
print(5/7)

print(3/2)   # 나누기
print(3//2)  # 몫
print(3%2)   # 나머지


# 슬라이싱?
korea_jumin_2000_before = "800101-1234567"
korea_jumin_2000_after = "000101-4345678"

foreign_jumin_2000_before = "900101-5678901"
foreign_jumin_2000_after = "000101-8901234"

print(korea_jumin_2000_before[7])
print(korea_jumin_2000_after[7])
print(foreign_jumin_2000_before[7])
print(foreign_jumin_2000_after[7])

if int(foreign_jumin_2000_after[7]) % 2 == 0:
    print("여자입니다.")
else:
    print("남자입니다.")



cookies = ["엄마손파이", "빈츠", "뽀또", "아이비"]

mompie_all=[]
mompie = int(input("엄마손 파이의 전채 개수를 입력해주세요.\n"))
for m1 in range(0, mompie):
    print(m1)
    m1.append(mompie_all)

mompie_all.append("엄마손파이")
print(mompie_all)

mompie = cookies[0]*10
binch = cookies[1]*20
bbo = cookies[2]*15
ivy = cookies[3]*8

print(len(mompie)) # 엄마손파이의 문자열의 개수가 50개임. 문자의 수.
