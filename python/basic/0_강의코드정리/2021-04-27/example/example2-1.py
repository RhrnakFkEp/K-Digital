'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 과제2-1. 100일이 되는 날짜

조건 :
- 오늘부터 사귀기 시작
- 현재날짜(2021-04-27)를 기준
- 사귄지 100일이 되는 날짜 출력
- datetime.timedelta 활용
'''

import datetime

# 현재 시간을 now에 담음
now = datetime.datetime.now()
# print(now)
print(f"오늘의 날짜는 {now.year}년 {now.month}월 {now.day}일 입니다.")

# 현재시간에 100일을 더함
after = now + datetime.timedelta(days = 100)
# print(after)

# f-string을 사용해서 년월일만 출력
print(f"오늘로 부터 100일 뒤의 날짜는 {after.year}년 {after.month}월 {after.day}일 입니다.")