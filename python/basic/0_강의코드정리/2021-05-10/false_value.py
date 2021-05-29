'''
12
'''

print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 반환됩니다")



# 음식주문 과제
# map과 split을 이용하게끔 조금 수정하기
# 음식 주문이 있을 때와 없을때
order = []
order_food = input("음식을 주문하세요\n")
order.append(order_food)

# print(order)
# print(order[0])

# 데이터가 있으면 True, 없으면 False
if order:
    # order == Ture가 생략된 형태
    print(f"조리해야하는 음식은 {order}입니다")
    # 배열의 맨 앞 요소를 빼내는 코드를 작성하면, 첫 번째 주문 음식이 제거됨
    print(f"{order[0]}의 조리가 완료되었습니다")
    del order[0]
        if order:
            print(f"조리해야하는 음식은 {order}입니다")
        else :
            print("조리해아하는 음식은 없습니다")
else:
    print("조리해야하는 음식은 없습니다")