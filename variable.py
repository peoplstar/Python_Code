name = "연탄이"
animal = "강아지"
age = 4 # 정수형
hobbit = "산책"
is_adult = age >= 3 # age가 3보다 크거나 같으면 boolean 형으로 is_adult에 저장

print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는 " + str(age) + "살이며," + hobbit + "을 아주 좋아해요") 
#age와 같은 정수를 print문에 출력시 str()로 변형
print(name, "는 ", age, "살이며, ", hobbit, "을 아주 좋아해요")
# + 대신 , 사용 가능 but, 공백 한개를 포함
print(name + "는 어른일까요? : " + str(is_adult))

'''
작은 띄움표 3개를 이용하면
여러줄로 주석입력 가능
Ctrl + / 전체 주석처리
'''

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station , 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : X 행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")