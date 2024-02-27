# 예제, Line 클래스

class Line:
    def __init__(self,length): # 생성자
        self.length=length
        print(f'{self.length} 길이의 선이 생성되었습니다.')

    def __del__(self):  # 소멸자
        print(f'{self.length}길이의 선이 삭제되었습니다')

line1 = Line(10)
line2 = Line(20)
del(line1)