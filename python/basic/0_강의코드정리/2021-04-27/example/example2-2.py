'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 과제2-2. 1년 뒤 날짜

조건 :
- 현재날짜(2021-04-27)를 기준으로 1년 뒤 날짜 출력
- replace 활용
'''

import datetime

now = datetime.datetime.now()
# print(now)

after = now.replace(year = now.year + 1)
# print(after)

print(f"현재날짜는 {now.year}년 {now.month}월 {now.day}일 입니다.")
print(f"1년 뒤의 날짜는 {after.year}년 {after.month}월 {after.day}일 입니다.")