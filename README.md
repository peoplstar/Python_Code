# Python Training

`I'll share the link  i heard in the youtube lecture `

- ### Link : [Youtube](https://www.youtube.com/watch?v=kWiCuklohdY&t=15841s)

## - __02.08__ -
> **<h3>Variable</h3>**
```python
name = "연탄이"
animal = "강아지"
age = 4
hobbit = "산책"
is_adult = age >= 3 
```
- Python에서 변수 선언시 자료형을 **언급**하지 않는다.

```python
print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는 " + str(age) + "살이며," + hobbit + "을 아주 좋아해요") 
```
- print는 String으로 인식하기에 age와 같은 정수형은 **str()**로 형변환

> **<h3>Sentence</h3>**
```python
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "this is python"
print(sentence2)
sentence3 = """ 
나는 소년이고,
this is python
""" 
```
- String 초기화시 `' '` , `" "` 로 가능
- `"""` , `"""` 로 묶어주면 __줄바꿈 공백__까지 입력 가능
> **<h3>Slicing</h3>**
```python
secret_num = "000000-3111111"
print("성별 : " + secret_num[7])
print("연생 : " + secret_num[0:2])
print("월 : " + secret_num[2:4]) 

print("생년월일 : " + secret_num[:6])
print("뒤 7자리 : " + secret_num[7:])
```
- **`[7]`** : 인덱스 7의 값을 출력
- **`[2:4]`** : 인덱스 2 부터 4 직전 값 까지 출력
- **`[:6]`** : 처음부터 6 직전 값 까지 출력
- **`[7:]`** : 7 부터 끝까지 출력

> **<h3>Formating</h3>**
```python
print("나는 %d살입니다." % 20) # printf("%d", operator)
print("나는 %s살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬") #  printf("%s", operator) 

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print("나는 {}살입니다.".format(20)) # {}에 값이 포매팅된다.
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
```
- ~~`print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))` 이것만 사용~~

## - __02.09__ -
> **<h3>Math</h3>**
```python
print(1 != 3)
print(not (1 !=3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (7 < 5))
print((3 > 0) | (7 < 5))
```
- `!=` 와 `not`은 True 일때 False, False 일때 True 값을 반환

```python
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수값 생성
print(randrange(0,10)) # 0 ~ 10 미만의 임의의 값 생성
print(randint(0,9)) # 0 ~ 9 이하의 임의의 값 생성
```

| <img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/int(random()).PNG" width="80%" height="100%" alt="int(random())"></img> |<img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/randrange().PNG" width="85%" height="100%" alt="randrange()"></img>|<img src="https://github.com/peoplstar/Python_Code/blob/main/random_ex/randint().PNG" width="90%" height="100%" alt="randint()"></img>|   
|:---:|:---:|:---:|
|`print(int(random() * 10))`|`print(randrange(0,10))`|`print(randint(0,9))`|

## - __02.10__ -
> **<h3>List</h3>**

```python
num_list = [10, 20, 30]
subway = ["유재석", "조세호", "박명수"]
empty = list() 
empty = []
subway[-1]
```
- List는 인덱스를 지닌 배열과 동일
- 인덱스 -1 인 경우는 가장 마지막 인덱스에 접근
  
> **<h3>List Function</h3>**
```python
subway.append("하하")
subway.insert(1, "정형돈")
num_list.sort()
num_list.reverse()
del num_list[2]
num_list.index(5)
```
### - __임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때__ -
```python
import sys
data = list(map(int,sys.stdin.readline().split()))   
```
split()은 문자열을 나눠주는 함수입니다.
괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눕니다.

list()는 자료형을 리스트형으로 변환해주는 함수입니다.
map()은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 list()로 감싼다.   

`.append("temp")` : temp 값을 마지막 인덱스에 추가   
`.insert(1,"temp")` : 인덱스 1 인 위치에 temp 값 대입 <mark> &</mark> 그 이후 값은 모두 한자리씩 밀려남   
`.sort()` : 오름차순으로 정렬   
`.reverse()` : 리스트의 내부를 역순으로 뒤집음 
`del num_list[2]` : 인덱스가 2인 부분의 값을 삭제   
`.index(5)` : 리스트에 해당 값이 있으면 위치 값을 출력 <mark>&</mark> 없으면 ValueError

> **<h3> Dictionary</h3>** 
```python
cabinet = {3:"유재석", 100:"김태호"}
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
cabinet["A-3"] = "마우스"
cabinet["C-23"] = "패드"
```
- `{key : "value"}` 의 형식으로 key와 value를 쌍 형태
- Dictionary 에서 key는 고유한 값이기에 중복될 수 없다.
- Key의 값은 변하면 안되기에 Key에는 List를 사용 할 수 없지만     
Tuple은 사용 가능하다.

