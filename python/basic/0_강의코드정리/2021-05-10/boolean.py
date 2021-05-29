'''
3
'''

x = 10
under_20 = x < 20
print(under_20)
print(type(under_20))

print("under_20 :", under_20)
print("not under_20 :", not under_20)

# pdf 142p
# ticket : 티켓
# time : 시간. 시에 해당하는 것만. int

# and 실제 예
# 유명 연예인 공연 티켓 예매
# 조건 : 티켓 1장 구매, 오후 3시 이후

# 조건 만족, 
# print("공연을 볼 수 있습니다")
# 조건 불만족,
# print("공연을 볼 수 없습니다")

ticket = int(input("티켓을 몇 장 구매하시겠습니까?\n"))
time = int(input("공연을 관람하실 시간을 0~24사이의 숫자로 입력해주세요\n"))

print(0 < time < 24) # Ture / False
time0_24 = 0


if (0 < time < 24) == True:
    time0_24 = time
print(time0_24)

if ticket <= 1 and time0_24 > 15:
    print("공연을 관람하실 수 있습니다")
else:
    print("공연을 관람하실 수 없습니다")


print("\n\n\n\n\n")


## OR 연산자
price = int(input("결제할 금액의 숫자만 입력해주세요\n"))

print("\n우리카드와 신한카드로 결제하시면, 해당 금액에서 10% 할인이 적용됩니다")
print("결제 가능한 카드는 우리카드, 신한카드, 농협카드, BC카드, 국민카드입니다")
card = input("어떤 카드로 결제하시겠습니까?\n")
print()
if card == "우리카드" or card == "신한카드":
    print(f"{card}를 선택하셨습니다")
    print(f"결제하실 금액은 {price*0.9}원 입니다")
else:
    print(f"{card}를 선택하셨습니다")
    print("할인이 적용되지 않습니다")
    print(f"결제하실 금액은 {price}원 입니다")