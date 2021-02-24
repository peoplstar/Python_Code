# Python Training

`I'll share the link  i heard in the youtube lecture `

- ## Link : [Youtube](https://www.youtube.com/watch?v=kWiCuklohdY&t=15841s)

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
> **<h3>`with`</h3>**
- 일반 입출력 시 `open()`,`close()` 두번에 걸쳐 실행
- `with`연산자 이용시 `close()`문을 사용하지 않아 번거로움을 제거

```python
with open("study.txt", "w", encoding="utf8") as study_file: 
    study_file.write("Python을 공부합니다.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read()) 
```
- `as study_file` : 불러온 `study.txt` 파일내용을 변수 `study_file`에 임시 저장