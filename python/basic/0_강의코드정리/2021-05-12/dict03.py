'''
3
'''

dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

print("요소 제거 이전 :", dictionary)

del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후 :", dictionary)


# 리스트에서는 리스트 길이를 넘는 인덱스에 접근하면 IndexError 발생. 
# 딕셔너리도 존재하지 않는 키에 접근하면 KeyError 발생함
# 존재하지 않는 키를 제거하려고 해도 KeyError 발생

dictionary = {}
# print(dictionary["key"])   # KeyError 
# del dictionary["key"]      # KeyError



