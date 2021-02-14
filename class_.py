class Unit:

    def setData(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __init__(self, name, hp, damage): # __init__ : 초기화 메소드 \ 객체가 생성될 때 자동으로 호출되어 성질 부여시켜줌
        self.setData(name, hp, damage)
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))


class AttackUnit:

    def setData(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __init__(self, name, hp, damage): # __init__ : 생성자
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
print("")

marine1 = Unit("마린", 40, 5) # 생성
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
wraith1 = Unit("레이스", 80 ,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("클로킹 레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True: # 객체에 함수를 외부에서 생성가능 \ 확장한 함수는 해당 객체에만 사용가능
    print("{0} 는 클로킹 상태입니다.".format(wraith2.name))

# 상속

class Pencil:
    def __init__(self, name, price):
        self.name = name   
        self.price = price        

class Pen(Pencil): # 상속하려는 클래스를 ()에 대입
    def __init__(self, name, price, ink):
        Pencil.__init__(self,name,price)
        self.ink = "Auto"

