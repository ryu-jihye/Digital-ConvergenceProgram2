#일반 유닛
class Unit:  #지상 유닛에 speed 추가
    def __init__(self, name, hp, speed): #스피드 추가
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) #self.name도 가능
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage): #일반 유닛도 공격 받을 수 있기에 공격 유닛의 해당 부분을 옮김
        print("{0} : {1} 데미지를 얻었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

#공격 유닛
class AttackUnit(Unit): #(Unit)이라는 class 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        #self.name, self.hp 모두 일반 유닛과 겹칩 -> 상속받을 수 있음
        self.damage = damage

    def attack(self, location): #location은 전달받은 값을 사용
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

#마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 자기 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크 클래스
class Tank(AttackUnit):
    #시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False #시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        #현재 시즈모드가 아닐 때 - 시즈모드 하면 됨
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        #현재 시즈모드일 때 - 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
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

#레이스 : 공중유닛
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제 합니다.".format(self.name))
            self.clocked = False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")


#실제 게임 진행
game_start()

#마린 3개 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2개 생성
t1 = Tank()
t2 = Tank()

#레이스 1개 생성
w1 = Wraith()

#유닛 일괄 관리(생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동