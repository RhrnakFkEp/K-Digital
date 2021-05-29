import datetime

# print("현재시각 출력")
now = datetime.datetime.now()
# print(now)

# # type() : 데이터의 타입확인
# print(type(now.year))

# print(now.year, "년") #, 로 이어붙였기에 띄워쓰기가 됨.
# print(str(now.year)+"년") 
# # int와 str을 연결연산하기에 int를 str으로 바꿔주어야오류발생하지 않음.

# print(now.month, "월")
# print(now.day, "일")

# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()


# 시간 출력방법
print("# 시간을 포맷에 맞춰 출력")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
# string format time : 시간을 문자열 형태로 불러옴
# Y : year, m : month, d : day
# H : hour, M : minute, s : second
# % : % 기호 뒤에 오는 포멧에 따라 변수를 받을것임
# ()(브레이스 괄호) 내에 변수를 가져올 수 있음.
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month, now.day, now.hour, now.minute, now.second)
# \ : 줄바꿈의 의미. 한줄로 적기에는 너무 길기에 코드 자체를 가독성을 위해 나눌 때 사용
# 대부분 쉼표(,) 뒤에서 사용
print(output_a)
print(output_b)

output_b1 = f"{now.year}년 {now.month}월 {now.day}일 \
{now.hour}시 {now.minute}분 {now.second}초"
print(output_b1)
# 탭 들어가는것도 인식.

output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# %d가 숫자데이터를 가져오는 것도 있으니까
# 날짜와 구분하기위함이 아닌가? day와 digit을 구분?
print(output_c)

a =3
print("으아 %d 으아" %3)
# 이것도 색이 이러네. 도대체 이유가 뭐지.