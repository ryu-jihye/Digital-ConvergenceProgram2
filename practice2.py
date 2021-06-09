#파일 입출력

#파일 내용 추가1
score_file = open("score.txt", "w", encoding="utf-8") #w:쓰기용
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

#파일 내용 추가2
score_file = open("score.txt", "a", encoding="utf-8") #a:append(이어쓰기)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

#파일 내용 읽기
score_file = open("score.txt", "r", encoding="utf-8") #r:읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline()) #한 줄만 읽어옴(커서는 다음 줄로 이동)
print(score_file.readline(), end="") #end="" : 줄 바꿈 x
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True: #무한 루프
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() #line형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

#pickle
import pickle
profile_file = open("profile.pickle", "wb") #wb :쓰기 형식, 바이너리 형식
profile = {"이름" : "박명수", "나이" : 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb") #rb : 읽기 형식, 바이너리 형식
profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
print(profile) #{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}   
profile_file.close()

#with #.close 없이 바로 종료 가능
import pickle
with open("profile.pickle", "rb") as profile_file: #rb : 읽기 형식, 바이너리 형식
    print(pickle.load(profile_file))
 

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read()) #파이썬을 열심히 공부하고 있어요

#퀴즈
#x 주차 주간 보고
#부서 :
#이름 :
#업무 요약 :

#1 ~ 10주차까지의 보고서 파일을 만드는  프로그램 작성하기

for i in range(1, 11):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("{0}주차 주간 보고".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

#클래스
#마린 : 공격 유닛, 군인. 총 쏠 수 있음
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데 일반모드와 시즈 모드로 나뉨
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage) #마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
attack(tank_name, "1시", tank_damage) #탱크 : 1시 방향으로 적군을 공격합니다. [공격력 35]

#일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#__init__ : 파이썬에서 쓰이는 생성자(자동으로 호출)
#self를 제외하고 동일한 갯수만큼 self.aa = aa로 생성해야 함

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지x)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): #location은 전달받은 값을 사용
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 얻었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name)) 

#파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
#공격을 두 번 받는 다고 가정
firebat1.damaged(25) #파이어뱃 : 현재 체력은 25 입니다.
firebat1.damaged(25) #파이어뱃 : 현재 체력은 0 입니다.
#파이어뱃 : 파괴되었습니다.

#상속

#일반 유닛
class Unit:
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp
       # self.damage = damage #메딕(의무병) 같은 경우 공격력x

#공격 유닛
class AttackUnit(Unit): #(Unit)이라는 class 상속받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        #self.name, self.hp 모두 일반 유닛과 겹칩 -> 상속받을 수 있음
        self.damage = damage

    def attack(self, location): #location은 전달받은 값을 사용
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 얻었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

#파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
#공격을 두 번 받는 다고 가정
firebat1.damaged(25) #파이어뱃 : 현재 체력은 25 입니다.
firebat1.damaged(25) #파이어뱃 : 현재 체력은 0 입니다.
#파이어뱃 : 파괴되었습니다

#다중상속(부모가 둘 이상)
#class Unit : 부모 클래스
#class AttackUnit : 자녀 클래스라고 지칭

#일반 유닛
class Unit:
    def __init__(self, name, hp): 
        self.name = name
        self.hp = hp
     

#공격 유닛
class AttackUnit(Unit): #(Unit)이라는 class 상속받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        #self.name, self.hp 모두 일반 유닛과 겹칩 -> 상속받을 수 있음
        self.damage = damage

    def attack(self, location): #location은 전달받은 값을 사용
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 얻었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

#드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송(공격x)

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) #self는 항상 넣어야 함
        Flyable.__init__(self, flying_speed)


#발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


#연산자 오버로딩(움직이는 것은 똑같이 move를 사용하기 위함)
class Unit:  #지상 유닛에 speed 추가
    def __init__(self, name, hp, speed): #스피드 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit): #(Unit)이라는 class 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        #self.name, self.hp 모두 일반 유닛과 겹칩 -> 상속받을 수 있음
        self.damage = damage

    def attack(self, location): #location은 전달받은 값을 사용
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 얻었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0
        Flyable.__init__(self, flying_speed)
    #움직이는 모든 것은 move로 정의하기 위함
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력도 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시 방향")
#battlecruiser.fly(battlecruiser.name, "9시 방향")
battlecruiser.move("9시 방향")

#pass
class Unit:  #지상 유닛에 speed 추가
    def __init__(self, name, hp, speed): #스피드 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass #일단은 완성된 것처럼 보이게 하고 넘어 감

#서플라이 디폿 : 건물, 1개 있을 때 8개 유닛 생성 가능
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

#pass를 통해 그대로 넘어감
def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    pass

game_start()
game_over()

#super
class Unit:  #지상 유닛에 speed 추가
    def __init__(self, name, hp, speed): #스피드 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)  #Unit.__init__(self, name, hp, 0)와 같은 기능 -> #건물은 이동x
        self.location = location