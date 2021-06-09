#숫자형
print(5)
print(-10)
print(3.14)
print(1000)
print(2*8)
print(3*(3+1))
#문자형
print('풍선')
print("나비")
print("zzzzzzzzzz")
print("zzzz"*2)
#boolean - 참과 거짓
print(5 > 10) #false
print(5 < 10) #true
print(True) #true
print(not True) #False

#변수 = 값을 저장하는 공간
animal = "강아지"
name = "연탄이"
age = 4 #str() = 정수형 값을 문자형으로 바꿔줌
hobby = "산책"
is_adult = age >= 3

'''이렇게 
하면 
여러 문장이 
주석 처리 
됩니다.
'''

# 애완동물을 소개해 주세요~
print("우리집 " + animal + "의 이름은 " + name + "이에요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며,"+ hobby +"을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

#퀴즈
#변수를 이용해서 다음 문장을 출력하라

station = "사당"
print(station + " 행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + " 행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + " 행 열차가 들어오고 있습니다.")

print(1+1) #2
print(3-2) #1
print(6/3) #2.0

print(2**3) #8
print(5%3) #% : 나머지 구하기 2
print(10%3) #1
print(5//3) #1 #// : 몫
print(10//3) #3

print(10>3) #True
print(4 >= 7)
print(3 == 3) #True
print(4 == 3) #False
print(1 != 3) #True
print(not 1!=3) #False

print((3>0) and (4<5)) #True
print((3>0) & (3<5)) #True
print((3>0) or (3>5)) #True
print((3 > 0) | (3>5)) #True

print(5>4>3) #True
print(5>4>7) #false

#간단한 수식
print(2+3*4) #14
print((2+3) * 4) #20
number = 2 + 3 * 4
print(number) #14
number = number + 2
print(number) #16
number += 2 # number = number + 2 같은 내용
number *= 2
print(number) #36
number /= 2
print(number) #18
number %= 2
print(number) #나머지 : 0

#숫자처리 함수
print(abs(-5)) #5
print(pow(4, 2)) #16
print(max(5, 12)) #12
print(min(5, 12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림값 : 4
print(ceil(3.14)) #올림값 : 4
print(sqrt(16)) #제곱근 : 4


#랜덤 함수
from random import *
print(random()) #0 ~ 1 사이의 임의의 값 생성
print(random() * 10) #0 ~ 10 사시의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 사시의 임의의 값(정수) 생성
print(int(random() * 10) + 1) #1~ 10이하의 임의의 값(정수) 생성

print(int(random() * 45) + 1)

print(randrange(1, 46)) #1~46미만의 임의의 값 생성

print(randint(1, 45)) #1~45이하의 임의의 값 생성


#퀴즈
#조건 : 랜덤으로 날짜 뽑기
#월별 날짜 : 28이전으로 정해야 함
#매월 1~3일은 스터디 준비를 해야 하므로 제외

from random import *
date1 = int(randrange(4, 29))
date2 = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(date1) + "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 " + str(date2) + "일로 선정되었습니다.")

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬을 공부하고 있어요'
print(sentence2)

#슬라이싱
jumin = "960131-1234567"
print("성별 : " + jumin[1])
print("연 : "+jumin[0:2]) #0~2직전까지
print("월 : " + jumin[2:4])
print("월 : " + jumin[4:6]) 
print("생년월일 : " + jumin[0:6]) #처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #다 소문자
print(python.upper()) #다 대문자
print(python[0].isupper()) #True
print(len(python)) #길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) #5
index = python.index("n", index+1)
print(index) #15

print(python.find("n")) #java를 찾을 경우 -1 반환
print(python.index("Java")) #error 발생
print("hi")

print(python.count("n")) #2

#문자열 포맷
print("a" + "b") #ab
print("a", "b") #a b 

#방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강"))
#방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))
#방법3
print("나는 {age}살 이며, {color}색을 좋아해요".format(age=20, color="파랑"))
#방법4
age = 20
color = "파랑"
print(f"나는 {age}살 이며, {color}색을 좋아해요")

#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
#\"\' : 문장 내에서 따옴표
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print('저는 \'나도코딩\'입니다.')

# \\ : 문장 내에서 \
print("C:\\Programs\\eclipse")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

#\b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") #RedApple

#퀴즈 -- 다시 풀기
#사이트별로 비밀번호를 만들어주는 프로그램 작성
#규칙 1 : http:// 제외
#규칙 2 : 처음 만나는 점 제외
#규칙 3: 남은 글자중 처음 세자리 + 글자 개수 + 글자 내 'e' 갯수 + "!"로 구성

#url = "http://naver.com"
url = "http://daum.net"
my_str = url.replace("http://", "") #규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] #규칙 2 : my_str 변수 내에서 처음부터 .전까지 자름
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0}의  {1} 입니다.".format(url, password))


#리스트 : 순서를 가진 객체의 집합
#지하철 칸 별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호")) #1

#하하 추가
subway.append("하하")
print(subway)

#정형돈을 유재석 / 조세호 사이에 추가
subway.insert(1, "정형돈")
print(subway)

#하나씩 뒤에서 꺼냄
subway.pop() #하하, 박명수 제외
print(subway) 

#같은 이름인 사람이 몇 명인지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석")) #2


#정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list) #[1, 2, 3, 4, 5]

#순서 뒤집기 가능
num_list.reverse()
print(num_list) #[5, 4, 3, 2, 1]

#모두 지우기
num_list.clear()
print(num_list) #[]

#다양한 자료형과 함께 사용
num_list = [5, 4, 3, 2, 1]
mix_list = ["조세호", 20, True]

#리스트의 확장
num_list.extend(mix_list)
print(num_list) #[5, 4, 3, 2, 1, '조세호', 20, True]

#사전 : {}
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5])
print("hi")

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"

print(cabinet["C-20"])
print(cabinet)

#간 손님
del cabinet["c-20"]
print(cabinet)

#key들만 출력
print(cabinet.keys()) #dict_keys(['A-3', 'B-100', 'C-20'])

#value 들만 출력
print(cabinet.values()) #dict_values(['김종국', '김태호', '조세호'])

#key, value 둘 다 출력
print(cabinet.items()) #dict_items([('A-3', '김종국'), ('B-100', '김태호'), ('C-20', '조세호')])

#폐점
cabinet.clear()
print(cabinet) #{}

#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1]) 

#menu.add("생선까스") #튜플은 add 불가

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합
#중복 안 됨, 순서 ㅇ벗음
my_set = {1, 2, 3, 3, 3}
print(my_set) #{1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합(java와 python을 모두 할 수 있는 사람)
print(java & python) #{'유재석'}
print(java.intersection(python))

#합집합(java나 python을 할 수 있는 사람)
print(java | python) #{'양세형', '김태호', '박명수', '유재석'}
print(java.union(python))

#차집합 (java는 할 수 있으나, 파이썬은 할 줄 모르는 개발자)
print(java - python) #{'양세형', '김태호'}
print(java.difference(python))

#파이썬을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) #{'김태호', '박명수', '유재석'}

#java를 까먹음
java.remove("김태호")
print(java) #{'양세형', '유재석'}


# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) #<class 'set'>

menu = list(menu)
print(menu, type(menu)) #<class 'list'>

menu = tuple(menu)
print(menu, type(menu)) #<class 'tuple'>

#퀴즈
#조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건 2:  댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건 3 : random 모듈의 shuffle과 sample을 활용 
#댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰

#(출력 예제)
# 당첨자 발표
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#-- 축하합니다 -- 

#활용 예제
from random import *
list = [1, 2, 3, 4, 5]
print(list)
shuffle(list)
print(list)

#풀이법
from random import *
users = range(1, 21) #1 ~ 20까지 
#print(type(users))
users = list(users) 
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

#if
weather = input("오늘 날씨는 어때요? ")
#if 조건 : 
#    실행 명령문

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

#반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}",format(waiting_no)) #대기번호 : {0} 0 ~ 4

for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no)) #대기번호 : 1 ~ 5

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer)) #아이언맨(토르/아이엠 그루트), 커피가 준비되었습니다.

