# 함수의 매개변수(parameter)와
# 인수(인자 : argument)
# 매개변수 : 함수를 정의할때 함수로 전달되는 값을 갖는 변수
# 인수 : 함수를 호출할대 전달되는 값(변수)
def get_area(w,h):
    w
    result = w*h
    print(f'사각형 가로={w}, 세로={h}, 면적은 {result}')
    return result

    # get_area(10,20)

# 문제. 사칙연산을 수행하는 함수 정의
# add(a,b) : 두 수 더하기
# sub(a,b) : 빼기
# mul(a,b) : 곱셈
# div(a,b) : 나눗셈

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

# 2. 디폴트 매개변수
# 매개변수의 기본값이 지정되어 있는 경우
# !!!!디폴트 매개변수는 반드시 마지막에 있어야 함!!!!
def greet(name,msg='siuuu'):
    print(name +','+msg)

greet('홍길동','hi')
# greet('홍길동') msg에 디폴트 값이 없을때
# 입력을 안하면 에러뜬다. 디폴트 값이 있으면 안뜸
# TypeError: greet() missing 1 required positional argument: 'msg'

# 3. 위치 매개변수(posittional parameter)
# 매개변수의 위치가 실인수로 전달받을 때 동일한
# 위치의 변수에 저장됌
# 매개변수의 순서대로 인수를 전달

# 4. 함수에 여러개 자료(리스트, 딕셔너리) 전달

def show_names(names):
    for name in names:
        print(name,end=' ')

show_names(['hong','shim','gang'])

def show_info(info):
    print(info)

info={'name':'hong','age':20}
show_info(info)

# 5. 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러개의ㅣ
# 값을 전달 받을 때 사용 예를들면 print()
# *args(변수이름)
# **kargs(변수이름) => key,value
# * 하나가 붙으면 여러개 변수를 넣을 수 있고
# ** 두개가 붙으면 키와 값의 형태로 받음
# *args 와 **kwargs 둘이 순서 못바꾼다.
print('hi','ho',end='\n') #**kargs 예시가 end='\n'임

# 1)*args 매개변수
def my_sum(*args):
    total = 0
    for arg in args:
        total +=arg
    return  total

print(my_sum(1,2))
print(my_sum(1))
print(my_sum(1,2,3))
print(my_sum(1,3,4,5,6))

# 2) **kwargs 매개변수

def show_infos(**kwargs):
    for key in kwargs.keys():
        print(key,kwargs[key])
    print()
    for value in kwargs.values():
        print(value)
    print()
    for item in kwargs.items():
        print(item)

show_infos(id='ABC')
show_infos(id='abcd',name='hong',age=30)

# 6. 키워드 인수(keyword arguments)
# C언어에는 이런거 없다.
# 인수들 앞에 키워드를 두어서 인수를 구별
# 인수의 위치가 매개변수의 위치와 달라도 됨
def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40)
# 매개변수 이름 = 값하면 그대로 전달됌
my_print(a=5,c=10,b=30)


# 위치인수와 키워드 인수를 함께 사용하는 경우
# 키워드 인수가 위치인수 뒤로 와야하는게 원칙!