# 함수
# 재사용 / 자주 사용하는 기능들을 위한 코드 집합
# 경제적, 관리용이
# 내장함수(bulit-in function) / 사용자 정의 함수
# 함수 정의 및 호출

# 예. 이름, 나이, 연락처 출력하는 함수 show_info()
def show_info():
    print('이름: 홍길동')
    print('age : 20')
    print('number : 010-2213-4568')

def show_info1():
    name=input('이름 입력 :')
    age=input('나이 입력 :')
    phone=input('연락처 입력 : ')
    print(f'이름: {name}')
    print(f'age : {age}')
    print(f'number : {phone}')


show_info1()

# 문제. 두 정수를 입력받아 더하고 그 결과를 출력하는
# 함수 add() 정의하기

def add():
    n1=int(input())
    n2 = int (input())
    return n1+n2
print(add())