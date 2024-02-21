# Day2 :
# 1.자료형(Data Type)

# 기본 자료형 : 정수(integer), 실수(float), 부울(bool), 문자열(str)
# iterative / 집합적 자료 / sequence: 리스트, 딕셔너리, 튜플, 세트

# 2진수, 8진수, 16진수, 10진수
#bin(), oct(), hex()

print('bin(123)=',bin(123))
print('bin(0o123)=',bin(0o123))
print('bin(0x123)=',bin(0x123))

print('oct(123)=',oct(123))
print('oct(0b11010111)=',oct(0b11010111))
print('oct(0x123)=',oct(0x123))


print('hex(123)=',hex(123))
print('hex(0b11010111)=',hex(0b11010111))
print('hex(0o123)=',hex(0o123))
print(0xA)
# 변수의 자료형 : 실행할 때 결정(동적타이핑)
# id(), type()

# 2)
# int(string), float(string), str(number)
# int(string) : 10진수가 기본
# int(string,2), int(string,8), int(string,base=16)

#int 함수
print("int('123')=",int('123'))
print('int(\'1010\',base=2)',int('1010',base=2)) #base= 생략하고 그냥 2만 써도 됌
print('int(\'ff\',16)',int('ff',16))
print("int('123',8)",int('123',8))

#float(string) : 문자열을 실수형으로 변환
print('float("13.5")=',float('13.5'))
print('float("13")=',float('13'))

#str(숫자): 문자열 변환
print('나이는 = %d' % int('20'))
print('나이는 = '+str(20))

#print('int(\'ff\',16)',int('ff'))
# 에러 : NameError, TypeError, VlaueError(사용한 값이 부적절한 경우등등)

# input() 함수 : 키보드로 입력받아서 문자열로 반환
# input(pormpt) : prompt는 화면에 표시되는 문자열
name = input('이름은:')
year = int(input('출생연도는:'))
print(f'이름은 {name}, 나이는 {2024-(year)}')

num=int(input('실수 입력: '))
result = num* 10
print(f'{num}*10= {result}')

# 연산자 : *,+
# 문자열 + 문자열 = 두 문자열을 연결
# 문자열 * 숫자 = 문자열을 숫자만큼 생성해서 연결

#SW => data + algorithm

#문제1.두 정수를 입력받아서 합계 출력
a,b=map(int,input().split())
print(a+b)

#문제2. 몸무게와 키 값을 입력받아서 BMI 지수 계산
# BMI = 몸무게 / 키의 제곱

weight= float(input('몸무게(kg): '))
height = float(input('키(m): '))
print(f'당신의 BMI : {weight/(height**2)}')

