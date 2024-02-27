# 상송 : 부모클래스로부터 상속받은 필드와
# 메소드를 이용하거나 추가 변경하여 활용(재사용)

# 메서드 재정의(overriding) : 상속받은 메서드를 다시 정의
class Car(object):
    def __init__(self,speed=0,color=''):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행한다')

class Truck(Car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color) # 이 문장을 반드시 먼저써야됌
        self.load = load

    #메소드 재정의(overriding)
    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행한다')

    def loading(self):
        print(f'최대 적재량{self.load}의 짐을 운반할 수 있는 트럭')



car1 = Car()
truck1 = Truck(0,'blue',5)
car1.drive()
truck1.drive()