class Unit:

    def setData(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2} ]".format(self.name, location, self.speed))

    def __init__(self, name, hp, speed): # __init__ : 초기화 메소드 \ 객체가 생성될 때 자동으로 호출되어 성질 부여시켜줌
        self.setData(name, hp, speed)
        print("[체력 : {0}] 의 {1} 유닛이 생성 되었습니다.".format(self.hp, self.name))

    def information(self, name, hp):
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

class AttackUnit(Unit):  # Unit class의 내용을 상속 받음.

    def setData(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def __init__(self, name, hp, speed, damage): # __init__ : 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable():

    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로  날아갑니다 [ 속도 : {2} ]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable): # # 다중 상속 : 부모 클래스를 2개 이상 상속
    
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩 (재정의) fly 와 move 하나의 움직이는 동작이므로 같은 의미를 가짐
                              # 따라서 fly와 move 함수를 하나로 통일
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

vulture = AttackUnit("벌쳐", 80, 20, 10)
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시") # move 함수는 default unit, fly 함수는 flyableUnit move를 오버라이딩 (재정의)
battlecruiser.move("9시")
# battlecruiser.fly(battlecruiser.name, "9시")

firebat1 = AttackUnit("파이어뱃", 50, 4, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
print("")

medic = Unit("메딕", 40, 4)
marine1 = AttackUnit("마린", 40, 4, 5) # 생성
marine2 = AttackUnit("마린", 40, 4, 5)
tank = AttackUnit("탱크", 150, 3 ,35)
wraith1 = FlyableAttackUnit("레이스", 80 ,5, 7)

print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = FlyableAttackUnit("클로킹 레이스", 80, 5, 7)
wraith2.clocking = True
if wraith2.clocking == True: # 객체에 함수를 외부에서 생성가능 \ 확장한 함수는 해당 객체에만 사용가능
    print("{0} 는 클로킹 상태입니다.".format(wraith2.name))