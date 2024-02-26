# 재귀함수(recursive function)
# 함수 내부에서 자신의 함수를 다시 호출

# 1~n 까지의 합 재귀함수

def my_sum(n):
    if n==1:
        return 1
    else:
        return n+my_sum(n-1)

print(my_sum(10))

# . 1*2*...*n : n! 계산하는 재귀함수

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# 내부함수

def outFunc(x,y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc(10,30))

# 람다(lambda)함수
# 한줄짜리 함수, return문을 사용하지 않음
# lambda <인수들>:<반환할 식>
# 람다함수는 함수 참조(주소)를 반환
# 변수로 람다함수 객체를 받아서 함수 호출한다
f = lambda :1
print(f())

add = lambda x=10,y=30:x+y #y는 디폴트 매개변수
print(add())
print(add(20))
print(add(10,50))      #포지션널 인자
print(add(y=10,x=500)) #키워드 인자

# 람다 표현식 : 함수 이름 명명하지 않고
# 즉, 변수에 할당하지 않고(위처럼f에) 바로 호출
#(lambda <인수들>:식)(인수들)

print((lambda x:x+10)(10))

# 람다표현식 안에서는 변수 생성 불가 :SyntaxError
# f = lambda x : y=10,x+y #y가 표현식에서 있으니 오류

def plus_ten(x):
    return x + 10

# [1,2,3,4,5] 에 동일하게 10을 더하는
#  것에 람다를 사용해보자

# new=[]
# # 기존 방법
# for n in [1,2,3,4,5]:
#     new.append(n+10)

#map을 사용 map(func,리터럴들)
print(list(map(plus_ten,[1,2,3,4,5])))
print(list(map(lambda x:x+10,[1,2,3,4,5])))

# 두 개의 리스트 요소 더하기

def add_list(x,y):
    new_list=[]
    for i in range(len(x)):
        new_list.append(x[i]+y[i])

    return new_list
a=[1,2,3,4]
b=[10,11,12,13]
print(add_list(a,b))

#map(func,iterable_data)함수

print(list(map(lambda x,y:x+y,a,b)))