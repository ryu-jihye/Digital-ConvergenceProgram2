#사칙연산
1+1 #2
1-2 #-1
2*2 #4
5/2 #2.5 (정수끼리 나눗셈을 해도 실수로 나옴)
4/2 #2.0

#나눗셈 후 소수점 이하를 버림(//)
5//2 #2
4//2 #2
5.5/2 #2.75(실수를 //로 사용 시 실수가 나오며 소수점 이하는 버림)

#나눗셈 후 나머지를 구함(%)
5%2 #1
#거듭제곱(**)
2 ** 10 #2의 10승

#값을 정수로 만들기(int)
int(3.3) #3
int(5/2) #2
int('10') #10

#객체의 자료형 알아내기(type)
type(10 #<class 'int'>

#몫과 나머지 구하기(divmod)
divmod(5, 2) #(2, 1) = 몫이 2, 나머지 1

quotient, remainder = divmod(5, 2)
print(quotient, remainder) #2 1

#진수, 8진수, 16진수
0b110 #6
0o10 #8
0xF #15

#실수 계산하기
3.5 + 2.1 #5.6
4.2 - 2.7 #1.5
1.5 * 3.1 #4.65
5.5 / 3.1 #1.7741935483870968

#실수와 정수 같이 계산(실수로 나옴) 
4.2 + 5 #9.2 

#값을 실수로 만들기(float)
float(5) #5.0
float(1+2) #3.0
float('5.3') #5.3
type(3.5) #<class 'float'>

#복소수(여기서 j는 허수)
1.2+1.3j #(1.2+1.3j)
complex(1.2, 1.3) #(1.2+1.3j)

#괄호 사용하기
(35+1)*2 #72

7 + (10-5)*2

int(0.2467 * 12 + 4.159)

print(int(102*0.6+225))

#변수 만들기
x=10
x #10
y='Hello World'
y #Hello World

#변수 자료형 알아내기
type(x) #int type
type(y) #str type

#변수 여러 개를 한 번에 만들기
x, y, z = 10, 20, 30
x #10
y #20
z #30

x = y = z = 10
x #10
y #10
z #10

x, y = 10, 20
x, y = y, x
x #20
y #10

#변수 삭제하기(del)
x = 10
del x
x #정의되지 않았다고 나옴

#빈 변수 만들기
x = None
print(x)
x #아무것도 출력x

#변수로 계산하기
a = 10
b = 20
c = a + b
c #30

#산술 연산 후 할당 연산자 사용
a = 10
a+20 #30
a #10

a=10
a = a + 10
a #20

d += 10 #d라는 변수 할당 x

#부호 붙이기
x = -10
+x #-10
-x #10

#매번 다른 값을 변수에 할당(input)
input() #'Hello World'

#input 함수의 결과를 변수에 할당
#변수 = input()

x = input()
#x에 입력한 값(Jeju)
#x 출력 시 Jeju 나옴

x = input('문자열을 입력하세요 : ')
#x에 입력한 값(coffee)
#x 출력 시 coffee 나옴

#두 숫자의 합 구하기
a = input('첫 번째 숫자를 입력하세요 : ')
b = input('두 번째 숫자를 입력하세요 : ')
a+b #1020

type(a) #str type
type(b) #str type

#입력값을 정수로 변환
a = int(input('첫 번째 숫자를 입력하세요 : '))
b = int(input('두 번째 숫자를 입력하세요 : '))
print(a+b) #30

#입력 값을 변수 두 개에 저장하기
a, b = input('문자열 두 개를 입력하세요 : ').split()
print(a) #star
print(b) #bucks

#두 숫자의 합 구하기
a, b = input('숫자 두 개를 입력하세요: ').split()
print(a + b) #5090

#입력 값을 정수로 변환
a, b = input('숫자 두 개를 입력하세요: ').split()
a = int(a) #50
b = int(b) #90
print(a+b) #140 혹은 print(int(a) + int(b))

#map을 이용하여 정수로 변환하기(split의 결과를 모두 int로 변환)
a, b = map(int, input('숫자 두 개를 입력하세요 : ').split())
print(a+b) #30

#입력 받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요 : ').split(','))
print(a+b) #30

# 연습문제: 정수 세 개를 입력받고 합계 출력하기
a, b, c = map(int, input().split()) #10, 20, 30
print(a + b + c) #60

