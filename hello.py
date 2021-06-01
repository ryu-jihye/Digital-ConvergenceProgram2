print("hello")
#실행 키는 shfit+enter 

boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""
print(boolVar)

#type() = 변수의 데이터 형식을 확인함
num = 100
type(num) #int
num2 = 100.0
type(num2) #float

num3 = 100
type(num)
num = 100 ** 100
num

a = 3.14
b = 3.14e5
print(a, b) #자바와 달리 a, b를 동시에 출력 가능

a= 5; b=3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b) #산술연산, //:몫, %:나머지

a = True; b = False
type(a); type(b) #둘 다 타입이 boolean 

a = (10 == 10) #true
b = (10 > 20) #false
print(a, b)

a = 10
a += 2; print(a) #12
a -= 3; print(a) #9
a *= 4; print(a) #36
a /= 3; print(a) #12.0


a=10 #변수 a에 10을 할당
print(a)

a=float(10) #a를 실수형으롭 변환
print(a)

a = 4 #변수 a에 정수 4를 할당
b = 2 #변수 b에 정수 2를 할당
print(a/b) #2.0


a = int(10.2); b=int(5.3)
print(a+b, a, b) #15, 10, 5 -> 정수형으로 출력

a='10.0' #a에 문자열 '10.0'을 할당
b=float(a) #a를 실수형으로 변환 후 변수 b에 할당
print(a) #10.0

print(b) #10.0

print(a+b) #a는 문자열, b는 실수형이므로 덧셈 불가

a = '10.0'
a = float(a) #a를 실수형으로 변환 후 a에 할당
b = a #실수형 a값을 b에 할당
print(a + b) #20.0(두 실수형의 합을 출력)

a = str(a) #변수a에 저장된 값을 문자열로 변환 후 a에 할당 
b = str(b) #변수b에 저장된 값을 문자열로 변환 후 b에 할당 
print(a+b) #10.010.0(문자와 문자와의 결함)

#순서가 섞이게 됨 = 파일로 작성하는 것이 편함
#input() : 표준입력함수로, 사용자가 문자열을 콘솔창에 입력할 수 있게 함 = java scanner
print("이름을 입력하세요 :") 
name = input() #conan 입력
print("안녕", name) # 안녕 conan


temp = float(input("온도를 입력하세요 : "))
print(temp)

#여러 줄로 된 문자열 사용하기
str = 'Hello\nWorld'
print(str) #\n : 줄바꿈


str= """""Hello
World"""""
print(str) #줄바꿈으로 나타남(Hello\nWorld)

#인덱스 : 글자 하나하나가 갖는 상대적인 주소
str = "Hello World"
str[0] #H
str[1:3] #le
str[3:] #lo World
str[::2] #HloWrd
str[5:9:2] #o

#H    e   l   l   o       W   o   r   l   d 
#0    1   2   3   4   5   6   7   8   9   10
#-11 -10 -9 -8  -7  -6  -5  -4  -3  -2  -1

# '+' : 문자열 연결 / '*' : 문자열 반복
str = "Hello"+"World"
str #HelloWorld
str = "Hello"*3
str #HelloHelloHello

#replace('기존 문자열', '새 문자열') -> 문자열의 요소들을 바꾸는 것은 아님
str = "THis is my pencil"
str.replace('my', 'nice') #THis is nice pencil
str #This is my pencil(기존 것 출력)

#문자열 공백 제거
str = "  Hello World "
str.strip() #Hello World (문자열 양쪽 공백 제거)
str.rstrip() #'  Hello World'(문자열 오른쪽 공백 제거)
str.lstrip() #'Hello World ' (문자열 왼쪽 공백 제거)

str = "hello world"
str.capitalize() #Hello world (문자열 첫 글자를 대문자로)
str.title() #Hello World (문자열 단어의 첫 글자를 대문자로)
str.upper() 
str = str.upper() #HELLO WORLD (문자열 문자들을 모두 대문자로)
str.lower() #hello world (문자열 문자들을 모두 소문자로)

s = ['conan', 'rose', 'ran'] #리스트 : 하나의 변수에 여러 값을 할당하는 자료형

#인덱스 : 리스트에 있는 값에 접근하기 위해, 이 값의 상대적인 주소를 사용하는 것
students = ['conan', 'rose', 'ran']
print(students[0]) #conan
print(students[-2]) #rose
print(len(students)) #3

#슬라이스 : 리스트의 인덱스를 사용하여 전체 리스트에서 일부를 잘라내어 반환(시작 인덱스부터 끝 인덱스 -1 까지)
#변수이름 [시작인덱스 : 끝인덱스] 또는 변수이름[시작 : 끝 : 증가폭]

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[0:4] #['서울', '부산', '인천', '대구']
cities[5:] #['광주', '울산', '수원']
cities[-8:] #['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[:] #['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[-50:4] #['서울', '부산', '인천', '대구']
cities[::2] #['서울', '인천', '대전', '울산']
cities[::-1] #['수원', '울산', '광주', '대전', '대구', '인천', '부산', '서울']


