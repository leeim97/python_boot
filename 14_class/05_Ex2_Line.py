# 예제, Line 클래스

class Line():
    def __init__(self,length): # 생성자
        self.length=length
        print(f'{self.length} 길이의 선이 생성되었습니다.')

    def __del__(self):  # 소멸자 (시간지나면 자동으로 삭제됌)
        print(f'{self.length}길이의 선이 삭제되었습니다')

    def __repr__(self): #print문이 실행되면 이 함수가 실행됨
        # __str__이랑 같이하면 __str__만 되는듯?
        return f'선의 길이 {self.length}인 선분'

    # def __str__(self):#print문이 실행되면 이 함수가 실행됨
    #     return f'선분 {self.length}'

    def __add__(self,other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __lt__(self, other):
        return self.length < other.length

    def __gt__(self, other):
        return self.length > other.length

    def __eq__(self, other):
        return self.length == other.length

    def __neg__(self,other):
        return self.length != other.length

line1 = Line(10)
line2 = Line(20)
# del(line1)
print(line1)
print(line2)
print(line1 + line2)# + 쓰면 __add__가 자동 실행됌
print(line1 - line2)# - 쓰면 __add__가 자동 실행됌
print(line1 > line2)# > 쓰면 __add__가 자동 실행됌
print(line1 < line2)

if line1 > line2:
    print('선분 1이 길어요')
else:
    print('선분 2가 길어요')