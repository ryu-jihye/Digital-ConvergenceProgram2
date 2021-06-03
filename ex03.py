a=10

def func1() :
    a=1
    print("func1에서 출력한 a:", a)

def func2() :
    a=1
    print("func2에서 출력한 a:", a)

func1()
func2()

#짧은 글 읽기
inFile = None
isStr = ""

inFile = open("c:/Temp/data.txt", "r", encoding='utf-8 ')

inStr = inFile.readline()
print(inStr, end="")
inStr = inFile.readline()
print(inStr, end="")
inFile.close();
#-------------------------------------
#긴 글 읽기
isStr = ""

inFile = open("c:/Temp/data.txt", "r", encoding='utf-8 ')

while True:
    inStr = inFile.readline()
    if inStr == "":
        break
        print(inStr, end="")
    inFile.close()

inFile = None
#변수
inStr = ""
inFile = open("c:/Temp/data.txt", "r", encoding='utf-8 ')
inList = inFile.readlines()

print(inList)
inFile.close()


#inFile = None
#inStr = ""
#fileName = input("파일명을 입력하세요: ")

#inFile = open(fileName, "r", encoding='utf-8')
#inList = inFile.readlines()
#for inStr in inList

outFile = None
outStr = ""
outFile = open("c:/temp/data2.txt", "w", encoding='utf-8')
while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFile.writelines(outStr + "\n")
    else:
        break

outFile.close()

import shutil
shutil.copyfile("d:/Temp/123.txt", "d:/Temp/1234.txt")

from calculator import Calculator
class advancedCalculator(Calculator):
    def pow(self):
        print("===pow() start ===")
        print("num1^num2= ", self.num1**self.num2)

myCal = advancedCalculator(4.2)
myCal.pow()

class Person:
    pocket=[] #속성 만들기

    def put_pocket(self, stuff):
        self.pocket.append(stuff)

conan = Person()
conan.put_pocket('스마트폰')

rose = Person()
rose.put_pocket('책')

print("conan :", conan.pocket)
print("rose :", rose.pocket)

def calcTotalPrice(gps):
    dcRate=0;
    totalPrice=0

    if len(gps)==1:
        dcRate=5;
    elif len(gps)==2:
        dcRate=10;
    elif len(gps)==3:
        dcRate=20;
    elif len(gps)>=4:
        dcRate=30;

    for item in gps:
        totalPrice+=item*(1-dcRate/100)

    return[dcRate,totalPrice]

    import dcGoods as dg

if __name__=='__main__':
    flag = True
    goodPrices=[]

    while flag:

     purchase=int(input('상품을 구매 하시겠습니까? 1.구매 2.종료'))

     if purchase ==1:
        price = int(input('구매한 상품의 금액을 입력하세요.'))
        goodPrices.append(price)
     elif purchase ==2:
        result=dg.calcTotalPrice(goodPrices)
        flag = False

print('할인율:',result[0],'%')
print('총합계:',result[1],'원')