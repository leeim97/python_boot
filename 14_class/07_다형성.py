# 다형성(polymorphism)

class Animal():
    def __init__(self,name):
        self.name=name

    def talk(self):
        #raise NotImplementedError는
#어떤 클래스에 추상 메서드가 있는 경우 이 메서드를 서브클래스에서 구현하지 않았을 때 NotImplementedError를 발생시킬 수 있습니다.
#이것은 개발자에게 해당 메서드를 오버라이드하여 구현할 것을 요구하는 신호가 됩니다.

        raise NotImplementedError('subclass must implement abstract method')

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'woof woof!'

animals= [Cat('Missy'),Cat('Mr.Mistoffelees'),Dog('zion')]

for animal in animals:
    print(animal.name+' : '+animal.talk())