'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 14
- 혼자 공부하는 파이썬 CH02-4
- format04.py
'''

output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)

print(output_j)
print(output_k)

plus_minus = output_k[0]
print(plus_minus)
# 부호만 뽑아낼 수 있음 