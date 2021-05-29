'''
4
'''

number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다")

if number < 0:
    print("음수입니다")

if number == 0:
    print("0 입니다")


# if/elif/else로 바꾸기

if number > 0:
    print("양수입니다")
elif number < 0:
    print("음수입니다")
elif number == 0:
    print("0 입니다")
else:
    print("올바르지 않은 숫자입니다")