a = [1, 2, ['a', 'b', ['life', 'is']]]
            #0    1          2
a[2][2][0] #life

#리스트의 연산(덧셈)
students1 = ['conan', 'rose']
students2 = ['ran', 'kid', 'detective']
print(students1+students2) #['conan', 'rose', 'ran', 'kid', 'detective']
print(students1) #['conan', 'rose']
total_students = students1 + students2
total_students #['conan', 'rose', 'ran', 'kid', 'detective']

#리스트의 연산(곱셈)
total_students*2 #['conan', 'rose', 'ran', 'kid', 'detective', 'conan', 'rose', 'ran', 'kid', 'detective']

#리스트의 연산(in)
'kid'in students2 # True 

#리스트 추가
students = ['conan', 'rose']
#>>> students.append('ran') => 요소 추가
#>>> students
#['conan', 'rose', 'ran']

students.extend(['kid', 'detective']) #=> 리스트 추가
#>>> students
#['conan', 'rose', 'ran', 'kid', 'detective']

students.insert(0, 'areum') #0의 위치에 'arenum 추가
#>>> students 
#['areum', 'conan', 'rose', 'ran', 'kid', 'detective']

students.remove('detective') #리스트 내 특정 값 삭제
students #['areum', 'conan', 'rose', 'ran', 'kid']

students.pop() #kid(마지막 요소 또는 특정 인덱스의 요소 삭제)
students #['areum', 'conan', 'rose', 'ran']

students[1:2]=['detective', 'areum'] #1과 2위치에 해당 값 추가
students #['areum', 'detective', 'areum', 'rose', 'ran']

number = [1, 2, 2, 3, 4, 5, 5, 5]
number.count(2) #특정 값 개수 구하기

number = [10, 20, 30, 40, 50]
20 in number # True(특정값 유무 확인하기)

number = [10, 20, 30, 40, 50]
number.reverse()
number #[50, 40, 30, 20, 10](리스트 순서 뒤집기)

number = [23, 55, 33, 22, 44, 12, 4]
number.sort() 
number #[4, 12, 22, 23, 33, 44, 55] = 리스트 요소 정렬하기

#튜플 : 읽기만 가능(값 바꾸기 불가)
numbers = (10, 20, 30)
numbers
numbers = 10, 20, 30
numbers

numbers = (10)
type(numbers) #int type
numbers = 10
type(numbers) #int type

numbers = (10,) #튜플로 만들고 싶을 땐 ,붙이기
type(numbers) #tuple type
numbers = 10,
type(numbers) #tuple type

numbers = (10, 20)
numbers.append(40) #오류 발생
numbers[0]=30 #오류 발생
del(numbers[0]) #오류 발생

#튜플 자체는 del() 함수로 삭제 가능
del(numbers)
type(numbers)

#튜플의 사용 = 튜플 이름[인덱스]
numbers = (10, 20, 30, 40)
numbers[0]+numbers[2] #40
#튜플 이름[시작인덱스:끝인덱스]
numbers[1:3] #(20, 30)
numbers[1:] #(20, 30, 40)
numbers[-3:] #(20, 30, 40)

#튜플의 연산
numbers = (10, 20, 30, 40)
letters = ('a', 'b')
numbers + letters # (10, 20, 30, 40, 'a', 'b')
letters*3 #('a', 'b', 'a', 'b', 'a', 'b')

#딕셔너리 : 중괄호({})로 묶여 있으며 키와 값이 쌍으로 있음
dic1 = {1:'one', 2:'two', 3:'three'}
dic1 #{1: 'one', 2: 'two', 3: 'three'}

#딕셔너리 새로운 요소 추가
dic1[4]='four'
dic1 #{1: 'one', 2: 'two', 3: 'three', 4: 'four'}

#딕셔너리 요소값 변경 
dic1[4] = '사'
dic1 #{1: 'one', 2: 'two', 3: 'three', 4: '사'}

#딕셔너리 요소 삭제
del(dic1[4])
dic1 #{1: 'one', 2: 'two', 3: 'three'}

#딕셔너리 키를 이용하여 값에 접근
dic1[1] #one
dic1[3] #three

#딕셔너리 get()함수로 요소 접근
dic1.get(2) #two

#딕셔너리 존재하지 않는 값에 접근하는 경우
dic1[5] #error 발생
dic1.get(5) #반환하는 값이 없음

#딕셔너리이름.values() : 모든 값 반환
dic1.values() #dict_values(['one', 'two', 'three'])
#딕셔너리이름.items() : 튜플 형태로 반환
dic1.items() #dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
#in 딕셔너리 : 키가 딕셔너리에 있으면 True
1 in dic1 #True
5 in dic1 #False
8 not in dic1 #True
2 not in dic1 # False

#print[] 서식 지정 vs format() : 서식을 지원하는 print() & format()
#서식은 앞에 %가 붙음, %d는 정수를 의미
print("100") #100
print("%d" %100) #100
print("100+100") #100+100
print("%d" %(100+100)) #200

print("{}".format(100)) #100
print("{}".format(100+100)) #200

print("%d %d" %(100, 200)) #100 200