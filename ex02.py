a = [1, 2, 3, 4]
while a:
    print(a.pop())

    print("반복문 안")
print("반복문 밖")

#--------------------------------------------------------------------------------------------------
#1번
a = 80
b = 75
c = 55
(a+b+c) / 3 #70.0

#3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#5
a = "a:b:c:d"
b = a.replace(":", "#") #:를 #로 바꾸기
print(b) 

#7['Life', 'is', 'too', 'short'] 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) #단어들 사이마다 공백을 넣어줘야 함
print(result)

#9
a[[1]] = 'python'
#오류 이유 : 딕셔너리의 키로는 변하는 값을 사용할 수 없기 때문
#위의 키로 사용된 [1]은 리스트로 변하는 값
#키로 사용되는 값들은 변하지 않는 값 필요(문자열, 튜플, 숫자)


#11 중복 값 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a) #a 리스트를 집합 자료형으로 변환
b = list(aSet) #집합자료형을 리스트 자료형으로 다시 변환
print(b)

#2 13이 홀수인지 짝수인지 판별
1%2
2%2
3%2
4%2

#4 
pin = "881120-1068234"
print(pin[7]) #1이면 남자, 2면 여자

#6[1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]
a = [1, 3, 5, 4, 2]
a.sort() #정렬
a.reverse() #순서 바꿈
print(a)

#8 튜플에 값 추가(튜플은 값 변경 x)
a = (1, 2, 3)
a = a + (4,) #새로운 튜플 생성, 그 값이 a 변수에 대입
print(a)

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#12
a = b= [1, 2, 3]
a[1] = 4
print(b) #[1, 4, 3] a와 b 변수 모두 동일한 [1,2,3] 리스트 객체 사용하기 때문

x=10
if x == 10:
    print('10입니다.')
    print('ten')

number = int(input('숫자를 입력하세요:'))
if number%2 == 0:
    print('입력하신 숫자는 짝수입니다.')
if number%2 != 0:
    print('입력하신 숫자는 홀수입니다.')

#>>> money = 2000
#>>> card = True
#>>> if money >= 3000 or card:
#...     print("택시를 타고 가라")
#... else:
#...     print("걸어가라")

#>>> pocket = ['papaer', 'cellphone', 'money']
#>>> if 'money' in pocket:
#...     print("택시를 타고 가라")
#... else:
#...     print("걸어가라")
#... 
#택시를 타고 가라

#>>> pocket = ['papaer', 'cellphone', 'money']
#>>> if 'money' in pocket:
#...     pass 
#... else:
#...     print("카드를 꺼내라")
#... #아무 결과 나오지 않음

#in

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """