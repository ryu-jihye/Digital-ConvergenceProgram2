#super 관련 다중상속의 경우 = 순서 상의 맨 마지막에 상속받는 경우만 상속받음
# 따라서 초기화 할 때 2번 초기화를 함 

class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
#1번
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

#2번 : 만약 Flyable을 Unit보다 먼저 상속 받는다면?
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

#해결법 : 1, 2번의 문제점 해결하기 위한 방법
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__() = 사용x
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽 
dropship = FlyableUnit() #1번 결과 : Unit 생성자
dropship = FlyableUnit() #2번 결과 : Flyable 생성자
dropship = FlyableUnit() #해결법 : Unit, Flyable 생성자 둘 다 생성됨

#퀴즈
#3개의 매물 존재
#강남 아파트 매매 10억 2010년
#마포 오피스텔 전세 3억 20007년
#송파 빌사 월세 500/50 2000년

#[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
                , self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)


for house in houses:
    house.show_detail()
