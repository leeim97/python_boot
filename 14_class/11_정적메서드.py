# 정적메서드(static method)
# : 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용하는 메서드
# : 순수함수(pure function)
# 메서드 위에 @staticmethod 키워드를 지정하여 정의

class Calc:
    @staticmethod #이거 적용한 함수는 self안나옴
    def add(a,b):
        print(a+b)

    @staticmethod
    def sub(a,b):
        print(a-b)

myCal = Calc()
myCal.add(10,20)
# 정적메소드(staticmethod)를 썻기때문에
# 인스턴스를 만들지않고
# 메서드를 바로 사용가능
Calc.add(10,20)

