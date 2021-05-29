# 과제 2 : 코로나 예제
# 1. 열체크 (37.5) temp >= 37.5
#  - 코로나 검사

# 열 : temp
# 코로나 : covid19
# 문자 : message

temp = 36.5
covid19 = ""
message = "코로나19 컴사에서 양성판정을 받으셨습니다."

if temp >= 37.5:
    print("격리")
elif "양성" in message:
    print("코로나19 확진 판정 받으셨습니다. 격리실에 구금됩니다")
    covid19 = "1"
else : 
    print("코로나19 확진자가 아닙니다. 진료를 권합니다")

print(covid19)


temp - 36.5
covid19 = ""
message = "코로나19 컴사에서 음성판정을 받으셨습니다."

if temp >= 37.5 and "양성" in message:
    print("코로나19 확진자입니다. 격리실로 이동해주십시오")
else :
    print("코로나19 확진자가 아닙니다. 진료를 권합니다")

print("\n\n\n\n")

# 음식으로 or 연산을 활용하여 예를 만들어보세요.
print ("짜장면, 짬뽕, 탕수육")
food = input("먹고 싶은 음식을 골라주세요, 없으면 아무것도 입력하지 말고 enter키를 눌러주세요\n")

if food == "짜장면" or food == "짬뽕" or food == "탕수육":
    print("음식을 선택하셨습니다")
    print("배고프시군요")
else:
    
    print("음식을 선택하지 않으셨습니다")
    print("원하는 음식이 없거나 배가 고프지 않으시군요")