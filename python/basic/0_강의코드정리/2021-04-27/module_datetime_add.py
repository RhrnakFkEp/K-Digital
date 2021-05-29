'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 예제 module_datetime_add.py
'''

import datetime
now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks = 1, days = 1, hours= 1, minutes = 1, seconds = 1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()


# 과제
# 오늘 나는 사귀었습니다. 2021-04-27
# 100일이 되는 날짜?  datetime.timedelta 사용
# 100일이 되는 날짜 출력


# 특정 시간 요소 교체(replace)
print("# now.replace()로 1년 더하기")
output = now.replace(year = (now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# 과제
# 1년째 되는 날짜 출력


nextYear = now + datetime.timedelta(days = 365)
print(f"{nextYear.year}년 {nextYear.month}월 {nextYear.day}일 {nextYear.hour}시 {nextYear.minute}분 {nextYear.second}초")
