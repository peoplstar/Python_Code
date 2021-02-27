try:
    print("[한 자리 나누기 전용 계산기]")
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
