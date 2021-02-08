import sys
print("Python", "java", "C++", sep=",", end="?") # sep 값을 통해 문자간 공백 처리를 변경할 수 있음 
                                                 # end 값을 통해 문자열 마지막을 변경 default는 줄바꿈
print("무엇이 더 재미있을까요?")

print("Jack Daniels", "Don Royal", file=sys.stdout)  
print("Jack Daniels", "Don Royal", file=sys.stderr) 

# 출력 포맷

scores = {"수학":0, "영어":50, "코딩":100} # dictionary
for subject, score in scores.items(): # scores의 key 가 subject, values 가 score로 튜플로 보냄
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) 총 8칸을 확보한 후 왼쪽으로 정렬
                                                          # rjust(4) 총 4칸을 확보한 후 오른쪽으로 정렬

# 은행 대기순번표
# 001, 002, 003, 004, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(3) 3개의 공간 중 없는 부분을 0으로 채움

# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # input은 항상 문자열로 입력 받음
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 공백으로 두고, 오른쪽 정렬을 하되, 총 10자리 확보
print("{0: >10}".format(500)) # ' '= 공백처리 > = 오른쪽 정렬 10 = 10자리 확보

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