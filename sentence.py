sentence = '나는 소년입니다'
print(sentence)
sentence2 = "this is python"
print(sentence2)
sentence3 = """ 
나는 소년이고,
this is python
""" 
# """ 
# 공백까지 출력가능
# """ 
print(sentence3) 

# 슬라이싱
jumin = "000000-3111111"
print("성별 : " + jumin[7]) # 인덱스 7의 값을 출력
print("연생 : " + jumin[0:2]) # 0 부터 2 직전 값 까지 출력
print("월 : " + jumin[2:4]) # 2 부터 4 직전 값 까지 출력
print("일 : " + jumin[4:6]) # 4 부터 6 직전 값 까지 출력

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전 값 까지 출력
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지 출력
print("뒤 7자리 (뒤에서 부터) : " + jumin[-7:]) # 가장 마지막 인덱스 -1 -> 맨 마지막부터 7번째까지 출력

# 문자열 처리 함수

python = "python is Amazing"

print(python.find("python")) # 레퍼런스가 있으면 0  없으면 -1
print(python.index("python")) # 레퍼런스가 있으면 0 없으면 컴파일 에러
print(python.count("n")) # python 변수 안에 'n' 이 몇번 나왔는지 출력

# 문자열 포매팅

print("나는 %d살입니다." % 20) # printf("%d", operator)
print("나는 %s살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬") #  printf("%s", operator) 
print("Apple 은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print("나는 {}살입니다.".format(20)) # {}에 값이 포매팅된다.
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간")) # 인덱스가 0인 '파란', 인덱스가 1인 '빨간'

print("나이는 {age}색이고. {color}색을 좋아해요.".format(age = 20, color = "빨간")) 

age = 20
color = "빨간"
print(f"나이는 {age}색이고. {color}색을 좋아해요.") # python.ver 3.6 이상

# Quiz) 사이트별 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com
# 규칙 1 : http:// 부분을 제외
# 규칙 2 : 처음 만나는 '.' 이후 부분을 제외 
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + '!'로 구성
# 예) nav51!

page = "http://naver.com"
page = page[7:page.index('.')]
count = len(page)
e_count = page.count('e')
tmp = page[:3]
password = tmp + str(count) + str(e_count) + "!"
print("{} 의 비밀번호는 {} 입니다.".format(page,password))

# 정식 답안
my_str = "http://dreamwiz.com"
my_str = my_str.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2 => my_str[0:5] 0 부터 5 직전까지 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{} 의 비밀번호는 {} 입니다.".format(my_str,password))