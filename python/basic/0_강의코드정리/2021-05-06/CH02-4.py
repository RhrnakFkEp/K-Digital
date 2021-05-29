'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 11
- 혼자 공부하는 파이썬 CH02-4
- CH02-4.py
'''


"{} {}".format(1, 2, 3, 4, 5)
"{} {} {}".format(1, 2)

#----------------------------


a = "Hello Python Programming...!" 
a.upper()
# 여권 등은 전부 대문자로 되어있음

en_name = input("본인의 이름을 영문으로 기입해주세요")
up_en_name = en_name.upper()
print(up_en_name)

en_hobby = input("본인의 취미를 대문자로 기입해주세요")
up_en_hobby = en_hobby.lower()
print(up_en_hobby)


#---------------------------------


input_a = """
        안녕하세요        
문자열의 함수를 알아봅니다
"""

print(input_a)
print(input_a.strip())
# 양쪽 공백 제거됨
# 문장 중간에 있는 띄어쓰기는 없어지지 않음


# -------------------------------------


print("TrainA10".isalnum())
print("10".isdigit())
# 문자열이 아니라 숫자로 인식함

#---------------------------------------------
# find(), rfind()

output_a = '안녕안녕하세요'.find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

#-------------------------------------------
# in

print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

#-------------------------------------------

if password.alnum() == False:
    print("특수문자가 포함된 안전한 비밀번호 입니다.")
if password.isalnum() == False:
    print("특수문자가 포함된 안전한 비밀번호 입니다.")


word = input("단어를 입력하세요 :")
output_a = "안녕안녕하세요".find(word)
print(output_a)
len(word)

range(len(word))
output_a[range(len)) # 슬라이싱 개념

word_result = output_a[0:len(word)]
print(word_result)




	
if password.alnum() == False:
    print("특수문자가 포함된 안전한 비밀번호 입니다.")
if password.isalnum() == False:
    print("특수문자가 포함된 안전한 비밀번호 입니다.")

# --------------------------------------------------------------

word = input("단어를 입력하세요 :")
output_a = "안녕안녕하세요".find(word)
print(output_a)
len(word)

range(len(word))
output_a[range(len)) # 슬라이싱 개념

word_result = output_a[0:len(word)]
print(word_result)

sentance = "안녕하세요 신동욱 강사님"
word = input("단어를 입력하세요 : ")

output_a = sentance.find(word)
print(output_a)
print(type(output_a))

# dlrjgoqhrl
word_result = sentance[output_a:len(word)]
print(word_result)


password = input("비밀번호를 입력해주세요. 특수문자(!, @, #, $) 포함")

if '!' in password or '@' in password or '#' in password or '$' in password:
	print("특수문자가 포함되어있습니다. 정상 password입니다")
else:
	print("특수문자가 포함되어잇지 않습니다")




# split() : 문자열 자르기
a = "10 20 30 40 50".split(" ")
print(a)