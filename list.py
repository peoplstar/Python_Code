# list []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# list append

subway.append("하하")
print(subway)

# list 유재석 / 조세호 사이에 추가

subway.insert(1, "정형돈")
print(subway)

# list 중복 체크

subway.append("유재석")
print(subway.count("유재석"))

# list sort

num_list = [5,4,3,2,1]
num_list.sort()
print(num_list) 

num_list.reverse() # 반대로 sort
print(num_list)

# dictionary = {key : "value"}

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 만약 키값이 유효하지 않을 때 오류발생
print(cabinet.get(3)) # 만약 키값이 유효하지 않을 때 None 출력
print(cabinet.get(5, "사용 가능")) # None 대신 오류 값을 변경

print(3 in cabinet) # 3 이라는 값이 cabinet 에 있으면 True 없으면 False
cabinet = {"A-3":"컴퓨터", "B-2":"키보드"}
print(cabinet)
cabinet["A-3"] = "마우스"
cabinet["C-23"] = "패드"
print(cabinet)

del cabinet["C-23"] #  C-23 삭제
print(cabinet.keys()) # key 값들만 출력
print(cabinet.values()) # value 값들만 출력
print(cabinet.items()) # key, value 쌍으로 출력

cabinet.clear() # dictionary 초기화

# tuple add append 등 항목 추가 불가능

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# Quiz) 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 주는 추첨 프로그램 작성

# 조건 1 : 20명이 댓글 작성하였고 아이디는 1~20 을 가정
# 조건 2 : 무작위 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *

person = range(1,21) # 1 부터 21 미만까지 숫자 생성 class = 'range'
person = list(person)
shuffle(person)

winners = sample(person ,4) # person list에서 4개를 뽑음
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")
