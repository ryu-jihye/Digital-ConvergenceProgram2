coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

    a=0
    while a<10:
            a=a+1
            if a % 2 == 0: continue
            print(a) #1 3 5 7 9

for i in range(10):
    print("Hello World", i) #Hello World 10번 반복

for i in range(0, 10, 3):
    print("Hello World", i) #0, 3, 6, 9

for i in range(10, 7, -1):
    print("Hello World", i) #10, 9, 8

a = [10, 20, 30, 40, 50]
for i in a:
    print(i) #10 20 30 40 50

students = ['conan', 'rose', 'ran']
for student in students:
    print(student)

 #end : 공백
for letter in 'Hello':
    print(letter, end='')   

for letter in reversed('Hello'):
    print(letter, end='')

dan = 3
for i in range(1, 10, 1):
    print("%d * %d = %2d" %(dan, i, dan*i))

print("구구단을 출력합니다.\n")
for x in range(2, 10):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 9):
        print(x, "X", y, "=", x*y)
print("---------------------")

for i in range(1, 9):
    for j in range(2, 9):
            print(j, 'x', i, '=', j*i, end='\t')
            print()


#리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
        result.append(num*3)

print(result) #[3, 6, 9, 12]


#---------------------------------------------------
#2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
i = 1
while i<= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result) #166833
    
#5 A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#for문을 사용하여 A 학급의 평균 점수를 구해 보자.

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in a:
    total += score
average = total / len(a)
print(average) #79.0

#6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
#numbers = [1, 2, 3, 4, 5]
#result = []
#for n in numbers:
#    if n % 2 == 1:
#        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result) #[2, 6, 10]

#함수의 선언(def)
def add(v1, v2):
    result = 0
    result = v1 + v2
    return result

#main code
sum = 0
sum = add(100, 200)
print("%d와 %d의 add()함수의 결과는 %d" %(100, 200, sum))

#-----------------------------
def calculator(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    return result

result = 0
num1, num2, operator = 0, 0, ''
operator = input('계산 선택(+, -, *, /) : ')
num1 = int(input('첫 번째 숫자 입력 :'))
num2 = int(input('두 번째 숫자 입력 :'))
result = calculator(num1, operator, num2)
print('%d %s %d = %d' % (num1, operator, num2, result))

def print_hello():
    print('Hello World')

#반환값과 매개변수1
def function1():
    result = 10
    return result

def function2():
    print("반환값 없는 함수 실행")
sum = function1()

print("funtion1()에서 반환한 값 = %d" % sum)
function2()

#반환값과 매개변수2
def para2_func(num1, num2):
    result = 0
    result = num1 + num2
    return result

def para3_func(num1, num2, num3):
    result = 0
    result = num1 + num2 + num3
    return result
sum = 0
sum = para2_func(10, 20)
print("매개변수 2개인 함수 호출 결과 = %d" %sum) #30
sum = para3_func(10, 20, 30)
print("매개변수 3개인 함수 호출 결과 = %d" %sum) #60

def printVar(a, b):
    print("a: ", a, "b : ", b)

printVar(a=10, b=20) #a:  10 b :  20
printVar(b=20, a=10) #a:  10 b :  20

def add_many(*args):
    result = 0
    for i in args:
            result = result + i
    return result

print("1~3", add_many(1, 2, 3)) #6
print("1~8", add_many(1,2,3,4,5,6,7,8)) #36

def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(a=1) #{'a': 1}
print_kwargs(name='conan', age=10) #{'name': 'conan', 'age': 10}

def add_and_mul(a, b):
    return a+b, a*b

print(add_and_mul(3, 4)) #(7, 12)

def print_info(name, age, address='비밀'):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)
print_info('conan', 8, "Brown's")
print_info('conan', 8)

def print_info2(name, address='비밀', age ):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)
print_info('conan', 8, "Brown's")