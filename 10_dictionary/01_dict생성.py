# 딕셔너리 생성
# -집합적 자료,순서 의미가 없음
# item => 키(key):값(value)으로 구성되어 있음
# {key:value1,key2:value2,key3:value3}
# {} 또는 dict()를 이용하여 생성
# key로 데이터 접근

# d={}
d = dict()
print(d,type(d))

d2= {1:'a',2:'b',3:'c'}
print(d2)
# key의 순서는 생성된 순서대로 구성
# key와 value는 사용자가 지정하는 것, 규정이 없다
# key는 숫자, 문자열 다 가능하나 유일하게 구별되어야 함
# value는 중복 가능

# 2. 딕셔너리 요소 접근 : key를 사용
# 딕셔너리[키이름]

# 3. 키로 접근하여 값을 가져옴
print(d2[1]) #인덱싱의 1이 아닌 키 1이다.

d2[1]=10
print(d2)

# 4. 딕셔너리의 요소 추가 : 딕셔너리[키] = 값
d2['4']=100
print(d2)

# 5. 키는 유일한 값!!!!!!!!
# 동일한 키값을 갖는 경우 맨 마지막에 입력한 키가 적용
d3 = {'a':1,'b':100,'c':'hello','b':1000}
print(d3)

# 6. 값(value)는 하나,여러개의 집합적 자료를 가질 수 있다
d4 = {'name':['kim','hong','lee'],
      'score':[100,90,80],
      'gender':['F','M','M'],
      'phone':('1230','123','789')}

print(d4)
print(d4['name'])

# 7. 요소 삭제 : del(딕셔너리[키])
del(d4['gender'])
print(d4)