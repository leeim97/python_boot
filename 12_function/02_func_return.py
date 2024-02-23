# 함수 반환문 return

def get_area():
    w = int(input('가로길이 : '))
    h= int(input('세로길이 : '))
    result = w*h
    print(f'사각형 가로={w}, 세로={h}, 면적은 {result}')

# print(get_area())


# 여러개를 반환할 수 있고,튜플을 반환할 수 있고
#리스트를 반환할 수 있고 dict도 반환한다.
def multi_return():
    return 1,2,3

# value = multi_return()
# w,h,area=value
# print(value,type(value))
# print(w,h,area)

def get_name():
    names=[]
    for i in range(3):
        name=input('이름 입력 : ')
        names.append(name)

    return names

names= get_name()
print(names)

def get_info():
    name = input('이름입력 : ')
    age = input('나이 : ')
    info = {'name':name,'age':'age'}
    return info


info = get_info()
print(info)