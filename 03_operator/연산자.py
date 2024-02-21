# 연산자

# 1. 산술연산자 : +, -, *, /,%,//, **

# divmod(x, y) : x를 y로 나눈 몫과 나머지 반환

# 문제1. 10000초는 몇시간 몇분 몇초인가?

time = 10000

hours = time // 3600
time = time % 3600
minutes = time //60
seconds = time %60
print(f'{time}은 {hours}시간 {minutes}분 {seconds}초 입니다. ')


# 2. 관계 연산자 : > < >= <= == !=

a = 100
b =5 
result = a==b
print(f'{a}=={b}의 결과는 {result}')
print(f'{a}=={b}의 결과는 {a==b}')
print(f'{a}!={b}의 결과는 {a!=b}')
print(f'{a}>{b}의 결과는 {a>b}')

# 3. 논리 연산자 : and or not

print( a > 200 and a<300)
print( not (a>200))

# 4. 비트 연산자 : & | ^ ~ >> <<
print(f'~a : {~a}')
print(f'{b}<<1 : {b<<1}')
print(f'{b}<<3 : {b<<3}')
print(f'{b}>>1 : {b>>1}')
print(f'{a}>>3 : {a>>3}')

# 대입연산자 : += -= *= /= //= %=
print('a=',a)
a+=10
print('a+=10 : ',a)

# 실습문제1. 지폐교환기
#풀이1
money= int(input('지폐로 교환할 돈은 얼마?'))
five_4 = money // 50000
money-= five_4*50000

one_4 = money // 10000
money -= one_4 * 10000

five_3 = money // 5000
money -= five_3 * 5000

one_3 = money //1000
money -= one_3*1000
#풀이2
money= int(input('지폐로 교환할 돈은 얼마?'))
change=[50000,10000,5000,1000]

for i in change:
    print(f'{i}원짜리 ==>',money //  i)
    money %= i

print('지폐로 바꾸지 못한 돈 ==> ',money)

print('50000원짜리 ==> ',five_4)
print('10000원짜리 ==> ',one_4)
print('5000원짜리 ==> ',five_3)
print('1000원짜리 ==> ',one_3)
print('지폐로 바꾸지 못한 돈 ==> ',money)


