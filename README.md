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

|<img src="random_ex/int(random()).png" width="80%" height="100%" alt="int(random())"></img>|<img src="random_ex/randrange().png" width="85%" height="100%" alt="randrange()"></img>|<img src="random_ex/randint().png" width="90%" height="100%" alt="randint()"></img>|   
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

```python
for waiting_number in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_number))

for waiting_number in range(0, 5): 
    print("대기번호 : {0}".format(waiting_number))

    starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}손님, 커피가 준비되었습니다.".format(customer))

```

<img src = "test.PNG">