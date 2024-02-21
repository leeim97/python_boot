# 조건문

# if~else 문
num= int(input('정수입력: '))
if num >10:
    print('10보다 크네요')
else:
    print('10보다 작거나같요')

#연습문제1. 등록된 아이디와 비번 확인 로그
reg_id='flower'
reg_pwd=str(1234)

id=input('아이디 입력 : ')
pwd=input('비밀번호 입력 : ')

if reg_id == id and pwd == reg_pwd:
    print('로그인 성공!')
else:
    print('로그인 실패!')

# 중첩 if : if 조건이 만족하는 경우 또 다른 조건에 따라 실행하는 경우
# if 아래 if 존재

#if~elif~else 문

# 점수 입력(0~100) 받아서 학점 출력
# 90<= ->A
# 80 <=  <90 ->B
# 70 <= <80 ->C
#60<=  <70 ->D
#60> ->F
score=int(input())
if score >=90 :
    print('A')
elif 80 <= score <90:
    print('B')
elif 70 <= score <80:
    print('C')
elif 60<= score <70 :
    print('D')
else:
    print('F')
