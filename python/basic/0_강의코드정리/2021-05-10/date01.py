'''
6
'''

import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month, now.day,
    now.hour, now.minute, now.second
))

print(f"{now.year}년 {now.month}월 {now.day}일\
{now.hour}시 {now.minute}분 {now.second}초")


# 과제
# 특정 파일을 선택하는 코드
# 파일명만 가져옴
# 파일명을 변경하는 코드
# import os
# 추가적을 작성하기 