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

