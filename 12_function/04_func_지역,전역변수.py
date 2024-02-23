# 지역변수(local varaiable)와 전역변수(global variable)
# 지역변수 : 함수 내부에서 정의된 변수, 함수 안에서만 사용가능
# 함수가 호출시 생성되고, 함수 종료시 소멸
a=10
print(a)

def show_info(name):
    age=10
    print(name,age)

show_info('age')

def show():
    # a=1  #a를 정의하면 여기서 a는 지역변수
    b= a+1 #위에서 a= 값이라고 정의 안하면
           #a는 전역변수 그대로 b에 들어감

    # 전역변수 a를 쓸꺼면 global a라고 해주면됌

    print(f'지역변수 a : {a}' ,id(a))
    print(f'지역변수 b : {b}' ,id(b))

# 지역변수명과 전역변수 이름이 같은 경우
# 지역변수가 우선한다.

def show1():
    a=1
    b = a + 1

    print(f'지역변수 a : {a}', id(a))
    print(f'지역변수 b : {b}', id(b))


def show2():
    a = 1       # 지역변수
    b = a + 1

    print(f'지역변수 a : {a}', id(a))

# def show1():
#     a= a+1 #지역변수를 찾음 :오류 발생
#     b = a + 1
#
#     print(f'지역변수 a : {a}', id(a))



def show3():
    b = a + 1 # a: 전역변수

    print(f'지역변수 a : {a}', id(a))

def show4():
    global a  # 전역변수 사용
    a = a + 1

    print(f'지역변수 a : {a}', id(a))


show()
print(f'전역변수 a : {a}',id(a))


def sub(x,y):
    global b
    a =7
    x,y=y,x
    b=3
    print(a,b,x,y)

a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)

# 리스트를 인자로 넘기면 주소를 넘기기 때문에
# 얕은 복사가 되므로 원본을 건들고 싶지 않으면
# 복사해서 써라~~
def show_list(my_list):
    cpy_list=my_list.copy()
    cpy_list[-1]=100
    print(cpy_list,id(cpy_list))

my_list=[1,2,3,4]
show_list(my_list)
print(my_list,id(my_list))