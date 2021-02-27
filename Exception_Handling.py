try:
    print("[나누기 전용 계산기]")
    num = [] # empty list 
    num.append(int(input("첫번째 숫자를 입력하세요 : ")))
    num.append(int(input("두번째 숫자를 입력하세요 : ")))
    num.append(int(num[0] / num[1]))
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))
except ValueError:
    print("Error! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Error! 알 수 없는 에러 발생.")
    print(err)

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

# Quiz) 자동주문 시스템 중 시스템 코드를 확인하고 적절한 예외처리 구문을 삽입해라.

# 조건 1 : 1보다 작거나 숫자가 아닌 값은 ValueError로 처리
#          출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 주문할 수 있는 총 주문량은 10마리, 재료 소진 시 사용자 정의 에러
#          [SoldOutError] 발생시키고 프로그램 종료
#           출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."


chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

while(True):
    print("남은 치킨 : {0}".format(chicken))
    try:
        order = int(input("치킨 몇 마리 주문하시겠습니까? :"))
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
        
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문하셨습니다.".format(waiting, chicken))
            waiting += 1
            chicken -= order
    