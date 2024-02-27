class Dog():
    dog_id=0 # 클래스 변수
    # 클래스에서 공동으로 사용하는 전역변수느낌

    def __init__(self,name='',breed='',size='',age='',color=''):
        self.name=name
        self.breed=breed
        self.size=size
        self.age=age
        self.color=color
        Dog.dog_id+=1 #Dog클래스의 dog_id

    def eat(self,food):
        print(f'{self.name}이 {food}를 먹는다')

    def sleep(self):
        print(f'{self.name}이 잠잔다')

    def sit(self):
        print(f'{self.name}이 앉아있다')

    def run(self):
        print(f'{self.name}이 뛴다')

dog1 = Dog('삐삐','Maltese','small','2','white')
print(f'dog1의 dog_id : {dog1.dog_id}')
dog2 = Dog('벤ㅇ','chow chow','medium','3','brown')
print(f'dog2의 dog_id : {dog2.dog_id}')
dog3 = Dog('뭉치','mastiff','large','5','black')
print(f'dog3의 dog_id : {dog3.dog_id}')

dog1.eat('fddo')
dog1.sleep()
dog4 = Dog()
print(f'dog4의 dog_id : {dog4.dog_id}')

# 인스턴스 변수 : 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
# 클리스이름.클래스변수명 으로 메서드 내부에서 사용하고
# 인스턴스이름.클래스변수명 으로 사용