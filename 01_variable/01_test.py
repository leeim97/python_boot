# Day 1 : 변수에 대해서 실습

#변수란 데이터를 저장하는 메모리 주소
#파이썬의 변수 : 동적타이핑, 레퍼런스-> 변수 선언이 필요 없다
#id(),type()
#print()

# 실습1 : 두 변수의 값 교환(Swap)
'''
a = 10
b = 5
a,b = b,a
print(a,b)
'''
#''' ''' 하면 문자열로 인식함 그래서 주석과 같은 효과

a,b= 10,5
print('a=',a,'b=',b)
a,b=b,a
print('a=',a,'b=',b)


# 실습2 : 변수 삭제
#del a
#print(a)
#NameError

# 실습3 : 변수의 값 출력
age=28
name='lee'
print(name,age)

addr= '서울시 송파구'
result=name+"은 "+addr+'에 살아요'
print(result)

print(name+": 나이는 "+str(age)+' 입니다')
#TypeError
#숫자를 문자열로 변환하는 함수 활용 : str(숫자)

# 실습4: 변수를 이용한 계산 결과값 출력
# 삼각형의 넓이 계산해서 출력

w = 10
h = 5
s = w*h/2
print('넓이 = ',s)

#print() 함수의 다양한 출력
#print('문자열',변수)

#포맷 서식
#방법1 :'서식' % 값 ,format string 사용 (문자열 형태로 만든 다음 함) 
# format string: %f, %d ,%s, %c, %x, %o,%%
#               실수,정수,문자열,하나의 문자,16진수,8진수,%

print('넓이=%d' %s)  #d 정수 , f 실수
result= '%s은 %s에 살고 나이는 %d' %(name,addr,age)  #변수 두 개 이상일대 괄호
result2= '넓이=%5.2f'  %s #자리수에 .도 들어감
pcnt = 10.5
result3= '전체면적의 %.2f%%입니다' %pcnt
print(result)
print(result2)
print(result3)



# 방법2 : format() 함수
# format(숫자,'숫자서식')

result4= format(s,'.2f')
print(result4)
print(format(100,'5d'))
print(format(10300,',')) #세자리마다 ,로 나타내줌

#연습문제
#다음의 변수 값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기


kor=90
eng=80
math=75

sum=kor+eng+math
avg=sum/3

print('총점: %d, 평균: %5.2f' %(sum,avg))
print('총점: ',sum,', 평균: ',format(avg,'5.2f'),sep='')

# 방법3 : str.format() 함수  
#      '{1:서식} {0:서식} {2:서식}'.format( , , ) 함수 ch)순서는 내맘대로
print('{0:.3f}'.format(3.1415927))
print('{0:5d} {1:05d}{2:.3f}'.format(kor,math,eng))

# 가장 최신 방법
# 방법4 : f'string => 3.6버전 부터 제공
result5=f'수학:{math:05d} 국어:{kor:7.3f} {eng} 'f'수학:{math:05d} 국어:{kor:7.3f} {eng} '
print(result5)


balance=10300.0
print(balance)
print(int(balance))
print(format(int(balance),','))

# 상수 : 고정된 변수
# 리터럴 : 값 그 자체 실수, 정수, 문자, 문자열, None, True, False

#print()함수의 매개변수 활용
print(kor, math, eng, end='///') 
print(kor, math, eng, sep='*')

