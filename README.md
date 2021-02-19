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

