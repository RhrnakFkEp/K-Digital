dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}


print("name :", dictionary["name"])
print("type :", dictionary["type"])
print("ingredient :", dictionary["ingredient"])
print("origin :", dictionary["origin"])


dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"] )


print(dictionary["ingredient"])
print(dictionary["ingredient"][1])
# 인덱스 번호로도 추출 가능


dict_key = {
    # name : "7D 건조 망고", # NameError
    "name" : "7D 건조 망고", # NameError
    type : "당절임"     # class type으로 당절임이 들어감
}


#########################################################################
# 과제 1: 대충 정규식 사용해서 뭔가 업그레이드 1 보면 기억나겠지?
# 과제 2: 정규식 사용해서 타임스템프 
# 과제 3 딕셔너리 
# 수강생리스트 연생. 리스트를 
# 인공지는 A반에 해당하는 걸 이름, 성별, 전공, 년생 추출해서 딕셔너리 타입으로 만들기 ㅇㅇ
# 그냥. 현재 년도 추출해서 년도 끝자리 숫자 2개 e.g. 21. 이것보다 년도가 크면, 1900년대생이고,
# 그것보다 작으면, 2000년대생하면 되잖아?

# AI_A = {
#     "name" : ["이름들"],
#     "major" : ["전공들"],
#     "gneder" : ["성별들"],
#     "age" : [나이들]
# }

# CSV, Excel = > 특정변수 대입
# readline. for 구문, open 활용 
# 판다스 loc iloc 등

# 처음에는 있는것부터 만들어보고
# 뒤로갈수록 없는걸 만들면됨
# 만들었던것도 새로운 방법으로 업그레이드, 최적화 등을 하는것.
###################################################################

# 키 값이 없어도 새롭게 생성됨
dictionary["price"] = 5000
print(dictionary)

dictionary["test"] = [5000, 10000]
print(dictionary)


# 요소 자체가 제거됨
del dictionary["test"]
print(dictionary)
