def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money : 
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(money))
        return balance

def withdraw_night(balance, money): # 밤에 출금하여 수수료발생
    commission = 100 # 수수료 100원
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 200)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission,balance))

# 기본값 설정

def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "C언어")

# 같은 나이 같은 수업 같은 학교.

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile("박명수") # 인자를 기본으로 설정하여 이름만 넘겨줘도 실행가능

# 가변 인자 
def profile(name, age, *main_lang): # *main_lang 시 인자를 여러 개 입력 받을 수 있음.
    print("이름 : {0}\t 나이 : {1}\t".format(name,age), end = " ") # end = " " 출력 시 줄바꿈을 이행하지 않음
    for lang in main_lang:
        print(lang, end = " ")
    print() # 줄바꿈

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 23, "KOtiln", "Swift")

# 지역변수 = [함수내에서만 이용가능 / 함수호출시 생성 함수호출 / 끝날 시 사라짐]
# 전역변수 = [프로그램 어디에서도 호출 가능]

gun = 10 # 전역 변수

def checkprint(soldiers): # 경계근무
    gun = 20 # 전역 변수를 사용하기 위해서는 -global gun- 변수 앞에 global을 사용
    gun = gun - soldiers # 지역 변수
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 지역 변수
checkprint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 지역 변수

# Quiz) 표준 체중을 구하는 프로그램

# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#       함수명 : std_weight
#       전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시
# 출력 예제 : 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(heigth, gender):
    if gender == "남자":
        return pow(heigth, 2) * 22
    else:
        return pow(heigth, 2) * 21

gender = input("성별을 입력해주세요 : ")
heigth = int(input("키를 입력해주세요 : ")) # input은 항상 문자열로 받기때문에 int로 형변환
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(heigth, gender, round(std_weight(heigth / 100, gender) ,2)))
