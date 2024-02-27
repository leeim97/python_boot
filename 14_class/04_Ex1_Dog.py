class Dog():
    def __init__(self,name,breed,size,age,color):
        self.name=name
        self.breed=breed
        self.size=size
        self.age=age
        self.color=color

    def eat(self,food):
        print(f'{self.name}이 {food}를 먹는다')

    def sleep(self):
        print(f'{self.name}이 잠잔다')

    def sit(self):
        print(f'{self.name}이 앉아있다')

    def run(self):
        print(f'{self.name}이 뛴다')

dog1 = Dog('삐삐','Maltese','small','2','white')
dog2 = Dog('벤ㅇ','chow chow','medium','3','brown')
dog3 = Dog('뭉치','mastiff','large','5','black')

dog1.eat('fddo')
dog1.sleep()