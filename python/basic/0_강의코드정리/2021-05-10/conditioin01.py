'''
9
'''

import datetime

now = datetime.datetime.now()
print(now)


print(now.day)

if now.day % 2 == 0:
    print("짝수반이 출석합니다")
else:
    print("홀수반이 출석합니다")