####   **- Dictionary Key**
```python
print(cabinet[3]) # 만약 키값이 유효하지 않을 때 오류발생
print(cabinet.get(3)) # 만약 키값이 유효하지 않을 때 None 출력
print(cabinet.get(5, "사용 가능")) # None 대신 오류 값을 변경
print(3 in cabinet) # 3 이라는 값이 cabinet 에 있으면 True 없으면 False
```

## - __02.11__ -
> **<h3>Conditional</h3>**
```python
weather = input("오늘 날씨는 어때요? : ") 
temp = int(input("기온은 어때요? : "))
    print("우산을 챙기세요")
elif weather == "미세먼지": # else if
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")  

if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("따뜻해요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: 
    print("많이 추워요")
```
- `and` = `&`  &nbsp;&nbsp;,&nbsp;&nbsp;  `or` = `|`
- input은 항상 문자열 `[` scanf , cin << `]` 와 유사 
- 항상 문자열로 받기에 `int(input())`로 형변환이 필요

####   **- For 반복문**
```python
for waiting_number in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_number))

for waiting_number in range(0, 5): 
    print("대기번호 : {0}".format(waiting_number))

    starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}손님, 커피가 준비되었습니다.".format(customer))
```
####   **- While 반복문**
```python
customer = "토르"
index = 5
while index >= 1: 
    print("{0}, 커피가 준비 되었습니다. {1}번 남았아요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# continue, break
absent = [2, 5] 
no_book = [7]
for student in range(1, 11):
    if student in absent: # student가 absent 에 포함 되어있다면
        continue 
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로".format(student))
        break
    print("{0}, 책 읽어봐.".format(student))
print("\n\n")
```
- `while ()` 내부 조건식이 False 일때 반복 종료
- `continue`  다음 반복으로 건너뜀
- `break` 반복문 종료

## - __02.12__ -
> **<h3>Function</h3>**
```python
# 기본값 설정

def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "C언어")
```
```python
# 같은 나이 같은 수업 같은 학교.

def profile1(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))

profile1("박명수")
```
- 인자를 기본으로 설정하여 이름만 넘겨줘도 실행가능
```python
# 가변 인자 
def profile2(name, age, *main_lang): 
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end = " ") # end = " " 출력 시 줄바꿈을 이행하지 않음
    for lang in main_lang:
        print(lang, end = " ")
    print() # 줄바꿈

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile2("김태호", 23, "KOtiln", "Swift")
```
- `*main_lang` 시 인자를 여러 개 입력 받을 수 있음
------
```python
gun = 10 # 전역 변수

def checkprint(soldiers): # 경계근무
    gun = 20 # ------(1)
    gun = gun - soldiers # 지역 변수
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 지역 변수 '10 출력'
checkprint(2) # 2명이 경계 근무 나감 '18' 출력
print("남은 총 : {0}".format(gun)) # 지역 변수 '10 출력'
```
- **지역변수** = `[`함수 내에서만 이용가능 `/` 함수 호출 시 생성 함수호출 `/` 끝날 시 사라짐`]`
- **전역변수** = `[`프로그램 어디에서도 호출 가능`]`
- **---- (1)** 에서 전역 변수로 사용하기 위해서는 `global gun`와 같이 변수 앞에 `global` 을 사용 
  
## - __02.13__ -
> **<h3>Standard In & Ounput</h3>**
```python
print("Python", "java", "C++", sep=",", end="?")  
print("무엇이 더 재미있을까요?")
```
- `sep` 값을 통해 문자간 공백 처리를 변경 
- `end` 값을 통해 문자열 마지막을 변경 **default는 줄바꿈**
```python
scores = {"수학":0, "영어":50, "코딩":100} # dictionary
for subject, score in scores.items(): # scores의 key 가 subject, values 가 score로 튜플로 보냄
    print(subject.ljust(8), str(score).rjust(4), sep=":")
                                                          
```
- `ljust(8)` 총 8칸을 확보한 후 왼쪽으로 정렬
- `rjust(4)` 총 4칸을 확보한 후 오른쪽으로 정렬
```python
# 001, 002, 003, 004, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) 
```
- `zfill(3)` 3개의 공간 중 없는 부분을 0으로 채움 `[ zero fill ]`
```python
# 빈 자리는 공백으로 두고, 오른쪽 정렬을 하되, 총 10자리 확보
print("{0: >10}".format(500)) # ' ' : 공백처리 > : 오른쪽 정렬 10 : 10자리 확보

# 양수일 땐 + 표시, 음수일 때 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<-10}".format(-500))

# 3자리마다 ,처리 +- 부호처리
print("{0:+,}".format(-1000000000))
print("{0:-,}".format(1000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # 소수 둘째자리까지 출력
```
## - __02.16__ -
> **<h3>File Input</h3>**
```python
score_file = open("score.txt","w",encoding="utf8") 
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # score.txt 파일이 생성되면서 print 해당 문자열이 텍스트파일안에 저장
```
```python
score_file = open("score.txt", "a", encoding="utf8") 
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
```
```python
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # score.file을 읽어 한번에 출력
score_file.close()
```
- 쓰기위한 목적 `W` , 읽기위한 목적 `R` , 덮어쓰기 `A` ,  `encondig="utf8"` 을 입력하지 않을시 한글 깨짐 현상
  
