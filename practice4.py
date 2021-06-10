#에러상황 -> 예외처리

print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

#숫자가 아닌 문자열을 넣을 때 오류 발생 -> 예외처리 하도록 함
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: #0으로 나눌 때 예외
    print(err) #division by zero


#리스트 만들기
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: #0으로 나눌 때 예외
    print(err) #division by zero

#리스트 만들기 중 nums.append(int(nums[0] / nums[1])) 빠진 경우
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    #list index out of rang로 오류 표시
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: #0으로 나눌 때 예외
    print(err) #division by zero    
#해결법(나머지 모든 에러)
except Exception as err: #Exception as err 에러 표시
    print("알 수 없는 에러가 발생하였습니다.")

#에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: #10이상 표시할 때 발생하는 에러
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

#사용자 정의 예외 처리
class BigNumberError(Exception):
    #pass
    def __init__(self, msg):
       self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: #10이상 표시할 때 발생하는 에러
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요2")
    print(err)


#finally : 예외 처리 구문 중 정상적이건, 오류가 나건 무조건 실행
class BigNumberError(Exception):
    #pass
    def __init__(self, msg):
       self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError: #10이상 표시할 때 발생하는 에러
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요2")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


#퀴즈
#자동 주문 시스템 제작
#조건 1 : 1도가 작거나 숫자가 아닌 입력값이 들어올 때 ValueError로 처리
        #출력 메시지 : "잘못된 값을 입력하였습니다"
#조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        #치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        #출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

#[코드] #기존 코드는 -1 입력시 chicken 값 증가됨

class SoldOutError(Exception): #조건 2
    pass

chicken = 10
waiting = 1 #홀 안에 현재 만석. 대기번호 1번부터 시작
while(True):
    try :
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0: #조건 1 해결법
            raise ValueError 
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료 되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break #while문 탈출