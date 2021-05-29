'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 혼자 공부하는 파이썬 CH07-1 예제 module_random.py
'''
import random
print("# random 모듈")

# random() : 0.0 <= x <= 1.0 사이의 float을 리턴
print("- random() : ", random.random())

# uniform(min, max) : 지정한 범위 사이의 float을 리턴
print("- uniform(10, 20) : ", random.uniform(10, 20))

# randrange() : 지정한 범위의 int 리턴
# - randrange(max) : 0부터 MAX 사이 값을 리턴
# - randrange(min, max) : min부터 max 사이 값을 리턴
print("- randrange(10): ", random.randrange(10))

# choice(list) : 리스트 내부 요소를 랜덤하게 선택
print("- choice([1, 2, 3, 4, 5]) :", random.choice([1, 2, 3, 4, 5]))

# shupple(list) : 리스트의 요소를 랜덤하게 섞음
print("- shuffle([1, 2, 3, 4, 5]", random.shuffle([1, 2, 3, 4, 5]))
rd_sf = random.shuffle([1, 2, 3, 4, 5])   # 섞어주긴 하는데 출력을 못함. 즉, 그 자리에서 바로 섞고 리턴값을 넘겨주지 않음.
print(rd_sf)

# sample(list, k = <숫자>) : 리스트의 요소 중 k개를 추출
print("- sample([1, 2, 3, 4, 5], k = 2) : ", random.sample([1, 2, 3, 4, 5], k = 2))

# 샘플을 사용해서 주사위에 해당하는 것을 제작.
# 주사위 1~6, k = 3(던지는 횟수)
# 주사위 : dice
# Number of throws : 던지는 횟수. ->NuOTh
print("- dice([1, 2, 3, 4, 5, 6], NuOTh = 3) : ", random.sample([1, 2, 3, 4, 5, 6], k = 3)) 
# 주사위는 비복원추출. 이함수는 비복원추출임. 중복값 출력 X