- `write()`를 사용할 시 줄바꿈을 포함하지 않는다.   
 따라서 `\n `포함시켜줘야함.

> **<h3>File Output</h3>**
```python
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 읽어오는 내용이 없으면
        break
    print(line, end="")
score_file.close()
```
```python
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 line을 읽어서 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
```
- `print(line)`만 이용 할 시 한 줄 읽고 커서는 자동으로 다음 줄로 이동
- 총 2번의 줄바꿈이 일어나게 되므로 `print(line, end="")` 로 출력 
> **<h3>with 연산자</h3>**
- 일반 입출력 시 `open()`,`close()` 두번에 걸쳐 실행
- `with`연산자 이용시 `close()`문을 사용하지 않아 번거로움을 제거

```python
with open("study.txt", "w", encoding="utf8") as study_file: 
    study_file.write("Python을 공부합니다.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read()) 
```
- `as study_file` : 불러온 `study.txt` 파일내용을 변수 `study_file`에 임시 저장

## - __02.18__ -
> **<h3>Class</h3>**
```python
class Unit:
    
    def setData(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2} ]".format(self.name, location, self.speed))

    def __init__(self, name, hp, speed)
        self.setData(name, hp, speed)
        print("[체력 : {0}] 의 {1} 유닛이 생성 되었습니다.".format(self.hp, self.name))

    def information(self, name, hp):
        print("이름 : {0}, 체력 : {1}".format(self.name, self.hp))

Marin = Unit("마린", 40)
```
- ` __init__` : 초기화 메소드, 객체가 생성될 때 자동으로 호출되어 성질 부여시켜줌
- 객체내의 메소드를 생성할 때 `def example(self):`와 같이 `self`를 필히 넣어야한다.
> 상속
```python
class AttackUnit(Unit):

    def setData(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 
``` 
-  **Unit class**의 내용을 상속 받음.
-  상속받을 클래스의 이름을 `class AttackUnit(Unit)`와 같이 () 안에 작성
> 다중 상속
```python
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속 : 부모 클래스를 2개 이상 상속
    
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩 (재정의)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
```
- 메소드 오버라이딩 :  `fly` 와 `move` 하나의 움직이는 동작이므로 같은 의미를 가진다.
따라서 `fly`와 `move` 함수를 하나로 통일
- `FlyableAttackUnit` 클래스에서는 `move`로 이용하기 위해 `self.fly()`로 함수 재정의

## - __02.27__ -
> **<h3>Except Handling</h3>**
```python
try:
    print("[한 자리 나누기 전용 계산기]")
    num = [] # empty list 
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(int(input("두번째 숫자를 입력하세요 : ")))
    num.append(int(num[0] / num[1]))
    print("{0} / {1} = {2}".format(num[0], num[1], num[4] ))
except ValueError:
    print("Error! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Error! 알 수 없는 에러 발생.")
    print(err)
```
- 디버깅 중 발생할 수 있는 오류를 예외처리
- `except ValueError`와 `except ZeroDivisionError`처럼 해당 오류만 예외적으로 처리할 수 있다.
- 그 외에 오류는 `except:`로 일괄적으로 처리
- 그 외에 오류가 무엇인지 알려면 `except Exception as ...`을 이용
- `ZeroDivisionError`의 내용을 `as err`로 `err`라는 변수처럼 이용할 수 있다.

```python
try:
    print("[두 자리 나누기 전용 계산기]")
    num = [] # empty list 
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(int(input("두번째 숫자를 입력하세요 : ")))
    num.append(int(num[0] / num[1]))
    if not(100 > num[0] > 10) or not(100 > num[1] > 10):
        raise ValueError
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))
except ValueError:
    print("Error! 잘못된 값을 입력하였습니다.")
```
- `raise`를 이용해 강제로 오류를 발생시켜 처리할 수 있다.

