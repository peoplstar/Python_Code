print(1 != 3)
print(not (1 !=3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (7 < 5))
print((3 > 0) | (7 < 5))

print(5 > 4 > 3)
print(7 > 4 > 5)

number = 2 + 3 * 4
print(number)
number += 2 
print(number)
number /= 2 
print(number)

print(abs(-53)) # 53의 절대값
print(pow(4,3)) # 4의 3 제곱
print(max(41,63)) # 가장 큰 값 출력
print(round(4.6)) # 반올림

from math import floor # math library 에 있는 모든 것을 활용하겠다.
from math import ceil # math library 에 있는 모든 것을 활용하겠다.
from math import sqrt # math library 에 있는 모든 것을 활용하겠다.

print(floor(4.99)) # 내림
print(ceil(3.06)) # 올림
print(sqrt(16)) # 제곱근

from random import random # math library 에 있는 모든 것을 활용하겠다.
from random import randrange # math library 에 있는 모든 것을 활용하겠다.
from random import randint # math library 에 있는 모든 것을 활용하겠다.

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 정수값 생성
print(randrange(1,45)) # 1 ~ 45 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz) 스터디 모임에 가입하여 월 4회 스터디를 하는데 3번은 온라인, 1번은 오프라인으로 수업
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램

# 조건 1 : 랜덤으로 날짜를 뽑음
# 조건 2 : 월별 날짜가 다르므로 최소 일수인 28일 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 위해 제외시킴

# 출력문 예제 ) "오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다."

#from random import * : 위 실습을 과정이 있기에 주석처리
date = randint(4,29)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
