# if 조건:
#         실행 명령문

weather = input("오늘 날씨는 어때요 ? : ") # input은 항상 문자열로 받음.scanf , cin << 
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지": # else if
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온이 어때요? : ")) # 항상 문자열이기에 int으로 형변환
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("따뜻해요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: 
    print("많이 추워요")

# for 반복문 

for waiting_number in [0, 1, 2, 3, 4]: # [0, 1, 2, 3, 4]  대신 range(5) 사용 가능
    print("대기번호 : {0}".format(waiting_number))

for waiting_number in range(1, 6): 
    print("대기번호 : {0}".format(waiting_number))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}손님, 커피가 준비되었습니다.".format(customer))

# while 반복문

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
        continue # 다음 반복으로 건너뜀
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로".format(student))
        break # 반복문 종료
    print("{0}, 책 읽어봐.".format(student))
print("\n\n")

# 출석번호가 1,2,3,4 앞에 100을 붙이기로함
students = range(1,6)
print(list(students[0:]))
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["iron man", "Thor", "groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)

# Quiz) 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수 구하는 프로그램
# 조건 1 : 운행 소요 시간은 5분 ~ 50분 사이의 난수
# 조건 2 : 5분 ~ 15분의 소요시간 승객만 매칭

from random import *

cnt = 0
check = "O"
for i in range(0,50): # 총 50명의 승객
    customer = randrange(5,51) # 매칭 시간 5 ~ 50분 난수
    if 5 <= customer <= 15: # 매칭 성공 시 
        check = "O" # 매칭 성공 시 [] 사이에 O 를 출력
        cnt += 1
    else: # 매칭 실패 시
        check = " " # 매칭 실패 시 [] 사이에 공백을 출력
    
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i+1, customer))
print("총 탑승 승객 : {0}분".format(cnt))