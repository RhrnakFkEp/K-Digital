'''
5
'''

# 날짜/시간과 관련된 기능을 가져옴
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")


year = now.year
print(year)
print(type(year))
print(str(year)[-2:])
# print(str(now.year)[-2:])

# 1~9 월은 앞에 0이 필요.
# 09월 등
print(now.month)

if 1 <= now.month <= 9:
    month = "0" + str(now.month)
    print(month)
else:
    month = str(now.month)
    print(month)

# 과제
# 일. 1~9 앞에 0 필요
# 시만 가지고 if 구문 or import os로 
# 1T와 2T. 그거임ㅇㅇ
# 1T : 09~10시이전
# ... 
# 8T : 17~18이전
# 1T, 2T 표현해서 출력.