#while
customer = "토르"
index = 5
#while (조건):
while index >= 1:
    print("{0}, 커피가 준비되었습니다 {1}번 남았습니다.".format(customer, index))
    index -=1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")

# customer = "아이언맨"
# while True:
#      print("{0}, 커피가 준비되었습니다 호출 : {1}번".format(customer, index))
#      index += 1

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?") #토르가 왔을 때 반복문 탈출함 

#continue, break
absent = [2, 5] #결석
no_book = [7] #책을 깜빡함

for student in range(1, 11): #1~10번
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break #반복문 탈출 
    print("{0}, 책을 읽어봐".format(student)) #2, 5를 넘어가고 계속 이어짐

#한 줄 for
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students) #[1, 2, 3, 4, 5]
studnets = [i+100 for i in students]
print(studnets) #[101, 102, 103, 104, 105]


#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students] #[8, 4, 10]
print(students)

#학생 이름을 대문자로 변환
students =  ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) #['IRON MAN', 'THOR', 'I AM GROOT']

#퀴즈
#50명의 승객과 매칭 기회 있음
# 5~50분 사이의 난수로 소요시간이 걸림
# 5~15 사이의 승객만 매칭해야 함

#출력문 예제 
#[0] 1번째 손님 (소요시간 : 15분)
#[]  2번째 손님 (소요시간 : 50분)
#[0] 3번째 손님 (소요시간 : 5분)

