score_file = open("score.txt","w",encoding="utf8") # 쓰기위한 목적 w, 읽기위한 목적 r, encondig="utf8"을 입력하지 않을시 한글 꺠짐 현상
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # score.txt 파일이 생성되면서 print 해당 문자열이 텍스트파일안에 저장

score_file = open("score.txt", "a", encoding="utf8") # 덮어쓰기 "a"
score_file.write("과학 : 80") # write()를 사용할 시 줄바꿈 포함 X 따라서 \n 포함시켜줘야함.
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # score.file을 읽어 한번에 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 읽어오는 내용이 없으면
        break
    print(line, end="") # 한 줄씩 읽기, 한 줄 읽고 커서는 자동으로 다음 줄로 이동, 다음 줄 이동 안하기 위해서 end=""
score_file.close()

print()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 line을 읽어서 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print("\n")
# pickle 항상 바이너리타입
# 바이너리란 ? .jpg, .png, .mp3와 같은 .exe 실행파일 등이 바이너리 파일

# import pickle
# profile_file = open("profile.pickle", "wb") # 바이너라타입이기에 w 뒤에 b 를 붙여준다.
# profile = {"이름":"유재석", "나이":30, "취미":["축구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)# pickle를 이용해서 파일에 작성, profile에 있는 정보를 file에 저장
# profile_file.close()

# with 연산자 : 일반 파일입출력과 달리 close()문을 사용 안해도 됨

with open("study.txt", "w", encoding="utf8") as study_file: # txt로 불러온 파일은 study_file에 저장
    study_file.write("Python을 공부합니다.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read()) 

# Quiz) 매주 1회 작성해야 하는 보고서를 아래와 같이 출력

# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차 부터 50주차까지 보고서 파일을 만드는 프로그램을 작성
# 조건 : 파일명은 1주차.txt 2주차.txt ..와 같이 만듭니다.

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")