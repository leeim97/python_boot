# 클래스 메서드(class method)
# - 인스턴스를 통하지 않고 클래스에서 바로 호출
# - @classmethod를 지정하여 사용

class Person:
    count = 0 # 클래스 변수

    def __init__(self):
        Person.count += 1

    @classmethod #자동으로 cls 키워드 생김
    def print_count(cls): #cls : 클래스 의미
        print(f'{cls.count}명 태어났어요')
    @classmethod
    def create(cls):   # 생성자와 같은 메서드
        p = cls() # Person()이거랑 같음
        return p
kim = Person()
Person.print_count()

choi = Person()
Person.print_count()

lee = Person.create() #클래스 메서드로 인스턴스 생성
Person.print_count()
