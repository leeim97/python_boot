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
        #Car.__init__(spped,color) 처럼 직접 상속받을 클래스 이름 언급해도됌
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

# 아래 코드 보면 super().안쓰고 클래쓰 이름 써서 상속받음
'''
class Person:
    def __init__(self, name, age, position):
       self.Name = name
        self.Age = age
        self.Position = position
    def show_info(self):
        print('이름 : {}'.format(self.Name))
        print('나이 : {}'.format(self.Age))
        print('직위 : {}'.format(self.Position))
        print("저는 {0} {1}입니다. 나이는 {2}입니다.".format(self.Position, self.Name, self.Age))
class Researcher(Person):
    def __init__(self, name, age, position, degree):
        Person.__init__(self,name, age, position)
        self.Degree = degree
    def show_info(self):
        Person.show_info(self)
        print("저는 {} 입니다.".format(self.Degree))
'''