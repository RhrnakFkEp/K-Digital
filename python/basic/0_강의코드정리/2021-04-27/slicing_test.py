'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 슬라이싱
'''

name = "신동욱"
print(name[0:1])
# 0 ~ 1미만 번지 가져와서 print

# 신 -> 이
name = name.replace(name[0:1], "이")
name = name.replace("이", "신")
print(name) 

print(name.index("신")) # 인덱스를 가져옴.

# --------------------------

email = "sdw1904@naver.com"
eindex = email.index("@")
print(eindex)

email2 = "sykin415@gmail.com"
eindex = email2.index("@")
print(eindex)

emails = ["sdw1904@naver.com", "sykin415@gmail.com", "d2kims@naver.com"]

epass = []

for email in emails:
    # print(email)
    eindex = email.index("@")
    # print(eindex)
    # print(email[0:eindex])

    email_replace = email[0:eindex]
    # print(email_replace)

    if email_replace == "d2kims":
        # print("정상")
        # print(email_replace.replace("d2kims","jakook3"))
        epass.append(email_replace.replace("d2kims","jakook3"))

print(epass)


#판다스 도전하기

