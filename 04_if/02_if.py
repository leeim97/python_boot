# 짝수판단
num=int(input('정수 입력 : '))

if num %2 ==0:
    print('짝수')
else:
    print('홀수')

# 제일 큰 수 출력

a=int(input('정수1 입력 : '))
b=int(input('정수2 입력 : '))
c=int(input('정수3 입력 : '))

max=0
if a>=b:
    max=a
else:
    max=b

if max >= c:
    pass
else:
    max=c

print(max)      

# 도형 선택하여 해당하는 도형의 면적 구하기

num = int(input('도형 입력(1: 사각형,2: 삼각형, 3: 원)'))

if num==1:
    we=int(input('가로 입력 : '))
    he = int(input('세로 입력 : '))
    print('사각형의 면적 = %.2f'%(we*he))
elif num==2:
    we=int(input('밑변 입력 : '))
    he = int(input('높이 입력 : '))
    print('삼각형의 면적= %.2f'%(we*he/2))
elif num==3:
    r=int(input('반지름 입력 : '))
    print('원의 면적 = %.2f'%(3.141592*(r**2)))
else:
    print('다시 선택 해주세요')


# 컴퓨터와 주사위 놀이하기
from random import randint
value= int (input('주사위 눈의 수의 입력 : '))
com_val= randint(1,6)

if value > com_val:
    print('WIN')
elif value < com_val:
    print('LOSE')
else:
    print('DRAW')
