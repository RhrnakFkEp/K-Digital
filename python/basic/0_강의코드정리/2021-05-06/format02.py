'''
작성일자 : 2021-05-06
작성자 : 이예희
작성내용 : 파이썬 예제 12
- 혼자 공부하는 파이썬 CH02-4
- format02.py
'''

output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c) 
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)