from random import *
cnt = 0 #총 탑승 승객수
for i in range(1, 51): #1~50이라는 승객 수
    time = randrange(5, 51)
    if 5 <= time <= 15: #매칭 성공 : 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가처리
        print("[0] {0}번째 손님(소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: #매칭 실패 
        print("[] {0}번째 손님(소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 수 : {0}분".format(cnt))

#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

#balance = deposit()
balance = 0 #잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 500)
#print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원 이며, 잔액은 {1} 원 입니다.".format(commission, balance))

#기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업 
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석") #이름 : 유재석    나이 : 17       주 사용 언어: 파이썬
profile("김태호")

#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20) #유재석 20 파이썬
profile(main_lang="자바", age=25, name="김태호") #김태호 25 자바

#가변인자
#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ") #end=" " 밑에 있는 문장 계속 출력
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수 : 함수 호출내에서만 사용
# 전역변수 : 어디서든 사용 가능

gun = 10

def checkpoint(soldiers): 
    global gun #전역 공간에 있는 gun 사용 
    gun = gun - soldiers
    print("[함수 내] 남은 총  : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun -soldiers
    print("[함수 내] 남은 총  : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

#퀴즈 : 표준 체중을 구하는 프로그램
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

#조건 1 : 표준 체중은 별도의 함수 내에서 계산
        #함수명 : std_weight
        #전달값 : 키(height), 성별(gender)
#조건 2 : 표준 체중은 소수점 둘째자리까지 표시

#예) 키 175cm 남자 표준 체중은 67.38kg입니다.

def std_weight(height, gender): #키 : m단위(실수), gender : "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 #cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1} 표준 체중은 {2}kg입니다.".format(height, gender, weight))

#표준 입출력
print("Python", "Java", "Javascript", sep=" vs ") #Python vs Java vs Javascript

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미 있을까요?")

import sys
print("Python", "Java", file=sys.stdout) #표준출력
print("Python", "Java", file=sys.stderr) #표준에러

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #키와 value를 쌍으로 tuple로 보냄
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    #ljust : 8칸을 확보한 상태에서 왼쪽으로 정렬 

#은행 대기 순번표 
#001, 002, 003, .........
for num in range(1, 21):
    print("대기 번호 : "+ str(num).zfill(3)) 
    #0을 채움(zfill), 값이 없는 경우 0으로 채움(3공간)

answer = input("아무 값이나 입력하세요 : ") #input으로 나오는 값은 항상 String값으로 저장
print(type(answer)) #answer = 10하면 출력 시 str(answer) 필요
print("입력하신 값은 " + answer + "입니다.")


#빈 자리는 빈 공간으로 두고 오른쪽으로 정렬하되, 총 10자리 공간을 확보
print("{0: > 10}".format(500))
#양수일 때는 + 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500)) #+500
print("{0: >+10}".format(-500)) #-500

#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500)) #+500______
print("{0:_<10}".format(500)) #500_______

#3자리마다 콤마를 찍기
print("{0:,}".format(10000000000000))

#3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000000)) #+10,000,000,000,000
print("{0:+,}".format(-10000000000000)) #-10,000,000,000,000

#3자리 마다 콤마 찍어주기, 부호도 붙이고, 자릿수 확보하기
#빈자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000000))#+100,000,000,000,000^^^^^^^^^^

#소수점 출력
print("{0:f}".format(5/3)) #1.666667

#소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3)) #1.67
