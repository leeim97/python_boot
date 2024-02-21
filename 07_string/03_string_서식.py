# 1. 문자열 정의 : 한줄, 여러줄
text1 = 'Python is great!'
text2 = "Yes, it is."
text3 = "It's not like any other"
text4 = 'Don\'t walk.'
#다음 문장할때 \해주면 줄 안바뀜
text5 = 'This \n is \
contain \
temp'
print(text5)
#그냥 쓰면 이 형태로 나옴
text6 = """apple\n
banana
melon 
"""
print(text6)

#2. 문자열 포맷(서식) 지정
# 1) 포맷코드 '문자열 포맷코드' % (변수들)
#    '%05d %.2f %s %c ' % ( , , , )
print('%s는 %d살입니다' %('홍길동', 10))

# 2) '문자열 {위치인덱스}'.format(변수)
#    ' {0:.2f} {2:5d} {1:s} '.format( , , )
name='kim'
age=10
print('{0}은 {1}살입니다'.format(name, age))

#     '문자열 {변수}'.format(변수=값)
print('{name}은 {age}살입니다'.format(name='홍길동', age=10))

# 3) format(변수, '서식' )
#    format(bmi, '.2f')

# 4) f'string : f' {변수 } {변수:서식 } '
print(f'{name}은 {age}살입니다.')

#3. 날짜 출력 포맷
# 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜 /

# 모듈(module) : 함수나 변수를 모아 놓은 파일
from datetime import date, datetime, timedelta

today = date.today()
print(today, type(today))
print(f'{today.year}년 {today.month}월 {today.day}일')
print(type(today.year))

#method: 메서드, field :객체의 변수
curr_time = datetime.now().time()
print(curr_time, type(curr_time))
print(curr_time.hour, curr_time.minute, \
      curr_time.second, curr_time.microsecond)

# timedelta() : 날짜 계산
print(today + timedelta(days=-1))
print(today + timedelta(weeks=1))

curr_datetime = datetime.now()
print(curr_datetime + timedelta(hours=-1))
print(curr_datetime + timedelta(days=2, hours=4))

# strftime() :날짜,시간 서식 지정
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %I:%M:%S %p'))
print(curr_datetime.strftime('%y년%m월%d일 %I:%M:%S %p'))


# 4. 문자열 정렬
# 왼쪽정렬 : <
# 오른쪽정렬 : >
# 가운데정렬 : ^
# 공백문자 -지정 : -

text = 'Python is great!'

print('{0:#<20}'.format(text), 'end')
print(f'{text:>20}')
print('{0:*^20}'.format(text), 'end')
print(f'{text:#^20}')