```python
class BigNumError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("[한 자리 나누기 전용 계산기]")
    num = [] # empty list 
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(int(input("두번째 숫자를 입력하세요 : ")))
    num.append(int(num[0] / num[1]))
    if num[0] > 10 or num[1] > 10:
        raise BigNumError("입력값 : {0}    {1}".format(num[0],num[1]))
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))
except BigNumError as err:
    print("Error! 잘못된 값을 입력하였습니다.")
    print(err)
finally:
    print("실행을 종료합니다.")
```
- 사용자 정의 예외처리 : 정해진 것이 아닌 사용자가 직접 오류를 예외처리하여 사용
- `raise`를 통해 원하는 예외를 불러옴
- `class BigNumError(Exception)`로 원하는 예외를 정의
- `BigNumError()`를 통해 원하는 메세지 전환
- `def __str__`클래스 자체의 내용을 출력하고 싶을 때(`__init__`에서 규정한) 형식을 지정하는 메서드
- `finally:`를 통해 `try`구문 종료시 무조건 실행

## - __03.03__ -
> **<h3>User Module</h3>**
```python
# module_test.py
# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))
# 조조 할인 가격
def price_morning(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 6000))
# 군인 할인 가격
def price_soldier(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 5000))
```
- 다른 파일에서 이용 할 만한 함수를 정의
```python
import module_test
module_test.price(3) # 3명의 영화 가격
module_test.price_morning(4) # 4명의 조조 할인 가격
module_test.price_soldier(7) # 7명의 군인 할인 가격

print("")

import module_test as movie
movie.price(3) # 3명의 영화 가격
movie.price_morning(4) # 4명의 조조 할인 가격
movie.price_soldier(7) # 7명의 군인 할인 가격

print("")

from module_test import *
price(3) # 3명의 영화 가격
price_morning(4) # 4명의 조조 할인 가격
price_soldier(7) # 7명의 군인 할인 가격

print("")

from module_test import price, price_morning
price(3)
price_morning(4)
# price_soldier(7) 사용불가
```
- `from` `import`를 이용하여 module_test.py의 함수를 활용
- `import ... as ...`를 이용하여 이름을 재정의해 편리하게 이용
- `from ... import *` ...내의 모든 함수를 활용

## - __03.04__ -
> **<h3>Package</h3>**
```python
# ThailandPackage
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] : 50만원")

# VietnamPackage
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] : 60만원")

# 실행할 package.py

import travel_package.thailand
trip_to = travel_package.thailand.ThailandPackage()
trip_to.detail()

from travel_package.vietnam import VietnamPackage 
trip_to = VietnamPackage()
trip_to.detail()

from travel_package import vietnam 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
```
- `import` 시 폴더이름.파일명으로 패키지를 불러 사용가능하지만, 파일내의 class명이나 함수명을 직접 부를순 없다.
- `from ... import ...` 구문은 파일내의 class명이나 함수명을 직접 부를순 있다.
```python
# __init__.py
__all__ = ["vietnam","thailand"]
```
- `from ... import *` 구문에서 어느 모듈을 사용할 지 `__all__ =` 를 통해  __`__init__.py`__ 파일로 정의해줘야한다.
```python
# 외부에서 모듈 사용하는 것인지 알아보는 여부
# Thailand.py
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] : 50만원")

if __name__ == "__main__":
    print("Thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 만 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
```
- `if __name__ : "__main__"` 사용자가 `__main__`인지 여부 확인
- 외부에서 모듈 호출시 `else`구문 호출
## - __04.20__ -
> **<h3>PyInstaller</h3>**

`pip install pyinstaller`를 통해 쉽게 exe 파일로 변환이 가능하다. 만약 `installtest.py`를 exe로 만들고자 하면 터미널 창에 `pyinstaller .\installtest.py` 하면 build , dist 디렉터리가 생기는데 dist 내부에 installtest.exe가 생성된다.   build, dist 내부에 다른 파일 없이 하나의 .exe 파일로 만들고 싶다면 `pyinstaller -F .\installtest.py`하면 exe 파일 하나만 생성된다. [installtest_image]  우린 생성된 이 파일은 cmd에서 직접 입력해서 열어볼 수 밖에 없다. 만약 Graphics User Interface가 있는 파일을 응용 프로그램으로 바꿀 때는 `pyinstaller -w -F .\installtest.py` 와 같이 `-w` windows 버젼 옵션을 붙이면 된다. GUI가 포함된 파일 같은 경우 이미지 파일을 할당하여 사용하는 경우가 많다. 하지만 해당 .exe 파일은 하나로 압축된 형태라 실행할 때 마다 압축해제하여 임시폴더 내의 이미지 파일을 불러오게 되는데 임시폴더명은 항상 바뀌기에 되어 관리가 되질 않는다. 따라서 만들어 놓은 GUI의 소스 파일 .py에 해당 코드를 입력하여 경로를 지정해야 한다.
```python
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

// 사용될 이미지 파일 앞에 resource_path(이미지 경로)를 넣는다.
```
또한, pyinstaller 할 때 이미지 파일을 명시적으로 추가해줘야한다. `pyinstaller -w  --add-data '추가할 파일;어느 위치에 넣을지' -F .\____.py`
