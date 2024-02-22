# 튜플 생성
tt=(1,)

t1=(1,2,3)
print(t1,type(t1))

t2 = 4,5,6
print(t2)

t3 = t1,(7,8,9)
print(t3)

t4 = [1,2],[3,4,5]
print(t4)

# tuple()쓸때 안에 리스트 형태로 넣어야됌 약속임
t5 = tuple([1,2,3])
print(t5)

# 문자열이 한글자씩 쪼개짐
t6 = tuple('hello')
print(t6)

# 리스트를 튜플로 바꾸기
list1= [1,2,3]
t7 = tuple(list1)
print(list1,t7)

# 튜플을 리스트로 변환
list2= list(t4)
print(list2)
